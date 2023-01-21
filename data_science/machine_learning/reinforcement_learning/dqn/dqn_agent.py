# Taken from: https://alexandervandekleut.github.io/deep-q-learning/

import numpy as np
import tensorflow as tf
import gym
import matplotlib.pyplot as plt
from tqdm.notebook import trange

from utils import ReplayBuffer


class Agent:
    def __init__(self, state_shape, num_actions, num_envs, alpha=0.001, gamma=0.95, epsilon_i=1.0, epsilon_f=0.01, n_epsilon=0.1, hidden_sizes = []):
        self.epsilon_i = epsilon_i
        self.epsilon_f = epsilon_f
        self.n_epsilon = n_epsilon
        self.epsilon = epsilon_i
        self.discount_factor = gamma
        self.learning_rate = alpha

        self.num_actions = num_actions
        self.state_shape = state_shape
        self.num_envs = num_envs

        self.Q = self.create_model()
        
        # target network
        self.Q_ = self.create_model()

        self.synchronize()

    def create_model(self):
        init = tf.keras.initializers.HeUniform()
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(24, input_shape=self.state_shape, activation='relu', kernel_initializer=init))
        model.add(tf.keras.layers.Dense(12, activation='relu', kernel_initializer=init))
        model.add(tf.keras.layers.Dense(self.num_actions, activation='linear', kernel_initializer=init))
        model.compile(loss=tf.keras.losses.Huber(), optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate), metrics=['mae'])

        return model
    
    def synchronize(self):
        self.Q_.set_weights(self.Q.get_weights())

    def act(self, s_t):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.num_actions, size=self.num_envs)
        return np.argmax(self.Q(s_t), axis=1)
    
    def decay_epsilon(self, n):
        self.epsilon = max(
            self.epsilon_f, 
            self.epsilon_i - (n/self.n_epsilon)*(self.epsilon_i - self.epsilon_f))

    def update(self, batches):
        # in one batch is a list of: [state, action, reward, state_next, done]
        X = []
        y = []
            
        actual_states = np.array([s[0] for s in batches])
        actual_preds = self.Q.predict(actual_states)
        next_states = np.array([s[3] for s in batches])
        target_preds = self.Q_.predict(next_states)

        for index, (state, action, reward, next_state, trunc, done) in enumerate(batches):
          if (not done) and (not trunc):
              max_future_q = reward + self.discount_factor * np.max(target_preds[index])
          else:
              max_future_q = reward

          current_qs = actual_preds[index]
          current_qs[action] = (1 - self.learning_rate) * current_qs[action] + self.learning_rate * max_future_q

          X.append(state)
          y.append(current_qs)
        
        self.Q.fit(X, y, batch_size=32, verbose=0, shuffle=True)
            



def train(env_name, T=20000, num_envs=32, batch_size=32, sync_every=100, hidden_sizes=[24, 24], alpha=0.001, gamma=0.95):
    env = gym.vector.make(env_name, num_envs=num_envs)
    state_shape = env.observation_space.shape
    num_actions = env.single_action_space.n
    agent = Agent(state_shape, num_actions, num_envs, alpha=alpha, hidden_sizes=hidden_sizes, gamma=gamma)
    rewards = []
    buffer = ReplayBuffer()
    episode_rewards = 0
    state, info = env.reset()
    for t in trange(T):
        if t%sync_every == 0:
            agent.synchronize()
        
        action = agent.act(state)
        state_next, reward, done, trunc, info = env.step(action)
        buffer.remember(state, action, reward, state_next, trunc, done)
        state = state_next

        agent.update(buffer.sample(batch_size))
        agent.decay_epsilon(t/T)
        episode_rewards += reward

        for i in range(env.num_envs):
            if done[i] or trunc[i]:
                rewards.append(episode_rewards[i])
                episode_rewards[i] = 0
                state[i] = env.reset_at(i)
            
    # plot(pd.DataFrame(rewards), window=10)
    plt.plot(rewards)
    return agent