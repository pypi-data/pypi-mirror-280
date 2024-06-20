from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

class KMeans(object):
    def __init__(self, n_cluster=2, dist=euclidean_distances, random_state=42):
        """
        Class KMeans for implementing the K-Means clustering algorithm.

        Parameters:
        - n_clusters: Number of clusters to form (default: 2).
        - dist: Distance metric to use (default: euclidean_distances).
        - random_state: Seed for random number generation (default: 42).
        """
        self.n_cluster = n_cluster
        self.dist = dist
        self.rstate = np.random.RandomState(random_state)
        self.cluster_centers = []  # Contains the cluster centers
        self.y_pred = None  # Contains predicted labels for samples

    def fit(self, X):
        """
        Method to train the K-Means algorithm on input data X.

        Parameters:
        - X: Array-like or matrix, shape (n_samples, n_features).
        """
        rint = self.rstate.randint
        initial_indices = [rint(X.shape[0])]  # Initializing the first centroid index
        for _ in range(self.n_cluster -1):  # Loop to obtain self.n_clusters -1 unique initial indices for centroids
            # Generate a random index between 0 (inclusive) and X.shape[0] (exclusive)
            i = rint(X.shape[0])
            # Ensure the generated index is unique
            while i in initial_indices:
                i = rint(X.shape[0])
            # Add the unique index to the list of intial_indices
            initial_indices.append(i)
        # Inizializing the entroids using the selected intiial indices
        self.cluster_centers = X[initial_indices, :]

        continue_condition = True

        while continue_condition:
            # Save a copy of the current centroids for convergence comparison
            old_centroids = self.cluster_centers.copy()

            self.y_pred = self.prediction(X)

            # Update centroids based on the mean of data points in each cluster
            for i in set(self.y_pred):
                self.cluster_centers[i] = np.mean(X[self.y_pred == i], axis=0)

            # Check for convergence by comparing old and new centroids
            if (old_centroids == self.cluster_centers).all():
                # If centroids haven't changed, set continue_condition to False to exit the loop
                continue_condition = False

    def prediction(self, X):
        """
        Method to predict the cluster membership for each sample in X.

        Parameters:
        - X: Array-like or matrix, shape (n_samples, n_features).

        Returns:
        - Array containing the predicted cluster indices for each sample.
        """
        distance = self.dist(X, self.cluster_centers)
        return np.argmin(distance, axis=1)
