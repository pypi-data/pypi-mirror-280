import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from torch import nn, optim


def mae(pred, y):
    error = pred - y
    return torch.mean(torch.abs(error))


def mape(pred, y):
    error = pred - y
    return torch.mean(torch.abs(error/y)) * 100


class Neural_Network(nn.Module):

    def _init_(self, input_size, hidden_size, output_size):
        super(Neural_Network, self)._init_()
        self.layer_1 = nn.Linear(input_size, hidden_size[0])
        self.layer_2 = nn.Linear(hidden_size[0], hidden_size[1])
        self.layer_3 = nn.Linear(hidden_size[1], output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.layer_1(x)
        x = self.sigmoid(x)
        x = self.layer_2(x)
        x = self.sigmoid(x)
        x = self.layer_3(x)
        return x


salaries = pd.read_csv('ds_salaries new.csv')

# shuffle dei dati

salaries = salaries.sample(frac=1, random_state=42).reset_index(drop=True)

# rimuovo salary poichè è ridondante e rimuovo salary_currency perchè non ci da alcuna informazione.

salaries.drop(['salary', 'salary_currency'], axis=1, inplace=True)

# rimozione di duplicati

salaries.drop_duplicates(inplace=True, ignore_index=True)

outlier_batch = salaries['salary_in_usd'].copy()
q1 = np.percentile(outlier_batch, 25)
q3 = np.percentile(outlier_batch, 75)
iqr = q3 - q1
lower_bound = q1 - (iqr * 1.5)
upper_bound = q3 + (iqr * 1.5)
lower_mask = outlier_batch < lower_bound
upper_mask = outlier_batch > upper_bound
outlier_batch[lower_mask | upper_mask] = np.nan
salaries['salary_in_usd'] = outlier_batch

salaries.dropna(inplace=True, ignore_index=True)  # rimuove righe con nan (outlier e missing values)

y = salaries['salary_in_usd'].values

categorical_features = ['work_year', 'experience_level', 'employment_type', 'job_title', 'employee_residence',
                        'remote_ratio', 'company_location', 'company_size']
x = salaries.drop('salary_in_usd', axis=1)
x = pd.get_dummies(data=x, columns=categorical_features).values

# non facciamo la z-score perchè sono tutte features categoriche

torch.manual_seed(42)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)

# holdout dei dati
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)

# passaggio ai tensori

x_train = torch.from_numpy(x_train).float().to(device)
x_test = torch.from_numpy(x_test).float().to(device)
y_train = torch.from_numpy(y_train).float().to(device)
y_test = torch.from_numpy(y_test).float().to(device)

min_loss = 10e100
for lr in [0.0001, 0.001, 0.01, 0.1]:
    for C in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]:
        model = Neural_Network(input_size=x_train.shape[1], hidden_size=[5, 3], output_size=1).to(device)
        epochs = 100
        optimizer = optim.SGD(model.parameters(), lr=lr, weight_decay=C)
        criterion = nn.MSELoss()

        for epoch in range(epochs):
            model.train()
            train_output = model(x_train)
            train_output = train_output.squeeze()
            train_loss = criterion(train_output, y_train)
            train_loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            model.eval()
            with torch.inference_mode():
                test_output = model(x_test)
                test_output = test_output.squeeze()
                test_loss = criterion(test_output, y_test)
                if test_loss < min_loss:
                    min_loss = test_loss
                    best_hyperparameters = {'lr': lr, 'C': C}
                    test_mae = mae(test_output, y_test)
                    test_mape = mape(test_output, y_test)
                    train_mae = mae(train_output, y_train)
                    train_mape = mape(train_output, y_train)

print(f'Best_HyperParameters: {best_hyperparameters}')
print(f'Best_Loss: {min_loss}')
print(f'Train MAE: {train_mae} | Test MAE: {test_mae}')
print(f'Train MAPE: {train_mape} | Test MAPE: {test_mape}')