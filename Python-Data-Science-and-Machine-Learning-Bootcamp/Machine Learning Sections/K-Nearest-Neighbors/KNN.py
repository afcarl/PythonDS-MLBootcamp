#!/usr/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
%matplotlib inline

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/K-Nearest-Neighbors/'

# 100% unaware at this point what is in Classified Data
df = pd.read_csv(path + 'Classified Data', index_col=0)

df.head()
df.info()
df.describe()

scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))

scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))

scaled_features


# Grabbing all of the scaled features and creating a dataframe from them minus the target class
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
df_feat.head()

# Now everything has been scaled correctly, we can proceed with putting it into a ML
# Algorithm

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

X = df_feat
y = df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# here we change the degree of k by setting n_neighbors
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)

print(classification_report(y_test, predictions))
# This 92% precision is pretty good, but we can improve it with a better k value
# We find the optimum k value using the elbow method

error_rate = []
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    prediction = knn.predict(X_test)
    # now we need to get the average error rate
    # we use numpy to calculate the average of each prediction that is not equal
    # to y_test. In other words, we are calculating the average value of each wrong
    # predictions, i.e. the error rate
    error_rate.append(np.mean(prediction != y_test))


plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate, color='blue', linestyle='dashed', marker='o',
        markerfacecolor='red', markersize=10)
plt.title('Error Rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
# we are choosing k=17 even though there are lower error rates.
# this is because the error rate from k=16 - k=19 is relatively stable.

knn = KNeighborsClassifier(n_neighbors=17)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print(classification_report(y_test, pred))
# here we get a precision of 95%, better than our original 92%
