# Taken from https://alexandervandekleut.github.io/deep-q-learning/

from collections import deque
import random
import gym
import numpy as np
import matplotlib.pyplot as plt
from tqdm.notebook import trange

from dqn_agent import Agent


class ReplayBuffer:
    def __init__(self, size=1000000):
        self.memory = deque(maxlen=size)
        
    def remember(self, s_t, a_t, r_t, s_t_next, d_t):
        self.memory.append((s_t, a_t, r_t, s_t_next, d_t))
        
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



class VectorizedEnvWrapper(gym.Wrapper):
    def __init__(self, make_env, num_envs=1):
        super().__init__(make_env())
        self.num_envs = num_envs
        self.envs = [make_env() for env_index in range(num_envs)]
    
    def reset(self):
        return np.asarray([env.reset() for env in self.envs])
    
    def reset_at(self, env_index):
        return self.envs[env_index].reset()
    
    def step(self, actions):
        next_states, rewards, dones, infos = [], [], [], []
        for env, action in zip(self.envs, actions):
            next_state, reward, done, info = env.step(action)
            next_states.append(next_state)
            rewards.append(reward)
            dones.append(done)
            infos.append(info)
        return np.asarray(next_states), np.asarray(rewards), \
            np.asarray(dones), np.asarray(infos)


def train(env_name, T=20000, num_envs=32, batch_size=32, sync_every=100, hidden_sizes=[24, 24], alpha=0.001, gamma=0.95):
    env = VectorizedEnvWrapper(lambda: gym.make(env_name), num_envs)
    state_shape = env.observation_space.shape
    num_actions = env.action_space.n
    agent = Agent(state_shape, num_actions, num_envs, alpha=alpha, hidden_sizes=hidden_sizes, gamma=gamma)
    rewards = []
    buffer = ReplayBuffer()
    episode_rewards = 0
    s_t = env.reset()
    for t in trange(T):
        if t%sync_every == 0:
            agent.synchronize()
        
        a_t = agent.act(s_t)
        s_t_next, r_t, d_t, info = env.step(a_t)
        buffer.remember(s_t, a_t, r_t, s_t_next, d_t)
        s_t = s_t_next
        for batch in buffer.sample(batch_size):
            agent.update(*batch)
        agent.decay_epsilon(t/T)
        episode_rewards += r_t

        for i in range(env.num_envs):
            if d_t[i]:
                rewards.append(episode_rewards[i])
                episode_rewards[i] = 0
                s_t[i] = env.reset_at(i)
            
    # plot(pd.DataFrame(rewards), window=10)
    plt.plot(rewards)
    return agent