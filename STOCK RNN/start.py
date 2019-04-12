# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import requests
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

class RNN:
    
    def get_data():
        API_KEY = 'Q4UT1U6TTKR2FTY2'
        r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GOOGL&interval=1min&outputsize=full&apikey=' + API_KEY)
        result = r.json()
     
        
    def transform_data():
        get_data()
        from sklearn.preprocessing import MinMaxScaler
        scale = MinMaxScaler(feature_range = (0, 1))
        training_set_scaled = scale.fit_transform(result)
        
        
        
    
# Importing the training set
dataset_train = pd.read_csv('Google_Stock_Price_Train.csv')
training_set = dataset_train.iloc[:, 1:2].values

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)




