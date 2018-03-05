import pandas as pd
import seaborn as sns
import numpy as np



path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Deep Learning/'
data = pd.read_csv(path + 'bank_note_data.csv')

data.head()

sns.countplot(x='Class', data=data)

sns.pairplot(data, hue='Class')

# prepping data
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(data.drop('Class', axis=1))

scaled_feats = scalar.fit_transform(data.drop('Class', axis=1))

df_feats = pd.DataFrame(scaled_feats, columns=data.columns[:-1])
df_feats.head()

from sklearn.model_selection import train_test_split
X = np.float32(df_feats)
y = data['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

import tensorflow.contrib.learn as learn
import tensorflow as tf


feature_columns = [tf.contrib.layers.real_valued_column("", dimension=3)]


classifier = learn.DNNClassifier(hidden_units=[10,20,10], n_classes=2, feature_columns=feature_columns, model_dir=(path+'FinalProjectOutput'))
classifier.fit(X_train, y_train, steps=200, batch_size=20)

preds = list(classifier.predict(X_test))

from sklearn.metrics import classification_report

print(classification_report(y_test, preds))


# 100% accuracy, need to do a reality check... Compare with RFC


from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=200)

rfc.fit(X_train, y_train)

r_preds = rfc.predict(X_test)

print(classification_report(y_test, r_preds))
# 99% works for me!!!
