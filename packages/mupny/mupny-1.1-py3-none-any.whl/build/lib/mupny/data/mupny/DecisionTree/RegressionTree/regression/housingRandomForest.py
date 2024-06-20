import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.preprocessing import RobustScaler, StandardScaler  # StandardScaler(z-score) is suscetible to outliers
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn import metrics

# the dataset used is different from the dataset used in the lessons 2021-11-25_16.30
housing = pd.read_csv('../data/housing.csv')

housing['total_bedrooms'].fillna(housing['total_bedrooms'].median(), inplace=True)
print(housing.info())

X = housing[['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income']]
y = housing['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalization
normalization = RobustScaler()
normalization.fit(X_train)

X_train = normalization.transform(X_train)
X_test = normalization.transform(X_test)

'''
criterion{“squared_error”, “friedman_mse”, “absolute_error”, “poisson”}, default=”squared_error”
friedman_mse -> similar to squared_error but best speed (good trade-off mwith large dataset)
ccp_alpha -> Complexity parameter used for Minimal Cost-Complexity Pruning. 
    The subtree with the largest cost complexity that is smaller than ccp_alpha will be chosen. 
    By default, no pruning is performed 
'''
model = DecisionTreeRegressor(random_state=42, max_depth=10, min_samples_leaf=10, criterion='friedman_mse',
                              ccp_alpha=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)

print(f"MAE: {mae}")
print(f"MSE: {mse}")

# plt.figure(figsize=(12, 8))
# plot_tree(model.fit(X_train, y_train))
# plt.show()

'''
n_jobs -> The number of jobs to run in parallel. fit, predict, decision_path and apply are all parallelized 
    over the trees. None means 1 unless in a joblib.parallel_backend context. -1 means using all processors.
n_estimators -> The number of trees in the forest. 
max_features -> The number of features to consider when looking for the best split.
max_sample -> If bootstrap is True, the number of samples to draw from X to train each base estimator.
'''
model_forest = RandomForestRegressor(random_state=42, max_depth=10, min_samples_leaf=10, criterion='friedman_mse',
                                     n_estimators=50, max_features=5, ccp_alpha=1000, max_samples=0.8)
model_forest.fit(X_train, y_train)

y_pred = model_forest.predict(X_test)

mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)

print(f"MAE random forest: {mae}")
print(f"MSE random forrest: {mse}")
