import numpy as np
import pandas as pd


# SF SALARIES
path = '/home/zbloss/Desktop/PythonDS-MLBootcamp/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Analysis/Pandas/Pandas Exercises/'
sal = pd.read_csv(path + 'Salaries.csv')

sal.head()

sal.info()
sal['BasePay'].mean()

sal['OvertimePay'].max()

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# Total pay including benefits of the highest paid Person

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']
# sal.loc[sal['TotalPayBenefits'].idxmax()] same thing but more advanced method

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']

# What was the mean BasePay of all employees per year? (2011-2014)
sal.groupby('Year')['BasePay'].mean()

# How many unique job titles are there?
sal['JobTitle'].nunique()

# what are the top 5 most common jobs
sal['JobTitle'].value_counts().head(5)

# How many job titles were represented by only one person in 2013?
sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

# How many people have the word 'Chief' in their job title?

def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

sum(sal['JobTitle'].apply(lambda x: chief_string(x)))



# Is there a correlation between JobTitle length and TotalPayBenefits
sal['title_len'] = sal['JobTitle'].apply(len)

sal[['TotalPayBenefits', 'title_len']].corr()
