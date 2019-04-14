#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:28:28 2019

@author: gavinswofford
"""

from question_logic import question_logic

import sys


class fluid:
    #below is asking for the number of days that will be excluded from the training model
    #this number is also important for prediciting
    def number_of_days():
        number_of_days = question_logic.number_of_days()
        return number_of_days
    
    def ticker():
        #ticker needs to be used for predicting and for training
        ticker = question_logic.ticker()
        return ticker
    
    #Had to have a while loop for data_type to check if things are spelled properly
    #if they are not then the loop continues 
    def data_type():
        data_type = question_logic.data_type_check()
        while data_type == 'RESTART':
            data_type = question_logic.data_type_check()
        
        return data_type
   #train Had to have a while loop for data_type to check if things are spelled properly
    #if they are not then the loop continues 
    def train():
        train = question_logic.asking_train()
        while train != True and train != False and train != sys.exit:
            train = question_logic.asking_train()
        return train
    
    #future is new so it would not take up as much space on the main doc i moved it here so i could also
    #call on this function as needed
    def future(number_of_days):
        #============================reconfigure all of this!!!!!!!!!!!!!!+===================
        print("future has to be a larger number than: " + str(number_of_days))
        future_Days = int(input("How many days in the future would you like to predict: "))
        future = int(future_Days) + int(number_of_days)
        """===============FUTURE IS FOR PREDICTING THE FUTURE PRICES OF THE SELECTED STOCK"""
        return future
    
 
    
        
