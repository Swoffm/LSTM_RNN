#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:46:01 2019

@author: gavinswofford
"""

import sys

from getting_data import RNN
from question_logic import question_logic


def questions():
    #api_key = 'Q4UT1U6TTKR2FTY2'
   
    #==========ASKING IF THE USER WOULD LIKE TO TRAIN THE DATA SET OR MAKE A PREDICTION===========
    
    train = question_logic.asking_train()
    #the while loop is looking for the return value of the function asking_train in the question logic class
    #only three values are actually checked for the return they are belows
    while train != True and train != False and train != sys.exit:
        train = question_logic.asking_train()

    if train == True:
        print('It worked train = true')
        number_of_days = int(input('How many days in the past would you like to compare your model (5-20): '))
        
        while train == True:
    
    

       
            """THIS IS ASKING FOR THE STOCK SYMBOL OR TICKER TO BE ENTERED INTO THE API URL!!!======="""
            ticker = input('What stock would you like to train: ').upper()
            
            #Below returns a DataFrame known as df
            df_Data_Frame = RNN.Stock_Data(str(ticker))
            #=====ABOVE====df_Data_Frame====== new variable for df which is the return of the function======
            #this is for asking high low so the program will decide what coloumn to include
            data_type = data_type_check()
         
            
            #==================This returns the_data which is used in SCALLING!!!1 ===========================================
            the_data = RNN.what_type_train(df_Data_Frame, data_type)
        #============BELOW THE DATA_TYPE_DF_PREDI WILL BE USED LATER!!!!!!!================
            data_type_DF_predi = RNN.getting_frame_of_the_data(df_Data_Frame, the_data)
        
            sc = RNN.scaling()
            #This is function needs to be passed to things for information DataFrame df and a data_type 
            #Data type is determend by the user above
            #======Below returns training_set_scaled that is why the function is being equaled to it
      
            training_set_scaled = RNN.scaling_training_set(number_of_days, the_data, sc)
        
            #named X_train beacuse it returns X_train
            X_train = RNN.X_train(training_set_scaled,the_data, number_of_days)
        
            #named Y_Train bc it returns y train for the nuerons!!!!!!!!=======
            y_train = RNN.Y_train(training_set_scaled,the_data, number_of_days)
        
            '''NEED TO ASK HOW MANY NUERONS TO BE ENTERED IN THE FIRST LAYER THIS IS UP TO THE USER
            THE NEXT LAYERS ARE ROUNDED 2/3 NUERONS IN THE HIDDEN LAYERS.'''
        
            number_of_nuerons_first = int(input('How many neurons would you like in the first layer: '))
            '''We now need to ask about the number of epochs to be run in the network'''
            epoch_size = int(input('How many epochs would you like: '))
        
            regressor = RNN.making_neurons(X_train, y_train, 
                                            number_of_nuerons_first,epoch_size)
        
            #Question about asking to contue training or not
            """Work on looping it back around"""
            cont_train = input('Would you like to contiune training (yes or no): ').upper()
            if cont_train == 'YES':
                    train = True
            elif cont_train == 'NO':
                    train = False
            
    if train == False:
            #train_or_predict = input('Would you like to train or predict: ').upper()
        
        
            #============================reconfigure all of this!!!!!!!!!!!!!!+===================
        print("future has to be a larger number than: " + str(number_of_days))
        future_Days = int(input("How many days in the future would you like to predict: "))
        future = int(future_Days) + int(number_of_days)
        """===============FUTURE IS FOR PREDICTING THE FUTURE PRICES OF THE SELECTED STOCK"""
        
  #  elif train_or_predict == 'PREDICT':
  
        print('Take the user to predicting')
  
        predicted_stock_price = RNN.making_prediction(regressor, sc, the_data, 
                                                      data_type_DF_predi, number_of_days, future)
        visual = RNN.visualize_predictions(predicted_stock_price, the_data, 
                                           data_type,number_of_days, ticker)
        
            
        
        
        
        
        
   
        
#  ===========WORK ON A WAY TO CHECK THE DATA SET UP A SYSTEM OF CHECKS AND BALANCES===============  
def data_type_check():
    data_type = str(input('What type of data would you like train (High, Low, Open, Close): ')).lower().capitalize()
    return data_type
        
#    if data_type != 'High' or data_type != 'Low' or data_type != 'Open' or data_type != 'Close':
#           return data_type_check()
#       
#       
#            
#    else:
#            return data_type
#            

















