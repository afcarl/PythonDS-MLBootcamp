import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/K-Nearest-Neighbors/'

dataframe = pd.read_csv(path + 'KNN_Project_Data')

dataframe.head()

#sns.pairplot(dataframe, hue='TARGET CLASS')
scaler = StandardScaler()
scaler.fit(dataframe.drop('TARGET CLASS', axis=1))

scaled_features = scaler.transform(dataframe.drop('TARGET CLASS', axis=1))
df_feat = pd.DataFrame(scaled_features, columns=dataframe.columns[:-1])

df_feat.head()

X = df_feat
y = dataframe['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print(classification_report(y_test, pred))

print(confusion_matrix(y_test, pred))

# Use elbow to improve k value

error_rate=[]
for i in range(1,100):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)
    error_rate.append(np.mean(pred != y_test))

plt.figure(figsize=(10,10))
plt.xlabel='K-Value'
plt.ylabel = 'Error Rate'
plt.plot(range(1,100), error_rate, color='blue', linestyle='dashed', marker='o', markersize=10, markerfacecolor='red')

knn = KNeighborsClassifier(n_neighbors=30)
pred = knn.predict(X_test)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(classification_report(y_test, predictions))
