import sys
import os
import shutil

import zipfile
import patoolib
import subprocess
from Folders import Folders
from Debug import Debug
from Blender import Blender
import blendfile
from shutil import copyfile
#print(os.pathsep)
#print(os.sep)

if os.name == 'nt':
    import win32api
    from win32com.shell import shell, shellcon
    import msvcrt
else:
    import keyboard  
# C:\assets\04102019_BlendSwap
class AssetUtils:
    def __init__(self, root):
        self.stop = False
        self.root = root
        self.original = os.path.join(self.root, "original")
        self.modified = os.path.join(self.root, "modified")
        self.unpacked = os.path.join(self.root, "unpacked")
        self.sanitizerPath = os.path.join(Folders.SCRIPTS_ROOT, "BlendSanitizer.py")
        
    def convertAndSanitizeFile(self, filePath):
        print(filePath)
             
             
    def getArchiveAndExtractedPaths(self, inFolder, outFolder, fileName):
        extractPath = os.path.join(outFolder, fileName)
        print(f"extractPath: {extractPath}")
        if (os.path.isdir(extractPath)):
            return (None, extractPath)
            
        print(f"Archive: {fileName}")
        
        archivePath = os.path.join(inFolder, fileName)
        return (archivePath, extractPath)
        
        
    def extractZip(self, inFolder, outFolder, fileName):
        archivePath, extractPath = self.getArchiveAndExtractedPaths(inFolder, outFolder, fileName)
        if (archivePath == None):
            return
 
        with zipfile.ZipFile(archivePath) as zip:
            zip.extractall(extractPath)
 
        
    def extractRar(self, inFolder, outFolder, fileName):
        archivePath, extractPath = self.getArchiveAndExtractedPaths(inFolder, outFolder, fileName)
        if (archivePath == None):
            return

        patoolib.extract_archive(archive = archivePath, outdir = extractPath)



        
    def sanitizeBlend(self, inFolder, outFolder, fileName):
        inPath = os.path.join(inFolder, fileName)
        
        #outPath = os.path.join(inFolder, fileName)
        #copyfile(inPath, outPath)
        
        
        
        Blender.LoadBlendAndRunPythonScript(inPath, self.sanitizerPath)

    def convertAndSanitizeFile(self, inFolder, outFolder, fileName):
        lFileName = fileName.lower()
        
        if (lFileName.endswith('.zip')):
            self.extractZip(inFolder, outFolder, fileName)
        elif (lFileName.endswith('.rar')):
            self.extractRar(inFolder, outFolder, fileName)
        elif (lFileName.endswith('.blend')):
            self.sanitizeBlend(inFolder, outFolder, fileName)
            
                
    def convertAndSanitizeFolder(self, inFolderRoot, outFolderRoot):
        for inFolder, subFolders, files in os.walk(inFolderRoot):
            for fileName in files:
                try:
                    if os.name == 'nt':
                        if msvcrt.kbhit():
                            ch = msvcrt.getch()     
                            if ch == b'q':
                                self.stop = True
                    else:
                        if keyboard.is_pressed('q'):
                            self.stop = True
                    if self.stop:
                        return          


                    outFolder = outFolderRoot
                    self.convertAndSanitizeFile(inFolder, outFolder, fileName)
                except:
                    #print (f"ERROR converting {fileName}")
                    continue
                
    @staticmethod
    def ConvertAndSanitizeAll(root):
        assetUtils = AssetUtils(root)
        #assetUtils.convertAndSanitizeFolder(assetUtils.original, assetUtils.unpacked)
        assetUtils.convertAndSanitizeFolder(assetUtils.unpacked, assetUtils.modified)
        
    @staticmethod
    def main():
        print("AssetUtils")
        pass    
            
    
    
    

if __name__ == "__main__":
    AssetUtils.main()
