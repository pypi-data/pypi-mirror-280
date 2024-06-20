import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch.cuda
import NN_PyTorch
import utilities
from utilities import *
from sklearn.model_selection import train_test_split
# Neural network with pytorch
from torch import nn
from torch import optim

# Load and describe dataset
salaries = pd.read_csv('dataset/ds_salaries new.csv')
utilities.describe_dataframe( salaries )

# Drop unuseful features
salaries.drop( ['salary', 'salary_currency'], axis=1, inplace=True )

# Replace missing values
salaries = utilities.replace_missing_values( salaries )

for feature in ["salary_in_usd"]:
    # Outliers replaced with np.nan
    salaries[feature] = utilities.handle_outliers( salaries[feature] )

    # Handle np.nan generated from outliers removal (can be removed or substituted with mean/median value)
    salaries[[feature]] = utilities.impute_missing_values( salaries[[feature]] )  # Using [['column name']] we obtain a DataFrame instead of Series
print( "---------- Null values after outliers removal ----------" )
print( salaries.isna().sum() )

# Remove duplicates
salaries.drop_duplicates(inplace=True)

# shuffling all samples to avoid group bias
salaries = salaries.sample(frac=1).reset_index(drop=True)

# feature selection - all of these are categorical
selected_features = ['work_year', 'experience_level', 'employment_type',
                     'job_title', 'employee_residence', 'remote_ratio',
                     'company_location', 'company_size']
# -- We can also drop target value to get all remaining features
# -- x = salaries.drop('salary_in_usd', axis=1)

# Data transformation/manipulation
# -- get_dummies convert categorical variable into dummy/indicator variables.
X = pd.get_dummies( salaries[selected_features] )
# -- pd.get_dummies(data=X, columns=categorical_features)
X = X.values
# Select target value
y = salaries['salary_in_usd'].values

# train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# data normalization
'''
# In this case normalization has no sense, because feature X are categorical (also encoded with get_dummies()). 
X_train, X_test = normalization(X_train, X_test)
y_train, y_test = normalization(y_train.reshape(-1, 1), y_test.reshape(-1, 1))
y_train = y_train.reshape(1, -1)
y_test = y_test.reshape(1, -1)
'''

print("end preprocessing")

# ######## Neural Network with pytorch ##########
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

torch.manual_seed(42)
# Passing to tensor
X_train = torch.from_numpy(X_train.astype('int')).float().to(device)  # .astype('int') to convert True/False into 1/0
X_test = torch.from_numpy(X_test.astype('int')).float().to(device)
y_train = torch.from_numpy(y_train).float().to(device)
y_test = torch.from_numpy(y_test).float().to(device)

min_loss = 100e100
for lr in [0.1, 0.01, 0.001, 0.0001]:
    for c in [100, 10, 1, 0.5, 0.01, 0.001, 0 ]:

        model = NN_PyTorch.NeuralNetwork( input_size=X.shape[1], hidden_size_1=5, hidden_size_2=3, output_size=1 ).to(device)
        loss_func = nn.MSELoss()  # How wrong we are with respect to predictions
        optimizer = optim.SGD( model.parameters(), lr=lr, weight_decay=c )  # Tells your model how to update its internal parameters to best lower the loss

        epochs = 3000
        for epoch in range(epochs):
            model.train()  # we just inform the model that we are training it
            y_train_pred = model(X_train)  # we obtain the predictions on training set
            y_train_pred = y_train_pred.squeeze()  # we adapt predicion size to our labels [2062x1] -> [2062] altrimenti non potremmo confrontarlo con y_train [2062]
            loss = loss_func(y_train_pred, y_train)  # compute loss function
            y_train_pred = torch.round(y_train_pred).float()  # transform predictions in labels (arrotondamento)
            # compute loss gradients with respect to model's paramters
            loss.backward()
            # update the model parameters based on the computed gradients
            optimizer.step()
            # In PyTorch, for example, when you perform backpropagation to compute
            # the gradients of the loss with respect to the model parameters, these
            # gradients accumulate by default through the epochs. Therefore, before
            # computing the gradients for a new batch, it's a common practice to zero
            # them using this line to avoid interference from previous iterations.
            optimizer.zero_grad()
            model.eval()
            # we are doing inference: we don't need to compute gradients
            with torch.inference_mode():
                # 1. Forward pass
                y_test_pred = model(X_test)
                y_test_pred = y_test_pred.squeeze()
                test_loss = loss_func(y_test_pred, y_test)
                y_test_pred = torch.round(y_test_pred).float()
                if test_loss < min_loss:
                    min_loss = test_loss
                    best_hyperparameters = {'lr': lr, 'c': c}

            if (epoch % 20) == 0:  # ogni 20 epoche printa
                print(f"Epoch: {epoch} | Loss: {loss:.5f} | Test Loss: {test_loss:.5f}")

print(f'Best hyperparameters: {best_hyperparameters}')
