#!/usr/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
%matplotlib inline
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Decision-Trees-and-Random-Forests/'


### LendingClub.com data analysis pre-fraud ###
# Construct a model to help investors decide whether they should invest in someone #
# predict 'not.fully.paid'

df = pd.read_csv(path + 'loan_data.csv')
df.info()
df.describe()
df.head()

df[df['not.fully.paid'] == 1]['fico'].hist(bins=35, color='blue', label='Not Fully Paid 1', alpha=0.6)
df[df['not.fully.paid'] == 0]['fico'].hist(bins=35, color='red', label='Not Fully Paid 0', alpha=0.6)
plt.legend()

# Create a countplot using seaborn showing the counts of loans by purpose with hue='not.fully.paid'
plt.figure(figsize=(11,7))
sns.countplot(x='purpose', hue='not.fully.paid', data=df)


# Show the trend between FICO Score and interest rate

sns.jointplot(x='fico', y='int.rate', data=df)


# Create lmplots to see if the trend differed between not.fully.paid and credit.policy
plt.figure(figsize=(11,7))
sns.lmplot(y='int.rate', x='fico', data=df, hue='credit.policy', col='not.fully.paid')


cat_feats = ['purpose']
final_data = pd.get_dummies(df, columns=cat_feats, drop_first=True)

final_data.info()

X = final_data.drop('not.fully.paid', axis=1)
y = final_data['not.fully.paid']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

dtree = DecisionTreeClassifier()

dtree.fit(X_train, y_train)

preds = dtree.predict(X_test)

print(classification_report(y_test, preds))
print(confusion_matrix(y_test, preds))

# Train the RandomForest Model
rfc = RandomForestClassifier(n_estimators=300)

rfc.fit(X_train, y_train)

rfc_preds = rfc.predict(X_test)

print(classification_report(y_test, rfc_preds))
print(confusion_matrix(y_test, rfc_preds))
