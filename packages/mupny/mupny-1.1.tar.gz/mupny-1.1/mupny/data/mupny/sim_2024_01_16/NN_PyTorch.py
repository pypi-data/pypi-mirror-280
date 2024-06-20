import torch
from torch import nn
from torch import optim

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size_1, hidden_size_2, output_size):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size_1)  # First layer -> Hidden Layer
        self.fc2 = nn.Linear(hidden_size_1, hidden_size_2)  # Hidden Layer -> Hidden Layer
        self.fc3 = nn.Linear(hidden_size_2, output_size)  # Hidden Layer -> Output
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x

    # Calculate accuracy (for classification classification metric)
    def accuracy_fn(self, y_true, y_pred):
        correct = torch.eq(y_true, y_pred).sum().item()  # torch.eq() calculates where two tensors are equal
        acc = (correct / len(y_pred)) * 100
        return acc


def mae(pred, y):
    error = pred - y
    return torch.mean(torch.abs(error))

def mse(pred, y):
    error = pred - y
    return torch.mean(error ** 2)

def mape(pred, y):
    error = pred - y
    return torch.mean(torch.abs(error / y)) * 100
