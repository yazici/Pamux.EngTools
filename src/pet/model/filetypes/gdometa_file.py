from pathlib import Path

from model.asset_query import AssetQuery

class GDOMetaFile:
    def __init__(self, filePath : str):
        self.__filePath = filePath
        self.__assets = []
        
    @property
    def isFresh(self):
        return True
    
    def load(self):
        self.__assets = []

        if not Path(self.__filePath).is_file():
            return

        with open(self.__filePath,"r") as file:
            for aLine in file.readlines():
                self.__assets.append(aLine.strip()) 

    def save(self):
        pass

    def extract(self):
        pass

    @property
    def assets(self):
        return self.__assets

    
        
        # public void SaveMetaData()
        # {
        #     var dir = this.PamuxMetaDataPath.Substring(0, this.PamuxMetaDataPath.LastIndexOf('\\'));
        #     if (!Directory.Exists(dir))
        #     {
        #         Directory.CreateDirectory(dir);
        #     }
        #     File.WriteAllLines(this.PamuxMetaDataPath, Assets);
        # }



        # private bool HaveFreshMetadataFile()
        # {
        #     return File.Exists(this.PamuxMetaDataPath) && File.GetLastWriteTimeUtc(this.PamuxMetaDataPath) > File.GetLastWriteTimeUtc(this.FullPath);
        # }

        # private void LoadMetaData()
        # {
        #     Assets.AddRange(File.ReadAllLines(this.PamuxMetaDataPath));
        # }
    


    # public void InitializePackageContent()
    #     {
    #         foreach (string asset in Assets)
    #         {
    #             var unityAssetMetaData = Add(this, asset) as UnityAssetMetaData;
    #             if (unityAssetMetaData == null)
    #             {
    #                 continue;
    #             }

    #             if (!unityAssetMetaData.IsLeaf)
    #             {
    #                 unityAssetMetaData.PreviewImage = null;
    #                 continue;
    #             }
    #             unityAssetMetaData.ReadUnityMetaFile();
    #         }
    #     }


    #  <uc:QueryPanel Grid.Row="0" Grid.Column="0" Grid.ColumnSpan="3"  x:Name="QueryPanel" />
    #     <uc:QueryResults Grid.Row="1" Grid.Column="0" Grid.ColumnSpan="3"/>

        #  <CommandBinding Command="{x:Static local:AssetLibrary.SearchInAssetStoreCommand}"
        #         Executed="SearchInAssetStore"
        #         CanExecute="CanExecuteCommand" />
        # <CommandBinding Command="{x:Static local:AssetLibrary.OpenAssetFolderCommand}"
        #         Executed="OpenAssetFolder"
        #         CanExecute="CanExecuteCommand" />
        # <CommandBinding Command="{x:Static local:AssetLibrary.OpenMetadataFolderCommand}"
        #         Executed="OpenMetadataFolder"
        #         CanExecute="CanExecuteCommand" />
        # <CommandBinding Command="{x:Static local:AssetLibrary.ViewMetadataCommand}"
        #         Executed="ViewMetadata"
        #         CanExecute="CanExecuteCommand" />
        # <CommandBinding Command="{x:Static local:AssetLibrary.UnpackUnityPackageCommand}"
        #         Executed="UnpackUnityPackage"
        #         CanExecute="CanExecuteCommand" />
        # <CommandBinding Command="{x:Static local:AssetLibrary.HarvestAssetCommand}"
        #         Executed="HarvestAsset"
        #         CanExecute="CanExecutePerAssetCommand" />
        # <CommandBinding Command="{x:Static local:AssetLibrary.HarvestAssetWithDependenciesCommand}"
        #         Executed="HarvestAssetWithDependencies"
        #         CanExecute="CanExecutePerAssetCommand" />



    #     public static char[] Separators = { ' ', ',', '\t', '.', ';', '/', '_' };
    

    #     private void GenerateKeywordRecursively(string keyword)
    #     {
    #         if (IsGenericKeyword(false, keyword))
    #         {
    #             return;
    #         }
    #         this.keywords.Add(keyword);
    #         GenerateKeywordRecursively(keyword.Substring(0, keyword.Length - 1).Trim());
    #     }

    #     string[] generics = new string[] { "the", "and", "but" };

    #     bool IsGenericKeyword(bool extension, string keyword)
    #     {
    #         if (extension)
    #         {
    #             if (keyword == "unity")
    #             {
    #                 return true;
    #             }
    #         }
    #         if (keyword.Length < 2)
    #         {
    #             return true;
    #         }

    #         if (keyword.Length == 2)
    #         {
    #             return keyword != "3d";
    #         }



    #         foreach (string g in generics)
    #         {
    #             if (keyword == g)
    #             {
    #                 return true;
    #             }
    #         }

    #         if (keyword.Length == 3)
    #         {
    #             return false;
    #         }
    #         return false;
    #     }




#   

#         private void EnumerateUnityPackageFiles(string directory, IList<string> nameStack)
#         {
#             if (nameStack.Count < 2)
#             {
#                 var lastSubDirectoryIndex = directory.Length + 1;
#                 foreach (var subDirectory in directory.EnumerateDirectories())
#                 {
#                     nameStack.Add(subDirectory.Substring(lastSubDirectoryIndex));
#                     EnumerateUnityPackageFiles(subDirectory, nameStack);
#                 }
#             }
#             else
#             {
#                 foreach (var unityPackageFileFullPath in directory.EnumerateFiles("*.unitypackage"))
#                 {
#                     AllAssets.Add(new UnityPackageMetaData(unityPackageFileFullPath, nameStack[0], nameStack[1]));
#                 }
#             }

#             if (nameStack.Count > 0)
#             {
#                 nameStack.RemoveAt(nameStack.Count - 1);
#             }
#         }