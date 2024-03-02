import os

import glob

from model.asset_query import AssetQuery
from model.unity_asset_container import UnityAssetContainer
from utils.paths import Paths

class PamuxAssetLibrary:
    def __init__(self):
        self.__assetContainers = []
        self.loadDatabase()


        # for gdoMetaPath in glob.glob(os.path.join(Paths.UnityAssetStoreMetadata, "**", "**", f"*.{Paths.MetadataExtension}")):
        #     self.__assetContainers.append(UnityPackagedAssets(None, gdoMetaPath))

    @property
    def shouldRecreateDatabase(self):
        return len(self.__assetContainers) == 0

    def ensureAssetDatabaseIsFresh(self):
        if self.shouldRecreateDatabase:
            self.recreateAssetDatabase()

    def recreateAssetDatabase(self):
        pass

    def loadDatabase(self):
        assetContainers = []
        self.enumerateDownloadedUnityAssetStoreFolders(Paths.UnityAssetStore, [], assetContainers)
    
        self.__assetContainers = assetContainers
        for asset in self.__assetContainers:
            asset.initialize()

    def enumerateDownloadedUnityAssetStoreFolders(self, directory: str, dirNames: list, assetContainers: list):
        if len(dirNames) < 2:
            for subDirectory in os.listdir(directory):
                fullName = os.path.join(directory, subDirectory)
                if not os.path.isdir(fullName):
                    continue

                dirNames.append(subDirectory)
                self.enumerateDownloadedUnityAssetStoreFolders(fullName, dirNames, assetContainers)

        else:
            for unityPackageFileFullPath in glob.glob(os.path.join(directory, "*.unitypackage")):
                if not os.path.isfile(unityPackageFileFullPath):
                    continue

                assetContainer = UnityAssetContainer(unityPackageFileFullPath, dirNames[0], dirNames[1])
                assetContainers.append(assetContainer)

        if len(dirNames) > 0:
            dirNames.pop()

    def query(self, queryText):
        result = []

        for assetContainer in self.__assetContainers:
            if assetContainer.match(AssetQuery(queryText)):
                result.append(assetContainer)

        return result
    
    def dump(self):
        for assetContainer in self.__assetContainers:
            assetContainer.dump()

