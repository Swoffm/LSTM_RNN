
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


class RNN:

    def Stock_Data(ticker):
        data_source = 'alphavantage'

        
    # ====================== Loading Data from Alpha Vantage ==================================

        api_key = 'Q4UT1U6TTKR2FTY2'

    # American Airlines stock market prices
        

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
        df = pd.DataFrame(df)

        # Double check the result
        df.head()
        return df
    
    def what_type_train(df, data_type):
        #data_type is defined by the user
        
        the_data = df.loc[:,data_type].as_matrix()
        
        #high_prices_df is needed later 
        
        #returning Data_type_df for later use
        
        return the_data
    
    def getting_frame_of_the_data(df, the_data):
       
        #high_prices_df is needed later 
        
        Data_Type_DF = pd.DataFrame(the_data)
        
        #returning Data_type_df for later use
        
        return Data_Type_DF
    
    def scaling():
        sc = MinMaxScaler(feature_range = (0, 1))
        return sc
         


            
    def scaling_training_set(number_of_days, the_data, sc):
       
        training_set_Data_Frame = np.delete(the_data, slice(len(the_data) - number_of_days,len(the_data)), 0)
        #training_set_Data_Frame = Data_Type_DF
 
        #training_set_low_prices = np.delete(low_prices, slice(len(df) - number_of_days,len(df)), 0)
        training_set = pd.DataFrame(training_set_Data_Frame)
        #training_set = pd.DataFrame(training_set_high_prices, training_set_low_prices)

      
        training_set_scaled = sc.fit_transform(training_set)
       
        return training_set_scaled
       
        #return training_set
    
    
    def data_struct():
        pass
    
    def Y_train(training_set_scaled, the_data, number_of_days):
        X_train = []
        y_train = []

#the first int in this range corresponds with how often it LEARNS!!!!!!!!! 
        for i in range(60, len(the_data) - number_of_days):
            X_train.append(training_set_scaled[i-number_of_days:i, 0])
            y_train.append(training_set_scaled[i, 0])
        y_train = np.array(y_train)

        return y_train
    
    def X_train(training_set_scaled, the_data, number_of_days):
        X_train = []
       # y_train = []
#the first int in this range corresponds with how often it LEARNS!!!!!!!!! 
        for i in range(60, len(the_data) - number_of_days):
            X_train.append(training_set_scaled[i-number_of_days:i, 0])
           
        X_train = np.array(X_train)
       

    # Reshaping
    #np.reshape reshapes a numpy array
       
        return X_train
    
    def making_neurons(X_train, y_train, 
                       number_of_neurons_first, epoch_size):
        
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        
        '''=================MAKE DROPOUT RATE AND BATCH SIZE ALL BASED ON USERINPUT!!!=================='''
        # Initialising the RNN
        regressor = Sequential() 
        #THIS HIDDEN LAYER NEURONS IS BASED ON THE IDEA THAT THE NUMBER OF
        #NEURONS IN THE HIDDEN LAYERS NEEDS TO BE 2/3 OF THE FIRST LAYER
        hidden_layer_neurons = round(number_of_neurons_first * (2/3))

        # Adding the first LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = number_of_neurons_first, return_sequences = True, input_shape = (X_train.shape[1], 1)))
        #20% of the neurons will be ignored 
        regressor.add(Dropout(0.2))

        # Adding a second LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = hidden_layer_neurons, return_sequences = True))
        regressor.add(Dropout(0.2))

        # Adding a third LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = hidden_layer_neurons, return_sequences = True))
        regressor.add(Dropout(0.2))

        # Adding a fourth LSTM layer and some Dropout regularisation
        regressor.add(LSTM(units = hidden_layer_neurons))
        regressor.add(Dropout(0.2))

        # Adding the output layer
        regressor.add(Dense(units = 1))

        # Compiling the RNN
        regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

        # Fitting the RNN to the Training set
        regressor.fit(X_train, y_train, epochs = epoch_size, batch_size = 32)
        
        return regressor


    
    

         

    def making_prediction(regressor, sc, the_data, data_type_DF_predi, number_of_days, future):
        
        real_stock_price_high = np.delete(the_data, len(the_data) - number_of_days, 0)

       # real_stock_price_low = np.delete(low_prices, slice(3653), 0)

        real_stock_price_high_df = pd.DataFrame(real_stock_price_high)
        # Getting the predicted stock price of 2017
        dataset_total = pd.concat((data_type_DF_predi, real_stock_price_high_df), axis = 0)
        """THIS CHANGES THE NUMBER OF DAYS PREDICTED ITS SUPER IMPORTNANT"""
        inputs = dataset_total[len(dataset_total) - len(real_stock_price_high_df) - (future):].values
        inputs = inputs.reshape(-1,1)
        inputs = sc.transform(inputs)
        X_test = []
        """change the 100 here 
        and above
        THIS CHANGES THE NUMBER 
        OF DAYS PREDICTED 
        ITS SUPER IMPORTNANT"""
        
        #the first number in the 60 
        #FUTURE HAS TO BE GREATER THE NUMBER OF DAYS OR IT WONT FILL IN THE GRAPH AND ITLL LOOK OFF
        for i in range(number_of_days, (future)):
            X_test.append(inputs[i-number_of_days:i, 0])
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        predicted_stock_price = regressor.predict(X_test)
        predicted_stock_price = sc.inverse_transform(predicted_stock_price)

        print(predicted_stock_price)
        
        return predicted_stock_price
    
    
    
    def visualize_predictions(predicted_stock_price, the_data,
                              data_type, number_of_days, ticker):
        real_stock_price = np.delete(the_data, (slice(len(the_data) - number_of_days)), 0)
        
        
        plt.plot(real_stock_price, color = 'red', label = 'Stock ' + data_type)
        plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted ' + data_type + ' Price')
        plt.title(ticker + ' Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.legend()
        plt.show()
        
        
        
        
