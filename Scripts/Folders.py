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
    def getAllFoldersAndFiles(rootDir):
        for root, dirs, files in os.walk(rootDir, topdown=False):
            for name in files:
                yield os.path.join(root, name)
            for name in dirs:
                yield os.path.join(root, name)