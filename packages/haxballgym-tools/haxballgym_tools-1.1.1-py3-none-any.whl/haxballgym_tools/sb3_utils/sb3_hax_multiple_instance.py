import multiprocessing as mp
import os
import time
from typing import Optional, List, Union, Any, Callable, Sequence

import numpy as np
from stable_baselines3.common.vec_env import SubprocVecEnv, CloudpickleWrapper, VecEnv
from stable_baselines3.common.vec_env.base_vec_env import (
    VecEnvObs,
    VecEnvStepReturn,
    VecEnvIndices,
)
from stable_baselines3.common.vec_env.subproc_vec_env import _worker

from haxballgym.envs import Match
from haxballgym.gym import Gym


class SB3MultipleInstanceEnv(SubprocVecEnv):
    """
    Class for launching several HaxballGym instances into a single SubprocVecEnv.
    """

    MEM_INSTANCE_LIM = 10e4  # 10MB

    @staticmethod
    def estimate_supported_processes() -> int:
        import psutil

        vm = psutil.virtual_memory()

        est_proc_mem = round(
            (vm.available - SB3MultipleInstanceEnv.MEM_INSTANCE_LIM)
            / SB3MultipleInstanceEnv.MEM_INSTANCE_LIM
        )
        est_proc_cpu = os.cpu_count() or 1
        est_proc = min(est_proc_mem, est_proc_cpu)
        return est_proc

    def __init__(
        self,
        match_func_or_matches: Union[Callable[[], Match], Sequence[Match]],
        num_instances: Optional[int] = None,
        wait_time: float = 5,
    ):
        if callable(match_func_or_matches):
            assert num_instances is not None, (
                "If using a function to generate Match objects, "
                "num_instances must be specified"
            )
            if num_instances == "auto":
                num_instances = SB3MultipleInstanceEnv.estimate_supported_processes()
            match_func_or_matches = [
                match_func_or_matches() for _ in range(num_instances)
            ]

        def get_process_func(i):
            def spawn_process():
                match = match_func_or_matches[i]
                env = Gym(match)
                return env

            return spawn_process

        # super().__init__([])  # Super init intentionally left out for delay

        env_fns = [get_process_func(i) for i in range(len(match_func_or_matches))]

        # START - Code from SubprocVecEnv class
        self.waiting = False
        self.closed = False
        n_envs = len(env_fns)

        # Fork is not a thread safe method (see issue #217)
        # but is more user friendly (does not require to wrap the code in
        # a `if __name__ == "__main__":`)

        ctx = mp.get_context("spawn")

        self.remotes, self.work_remotes = zip(*[ctx.Pipe() for _ in range(n_envs)])
        self.processes = []
        for work_remote, remote, env_fn in zip(
            self.work_remotes, self.remotes, env_fns
        ):
            args = (work_remote, remote, CloudpickleWrapper(env_fn))
            # daemon=True: if crash, we should not cause things to hang
            process = ctx.Process(target=_worker, args=args, daemon=True)
            process.start()
            self.processes.append(process)
            work_remote.close()

            if len(self.processes) != len(env_fns):
                time.sleep(wait_time)  # Waiting time between starting instances

        self.remotes[0].send(("get_spaces", None))
        observation_space, action_space = self.remotes[0].recv()
        # END - Code from SubprocVecEnv class

        self.n_agents_per_env = [m.agents for m in match_func_or_matches]
        self.num_envs = sum(self.n_agents_per_env)
        VecEnv.__init__(self, self.num_envs, observation_space, action_space)

    def reset(self) -> VecEnvObs:
        for remote in self.remotes:
            remote.send(("reset", None))

        flat_obs = []
        for remote, n_agents in zip(self.remotes, self.n_agents_per_env):
            obs = remote.recv()
            if n_agents <= 1:
                flat_obs.append(obs)
            else:
                flat_obs += obs
        return np.asarray(flat_obs)

    def step_async(self, actions: np.ndarray) -> None:
        i = 0
        for remote, n_agents in zip(self.remotes, self.n_agents_per_env):
            actions_remote = actions[i : i + n_agents, :]
            if len(np.shape(actions_remote)) == 1:
                actions_remote = [actions_remote]

            remote.send(("step", actions_remote))
            i += n_agents

        self.waiting = True

    def step_wait(self) -> VecEnvStepReturn:
        flat_obs = []
        flat_rews = []
        flat_dones = []
        flat_infos = []
        for remote, n_agents in zip(self.remotes, self.n_agents_per_env):
            obs, rew, done, info = remote.recv()
            if n_agents <= 1:
                flat_obs.append(obs)
                flat_rews.append(rew)
                flat_dones.append(done)
                flat_infos.append(info)
            else:
                flat_obs += obs
                flat_rews += rew
                flat_dones += [done] * n_agents
                flat_infos += [info] * n_agents
        self.waiting = False
        return (
            np.asarray(flat_obs),
            np.array(flat_rews),
            np.array(flat_dones),
            flat_infos,
        )

    def seed(self, seed: Optional[int] = None) -> List[Union[None, int]]:
        res = super(SB3MultipleInstanceEnv, self).seed(seed)
        return sum([r] * a for r, a in zip(res, self.n_agents_per_env))

    def _get_target_remotes(self, indices: VecEnvIndices) -> List[Any]:
        # Override to prevent out of bounds
        indices = self._get_indices(indices)
        remotes = []
        for i in indices:
            tot = 0
            for remote, n_agents in zip(self.remotes, self.n_agents_per_env):
                tot += n_agents
                if i < tot:
                    remotes.append(remote)
                    break
        return remotes
