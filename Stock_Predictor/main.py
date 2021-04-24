import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression


quandl.ApiConfig.api_key = 'xpLpDBByVG29tYUiuq27'

df = quandl.get("WIKI/AMZN")
df = df[["Adj. Close"]]
print(df.head())

df["Adj. Close"].plot(figsize=(15, 6), color='g')
plt.legend(loc='upper left')
plt.show()

forcast = 30
df['Prediction'] = df[["Adj.Close"]].shift(-forcast)
print(df)

x = np.array(df.drop(["Prediction"], 1))
x = preprocessing.scale(x)

