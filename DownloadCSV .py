#Using Panda library for Data extraction and Parsing it .
#https://pandas.pydata.org/docs/

import pandas as pd #import panda as pd
#Currently using data from yahoo
CSV_URL = 'https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1558522033&period2=1590144433&interval=1d&events=history'
pd = pd.read_csv(CSV_URL) #Read the CSV

pd.head() #Print the top 10 lines jus to debug 

pd.to_csv('TEST.csv') #Save it as TEST ?
