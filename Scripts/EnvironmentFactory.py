import sys
import os
import shutil
import win32api
from win32com.shell import shell, shellcon
from Folders import Folders
from Debug import Debug
from Environment import Environment

class EnvironmentFactory:
    def __init__(self, originalFilePath, filePath):
        self.originalFilePath = originalFilePath
        self.filePath = filePath

    def __enter__(self):       
        if self.originalFilePath == None:
            self.file = open(self.filePath, "w")
        else:
            shutil.copyfile(self.originalFilePath, self.filePath)    
            self.file = open(self.filePath, "a")
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):        
        self.file.close()
        
    def addFolderAlias(self, alias, folder):
        self.file.write("l{}=dir /x \"{}\"\n".format(alias, folder))
        self.file.write("c{}=pushd \"{}\"\n".format(alias, folder))
        self.file.write("x{}=explorer \"{}\"\n".format(alias, folder))
        
    def addSetVariable(self, variable, value):
        self.file.write("set {}={}\n".format(variable, value))
        
    @staticmethod    
    def generateAliases():
        with EnvironmentFactory("aliases.txt", "gen_aliases.txt") as generator:
            generator.addFolderAlias("badd", Folders.getBlenderAddOnsFolder())
    
    @staticmethod    
    def generateScript():        
        with EnvironmentFactory(None, "gen_env.cmd") as generator:
            generator.addSetVariable("PATH", Environment.getSegmentedEnvironmentVariableNormalizedValue("PATH"))
            
    @staticmethod    
    def generate():
        EnvironmentFactory.generateAliases()
        EnvironmentFactory.generateScript()