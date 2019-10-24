#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:16:43 2019

@author: gavinswofford
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:29:24 2019

@author: gavinswofford
"""


# Part 1 - Data Preprocessing
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import urllib.request, json
import os
import tensorflow as tf # This code has been tested with TensorFlow 1.6
from sklearn.preprocessing import MinMaxScaler
import json
import requests
# Importing the libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

data_source = 'alphavantage'

if data_source == 'alphavantage':
    # ====================== Loading Data from Alpha Vantage ==================================

    api_key = ''

    # American Airlines stock market prices
    ticker = "TSLA"

    # JSON file with all the stock market data for AAL from the last 20 years
    
    url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s"%(ticker,api_key)

    # Save data to this file
    file_to_save = 'stock_market_data-%s.csv'%ticker

    # If you haven't already saved data,
    # Go ahead and grab the data from the url
    # And store date, low, high, volume, close, open values to a Pandas DataFrame
    if not os.path.exists(file_to_save):
        with urllib.request.urlopen(url_string) as url:
            data = json.loads(url.read().decode())
            # extract stock market data
            data = data['Time Series (Daily)']
            df = pd.DataFrame(columns=['Date','Low','High','Close','Open'])
            for k,v in data.items():
                date = dt.datetime.strptime(k, '%Y-%m-%d')
                data_row = [date.date(),float(v['3. low']),float(v['2. high']),
                            float(v['4. close']),float(v['1. open'])]
                df.loc[-1,:] = data_row
                df.index = df.index + 1
        print('Data saved to : %s'%file_to_save)        
        df.to_csv(file_to_save)

    # If the data is already there, just load it from the CSV
    else:
        print('File already exists. Loading data from CSV')
        df = pd.read_csv(file_to_save)
        
        
        
df = df.sort_values('Date')

# Double check the result
df.head()


high_prices = df.loc[:,'High'].as_matrix()



high_prices_df = pd.DataFrame(high_prices)

low_prices = df.loc[:,'Low'].as_matrix()

training_set_high_prices = np.delete(high_prices, slice(3653,3683), 0)

training_set_low_prices = np.delete(low_prices, slice(3653,3683), 0)

training_set = pd.DataFrame(training_set_high_prices, training_set_low_prices)

# Recurrent Neural Network

# Feature Scaling
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

#training_set_low_prices_scaled = sc.fit_transform(training_set_low_prices)

# Creating a data structure with 60 timesteps and 1 output
X_train = []
y_train = []

# the 60 below is for time stamps to use. If it is to low or to high
#it wont be accurate Experiment with that number
#it'll go through 60 stock prices then output one

for i in range(60, 3653):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping
#np.reshape reshapes a numpy array
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))



# Part 2 - Building the RNN


# Initialising the RNN
regressor = Sequential() 

# Adding the first LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 55, return_sequences = True, input_shape = (X_train.shape[1], 1)))
#20% of the nuerons will be ignored 
regressor.add(Dropout(0.2))

# Adding a second LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 55, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a third LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 55, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a fourth LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 55))
regressor.add(Dropout(0.2))

# Adding the output layer
regressor.add(Dense(units = 1))

# Compiling the RNN
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
regressor.fit(X_train, y_train, epochs = 75, batch_size = 32)



# Part 3 - Making the predictions and visualising the results


real_stock_price_high = np.delete(high_prices, slice(2200), 0)

real_stock_price_low = np.delete(low_prices, slice(2200), 0)

real_stock_price_high_df = pd.DataFrame(real_stock_price_high)
# Getting the predicted stock price of 2017
dataset_total = pd.concat((high_prices_df, real_stock_price_high_df), axis = 0)
inputs = dataset_total[len(dataset_total) - len(real_stock_price_high_df) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)
X_test = []
for i in range(60, 80):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# Visualising the results
plt.plot(real_stock_price_high, color = 'red', label = 'Real Tesla High')
plt.plot(real_stock_price_low, color = 'green', label = 'Real Tesla Low')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Tesla Stock Price')
plt.title('Tesla Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Tesla Stock Price')
plt.legend()
plt.show()
