import json
import os

class Config:
    def __init__(self, path, prefixesPath):
        with open(path, "r") as configFile:
            self.__data = json.load(configFile)

        self.__prefixes = []
        with open(prefixesPath, "r") as prefixesFile:
            for prefix in prefixesFile.readlines():
                if prefix.strip() != "" and not prefix.startswith("#"):
                    self.__prefixes.append(prefix.strip())

    @property
    def prefixes(self):
        return self.__prefixes

    @property
    def unityAssetDownloadRoot(self):
        return self.__data["unity_asset_download_root"]
    
    @property
    def unityAssetMetadataRoot(self):
        return self.__data["unity_asset_metadata_root"]

    @property
    def AssetsTSV(self):
        return os.path.join(self.unityAssetMetadataRoot, "Assets.tsv")
    
    @property
    def AssetTypesTSV(self):
        return os.path.join(self.unityAssetMetadataRoot, "AssetTypes.tsv")
    
    @property
    def AssetKeywordsTSV(self):
        return os.path.join(self.unityAssetMetadataRoot, "AssetKeywords.tsv")
    
    @property
    def AssetFilesTSV(self):
        return os.path.join(self.unityAssetMetadataRoot, "AssetFiles.tsv")

    def getMetadataPathFromDownloadedPackagePath(self, downloadedPackagePath):
        return os.path.join(self.unityAssetMetadataRoot, downloadedPackagePath[len(self.unityAssetDownloadRoot)+1:].replace(".unitypackage", ".gdometa"))