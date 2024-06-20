import pandas as pd
import numpy as np
from neural_network_classification import NeuralNetwork

np.random.seed(42)

diabetes_df = pd.read_csv('data/diabetes.csv')

print(diabetes_df.shape)
print(diabetes_df.describe())
print(diabetes_df.isna().sum())  # quanti elementi nulli nella feature
print(diabetes_df.dtypes)

# shuffle to avoid group bias
diabetes_df = diabetes_df.sample(frac=1).reset_index(drop=True)

X = diabetes_df.drop(['Outcome'], axis=1).values
y_label = diabetes_df['Outcome'].values

train_index = round(len(X)*0.8)
X_train = X[:train_index]
y_label_train = y_label[:train_index]

X_test = X[train_index:]
y_label_test = y_label[train_index:]

mean = X_train.mean(axis=0)
std = X_train.std(axis=0)

X_train = (X_train - mean)/std
X_test = (X_test - mean)/std

nn = NeuralNetwork(learning_rate=0.001, epochs=100, lmd=10, layers=[X_train.shape[1], 50, 1])
nn.fit(X_train, y_label_train)
nn.plot_loss()
