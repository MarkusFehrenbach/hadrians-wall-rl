from env.game_state import GameState
import numpy as np


if __name__ == "__main__":
    gs = GameState()
    obs = gs.to_observation()
    print("shape:", obs.shape)
    print("dtype:", obs.dtype)
    np.set_printoptions(precision=3, threshold=500)
    print(obs)