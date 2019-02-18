import os
import shutil

from Folders import Folders

class Build:
    @staticmethod
    def PurgeBuildArtifacts():
        for name in Folders.getBuildArtifactsFolders():
            print("Removing: " + name)
            try:
                shutil.rmtree(name)
            except PermissionError:
                print("Can't delete")
                
                
Build.PurgeBuildArtifacts()