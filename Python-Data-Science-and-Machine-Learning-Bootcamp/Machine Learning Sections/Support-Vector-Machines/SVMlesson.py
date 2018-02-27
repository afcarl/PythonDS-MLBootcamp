import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from sklearn.datasets import load_breast_cancer

#Use Breast Cancer dataset built in to sklearn

cancer = load_breast_cancer()

print(cancer['DESCR'])
cancer.keys()

df_feat = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])

df_feat.head()

df_feat.describe()

cancer['target_names']

from sklearn.model_selection import train_test_split

X = df_feat
y = cancer['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# importing Support Vector Classifier
from sklearn.svm import SVC

# note the default kernel is radial
model = SVC()
model.fit(X_train, y_train)

preds = model.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, preds))
print(confusion_matrix(y_test, preds))
# we need to adjust our parameters (C, gamma) using a GridSearch
from sklearn.model_selection import GridSearchCV

param_grid = {'C':[0.1, 1, 10, 100, 1000] , 'gamma':[1, 0.1, 0.01, 0.001, 0.0001]}

# The higher the verbose number, the more text is displayed during the GridSearch
# GridSearches can take a long time
grid = GridSearchCV(SVC(), param_grid=param_grid, verbose=3)

grid.fit(X_train, y_train)
grid.best_params_
grid.best_estimator_
grid.best_score_

grid_preds = grid.predict(X_test)

print(confusion_matrix(y_test, grid_preds))
print(classification_report(y_test, grid_preds))
