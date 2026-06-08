from typing import Any
import numpy as np

from sb3_contrib import MaskablePPO
from sb3_contrib.common.wrappers import ActionMasker
# from stable_baselines3.common.utils import get_linear_fn
from env.hadrians_env import HadriansWallEnv
from training.configs import EXPERIMENTS
from training.callbacks import ReduceLROnPlateauCallback
import argparse

def mask_fn(env: Any) -> np.ndarray:
    """Return action mask as a numpy array of booleans for ActionMasker."""
    return np.array(env.get_valid_actions(), dtype=bool)

def train(experiment_name, config):
    env = HadriansWallEnv()
    env = ActionMasker(env, mask_fn)

    callback = ReduceLROnPlateauCallback()

    model = MaskablePPO(
        "MlpPolicy",
        env,
        verbose=1,
        learning_rate=config["learning_rate"], # if isinstance(config["learning_rate"], float) else get_linear_fn(*config["learning_rate"], 1.0),
        n_steps=config["n_steps"],
        batch_size=config["batch_size"],
        ent_coef=config["ent_coef"],
        policy_kwargs=dict(net_arch=config["net_arch"]),
        tensorboard_log=f"./tensorboard/{experiment_name}/",
    )

    model.learn(
        total_timesteps=config["total_timesteps"],
        callback=callback
    )
    model.save(f"models/{experiment_name}")
    print(f"Saved model: models/{experiment_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment", type=str, default="baseline")
    args = parser.parse_args()

    config = EXPERIMENTS[args.experiment]
    train(args.experiment, config)
