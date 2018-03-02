# a doc represetned as a vector of word counts is called a "Bag of Words"


# Term frequency function - TF(t,d) means number of occurences of t in d
# Inverse Document frequency - gauges the importance of the term
    # IDF(t) = log(D/t) where:
        # D = Total number of docs
        # t = number of docs with the term in them

# TF-IDF denoted W_x,y is:
    # W_x,y = (tf)_x,y * log(N/df_x)
        # (tf)_x,y is the frequency of x in y
        # df_x is the number of doucments containing x
        # N is the total number of documents

### Building a Spam filter ###
import nltk
import pandas as pd
path = '/home/zbloss/Github/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Natural-Language-Processing/'

#nltk.download_shell() use this to download stopwords

messages = [line.rstrip() for line in open(path + 'smsspamcollection/SMSSpamCollection')]

for mess_no,message in enumerate(messages[:10]):
    print(mess_no, message)
    print("\n")
messages = pd.read_csv(path + 'smsspamcollection/SMSSpamCollection', sep='\t', names=['label', 'message'])

messages.describe()
messages.groupby('label').describe()

messages['length'] = messages['message'].apply(len)

# We've now add a length column to our dataframe

import matplotlib.pyplot as plt
import seaborn as sns


messages['length'].plot.hist(bins=50)
messages['length'].describe() # someone sent a text with 910 chars

messages[messages['length'] == 910]['message'].iloc[0]


messages.hist(column='length', by='label', figsize=(10,6))

import string
mess = 'Sample message! Notice: it has punctuation'
nopunc = [c for c in mess if c not in string.punctuation]
from nltk.corpus import stopwords

nopunc = ''.join(nopunc)

stopwords.words('english')


nopunc.split()
clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
clean_mess


def text_process(mess):
    '''
    remove punc, stop words, then return clean words
    '''
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


messages.head()

messages['message'].head(5).apply(text_process)

### VECTORIZATION ###

from sklearn.feature_extraction.text import CountVectorizer

bow_trans = CountVectorizer(analyzer=text_process).fit(messages['message'])
print(len(bow_trans.vocabulary_))
# 11,425 words in our bow_trans vocab

mess4 = messages['message'][3]
print(mess4)

bow4 = bow_trans.transform([mess4])
print(bow4)
# basically, we have 7 unique words, 2 of them appear twice each

bow_trans.get_feature_names() # this will grab all of the unique words


messages_bow = bow_trans.transform(messages['message'])
# now we have a sparse matrix
print('Shape of sparse matrix is {}'.format(messages_bow.shape))
# the shape is simply the number of messages x number of unique words

# grab non 0 occurences
messages_bow.nnz

sparsity = ((100.00 * messages_bow.nnz)/ (messages_bow.shape[0] * messages_bow.shape[1]))
print('the sparsity is {}'.format(sparsity))

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_trans = TfidfTransformer().fit(messages_bow)

tfidf4 = tfidf_trans.transform(bow4)
print(tfidf4


# to check the frequency of a particular word

tfidf_trans.idf_[bow_trans.vocabulary_['university']]

messages_tfidf = tfidf_trans.transform(messages_bow)
# now we can apply an ml
from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(messages_tfidf, messages['label'])

# here it whether tfdif4 is spam or ham. Note this returns an array with the first element being the prediction
spam_detect_model.predict(tfidf4)[0]

all_pred = spam_detect_model.predict(messages_tfidf)


from sklearn.model_selection import train_test_split

msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['label'], test_size=0.3)

from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
    ])


pipeline.fit(msg_train, label_train)


preds = pipeline.predict(msg_test)

from sklearn.metrics import classification_report
print(classification_report(label_test, preds))

# very good 96% accuracy!!!
