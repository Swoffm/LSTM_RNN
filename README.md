# READ ME

First, before you start make sure you have all of the following libaries downloaded

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

Secondly, you need to create an API key at https://www.alphavantage.co

Thirdly, Once you get your own key go to the file marked NEWRNN/getting_data.py and place your api key in the variable slot that says API_Key = ''

Lastly, to run go the NEWRNN use the file titled MAINSTART


If you have any questions or need help running the program please email me at swofford.github@gmail.com


The file marked STOCK RNN contains a list of projects that I worked on while I was getting a better understanding for what RNNs do and how they operate. The file marked NEWRNN is my updated and improved version. To run the file you must go to the file named MAINSTART. 



The goal of this project was to make a basic stock market predictor that was easy to use and one that contained some versatility. The classes in the file are barbaric and sloppy nevertheless, it still requires improvements that will be worked on in the future. The end goal is to have a network that can accurately predict a trend when trained properly and a network that is user friendly, easily accessible and has great versatility.
