import gymnasium as gym
from gymnasium import spaces
import numpy as np
from env.game_state import GameState
from env.actions import N_ACTIONS, N_OBSERVATIONS
from env.rules import MAX_ROUNDS, get_valid_actions, apply_action, validate_action, get_final_score

class HadriansWallEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=(N_OBSERVATIONS, ),
            dtype=np.float32
        )

        self.action_space = spaces.Discrete(N_ACTIONS)

        self.state = None

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = GameState()
        obs = self.state.to_observation()
        return obs, {}
    
    def step(self, action):
        assert(validate_action(self.state, action), "Action is not valid")
        apply_action(self.state, action)
        obs = self.state.to_observation()
        done = (self.state.current_round > MAX_ROUNDS)
        reward = (get_final_score(self.state) if done else 0)
        return obs, reward, done, False, {}

    def get_valid_actions(self):
        return get_valid_actions(self.state)
    
    def render(self):
        print(f"Round {self.state.current_round}, Action {self.state.action_counter}")

    def close(self):
        pass