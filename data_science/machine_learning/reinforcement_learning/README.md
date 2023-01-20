# Reinforcement Learning

## Q table

Exemple: [solving the frozen lake with a q table](https://colab.research.google.com/drive/1_MdDwZKi2DG_8t2kzBLEr_D664j1U09w?usp=share_link).

## DQN

## PPO
Proximal Policy Optimization (PPO) is a reinforcement learning (RL) algorithm that is designed to optimize the policy of an agent in a computationally efficient manner. PPO is an on-policy RL algorithm, which means that it uses the agent's current policy to generate data and update the policy.

PPO is an iterative algorithm that uses a combination of trust-region optimization and stochastic gradient descent to update the policy. The algorithm starts by collecting data using the current policy, then it optimizes the policy by maximizing an objective function that is a combination of the expected reward (i.e. the policy's value) and a penalty term that discourages the policy from changing too much.

PPO uses a "clip" mechanism to ensure that the policy updates are not too drastic, this mechanism clips the probability ratio between the new and old policy, this helps to avoid large policy updates that can lead to instability.

It is a widely used algorithm in RL because of its good performance and stability, it has been applied to many domains, such as robotics, video games, and simulations.

## Actor & Critics

## Suggested readings:
* "Reinforcement Learning" by Andrej Karpathy (https://karpathy.github.io/2016/05/31/rl/)
* "Deep Reinforcement Learning Hands-On" by Maxim Lapan (https://medium.com/@m.lapan/deep-reinforcement-learning-hands-on-part-i-q-learning-double-q-learning-and-prioritized-experience-replay-44ab5d87a2c)
* "RL Adventure" by Thomas Simonini (https://simoninithomas.github.io/Deep_reinforcement_learning_Course/)
* "Reinforcement Learning" by Pieter Abbeel and John Schulman (http://rail.eecs.berkeley.edu/deeprlcourse/)
* "RL Course by David Silver" (http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)

# Credits
This page has been made with (but not only) the help of [Open AI ChatGTP](https://chat.openai.com/).