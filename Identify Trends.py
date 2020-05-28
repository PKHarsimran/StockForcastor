#Made By : Harsimran Sidhu
#Identify Trends

#import lib
import pandas as pd
import io
pd.set_option('display.max_rows', 260)
#pd.set_option('display.max_columns', 14)

data = pd.read_csv("TEST.csv", index_col=[0])
data.drop(0)
date = data['Date']
closeV = data['Close']
s = float(2/14)
s1 = float(2/22)

fastema = closeV.ewm(alpha=s,min_periods=13).mean()
slowema = closeV.ewm(alpha=s1,min_periods=21).mean()

#span is optional !
data['13EMA'] = fastema
data['21EMA'] = slowema
data['EMA spread'] = data['13EMA'] - data['21EMA']

data['Rolling Sum'] = data['EMA spread'].rolling(2).sum()

print(data)

print(data['Rolling Sum'].count())
count = data['Rolling Sum'].count()
x=21
while x < (count+17):
    Loc = data['Rolling Sum'][x:(x+5)]
    monInc = Loc.is_monotonic_increasing
    monDec = Loc.is_mon
    data.at[x, 'Increasing ?'] = monInc
    data.at[x, 'Decreasing ?'] = monDec
    if data.at[x,'Increasing ?'] == True and data.at[x,'Decreasing ?'] == False:
        data.at[x,'Trend ?'] = "Uptrend"
    elif data.at[x,'Increasing ?'] == False and data.at[x,'Decreasing ?'] == True:
        data.at[x,'Trend ?'] = "Downtrend"
    else:
        data.at[x, 'Trend ?'] = "-----"
    x+=1

print(data)