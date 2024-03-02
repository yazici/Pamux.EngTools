import os
from pathlib import Path
import shutil

class AssetMetadata:
    def __init__(self, parent, filePath : str):
        self.__parent = parent
        self.__filePath = filePath

        self.__name = Path(self.__filePath).stem
        self.__isComposite = self.__filePath.endswith(".prefab")

        self.__children = []

        self.__relativePath = None

        self.__guid = None

        if self.__parent is None:
            self.__root = self
            self.__depth = 1
        else:
            self.__root = self.__parent.root
            self.__depth = self.__parent.depth + 1
            self.__parent._children.append(self)

        self.__keywords = set()
            
    @property
    def previewImagePath(self):
        pass        

    @property
    def isLeaf(self):
        return len(self.__children) == 0
    
    @property
    def isHarvestable(self):
        return self.isLeaf
    
    @property
    def isComposite(self):
        return self.__isComposite

    @property
    def isExpanded(self):
        return self.__depth <= 3
    
    @property
    def name(self):
        return self.__name

    def ensureChild(self, name: str):
        pass

    def dump(self):
        # print("  " * self.__depth, self.__name)
        for child in self.__children:
            child.dump()

    def copy(self, sourceRoot: str, destinationRoot: str):
        shutil.copyfile(os.path.join(sourceRoot, self.__relativePath), os.path.join(destinationRoot, self.__relativePath))
