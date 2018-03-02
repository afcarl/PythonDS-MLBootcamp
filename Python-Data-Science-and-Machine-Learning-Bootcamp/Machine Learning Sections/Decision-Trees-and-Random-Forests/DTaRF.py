#!/usr/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
%matplotlib inline

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Decision-Trees-and-Random-Forests/'

df = pd.read_csv(path + 'kyphosis.csv')
df.head()

df.describe()

# Age is in months, Number is # of vertabres involved, Start is vertabre that
# The operation started on

sns.pairplot(df, hue='Kyphosis')


X = df.drop('Kyphosis', axis=1)
y = df['Kyphosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
dtree = DecisionTreeClassifier()

dtree.fit(X_train, y_train)


preds = dtree.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, preds))
print(confusion_matrix(y_test, preds))


from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=200)

rfc.fit(X_train, y_train)

rfc_preds = rfc.predict(X_test)
print(classification_report(y_test, rfc_preds))
print(confusion_matrix(y_test, rfc_preds))

df['Kyphosis'].value_counts()

# Skipping Tree Viz, because the vast majority of the time I will be working in
# Random Forests
