import sys
import os
import shutil
import win32api
from win32com.shell import shell, shellcon

from Folders import Folders
from Apps import Apps
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
            self.file.write("\n\n")
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
            
            generator.addSetVariable("PAMUX_PYTHON36_64_EXE", "%ProgramFiles(x86)%\Microsoft Visual Studio\Shared\Python36_64\python.exe")
            generator.addSetVariable("PAMUX_NOTEPADPLUSPLUS_EXE", Apps.NOTEPADPLUSPLUS_EXE)
            generator.addSetVariable("PAMUX_ENGTOOLS_GENDATA", Folders.ENGTOOLS_GENDATA)
            generator.addSetVariable("PAMUX_ENGTOOLS_ROOT", Folders.ENGTOOLS_ROOT)
            generator.addSetVariable("PAMUX_SCRIPTS_ROOT", Folders.SCRIPTS_ROOT)
            generator.addSetVariable("PAMUX_PAMWX_ROOT", Folders.PAMWX_ROOT)
            
            
    @staticmethod    
    def generate():
        EnvironmentFactory.generateAliases()
        EnvironmentFactory.generateScript()
        
        Folders.prepareFileSystem()