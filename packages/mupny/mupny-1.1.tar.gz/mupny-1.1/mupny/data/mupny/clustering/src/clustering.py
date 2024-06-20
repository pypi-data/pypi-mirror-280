from sklearn import datasets
import matplotlib.pyplot as plt
from k_means import KMeans
from sklearn.metrics import silhouette_score

seed = 42

n_cluster = 3

proc_data, y_true = datasets.make_blobs(
    n_samples=500,
    n_features=2,
    centers=n_cluster,
    random_state=seed,
    shuffle=True,
    center_box=(-10, 10),
    cluster_std=1
)

plt.figure()
plt.scatter(proc_data[:, 0], proc_data[:, 1], s=n_cluster)
plt.title("Original toy data")
plt.show()

k_means = KMeans(n_cluster=n_cluster, random_state=seed)
k_means.fit(proc_data)
y_preds = k_means.prediction(proc_data)
print(silhouette_score(proc_data, y_preds))

plt.scatter(proc_data[:, 0], proc_data[:, 1], c=y_preds, s=n_cluster)
plt.show()
