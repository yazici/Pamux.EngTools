import sys
import os
import shutil
import win32api
from win32com.shell import shell, shellcon

class Debug:
    @staticmethod
    def is_array(var):
        return isinstance(var, (list, tuple))
    
    @staticmethod
    def print(arg):   
        print("Printing {}".format(type(arg)))
    
        if isinstance(arg, str): 
            print(arg)
            return
            
        if isinstance(arg, list): 
            for item in arg:
                print(item)
                
        if isinstance(arg, set): 
            for item in arg:
                print(item)