import numpy as np
from env.hadrians_env import HadriansWallEnv

from env.actions import ACTION_END_ROUND, ACTION_ADVANCE_PRIESTS_TRACK

if __name__ == "__main__":
    env = HadriansWallEnv()
    max_reward = -23

    for i in range(1000):
        obs, _ = env.reset()

        done = False
        total_steps = 0

        while not done:
            # Get valid actions
            valid = env.get_valid_actions()
            valid_indices = np.where(valid)[0]

            if len(valid_indices) == 0:
                print("No valid actions - something went wrong")
                break

            # Pick a random valid action
            action = np.random.choice(valid_indices)
            if len(valid_indices) > 1:
                while action == ACTION_END_ROUND:
                    action = np.random.choice(valid_indices)

            # Step in environment
            obs, reward, done, truncated, info = env.step(action)
            total_steps += 1

            # print(f"Action: {action}")
            # env.render()
            # print()
            # print("-------------------------------------------------------------")

        max_reward = max(max_reward, reward)
        print(f"Game {i+1} finished in {total_steps} steps")
        print(f"Final score: {reward} (max: {max_reward})")
