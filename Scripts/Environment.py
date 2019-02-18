import sys
import os
import shutil
import win32api
from win32com.shell import shell, shellcon
from Folders import Folders
from Debug import Debug

#print(os.pathsep)
#print(os.sep)
        
class Environment:
    @staticmethod
    def main():
        pass    
        
    @staticmethod
    def getPathSegments():
        return getEnvironmentVariableSegments("PATH")
        
    @staticmethod
    def getEnvironmentVariableSegments(variable):
        return os.environ[variable].split(os.pathsep)
        
    @staticmethod
    def removeDuplicateSegments(segments, ignoreCase = True):
        temp = set()
        result = list()
        for segment in segments:
            name = segment
            if ignoreCase:
                name = name.lower()
            
            if name not in temp:
                temp.add(name)
                result.append(segment)
        return result        

    @staticmethod
    def mergeSegments(segments):
        result = ""
        for segment in segments:
            if result != "":
                result = result + os.pathsep
            result = result + segment
        return result   

    @staticmethod
    def getSegmentedEnvironmentVariableNormalizedValue(variable): 
        return Environment.mergeSegments(
            Environment.removeDuplicateSegments(
                Environment.getEnvironmentVariableSegments(variable)
            )
        )
    
    @staticmethod
    def normalizeSegmentedEnvironmentVariable(variable):
        normalizedValue = Environment.getSegmentedEnvironmentVariableNormalizedValue(variable)
        os.environ[variable] = normalizedValue
    
Environment.normalizeSegmentedEnvironmentVariable("PATH")

if __name__ == "__main__":
    Environment.main()
