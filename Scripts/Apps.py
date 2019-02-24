import sys
import os
import shutil
import win32api
from win32com.shell import shell, shellcon

from Folders import Folders
from Debug import Debug

#print(os.pathsep)
#print(os.sep)
        
class Apps:
    NOTEPADPLUSPLUS_EXE = os.path.join(Folders.getProgramFilesDirectory(), "Notepad++", "notepad++.exe")
    GIT_EXE = os.path.join(Folders.getProgramFilesDirectory(), "git",  "cmd", "git.exe")
    UNITY_EXE = os.path.join(Folders.getProgramFilesDirectory(), "Unity",  "Editor", "Unity.exe")
    BLENDER_EXE = os.path.join(Folders.getProgramFilesDirectory(), "Blender Foundation",  "Blender", "Blender.exe")

    
  
	# NuGet_EXE = "nuget.exe"
	# Putty_EXE = "putty.exe"
	# Pscp_EXE = "pscp.exe"
	# Rdp_EXE = "${env:windir}\system32\mstsc.exe"
	# DevEnvExe="${env:ProgramFiles(x86)}\Microsoft Visual Studio 14.0\Common7\IDE\devenv.exe"
	# BlenderExe="${env:ProgramFiles}\Blender Foundation\Blender\blender.exe"
	# SketchUpExe="${env:ProgramFiles}\SketchUp\SketchUp 2015\SketchUp.exe"
	# PaintDotNetExe="${env:ProgramFiles}\paint.net\PaintDotNet.exe"
	# FreeCADExe="${env:ProgramFiles}\FreeCAD_0.17.13433\bin\FreeCAD.exe"
	# OpenSCADExe="${env:ProgramFiles}\OpenSCAD\openscad.exe"
	# # GRBL Controller https://github.com/Denvi/Candle/
	# Candle_EXE = "${global:AppsRoot}\Candle\Candle.exe" 
	# GCAMExe="${global:AppsRoot}\gcam-se-win32-2015.05.13\gcam.exe"

	# KDiffExe="${env:ProgramFiles}\KDiff3\kdiff3.exe"
	# SevenZ_EXE ="${env:ProgramFiles}\7-Zip\7z.exe"
	# Gzip_EXE ="${global:AppsRoot}\gzip-1.3.12-1-bin\bin\gzip.exe"
	# Gzip_EXE ="${global:AppsRoot}\gnu\bin\gzip.exe"
	# Tar_EXE ="${global:AppsRoot}\gnu\bin\tar.exe"
    
    
    @staticmethod
    def main():
        print (Apps.NOTEPADPLUSPLUS_EXE)
        pass    
            
    
    
    

if __name__ == "__main__":
    Apps.main()
