import pandas as pd
import numpy as np


class LinearRegression:
    def __init__(self, learning_rate=1e-2, n_steps=2000, n_features=1, lmd=1):
        """
        :param learning_rate: learning rate value
        :param n_steps: number of epochs around gd
        :param n_features: number of features involved in regression
        :param lmd: regularization factor.

        lmd_ is an array useful when is necessary compute theta's update with regularization factor
        """
        self.learning_rate = learning_rate
        self.n_steps = n_steps
        # generiamo i parametri theta di partenza, uno per ogni feature.
        self.theta = np.random.rand(n_features)
        # parametro lambda per regolarizzazione
        """
        numpy.full
        Return a new array of given shape and type, filled with fill_value.
        >>> np.full((1, ), 100)
            array([100])
        >>> np.full((2, 2), 10)
            array([[10, 10],
                   [10, 10]])
        """
        self.lmd = lmd
        self.lmd_ = np.full((n_features, ), self.lmd)  # [100]
        self.lmd_[0] = 0

    def fit(self, X, y):
        # numero dei data sample (numero delle righe) / uguale a .shape[0]
        m = len(X)
        cost_history = np.zeros(self.n_steps)

        for step in range(0, self.n_steps):
            # np.dot = prodotto -> in questo caso tra una matrice e un vettore di 2 elementi (parametri theta)
            preds = np.dot(X, self.theta)

            # calcolo l'errore della predizione rispetto ai valori reali
            error = preds - y

            # calcolo i nuovi parametri theta secondo la formula del Gradient Descent
            self.theta = self.theta - (1/m * self.learning_rate * np.dot(X.T, error))

            # compongo la cost function -> mean squared error
            # np.dot(error.T, error) -> equivale ad elevare al quadrato la variabile error
            cost_history[step] = 1/(2*m) * np.dot(error.T, error)

        return cost_history

    def fit_reg(self, X, y):
        # numero dei data sample (numero delle righe) / uguale a .shape[0]
        m = len(X)
        cost_history = np.zeros(self.n_steps)

        for step in range(0, self.n_steps):
            # np.dot = prodotto -> in questo caso tra una matrice e un vettore di 2 elementi (parametri theta)
            preds = np.dot(X, self.theta)

            # calcolo l'errore della predizione rispetto ai valori reali
            error = preds - y

            # calcolo i nuovi parametri theta secondo la formula del Gradient Descent con la regolarizzazione
            self.theta = self.theta - ((1/m) * self.learning_rate * (np.dot(X.T, error) + self.theta.T * self.lmd_))

            # compongo la cost function -> mean squared error
            # np.dot(error.T, error) -> equivale ad elevare al quadrato la variabile error
            cost_history[step] = 1/(2*m) * (np.dot(error.T, error) + self.lmd * np.dot(self.theta.T[1:], self.theta[1:]))

        return cost_history

    def prediction(self, x):
        """
        perform a complete prediction about X samples
        :param x: test sample with shape (m, n_features)
        :return: prediction wrt X sample. The shape of return array is (m, )
        """
        x = np.c_[np.ones(x.shape[0]), x]

        return np.dot(x, self.theta)

    def learning_curves(self, X, y):
        m = len(x)
        cost_history = np.zeros(m)

        for i in range(m):
            c_h = self.fit_reg(X[:i+1], y[:i+1])
            cost_history[i] = c_h[-1]

        return cost_history
