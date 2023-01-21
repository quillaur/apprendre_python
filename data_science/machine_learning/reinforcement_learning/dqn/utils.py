# Taken from https://alexandervandekleut.github.io/deep-q-learning/

from collections import deque
import random
import gym
import numpy as np


class ReplayBuffer:
    def __init__(self, size=1000000):
        self.memory = deque(maxlen=size)
        
    def remember(self, s_t, a_t, r_t, s_t_next, trunc, d_t):
        self.memory.append((s_t, a_t, r_t, s_t_next, trunc, d_t))
        
    def sample(self, num=32):
        num = min(num, len(self.memory))
        return random.sample(self.memory, num)


class DiscreteToBoxWrapper(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        assert isinstance(env.observation_space, gym.spaces.Discrete), \
            "Should only be used to wrap Discrete envs."
        self.n = self.observation_space.n
        self.observation_space = gym.spaces.Box(0, 1, (self.n,))
    
    def observation(self, obs):
        new_obs = np.zeros(self.n)
        new_obs[obs] = 1
        return new_obs


