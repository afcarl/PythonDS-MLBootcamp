# Fully developed RS are very complex and resource intensive

# two most common types
    # Content based
        # gives you recommendations based on the similarity of items
    # Collaborative Filtering
        # Like amazon, based on knowledge of others opinions of items,
        # it can predict your opinion 'wisdom of the crowd'
# CF is more commonly used as it usually gives better results

# The algorithm has the ability to do feature learning on its own, which means
# it can start to learn for itself what features to use.

#CF can be broken into two sub-categories
    # Memory-Based Collaborative Filtering
    # Model-Based Collaborative Filtering

        # In the advanced notebook, we implement a Model-Based CF using Singular
        # Value Decomposition (SVD) and Memory-Based CF by computing cosine similarity


# We are creating a content-based recommender system for a dataset of movies

import numpy as np
import pandas as pd

path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Recommender-Systems/'

columns_names = ['user_id', 'item_id', 'rating', 'timestamp']
# use sep='\t' to denote the file is tab-delimitted
df = pd.read_csv(path + 'u.data', sep='\t', names=columns_names)

df.head()


movie_titles = pd.read_csv(path + 'Movie_Id_Titles')

movie_titles.head()
df = pd.merge(df, movie_titles, on='item_id')

df.head()

import matplotlib.pyplot as plt
import seaborn as sns

df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
df.groupby('title')['rating'].count().sort_values(ascending=False).head()

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())


ratings['numRatings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()


ratings['numRatings'].hist(bins=100, figsize=(10,6))
ratings['rating'].hist(bins=100, figsize=(10,6))
sns.jointplot(x='rating', y='numRatings', data=ratings, alpha=0.6)
# as the number of ratings goes up, so does the average rating

moviemat = df.pivot_table(index='user_id', columns='title', values='rating')

moviemat.head()

ratings.sort_values('numRatings', ascending=False).head(10)


starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

# This will show how people who have seen star wars rate other movies
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)


corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head(10)

# Here we have created a dataframe that holds the correlation of star wars user ratings with ratings
# of other moveis. From here, we see a lot of noise from movies with a low number of ratings, so we
# will remove all movies below a certain threshold
corr_starwars.sort_values('Correlation', ascending=False)


corr_starwars = corr_starwars.join(ratings['numRatings'])
corr_starwars[corr_starwars['numRatings']>100].sort_values('Correlation', ascending=False)
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['numRatings'])

corr_liarliar[corr_liarliar['numRatings']>50].sort_values('Correlation', ascending=False)
