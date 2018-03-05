from sklearn.metrics import classification_report
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
#print(iris['DESCR'])

X = np.float32(iris['data'])
y = iris['target']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

import tensorflow.contrib.learn as learn
import tensorflow as tf

feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]


classifier = learn.DNNClassifier(hidden_units=[10,20,10], n_classes=3, feature_columns=feature_columns, model_dir='./output')
classifier.fit(X_train, y_train, steps=5000)

iris_preds = classifier.predict(X_test)

accuracy_score = classifier.evaluate(X_test, y_test)["accuracy"]
print("Accuracy Score: {0:f}".format(accuracy_score))


iris_list_preds = list(classifier.predict(X_test))

print(classification_report(y_test, iris_list_preds))
