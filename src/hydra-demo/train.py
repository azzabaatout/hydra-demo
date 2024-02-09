import hydra
from omegaconf import DictConfig

@hydra.main(config_path='../../project_config', config_name='app_config')
def train_model(cfg: DictConfig):
    # Training logic here
    print(f"Training with learning_rate={cfg.model.learning_rate}, "
          f"batch_size={cfg.model.batch_size}, "
          f"optimizer={cfg.model.optimizer}")

if __name__ == "__main__":
    train_model()
