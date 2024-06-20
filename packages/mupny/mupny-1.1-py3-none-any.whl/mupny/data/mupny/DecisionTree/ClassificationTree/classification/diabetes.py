import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split

# Load the diabetes dataset
diabetes = pd.read_csv('../data/diabetes.csv')

# Print dataset stats
print(diabetes.describe())
print(diabetes.columns)

# Divide features and target variable transforming them into matrices
X = diabetes.drop(['Outcome'], axis=1).values
y = diabetes['Outcome'].values

# train_index = round(len(X)*0.8)

# X_train = X[:train_index]
# y_train = y[:train_index]

# X_test = X[train_index:]
# y_test = y[train_index:]

# Split the dataset into training and test sets through hold-out strategy
'''
StratifiedKFold is a variation of k-fold which returns stratified folds: 
each set contains approximately the same percentage of samples of each target class as the complete set

--> with stratify, don't use shuffle
'''
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2, stratify=y)

'''
Do we need data normalization if we use a DECISION TREE?
The answer is no. Why?
The process of scaling data through normalization is to ensure that a specific feature is not prioritized 
over another due to the feature values magnitude. In the case of decision trees, the algorithm makes decisions based 
on comparisons of feature values at different nodes of the tree, and the relative ordering of the values is what 
matters, not their absolute scale. Indeed, we just split data.
'''


# Create a decision tree classifier
'''
criterion: the function to measure the quality of a split <entropy|gini>
min_samples_leaf: sets the minimum number of samples required to be at a leaf node
max_depth:  limits the maximum depth of the decision tree

<< min_samples_leaf & >> max_depth  --->  more complexity (overfitting)
>> min_samples_leaf & << max_depth  --->  less complexity (underfitting)
'''
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_leaf=5)

# Train the classifier
clf = clf.fit(X_train, y_train)

# Compute predictions
y_pred = clf.predict(X_test)

print(f"Acc TEST: {metrics.accuracy_score(y_test, y_pred)}")
print(f"Confusion matrix TEST:\n {metrics.confusion_matrix(y_test, y_pred)}")

# Compute predictions on the training set and evaluating the model on such predictions
# Just for observing overfitting/underfitting
y_pred_train = clf.predict(X_train)
print(f"Acc TRAINING: {metrics.accuracy_score(y_train, y_pred_train)}")

# Plot the tree
plt.figure( figsize=(12, 8) )
plot_tree(clf, feature_names=diabetes.columns, filled=True)
# plt.show()
plt.savefig(f'../images/tree.png', format='png', bbox_inches='tight', dpi=199)