import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Natural-Language-Processing/'

yelp = pd.read_csv(path + 'yelp.csv')
yelp.head(10)
yelp.info()
yelp.describe()

len(yelp['text'][0].split(' '))
text_length = yelp['text'][0].split()
len(text_length)

def get_txt_count(text):
    return len(yelp['text'][text].split())

def word_count(text):
    return len(text.split())

yelp['text length'] = yelp['text'].apply(word_count)
yelp.head()

g = sns.FacetGrid(data=yelp, col='stars')
g.map(plt.hist, 'text length')
sns.boxplot(x='stars', y='text length', data=yelp)

sns.countplot(x='stars', data=yelp)

#Use groupby to get the mean values of the numerical columns, you should be able to create this dataframe with the operation:

stars = yelp.groupby('stars').mean()

stars_corr = stars.corr()

sns.heatmap(stars_corr, cmap='coolwarm', annot=True)


yelp_class = yelp[(yelp['stars']==1) | (yelp['stars']==5)]


X = yelp_class['text']
y = yelp_class['stars']


cv = CountVectorizer()

X = cv.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)



from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

nb.fit(X_train, y_train)

preds = nb.predict(X_test)


from sklearn.metrics import classification_report

print(classification_report(y_test, preds))


from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline


pipe = Pipeline([
    ('bow', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('model', MultinomialNB())
    ])

X = yelp_class['text']
y = yelp_class['stars']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

pipe.fit(X_train, y_train)

pipe_preds = pipe.predict(X_test)

print(classification_report(y_test, pipe_preds))
# Note: using the TfidfTransformer actually made worse predictions
