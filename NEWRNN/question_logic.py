#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:16:13 2019

@author: gavinswofford
"""
import sys
from getting_data import RNN

class question_logic:
    #this is to check if the input train is entered properly
    def asking_train():
        restart = str('RESTART')
        print('Press X to exit out of the program')
        to_Train_or_not_to_Train = input('Would you like to train or predict: ').upper()
         
        if to_Train_or_not_to_Train == 'TRAIN':
             return True
       #the while loop is looking for a return of False or True to stop that is why restart will keep the loop going
        elif to_Train_or_not_to_Train == 'PREDICT':
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
             
         
    