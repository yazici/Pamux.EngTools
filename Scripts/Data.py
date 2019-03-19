import sys
import os
import shutil
import win32api
from win32com.shell import shell, shellcon

from Folders import Folders
from Debug import Debug

#print(os.pathsep)
#print(os.sep)

class Data:
    THIRDPARTY_CATALOG = os.path.join(Folders.ENGTOOLS_DATA, "3rdParty.json")    
    CMAKE_BASED_CPP_PROJECT_WIZARD = os.path.join(Folders.ENGTOOLS_DATA, "CMakeBasedCppProject.pwiz")

    @staticmethod
    def main():
        print (Data.THIRDPARTY_CATALOG)
        pass    


if __name__ == "__main__":
    Data.main()
