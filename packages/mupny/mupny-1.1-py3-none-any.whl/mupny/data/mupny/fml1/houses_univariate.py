

import pandas as pd
import numpy as np
from linear_regression import LinearRegression
import matplotlib.pyplot as plt

# read dataset
houses = pd.read_csv('./data/houses.csv')

# descrivere il dataset
print(houses.describe())

# shuffle the dataset
# random state for reproducibility
houses = houses.sample(frac=1, random_state=42).reset_index(drop=True)

# x = houses['LotArea'] -> descrive la colonna, mentre con .values otteniamo un array di valori
x = houses['LotArea'].values
y = houses['SalePrice'].values

plt.plot(x, y, 'r.')
plt.show()

# another way to test the correlation
print(pd.DataFrame(list(zip(x, y)), columns=['LotArea', 'SalePrice']).corr())

# training set 80% del dataset
# round serve per prendere il numero intero
train_index = round(len(x) * 0.8)
x_train = x[:train_index]
y_train = y[:train_index]

# test set 20% del dataset
x_test = x[train_index:]
y_test = y[train_index:]

# media e deviazione standard dei valori delle feature x
# la calcoliamo solo sui dati di training perchè in realtà
#   non sappiamo nulla sui dati di test
# axis=0 serve per calcolare la media per colonna (non per riga)
mean = x_train.mean(axis=0)
std = x_train.std(axis=0)

# z-score normalization
x_train = (x_train - mean)/std
x_test = (x_test - mean)/std

# validation set 30% del training set

# validation_index = round(train_index * 0.7)
# x_validation = x_train[validation_index:]
# y_validation = y_train[validation_index:]

# nuovo training set 70% del training set originario (sottratto il validation set)
# x_train = x_train[:validation_index]
# y_train = y_train[:validation_index]

# aggiungiamo la colonna bias (theta_0) ad entrambi i dataset training e validation
# .shape[0] indica di prendere il numero di righe della matrice
"""
# ############## np.c_ ###############
# np.c_[np.array([1,2,3]), np.array([4,5,6])]
# array([[1, 4],
#        [2, 5],
#        [3, 6]])
# np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]
# array([[1, 2, 3, ..., 4, 5, 6]])
"""
x_train = np.c_[np.ones(x_train.shape[0]), x_train]
# x_validation = np.c_[np.ones(x_validation.shape[0]), x_validation]

# ---------------------------- Linear Regression ----------------------------------
# buildiamo la classe passando i parametri che vogliamo.
# .shape[1] indica di prendere il numero di colonne della matrice
lr = LinearRegression(learning_rate=0.0001,
                      n_steps=50000,
                      n_features=x_train.shape[1],
                      lmd=50)

# alleno il modello e ottengo la cost history,
# ovvero la funzione costo (pred - y) dovrebbe essere minore possibile
cost_history = lr.fit(x_train, y_train)

print(f'''Thetas: {*lr.theta, }''')
print(f'''Final train cost / MSE {cost_history[-1]:.3f}''')

plt.plot(range(lr.n_steps), cost_history, 'r-', label='Cost function')
plt.legend()
plt.xlabel("n° steps cost function")
plt.ylabel("errore tra predizione e valori target")
plt.show()

# calcoliamo le predizioni sui dati di training
lineX = np.linspace(x_train[:, 1].min(), x_train[:, 1].max(), 100)
lineY = [lr.theta[0] + lr.theta[1]*xx for xx in lineX]

plt.plot(x_train[:, 1], y_train, 'r.', label='Training data')
plt.plot(lineX, lineY, 'b--', label='Current hypothesis')
plt.legend()
plt.show()

mae = np.average(np.abs(lr.prediction(x_test) - y_test))
print(f'''MAE on test set: {mae:.3f}''')

