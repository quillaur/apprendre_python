# Taken from: https://alexandervandekleut.github.io/deep-q-learning/

import numpy as np
import tensorflow as tf


class Agent:
    def __init__(self, state_shape, num_actions, num_envs, alpha=0.001, gamma=0.95, epsilon_i=1.0, epsilon_f=0.01, n_epsilon=0.1, hidden_sizes = []):
        self.epsilon_i = epsilon_i
        self.epsilon_f = epsilon_f
        self.n_epsilon = n_epsilon
        self.epsilon = epsilon_i
        self.gamma = gamma

        self.num_actions = num_actions
        self.num_envs = num_envs

        self.Q = tf.keras.models.Sequential()
        self.Q.add(tf.keras.layers.Input(shape=state_shape))
        for size in hidden_sizes:
            self.Q.add(tf.keras.layers.Dense(size, activation='relu', use_bias='false', kernel_initializer='he_uniform', dtype='float64'))
        self.Q.add(tf.keras.layers.Dense(self.num_actions, activation="linear", use_bias='false', kernel_initializer='zeros', dtype='float64'))
        
        # target network
        self.Q_ = tf.keras.models.Sequential()
        self.Q_.add(tf.keras.layers.Input(shape=state_shape))
        for size in hidden_sizes:
            self.Q_.add(tf.keras.layers.Dense(size, activation='relu', use_bias='false', kernel_initializer='he_uniform', dtype='float64'))
        self.Q_.add(tf.keras.layers.Dense(self.num_actions, activation="linear", use_bias='false', kernel_initializer='zeros', dtype='float64'))
        
        self.optimizer = tf.keras.optimizers.Adam(alpha)  
    
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

    def update(self, s_t, a_t, r_t, s_t_next, d_t):
        with tf.GradientTape() as tape:
            Q_next = tf.stop_gradient(tf.reduce_max(self.Q_(s_t_next), axis=1)) # note we use Q_ 
            Q_pred = tf.reduce_sum(self.Q(s_t)*tf.one_hot(a_t, self.num_actions, dtype=tf.float64), axis=1)
            loss = tf.reduce_mean(0.5*(r_t + (1-d_t)*self.gamma*Q_next - Q_pred)**2)
        grads = tape.gradient(loss, self.Q.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.Q.trainable_variables))