#!/usr/bin/python3
import numpy as np
import pandas as pd
import seaborn as sns
import cufflinks as cf
cf.go_offline()
import matplotlib.pyplot as plt
%matplotlib inline

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Logistic-Regression/'
ad_data = pd.read_csv(path + 'advertising.csv')
ad_data.head()
ad_data.describe()
ad_data.info()

# Create a histogram of the Age
sns.distplot(ad_data['Age'], kde=False, bins=40)

# Create a jointplot showing Area Income vs Age
sns.jointplot(x='Age', y='Area Income', data=ad_data)

# Create a jointplot with kde distribution of Daily Time Spent on Site
# vs Age

sns.jointplot(x='Age', y='Daily Time Spent on Site', data=ad_data, kind='kde')

# Create a jointplot of 'Daily Time Spent on Site' vs 'Daily Internet Usage'
sns.jointplot(x='Daily Time Spent on Site', y='Daily Internet Usage', data=ad_data)
sns.pairplot(data=ad_data, hue='Clicked on Ad')


### LOGISTIC REGRESSION ###
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
ad_data.head()

X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']]
y = ad_data['Clicked on Ad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)
print(classification_report(y_test, predictions))
