# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:17:43 2019

@author: dheeraj_kumar
"""

#import os
def DrawPlayingBoard(row, column):
    #terminal_size = os.get_terminal_size()
    #if row<= terminal_size.lines and column <= terminal_size.columns:
        for r in range(row*2):
            if r%2 == 0:
                print("|"+"  |"*column)
            else:
                print("-"*column*3)
        return True
    #else:
        #return False
        
if __name__ == "__main__":
    DrawPlayingBoard(4,12)    
