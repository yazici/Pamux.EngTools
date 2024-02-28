from model.asset_query import AssetQuery

from model.filetypes.unitypackage_file import UnityPackageFile
from model.filetypes.gdometa_file import GDOMetaFile

from utils.string_utils import StringUtils

# *.unitypackage files are Unity Asset Containers
class UnityAssetContainer:
    Prefixes = ["Complete Projects", "Editor Extensions", "3D Models", "Unity Essentials", "Unity Tech Demos", "Sample Projects", 
                    "Packs", "Tutorials", "Terrain", "Environments", "Vegetation", "Systems"]
    
    def __init__(self, unityPackageFileFullPath : str, company: str, assetSubFolder: str):
        self.__unityPackageFile = UnityPackageFile(unityPackageFileFullPath)
        self.__company = company
        self.__categoryPath = self.get_category_path(assetSubFolder)
        self.__individualAssets = []
        self.__keywords = set()

    @property
    def name(self):
        return self.__unityPackageFile.name

    @property
    def company(self):
        return self.__company

    @property
    def category(self):
        return ":".join(self.__categoryPath)
    
    def get_category_path(self, assetSubFolder):
        result = []

        for prefix in UnityAssetContainer.Prefixes:
            if assetSubFolder.startswith(prefix):
                result.append(prefix.strip())
                assetSubFolder = assetSubFolder[len(prefix):].strip()

        if len(assetSubFolder) != 0:
            print(assetSubFolder)
            result.append(assetSubFolder)

        return result

    def initialize(self):
        if self.__unityPackageFile.gdoMetaFile.isFresh:
             self.__unityPackageFile.gdoMetaFile.load()
        else:
             self.__unityPackageFile.gdoMetaFile.extract()
             self.__unityPackageFile.gdoMetaFile.save()

        self.initializePackageContent()
        self.generateKeywords()
        
    def dump(self):
        for child in self.__individualAssets:
            child.dump()

    def match(self, query: AssetQuery):
        for token in query.tokens:
            if token not in self.__keywords:
                return False
        return True

    def initializePackageContent(self):
        pass

    def generateKeywords(self):
        self.generateKeywordsFor(self.name)
        self.generateKeywordsFor(self.category)
        self.generateKeywordsFor(self.company)

        for asset in self.__individualAssets:
            self.generateKeywordsFor(asset[len("Assets/"):], False)


    def generateKeywordsFor(self, keyword: str, prefixes = True):
        keyword = keyword.lower()

        if prefixes:
            for kw in StringUtils.splitex(keyword):
                self.generateKeywordsRecursively(kw)
        else:
            for kw in StringUtils.splitex(keyword):
                kw = kw.strip()

                if not StringUtils.isGenericKeyword(keyword.endswith("." + kw), kw):
                    self.__keywords.add(kw)

    def generateKeywordsRecursively(self, keyword: str):
        if StringUtils.isGenericKeyword(False, keyword):
            return
        self.__keywords.add(keyword)
        self.generateKeywordsRecursively(keyword[0: len(keyword) - 1].strip())



    
