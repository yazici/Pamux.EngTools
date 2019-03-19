import os
import shutil

from Folders import Folders
from Data import Data

class CMakeWrapper:
    def __init__(self, directory, subDirectories = None):
        self.cmakeFile = None
        self.directory = directory
        self.indentation = "    "
        if subDirectories == None:
            self.subDirectories = Folders.getImmediateSubFolders(self.directory)
        else:
            self.subDirectories = subDirectories
            
    def CMakeSetValueAsFileList(self, name, files):
        
        self.cmakeFile.write(f"SET({name}\n")
        for aFileName in files:
            self.cmakeFile.write(f"{self.indentation}{aFileName}\n")

        self.cmakeFile.write(f")\n\n")
    def CreateCMakeListsTxt(self):
        sourceFiles = []
        headerFiles = []
        
        for aFileName in Folders.getImmediateFiles(self.directory):
            if aFileName.endswith(".h"):
                headerFiles.append(aFileName)
            elif aFileName.endswith(".c"):
                sourceFiles.append(aFileName)
            elif aFileName.endswith(".cpp"):
                sourceFiles.append(aFileName)
                
        cmakeFilePath = os.path.join(self.directory, "CMakeLists.txt")
        with open(cmakeFilePath , "w+") as self.cmakeFile:
            self.cmakeFile.write("#\n")
            self.cmakeFile.write("# Generated using Pamux CMakeBasedCppWizard\n")
            self.cmakeFile.write("#\n\n")
            
            self.cmakeFile.write("CMAKE_MINIMUM_REQUIRED(VERSION 3.0)\n\n")
            
            self.CMakeSetValueAsFileList("SOURCE_FILES", sourceFiles)
            self.CMakeSetValueAsFileList("HEADER_FILES", headerFiles)
            
            for subDirectory in self.subDirectories:
                self.cmakeFile.write(f"add_subdirectory({subDirectory})\n")
        
        for subDirectory in self.subDirectories:
            cmakeWrapper = CMakeWrapper(os.path.join(self.directory, subDirectory))
            cmakeWrapper.CreateCMakeListsTxt()
            
            
class WizardBase:
    def __init__(self, pwizFilePath, projectRoot):
        self.pwizFilePath = Folders.getAbsolutePath(pwizFilePath)
        self.projectRoot = Folders.getAbsolutePath(projectRoot)
        self.currentDirectory = self.projectRoot
        self.section = "MAIN"   
        self.cmakeFile = None

    def Run(self):
        Folders.ensureDirectoryExists(self.currentDirectory)

        self.ReadWizardDefinition()
        self.CreateDirectoryStructure()
    
    def ProcessMainSectionLine(self, originalLine, normalizedLine):
        if normalizedLine == "begin_file_system":
            self.section = "FILE_SYSTEM"
        
    
            
    
        
    def ProcessFileSystemLine(self, originalLine, normalizedLine):
        if normalizedLine == "end_file_system":
            cmakeWrapper = CMakeWrapper(self.projectRoot, ["src", "tests", "examples", "3rdParty"])
            cmakeWrapper.CreateCMakeListsTxt()
            self.section = "MAIN"
            return
            
        if normalizedLine.startswith("/"):
            self.currentDirectory = Folders.getAbsolutePath(os.path.join(self.projectRoot, originalLine.strip()[1:]))
            Folders.ensureDirectoryExists(self.currentDirectory)
        else:
            filePathToCreate = Folders.getAbsolutePath(os.path.join(self.currentDirectory, originalLine.strip()))
            with open(filePathToCreate , "w+") as file:
                file.write("NOTHING")
                
    def ReadWizardDefinition(self):
        with open(self.pwizFilePath, "r") as pwizFile:
            for originalLine in pwizFile:
                normalizedLine = originalLine.strip()
                if len(normalizedLine) == 0:
                    continue
                if normalizedLine.startswith("#"):
                    continue
                
                normalizedLine = normalizedLine.lower()
                
                if self.section == "MAIN":
                    self.ProcessMainSectionLine(originalLine, normalizedLine)
                elif self.section == "FILE_SYSTEM":
                    self.ProcessFileSystemLine(originalLine, normalizedLine)
                    
    def CreateDirectoryStructure(self):
        #print(self.pwizFilePath)
        #print(self.projectRoot)
        pass       
                
                
# cppwiz C:\src\Pamux\Pamux.CppWizTest
class CMakeBasedCppWizard(WizardBase):        
    def __init__(self, projectRoot):
        WizardBase.__init__(self, Data.CMAKE_BASED_CPP_PROJECT_WIZARD, projectRoot)
       



