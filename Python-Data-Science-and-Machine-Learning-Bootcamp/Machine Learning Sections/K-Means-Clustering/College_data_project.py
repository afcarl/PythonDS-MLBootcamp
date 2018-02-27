import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report

### Use KMeans clustering to determine if a university is public or private

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/K-Means-Clustering/'

df = pd.read_csv(path + 'College_Data', index_col=0)

df.head()
df.info()
df.describe()

sns.lmplot(x='Grad.Rate', y='Room.Board', data=df, hue='Private', fit_reg=False, palette='plasma', size=10)

sns.lmplot(x='Outstate', y='F.Undergrad', data=df, hue='Private', fit_reg=False, palette='plasma', size=6)


g = sns.FacetGrid(data=df, palette='plasma', hue='Private', size=5, aspect=2)
g = g.map(plt.hist, 'Outstate', bins=20, alpha=0.6)



gradrate = sns.FacetGrid(data=df, palette='plasma', hue='Private', size=5, aspect=2)
gradrate = gradrate.map(plt.hist, 'Grad.Rate', bins=20, alpha=0.6)
plt.legend()


# There's a school that graduates for than 100% of its students?


df[df['Grad.Rate']>100]

# Adjusting Cazenovia College to make sense
df['Grad.Rate']['Cazenovia College'] = 100

gradrate = sns.FacetGrid(data=df, palette='plasma', hue='Private', size=5, aspect=2)
gradrate = gradrate.map(plt.hist, 'Grad.Rate', bins=20, alpha=0.6)
plt.legend()

kmeans = KMeans(n_clusters=2)
kmeans.fit(df.drop('Private', axis=1))

kmeans.cluster_centers_

def converter(private):
    if private == 'Yes':
        return 1
    else:
        return 0
df['Cluster'] = df['Private'].apply(converter)

print(classification_report(df['Cluster'], kmeans.labels_))
