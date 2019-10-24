#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:46:01 2019

@author: gavinswofford
"""

import sys

from getting_data import RNN
from question_logic import question_logic
from fluid import fluid


def questions():
    
   
    #==========ASKING IF THE USER WOULD LIKE TO TRAIN THE DATA SET OR MAKE A PREDICTION==========
        number_of_days = fluid.number_of_days()
        ticker = fluid.ticker()
        
        #Below returns a DataFrame known as df
        df_Data_Frame = RNN.Stock_Data(str(ticker))
        data_type = fluid.data_type()
        sc = RNN.scaling()
        #==================This returns the_data which is used in SCALLING!!!1 ===========================================
        the_data = RNN.what_type_train(df_Data_Frame, data_type)
        #============BELOW THE DATA_TYPE_DF_PREDI WILL BE USED LATER!!!!!!!================
        data_type_DF_predi = RNN.getting_frame_of_the_data(df_Data_Frame, the_data)
        
            
    
        train = True
        while train == True:
         
            
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
        
            number_of_neurons_first = int(input('How many neurons would you like in the first layer: '))
            '''We now need to ask about the number of epochs to be run in the network'''
            epoch_size = int(input('How many epochs would you like: '))
        
            regressor = RNN.making_neurons(X_train, y_train, 
                                            number_of_neurons_first,epoch_size)
        
            #Question about asking to contue training or not
            """Work on looping it back around"""
            cont_train = input('Would you like to contiune training (yes or no): ').upper()
            if cont_train == 'YES':
                ticker = fluid.ticker()
        
                #Below returns a DataFrame known as df
                df_Data_Frame = RNN.Stock_Data(str(ticker))
                data_type = fluid.data_type()
                
                #==================This returns the_data which is used in SCALLING!!!1 ===========================================
                the_data = RNN.what_type_train(df_Data_Frame, data_type)
                #============BELOW THE DATA_TYPE_DF_PREDI WILL BE USED LATER!!!!!!!================
                data_type_DF_predi = RNN.getting_frame_of_the_data(df_Data_Frame, the_data)
        
                
                train = True
            elif cont_train == 'NO':
                cont_train = False
            
            if cont_train == False:
                future = fluid.future(number_of_days)
                
                #this has the prediction
                predicted_stock_price = RNN.making_prediction(regressor, sc, the_data, 
                                                      data_type_DF_predi, number_of_days, future)
                #this brings up the graph
                visual = RNN.visualize_predictions(predicted_stock_price, the_data, 
                                           data_type,number_of_days, ticker)
                train = fluid.train()
                if train == False:
                    
                    print('Have a great day!!!!')
                    train = False
                elif train == True:
                    ticker = fluid.ticker()
        
                    #Below returns a DataFrame known as df
                    df_Data_Frame = RNN.Stock_Data(str(ticker))
                    data_type = fluid.data_type()
                
                    #==================This returns the_data which is used in SCALLING!!!1 ===========================================
                    the_data = RNN.what_type_train(df_Data_Frame, data_type)
                    #============BELOW THE DATA_TYPE_DF_PREDI WILL BE USED LATER!!!!!!!================
                    data_type_DF_predi = RNN.getting_frame_of_the_data(df_Data_Frame, the_data)
                    train = True
                else: 
                    print('Have a great day!!!!')
                
                
                
            
        
            
        
        
     
