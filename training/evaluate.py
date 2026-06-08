from sb3_contrib import MaskablePPO
from sb3_contrib.common.wrappers import ActionMasker
from env.hadrians_env import HadriansWallEnv

def mask_fn(env: HadriansWallEnv):
    return env.get_valid_actions()

def evaluate(model_path, n_games=1):
    base_env = HadriansWallEnv()
    env = ActionMasker(base_env, mask_fn)

    model = MaskablePPO.load(model_path, env=env)

    max_reward = -23

    for i in range(n_games):
        # Get valid actions
        obs, _ = env.reset()
        done = False
        total_steps = 0

        while not done:
            # Apply action mask
            action_masks = base_env.get_valid_actions()

            # Step in environment
            action, _ = model.predict(
                obs,
                deterministic=True,
                action_masks=action_masks,
            )
            obs, reward, done, _, _ = env.step(int(action))
            total_steps += 1

            # print(f"Action: {action}")
            # env.render()
            # print()
            # print("-------------------------------------------------------------")
        
        max_reward = max(reward, max_reward)
        print(f"Game {i+1} finished in {total_steps} steps")
        print(f"Final score: {reward} (max: {max_reward})")

if __name__ == "__main__":
    evaluate("models/baseline", n_games=1000)
