import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from yellowbrick.cluster import SilhouetteVisualizer

df = pd.read_csv('../data/housing.csv')
X = df.loc[:, ["median_income", "latitude", "longitude"]]
print(X.head())

#  X = StandardScaler.fit_transform(X)

sum_square_distance = []
K = range(2, 12)
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    sum_square_distance.append(kmeans.inertia_)
plt.plot(K, sum_square_distance, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Sum of squared distance for Opt K')
plt.show()

# for k in K:
#     kmeans = KMeans(n_clusters=k)
#     c_s = kmeans.fit_predict(X)
#     sih_avg = silhouette_score(X, c_s)
#     print(f'Cluster {k} ---- sih score = {sih_avg}')
#
#     vis = SilhouetteVisualizer(kmeans, colors='yellowbrick')
#     vis.fit(X)
#     vis.show()
#

kmeans = KMeans(n_clusters=5)
X["Cluster"] = kmeans.fit_predict(X)
X["Cluster"] = X["Cluster"].astype("category")


# sns.replot(x="longitude", y="latitude", hue="Cluster", data=X, height=6)
# plt.show()
#
# X["median_house_value"] = df["median_house_value"]
# sns.catplot(x="median_house_value", y="Cluster", data=X, kind="boxen", height=6)
# plt.show()
