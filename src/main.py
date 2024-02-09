import hydra
from omegaconf import DictConfig


# add config path and config name with hydra
@hydra.main(config_path="../project_config", config_name="app_config")
def my_app(cfg: DictConfig) -> None:
    print(cfg)


if __name__ == "__main__":
    my_app()
