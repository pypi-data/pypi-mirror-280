import gymnasium as gym
from gymnasium import spaces
import numpy as np
from sim_class import Simulation


class OT2Env(gym.Env):
    def __init__(self, render=False, max_steps=1000):
        super(OT2Env, self).__init__()
        self.render = render
        self.max_steps = max_steps

        # Create the simulation environment
        self.sim = Simulation(num_agents=1)

        # Define action and observation space
        # They must be gym.spaces objects

        self.action_space = spaces.Box(low=-1, high=1, shape=(3,), dtype=np.float32)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(6,), dtype=np.float32)

        # keep track of the number of steps
        self.steps = 0

    def reset(self, seed=None):
        # being able to set a seed is required for reproducibility
        if seed is not None:
            np.random.seed(seed)

        self.goal_position = np.array(
            [np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(0.5, 0.5)], dtype=np.float32
        )

        # Call the environment reset function
        observation = self.sim.reset(num_agents=1)

        pipette_pos = np.array(observation[next(iter(observation))]['pipette_position'], dtype=np.float32)
        observation = np.concatenate([pipette_pos, self.goal_position], axis=0)

        self.steps = 0

        return observation

    def step(self, action):
        # Execute one time step within the environment
        action = np.append(action, 0)

        # Call the environment step function
        observation = self.sim.run([action])

        pipette_pos = np.array(observation[next(iter(observation))]['pipette_position'], dtype=np.float32)
        observation = np.concatenate([pipette_pos, self.goal_position], axis=0)

        # Calculate the reward, this is something that you will need to experiment with to get the best results
        reward = -np.linalg.norm(pipette_pos - self.goal_position)

        distance_threshold = 0.05
        distance = np.linalg.norm(pipette_pos - self.goal_position)

        if distance < distance_threshold:
            terminated = True
            reward = 1
        else:
            terminated = False

        if self.steps > self.max_steps:
            truncated = True
        else:
            truncated = False

        self.steps += 1

        info = {}
        return observation, reward, terminated, truncated, info

    def render(self, mode='human'):
        pass

    def close(self):
        self.sim.close()


# %%
