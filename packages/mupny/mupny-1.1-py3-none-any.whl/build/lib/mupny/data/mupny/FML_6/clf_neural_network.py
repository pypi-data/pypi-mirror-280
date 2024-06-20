# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from classification_metrics import ClassificationMetrics

# Set a seed for random number generation to ensure reproducibility
np.random.seed(42)


# Define the sigmoid activation function
def sigmoid(n):
    return 1 / (1 + np.exp(-n))


# Define the derivative of the sigmoid function
def sigmoid_derivative(n):
    return n * (1 - n)


# Define the NeuralNetwork class with specified parameters
class NeuralNetwork:
    # Initialize the neural network with layers, epochs, learning rate, and regularization parameter
    def __init__(self, layers, epochs=700, alpha=1e-2, lmd=1):
        self.layers = layers
        self.n_layers = len(layers)
        self.epochs = epochs
        self.alpha = alpha
        self.lmd = lmd

        # Initialize weights, biases, and loss variables
        self.w = {}
        self.b = {}
        self.loss = []
        self.loss_val = []

    # Initialize weights and biases for each layer randomly
    def init_parameters(self):
        for i in range(1, self.n_layers):
            self.w[i] = np.random.randn(self.layers[i], self.layers[i - 1])
            self.b[i] = np.ones((self.layers[i], 1))

    # Perform forward propagation through the neural network
    def forward_propagation(self, X):
        # Initialize a dictionary to store intermediate values during forward propagation
        values = {}
        # Iterate through all layers of the neural network, excluding the input layer
        for i in range(1, self.n_layers):
            if i == 1:
                # Compute the weighted sum for the first layer
                values["Z" + str(i)] = np.dot(self.w[i], X.T) + self.b[i]
            else:
                # Compute the weighted sum for subsequent layers
                values["Z" + str(i)] = np.dot(self.w[i], values["A" + str(i - 1)]) + self.b[i]

            # Apply the sigmoid activation function
            values["A" + str(i)] = sigmoid(values["Z" + str(i)])

        return values

    # Compute the cost function with L2 regularization
    def compute_cost(self, values, y):
        # Get the number of training examples
        m = y.shape[0]

        # Extract the predicted values from the forward propagation results
        pred = values["A" + str(self.n_layers - 1)]

        # Compute the cross-entropy loss
        cost = -np.average(y.T * np.log(pred) + (1 - y.T) * np.log(1 - pred))

        # Compute the L2 regularization term
        reg_sum = 0
        for i in range(1, self.n_layers):
            reg_sum += np.sum(np.square(self.w[i]))
        L2_reg = reg_sum * (self.lmd / (2 * m))

        # Return the total cost including regularization
        return cost + L2_reg

    # Compute the derivative of the cost function
    def compute_cost_derivative(self, values, y):
        # Compute the derivative of the cross-entropy loss
        return -(np.divide(y.T, values) - np.divide(1 - y.T, 1 - values))

    # Perform a single backpropagation step and update parameters
    def backpropagation_step(self, values, X, y):
        # Get the number of training examples
        m = y.shape[0]

        # Initialize a dictionary to store the parameter updates
        params_upd = {}

        # Initialize the derivative of the weighted sum
        dZ = None

        # Iterate backward through the layers of the neural network
        for i in range(self.n_layers - 1, 0, -1):
            if i == (self.n_layers - 1):
                # For the output layer, compute the derivative of the cost function
                dA = self.compute_cost_derivative(values["A" + str(i)], y)
            else:
                # For hidden layers, compute the derivative using the chain rule
                dA = np.dot(self.w[i + 1].T, dZ)

            # Compute the derivative of the weighted sum
            dZ = np.multiply(dA, sigmoid_derivative(values["A" + str(i)]))

            if i == 1:
                # Compute the weight and bias updates for the first layer
                params_upd["W" + str(i)] = (1 / m) * (np.dot(dZ, X) + self.lmd * self.w[i])
            else:
                # Compute the weight and bias updates for subsequent layers
                params_upd["W" + str(i)] = (1 / m) * (np.dot(dZ, values["A" + str(i - 1)].T) + self.lmd * self.w[i])

            # Compute the bias updates
            params_upd["B" + str(i)] = (1 / m) * np.sum(dZ, axis=1, keepdims=True)

        # Return the computed parameter updates
        return params_upd

    # Update weights and biases based on the calculated updates
    def update(self, upd):
        for i in range(1, self.n_layers):
            self.w[i] -= self.alpha * upd["W" + str(i)]
            self.b[i] -= self.alpha * upd["B" + str(i)]

    # Train the neural network on the provided data
    def fit(self, X_train, y_train, X_val=None, y_val=None):
        self.loss = []
        self.loss_val = []
        self.init_parameters()

        for i in range(self.epochs):
            # Perform forward and backward passes, and update parameters
            values = self.forward_propagation(X_train)
            grads = self.backpropagation_step(values, X_train, y_train)
            self.update(grads)

            # Compute and record the training loss
            cost = self.compute_cost(values, y_train)
            self.loss.append(cost)

    # Make predictions on new data
    def predict(self, X_test):
        values = self.forward_propagation(X_test)
        pred = values["A" + str(self.n_layers - 1)]
        return np.round(pred)

    # Compute classification performance metrics
    def compute_performance(self, X, y):
        pred = self.predict(X)
        metrics = ClassificationMetrics(y, pred[-1])
        return metrics.compute_errors()

    # Plot the training loss curve
    def plot_loss(self):
        plt.plot(self.loss)
        plt.xlabel("epochs")
        plt.ylabel("loss")
        plt.title("Loss curve")
        plt.show()