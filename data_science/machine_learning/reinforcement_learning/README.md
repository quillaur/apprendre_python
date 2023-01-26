# Reinforcement Learning

## Q table

Exemple: [solving the frozen lake with a q table](https://github.com/quillaur/data_learning/blob/main/data_science/machine_learning/reinforcement_learning/frozen_lake_q_table.ipynb).

## [DQN](https://github.com/quillaur/data_learning/tree/main/data_science/machine_learning/reinforcement_learning/dqn)
DQN (Deep Q-Network) is a type of reinforcement learning algorithm that uses a neural network to approximate the Q-value function. It is used to train an agent to make decisions in an environment by maximizing the expected cumulative reward. The DQN algorithm was first introduced in a 2015 paper by Google DeepMind, and has since been used in many RL applications.

Exemple: [solving the CartPole with a DQN agent](https://github.com/quillaur/data_learning/blob/main/data_science/machine_learning/reinforcement_learning/dqn/cartpole_dqn_test.ipynb).

## PPO
Proximal Policy Optimization (PPO) is a reinforcement learning (RL) algorithm that is designed to optimize the policy of an agent in a computationally efficient manner. PPO is an on-policy RL algorithm, which means that it uses the agent's current policy to generate data and update the policy.

PPO is an iterative algorithm that uses a combination of trust-region optimization and stochastic gradient descent to update the policy. The algorithm starts by collecting data using the current policy, then it optimizes the policy by maximizing an objective function that is a combination of the expected reward (i.e. the policy's value) and a penalty term that discourages the policy from changing too much.

PPO uses a "clip" mechanism to ensure that the policy updates are not too drastic, this mechanism clips the probability ratio between the new and old policy, this helps to avoid large policy updates that can lead to instability.

It is a widely used algorithm in RL because of its good performance and stability, it has been applied to many domains, such as robotics, video games, and simulations.

## Actor & Critics

## Suggested readings:
* [Full course by Alexander Vandekleut](https://alexandervandekleut.github.io/)

# Credits
This page has been made with (but not only) the help of [Open AI ChatGTP](https://chat.openai.com/).