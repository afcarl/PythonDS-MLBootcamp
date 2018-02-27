import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

# Using Iris datasets

iris = sns.load_dataset('iris')

iris.head()

sns.pairplot(iris, hue='species')


# Setosta seems to be the most separable
setosa = iris[iris['species']=='setosa']
sns.kdeplot(setosa['sepal_width'], setosa['sepal_length'], cmap='plasma', shade=True, shade_lowest=False)


X = iris.drop('species', axis=1)
y = iris['species']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = SVC()
model.fit(X_train, y_train)

model_preds = model.predict(X_test)
print(classification_report(y_test, model_preds))
# fantastic default params! 98% accuracy! 100% precision on setosa and versicolor!

# Try to improve with a GridSearch

param_grid = {'C': [0.1, 1, 10, 100, 1000, 10000], 'gamma':[0.1, 0.01, 0.001, 0.0001, 0.00001]}
grid = GridSearchCV(SVC(), param_grid=param_grid, verbose=2)
grid.fit(X_train, y_train)
grid.best_estimator_
grid.best_params_
grid.best_score_

grid_preds = grid.predict(X_test)

print(classification_report(y_test, grid_preds))

# We only marginally improved our model, but it was worth the little time it took!
