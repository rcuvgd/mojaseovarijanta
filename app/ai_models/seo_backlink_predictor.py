import torch
import torch.nn as nn
import torch.optim as optim
from typing import List

class SEOBacklinkPredictor(nn.Module):
    def __init__(self, input_size: int = 8):
        super(SEOBacklinkPredictor, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 3)  # Output: [backlinks_top10, backlinks_top3, backlinks_top1]
        )

    def forward(self, x):
        return self.model(x)

def train_model(model, X_train, y_train, epochs=100, lr=0.001):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

def predict_backlinks(model, input_features: List[float]) -> List[float]:
    model.eval()
    with torch.no_grad():
        inputs = torch.tensor([input_features], dtype=torch.float32)
        outputs = model(inputs).numpy()[0]
    return [round(x) for x in outputs]
