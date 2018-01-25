import numpy as np
import pandas as pd


path = '/home/zbloss/Desktop/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Analysis/Pandas/Pandas Exercises/'
ecom = pd.read_csv(path + 'Ecommerce Purchases')

ecom.head()

# Find how many rows and columns there are
ecom.info()


# What is the avg Purchase Price?

ecom['Purchase Price'].mean()

# What were the highest and lowest Purchase Prices?
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()

# how many people have 'en' as their language of choice?

ecom[ecom['Language'] == 'en']['Language'].count()

# How many people have the job Title of Lawyer?

ecom[ecom['Job'] == 'Lawyer']['Job'].count()

# how many people made the purchase during the AM and how many people made the purchase during the PM
# hint check out value_counts()

ecom['AM or PM'].value_counts()

# What are the 5 most common Job Titles?

ecom['Job'].value_counts().head(5)

# someone made a purchase that came from Lot: "90 WT", what was the Purchase Price for this transaction?

ecom[ecom['Lot'] == "90 WT"]['Purchase Price']

# what is the email of the person with the follow Credit Card Number: 4926535242672853

ecom[ecom['Credit Card'] == 4926535242672853]['Email']

# How many people have American Express as their Credit Card Provider and made a purchase above $95?

ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()

# How many people have a credit card that expires in 2025?

#my way
def intwofive(date):
    if '25' in date.lower().split('/'):
        return True
    else:
        return False

ecom[ecom['CC Exp Date'].apply(lambda x: intwofive(x))].count()
#course way
ecom[ecom['CC Exp Date'].apply(lambda exp: exp[3:]== '25')].count()

# What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)

ecom['Email'].iloc[0]
ecom['Email'].iloc[0].split('@')
'''
def get_email(email):
    i = 0
    providers = []
    while i <= len(ecom['Email']):
        value_to = ecom['Email'].iloc[i].split('@')
        providers.append(value_to[1])
    return providers.value_counts()

'''
ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)
