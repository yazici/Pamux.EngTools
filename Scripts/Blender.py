import sys
import os
import shutil
import win32api
from win32com.shell import shell, shellcon
import subprocess

from Apps import Apps
from Folders import Folders
from Debug import Debug

#print(os.pathsep)
#print(os.sep)
        
class Blender:
    @staticmethod
    def main():
        print("Blender")
        pass    
            
    @staticmethod
    def LoadBlendAndRunPythonScript(blendFilePath, pythonScriptPath, otherArgs = ''):
        command = f"{Apps.BLENDER_280_EXE} --background {blendFilePath} --python {pythonScriptPath} {otherArgs}"
        print (command)
        #output = subprocess.check_output([Apps.BLENDER_280_EXE, f"--background --python {fileName}"])
        output = os.system(command)
        print(output)

if __name__ == "__main__":
    Blender.main()
