import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from omegaconf import DictConfig
import hydra
from simple_net import SimpleNet


@hydra.main(config_path='../../project_config', config_name='app_config')
def train_model(cfg: DictConfig):
    train_dataset = hydra.utils.instantiate(cfg.dataset)
    train_loader = DataLoader(train_dataset, batch_size=cfg.model.batch_size, shuffle=True)

    model = SimpleNet()
    model.train()

    criterion = nn.CrossEntropyLoss()

    optimizer = getattr(optim, cfg.model.optimizer)(model.parameters(), lr=cfg.model.learning_rate)

    for epoch in range(cfg.training.epochs):
        for batch in train_loader:
            inputs, targets = batch

            outputs = model(inputs)
            loss = criterion(outputs, targets)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch}: Loss = {loss.item()}")

    print("Training completed.")


if __name__ == "__main__":
    train_model()
