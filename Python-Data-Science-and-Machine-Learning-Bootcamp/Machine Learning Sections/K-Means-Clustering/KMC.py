import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# KMC is unsupervised learning
data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8, random_state=101)

# here we are using make_blobs() to generate some random blobby data.
plt.scatter(data[0][:, 0], data[0][:, 1], c=data[1], cmap='plasma')

kmeans = KMeans(n_clusters=4)
kmeans.fit(data[0])
# here we show the exact centers of each cluster
kmeans.cluster_centers_

#data[1] contains the correct labels, and kmeans.labels_ shows what the predicted labels are.
# usually we are done here, but because we know the actual labels, we will compare data[1]
# to kmeans.labels_
kmeans.labels_

fig, (ax1, ax2) = plt.subplots(1,2, sharey=True, figsize=(10, 6))
ax1.set_title('K Means')
ax1.scatter(data[0][:, 0], data[0][:, 1], c=kmeans.labels_, cmap='plasma')

ax2.set_title('Original')
ax2.scatter(data[0][:, 0], data[0][:, 1], c=data[1], cmap='plasma')

# The predicted values failed to pick up on the noisey sections
