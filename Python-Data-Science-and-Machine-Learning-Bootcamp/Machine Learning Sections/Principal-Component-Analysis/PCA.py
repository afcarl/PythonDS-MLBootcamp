import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


# PCA is just a transformation of the data that seeks to explain what features really
# affect the data

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

cancer.keys()
cancer['feature_names']
# We are going to see which components are the most important to this dataset
# i.e. we want to see which features most affect whether a tumor is cancer or benign

df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
cancer['target_names']

# Usually PCA is done first to see which features are more important than others

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

# Perform PCA

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(scaled_data)

x_pca = pca.transform(scaled_data)
scaled_data.shape
x_pca.shape

# Now we have transformed all of our 30 variables down to just 2 variables

plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0], x_pca[:,1], c=cancer['target'], cmap='plasma')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
# We now need to understand what the components are

pca.components_

# we create a dataframe that shows the two outcomes 0,1 and the relationship each feature has on it
df_comp = pd.DataFrame(pca.components_, columns=cancer['feature_names'])
df_comp
plt.figure(figsize=(10,6))
sns.heatmap(df_comp, cmap='plasma')
