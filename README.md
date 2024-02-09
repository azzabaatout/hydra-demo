
# Getting Started with Hydra

## Introduction
Hydra is a powerful tool for managing configurations in your development environment, compatible with both Conda and Poetry. This guide will walk you through the installation process and demonstrate the main features of Hydra that can significantly enhance your project.

## Installation
To install Hydra, use one of the following commands based on your environment:

- **Using Poetry:**
  ```
  poetry add hydra-core
  ```

- **Using Conda:**
  ```
  pip install hydra-core
  ```

## Hierarchical Configuration Composable from Multiple Sources
Hydra is invaluable in projects requiring the management of multiple configuration files. It brings flexibility and scalability to your configuration management.

### Example Scenario
Imagine working with these configuration files:
- `model.yaml`: Model configurations.
- `dataset.yaml`: Dataset-specific settings.
- `training.yaml`: Training parameters.

We use a `config.yaml` that references these specific files instead of containing direct configurations.

#### Main Configuration File (config.yaml)
```yaml
default: 
  - model.yaml: model
  - dataset.yaml: dataset
  - training.yaml: training
```

#### Hydra in Action
```python
from hydra import main
from omegaconf import DictConfig

@main(config_path="project_config", config_name="app_config") 
def my_app(cfg: DictConfig) -> None:
    print(cfg)

if __name__ == "__main__":
    my_app()
```
Key Aspects:
- `@hydra.main(...)`: Decorator for functions needing configurations.
- Hydra merges configurations based on `config.yaml`.
- The working directory changes dynamically, enhancing flexibility.

## Configuration Specified or Overridden from the Command Line
Hydra's command-line flexibility is crucial for AI projects involving extensive experimentation. Parameters like learning rates, batch sizes, and optimizers can be easily modified without code changes.

### Configuring Model Training
```yaml
model:   
  name: "ResNet50"  
training:   
  batch_size: 32   
  learning_rate: 0.001   
  optimizer: "Adam"
```

Override parameters from the command line for rapid experimentation:
```shell
python train.py training.learning_rate=0.01 training.optimizer=SGD
```

## Dynamic Command Line Tab Completion
Hydra simplifies configuration adjustments through dynamic command line tab completion, aiding in quick, error-free modifications.

- Typing `python train.py` and pressing Tab shows all available parameters.
- Typing `learning_rate=` or `optimizer=` suggests common values.

Setting up dynamic tab completion involves configuring your shell environment and ensuring compatibility with Hydra.

## Running Multiple Jobs with Different Arguments
Hydra's Multi-Run feature is ideal for batch processing or extensive testing. It simplifies executing multiple runs with different configurations.

### Example
Running multiple training jobs with varying learning rates and optimizers:
1. Learning rate = 0.01, Optimizer = SGD
2. Learning rate = 0.01, Optimizer = Adam
3. Learning rate = 0.001, Optimizer = SGD
4. Learning rate = 0.001, Optimizer = Adam

Each run is executed with specified parameter combinations, showcasing Hydra's capability to manage and simplify complex tasks in parameter setting.