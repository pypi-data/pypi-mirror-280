import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class NeuralNetwork():

    def __init__(self, learning_rate=0.001, lmd=0, epochs=100, layers=[]):
        self.w = {}
        self.b = {}
        self.layers = layers
        self.n_layers = len(layers)
        self.learning_rate = learning_rate
        self.lmd = lmd
        self.epochs = epochs
        self.loss = []
        self.X = None  # no
        self.y = None  # no

        self.A = {}
        self.Z = {}
        self.dW = {}
        self.dB = {}
        self.dA = {}
        self.dZ = {}

    # Initialize weights and bias for each layer randomly
    def init_parameters(self):
        for i in range(1, self.n_layers):
            self.w[i] = np.random.randn(self.layers[i], self.layers[i-1])
            self.b[i] = np.ones((self.layers[i], 1))

    def sigmoid(self, z):
        return 1 / ( 1 + np.exp(-z) )

    def sigmoid_derivative(self, A):
        return A * (1 - A)

    def forward_propagation(self):
        layers = len(self.w)
        # Inizialize a dictonary to store intermediate values during forward propagation
        values = {}

        # Iterate through all layers of the neural network, excluding the input layer
        for i in range(1, layers):
            if i == 1:
                # Compute the weighted sum for the first layer
                values['Z'+str(i)] = np.dot(self.w[i], self.X.T) + self.b[i]
            else:
                # Compute the weighted sum for subsequent layers
                values['Z'+str(i)] = np.dot(self.w[i], values['A'+str(i-1)]) + self.b[i]
            # Apply the weighted sum for subsequent layers
            values['Z' + str(i)] = self.sigmoid(values['Z' + str(i)])

        return values

    def compute_cost(self, A):
        m = self.y.shape[0]
        layers = len(A)
        Y_pred = A['A'+str(self.n_layers)]

        cost = -np.average(self.y.T * np.log(Y_pred) + (1 - self.y.T) * np.log(1- Y_pred))
        reg_sum = 0
        for l in range(l, layers):
            reg_sum += (np.sum(np.square(self.w[l])))
        L2_reg = reg_sum + (self.lmd / (2*m))

        return cost + L2_reg

    def compute_cost_derivative(self, A):
        # Compute the derivative of the cross-entropy loss
        return -(np.divide(self.y.T, A) - np.divide(1 - self.y.T, 1 - A))

    def backpropagation_step(self, values):
        layers = len(self.w)
        m = self.X.shape[0]
        params_upd = {}
        for i in range(layers, 0, -1):
            if i == layers:
                dA = self.compute_cost_derivative(values['A'+str(i)])
            else:
                dA = np.dot(self.m[i+1].T, dZ)

            # Compute the derivative of the weighted sum
            dZ = np.multiply(dA, self.sigmoid_derivative(values['A'+str(i)]))

            if i == 1:
                params_upd['W'+str(i)] = (1/m) * np.dot(dZ, self.X) + self.lmd * self.w[i]
                params_upd['B'+str(i)] = (1/m) * np.sum(dZ, axis=1, keepdims=True)
            else:
                params_upd['W'+str(i)] = (1/m) * np.dot(dZ, values['A'+str(1-1)].T) + self.lmd * self.w[i]
                params_upd['B'+str(i)] = (1/m) * np.sum(dZ, axis=1, keepdims=True)

        return params_upd

    def update(self, upd):
        for i in range(1, self.n_layers):
            self.w[i] = self.w[i] - self.learning_rate * upd['W'+str(i)]
            self.b[i] = self.b[i] - self.learning_rate * upd['B'+str(i)]

    def fit(self, X, y):
        self.X = X
        self.y = y
        self.init_parameters()

        for i in range(self.epochs):
            # Perform forward and backward propagation, and update parameters
            A_list = self.forward_propagation()
            grads = self.backpropagation_step(A_list)
            cost = self.compute_cost(A_list)
            self.update(grads)
            self.loss.append(cost)

    def plot_loss(self):
        plt.plot(self.loss)
        plt.xlabel("epochs")
        plt.ylabel("loss")
        plt.title("Loss curve")
        plt.show()