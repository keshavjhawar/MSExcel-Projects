import pandas as pd
from matplotlib import pyplot as plt

## 1.Changing str to timestamp for Date column
# df = pd.read_csv("/Applications/My Projects/Data Analytics"
#                  "/Python Projects/Time Series Analysis/aapl.csv",parse_dates=["Date"],index_col="Date")

# print(type(df.Date[0]))

## 2.Avg price of stock in January
# print(df['2017-01'].Close.mean())

## 3.Resampling to Monthly Data and Analysing
# print(df.Close.resample('M').mean())

# df.Close.resample('M').mean().plot()
# plt.show()
#
# df.Close.resample('W').mean().plot()
# plt.show()

# df.Close.resample('Q').mean().plot()
# plt.show()

## 4.Setting Datetime index
df1 = pd.read_csv("/Applications/My Projects/Data Analytics"
                  "/Python Projects/Time Series Analysis/aapl_no_dates.csv")

# print(df1.head())

rng = pd.date_range(start="6/01/2017",end="6/30/2017",freq="B")
# print(rng)

df1.set_index(rng,inplace=True)
# print(df1.head())

# df1.Close.plot()
# plt.show()




