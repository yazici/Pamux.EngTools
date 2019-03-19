import sys
import os
import shutil
import win32api
from win32com.shell import shell, shellcon

# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python get-pip.py
# python -m pip install pywin32

# PATHEXT+=PY
# C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\


#print (sys.version)
#print (sys.executable)
#print (os.path.dirname(sys.executable))

class Folders: 
    BLENDER_VERSION = "2.80"
    
    SRC_ROOT = "c:/src"
    ASSETS_ROOT = "c:/assets"
    APPS_ROOT = "c:/apps"
    
    BLENDER_APP_ROOT=os.path.join(APPS_ROOT, "blender-2.80")
    BLENDER_PYTHON_EXE=os.path.join(BLENDER_APP_ROOT, "2.80/python/bin")
    
    SCRIPTS_ROOT = os.path.dirname(os.path.abspath( __file__ ))
    PAMWX_ROOT = os.path.join(SCRIPTS_ROOT, "pamwx")
    
    ENGTOOLS_ROOT = os.path.dirname(SCRIPTS_ROOT)
    ENGTOOLS_GENDATA = os.path.join(ENGTOOLS_ROOT, "GenData")
    ENGTOOLS_DATA = os.path.join(ENGTOOLS_ROOT, "Data")
    
    BUILD_ARTIFACTS = set()
    BUILD_ARTIFACTS.add("bin")
    BUILD_ARTIFACTS.add("obj")
    BUILD_ARTIFACTS.add("__pycache__")

    PATH_ALIASES = {}
    
    
    
    @staticmethod
    def getStartupDirectory():
        # 'C:\\Users\\<USERNAME>\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        return shell.SHGetFolderPath(0, shellcon.CSIDL_STARTUP, None, 0) 
        
    @staticmethod
    def getCommonStartupDirectory():
        # 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        return shell.SHGetFolderPath(0, shellcon.CSIDL_COMMON_STARTUP, None, 0)
        
    @staticmethod
    def getProgramFilesDirectory():
        return shell.SHGetFolderPath(0, shellcon.CSIDL_PROGRAM_FILES, None, 0)
    
    @staticmethod
    def getProgramFilesx86Directory():
        return shell.SHGetFolderPath(0, shellcon.CSIDL_PROGRAM_FILESX86, None, 0)
    
    @staticmethod
    def getRoamingFolders():
        return shell.SHGetFolderPath(0, shellcon.CSIDL_APPDATA, None, 0)
    
    @staticmethod
    def getBlenderFolder():
        return os.path.join(Folders.getRoamingFolders(), "Blender Foundation", "Blender", Folders.BLENDER_VERSION)
    
    @staticmethod
    def getBlenderAddOnsFolder():
        return os.path.join(Folders.getBlenderFolder(), "scripts", "addons")
    
    @staticmethod
    def getAbsolutePath(alias_or_path):
        if (alias_or_path in Folders.PATH_ALIASES):
            return Folders.PATH_ALIASES[alias_or_path]()
        return os.path.abspath(alias_or_path)

    @staticmethod
    def getMatchingFolders(rootDir, namesToMatch):
        for root, dirs, files in os.walk(rootDir, topdown=False):        
            for name in dirs:
                if (name.lower() in namesToMatch):
                    yield os.path.join(root, name)
                    
    @staticmethod
    def getBuildArtifactsFolders():
        return Folders.getMatchingFolders(Folders.SRC_ROOT, Folders.BUILD_ARTIFACTS)
                    
    @staticmethod
    def getAllFolders(rootDir):
        for root, dirs, files in os.walk(rootDir, topdown=False):        
            for name in dirs:
                yield os.path.join(root, name)
                
    @staticmethod
    def getImmediateSubFolders(rootDir):
        return [name for name in os.listdir(rootDir)
            if os.path.isdir(os.path.join(rootDir, name))]  

    @staticmethod
    def getImmediateFiles(rootDir):
        return [name for name in os.listdir(rootDir)
            if os.path.isfile(os.path.join(rootDir, name))]  
            
    @staticmethod
    def getAllFoldersAndFiles(rootDir):
        for root, dirs, files in os.walk(rootDir, topdown=False):
            for name in files:
                yield os.path.join(root, name)
            for name in dirs:
                yield os.path.join(root, name)
    
    @staticmethod
    def ensureDirectoryExists(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod   
    def prepareFileSystem():
        Folders.ensureDirectoryExists(Folders.ENGTOOLS_GENDATA)
