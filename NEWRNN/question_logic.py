#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:16:13 2019

@author: gavinswofford
"""
import sys
#from fluid import fluid

class question_logic:
    #this is to check if the input train is entered properly
    def asking_train():
        restart = str('RESTART')
        print('Press X to exit out of the program')
        to_Train_or_not_to_Train = input('Would you like to train again: ').upper()
         
        if to_Train_or_not_to_Train == 'YES':
             return True
       #the while loop is looking for a return of False or True to stop that is why restart will keep the loop going
        elif to_Train_or_not_to_Train == 'NO':
             return False
       
        elif to_Train_or_not_to_Train == 'X':
             
             print('Thanks and have a nice day')
             #sys.exit alows to cancel the program running 
             #it is the best and easiest way
             return sys.exit
        #the restart below will be used in the askingquestion file 
        #it will look for the spelling RESTART to loop the program
        else:
             print('Check spelling: ')
             return restart
         
    #this is a function for number_of_days it had to go to a function bc it is used
    #in multiple spots
    def number_of_days():
        
        
        number_of_days = int(input('How many days in the past would you like to compare your model (5-20): '))
        
        return number_of_days
    
    #The ticker function here is used in diffrent places that's why its in a function in this class
    def ticker():
        ticker = input('What stock would you like to train: ').upper()
        
        return ticker
    
    #this is empty for expermients later
    def ticker_for_prediction_only():
        pass
    
    
    #this one is super important it checks to see what is entered for the data type
    #in fluid the function is called again if the proper return isnt there
    def data_type_check():
        restart = str('RESTART')
        data_type = str(input('What type of data would you like train (High, Low, Open, Close): ')).lower().capitalize()
        if data_type == 'High' or data_type == 'Low' or data_type == 'Open' or data_type == 'Close':
            return data_type
        else:
            return restart
        
    
    
        
            
    
       
        
             
         
    