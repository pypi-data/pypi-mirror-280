import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from LogisticRegression import LogisticRegression
plt.style.use(['ggplot'])
np.random.seed(42)

# read the dataset
diabetes = pd.read_csv('../data/diabetes.csv')

# Print dataset stats
print(diabetes.describe())
print(diabetes.columns)

# Shuffling all samples to avoid group bias
diabetes = diabetes.sample(frac=1).reset_index(drop=True)

# Select the features
X = diabetes.drop(['Outcome'], axis=1).values  # axis = 1 tutte le righe
# selected_features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#        'BMI', 'DiabetesPedigreeFunction', 'Age']
# X = diabetes[selected_features].values

# Select the target value
y = diabetes['Outcome'].values

# Perform train-test split
train_index = round(len(X) * 0.8)

X_train = X[:train_index]
y_train = y[:train_index]

X_test = X[train_index:]
y_test = y[train_index:]

# Compute mean and standard deviation ONLY ON TRAINING SAMPLES
mean = X_train.mean(axis=0)  # axis=0 -> media per colonna
std = X_train.std(axis=0)    # axis=0 -> deviazione standard per colonna

# Apply mean and std computed on the training samples to training set and test set
X_train = (X_train - mean) / std
X_test = (X_test - mean) / std

# Add a column of ones for the bias term
X_train = np.column_stack((np.ones(X_train.shape[0]), X_train))
X_test = np.column_stack((np.ones(X_test.shape[0]), X_test))
""" np.column_stack
>>> a = np.array((1,2,3))
>>> b = np.array((2,3,4))
>>> np.column_stack((a,b))
    array([[1, 2],
           [2, 3],
        [3, 4]])

Alternativa con np.c_
>>> X_train = np.c_[np.ones(X_train.shape[0], X_train]
"""

logistic_sgd = LogisticRegression(learning_rate=0.05,
                                  n_steps=1000,
                                  n_features=X_train.shape[1],
                                  lmd=0)

cost_history = logistic_sgd.fit(X_train, y_train)

print(f'''Thetas: {*logistic_sgd.theta, }''')
print(f'''Final train BCE {cost_history[-1]:.3f}''')

plt.plot(range(logistic_sgd.n_steps), cost_history, 'r-', label='Cost function')
plt.legend()
plt.xlabel("n° steps cost function")
plt.ylabel("errore tra predizione e valori target")
plt.show()

preds = logistic_sgd.predict(X_test, threshold=0.5)

print(f'''Performance: {(preds == y_test).mean()}''')
