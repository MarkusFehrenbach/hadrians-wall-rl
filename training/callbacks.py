from stable_baselines3.common.callbacks import BaseCallback
import numpy as np

class ReduceLROnPlateauCallback(BaseCallback):

    def __init__(
        self,
        patience: int = 50,
        factor: float = 0.5,
        min_lr: float = 1e-5,
        eval_freq: int = 10_000,
        verbose: int = 1
    ):
        super().__init__(verbose)
        self.patience = patience
        self.factor = factor
        self.min_lr = min_lr
        self.eval_freq = eval_freq

        self.best_mean_reward = -np.inf
        self.steps_without_improvement = 0
        self.current_lr = None
    
    def _on_training_start(self) -> None:
        self.current_lr = self.model.learning_rate
        if callable(self.current_lr):
            self.current_lr = self.current_lr(1.0)
    
    def _on_step(self):
        if self.n_calls % self.eval_freq != 0:
            return True

        if self.model.ep_info_buffer is not None:
            if len(self.model.ep_info_buffer) == 0:
                return True

            mean_reward = np.mean([
                ep["r"] for ep in self.model.ep_info_buffer
            ])

            if mean_reward > self.best_mean_reward:
                self.best_mean_reward = mean_reward
                self.steps_without_improvement = 0
                if self.verbose:
                    print(f"New best mean reward: {mean_reward:.2f}")
            else:
                self.steps_without_improvement += 1
                if self.verbose:
                    print(f"No improvement for {self.steps_without_improvement} evaluations "
                          f"(best: {self.best_mean_reward:.2f}, current: {mean_reward:.2f})")
            

            if isinstance(self.current_lr, float):
                if self.steps_without_improvement >= self.patience:
                    new_lr = max(self.current_lr * self.factor, self.min_lr)
                    if new_lr < self.current_lr:
                        self.current_lr = new_lr
                        self.model.lr_schedule = lambda _: new_lr
                        self.steps_without_improvement = 0
                        self.best_mean_reward = -np.inf
                        if self.verbose:
                            print(f"Reducing LR to {new_lr:.2e}")
            
        return True