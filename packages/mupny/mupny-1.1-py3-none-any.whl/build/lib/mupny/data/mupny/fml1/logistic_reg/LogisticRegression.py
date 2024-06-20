import numpy as np
np.random.seed(42)
class LogisticRegression:

    def __init__(self, learning_rate=1e-2, n_steps=2000, n_features=1, lmd=1):
        self.learning_rate = learning_rate
        self.n_steps = n_steps
        self.theta = np.random.rand(n_features)
        self.lmd = lmd
        self.lmd_ = np.full((n_features, ), lmd) # vettore riga
        self.lmd_[0] = 0
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def fit(self, X, y):
        """
        :param X:
        :param y:
        :return:
        Stochastic Gradient Descent
        — Updates model parameters using a single randomly selected training example at each iteration.
        — Fastest to converge but may have high variance in parameter updates.
        — Suitable for large datasets as it processes one data point at a time, saving memory.
        — May require more iterations to converge and may exhibit oscillations during training.
        """
        m = len(X)  # numero di sample nel dataset
        theta_history = np.zeros((self.n_steps, self.theta.shape[0]))  # matrice di zeri [n_steps*n_features]
        cost_history = np.zeros(self.n_steps)

        for step in range(self.n_steps):
            z = np.dot(X, self.theta)
            preds = self._sigmoid(z)
            error = preds - y

            self.theta = self.theta - ((1/m) * self.learning_rate * ( np.dot(X.T, error) + (self.theta.T * self.lmd_) ))
            theta_history[step, :] = self.theta.T

            # Cross-entropy loss with regularization
            loss = - (1/m) * (np.dot(y.T, np.log(preds)) + np.dot((1 - y.T), np.log(1-preds)))
            reg = ( self.lmd / (2*m) ) * np.dot(self.theta.T[1:], self.theta[1:])
            cost = loss + reg
            cost_history[step] = cost

        return cost_history

    def predict(self, X, threshold):
        z = np.dot(X, self.theta)
        preds = self._sigmoid(z)
        return preds >= threshold
