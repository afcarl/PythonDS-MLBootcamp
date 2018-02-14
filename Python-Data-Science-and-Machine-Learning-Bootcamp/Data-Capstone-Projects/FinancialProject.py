from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
%matplotlib inline
import matplotlib.pyplot as plt
sns.set_style('whitegrid')


# Optional Plotly Method Imports
import plotly
import cufflinks as cf
cf.go_offline()

# get stock info from major banks with pandas_datareader
'''
Bank of America
CitiGroup
Goldman Sachs
JPMorgan Chase
Morgan Stanley
Wells Fargo
'''

start_date = datetime.datetime(2006, 1, 1)
end_date = datetime.datetime(2016, 1, 1)

# Google Finance API has not been stable since 2017... Proceeding with caution
BAC = data.DataReader("BAC", 'google', start_date, end_date)
CITI = data.DataReader("C", 'google', start_date, end_date)
GS = data.DataReader("GS", 'google', start_date, end_date)
JPM = data.DataReader("JPM", 'google', start_date, end_date)
MS = data.DataReader("MS", 'google', start_date, end_date)
WFC = data.DataReader("WFC", 'google', start_date, end_date)

tickers = ['BAC', 'CITI', 'GS', 'JPM', 'MS', 'WFC']

# combining data sets together
bank_stocks = pd.concat([BAC, CITI, GS, JPM, MS, WFC],axis=1,keys=tickers)
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

bank_stocks.head()

# Displaying the top close price for each bank
bank_stocks.xs('Close', axis=1, level='Stock Info').max()


# creating dataframe to hold returns for each bank
returns = pd.DataFrame()

for bank in tickers:
    returns[bank+' Return'] = bank_stocks[bank]['Close'].pct_change()
returns.head()

sns.pairplot(returns[1:])

# Showing the worst and best days for each bank. 4 of them crashed on inaguration day
returns.idxmin()
returns.idxmax()

# Showing standard deviation, CitiGroup was the riskiest investment
returns.std()

#showing standard deviation during 2015
returns.ix['2015-01-01':'2015-12-31'].std()

returns.info()
# showing a distplot of Morgan Stanley's returns during 2015
sns.distplot(returns.ix['2015-01-01':'2015-12-31']['MS Return'],color='green',bins=100)

# Create a distplot using seaborn of the 2008 returns for CitiGroup

sns.distplot(returns.ix['2008-01-01':'2008-12-31']['CITI Return'], color='green', bins=100)

###################################
### HEAVY VISUALIZATION SECTION ###
###################################


# Create a line plot showing Close price for each bank for the entire index of time.
# (Hint: Try using a for loop, or use .xs to get a cross section of the data.)

for bank in tickers:
    bank_stocks[bank]['Close'].plot(label=bank, figsize=(16,16)).legend()


# Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008
plt.figure(figsize=(20,10))
BAC['Close'].ix['2008-01-01': '2008-12-31'].rolling(window=30).mean().plot(label='30 Day AVG BAC').legend()
BAC['Close'].ix['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE').legend()


# Create a heatmap of the correlation between the stocks Close Price
bank_stocks.head()
sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)
