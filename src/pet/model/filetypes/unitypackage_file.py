import os
from pathlib import Path

from model.asset_query import AssetQuery
from model.filetypes.gdometa_file import GDOMetaFile
from utils.paths import Paths

class UnityPackageFile:
    def __init__(self, filePath : str):
        self.__filePath = filePath
        self.__name = Path(self.__filePath).stem
        self.__gdoMetaFilePath = Paths.getGDOMetaPathFromUnityPackagePath(self.__filePath)
        self.__gdoMetaFile = GDOMetaFile(self.__gdoMetaFilePath)

    @property
    def gdoMetaFile(self):
        return self.__gdoMetaFile
    
    @property
    def name(self):
        return self.__name
        


    # public static void ExtractMetaData(string unityPackageFullPath, IList<string> assets)
    #     {
    #         var archive = ArchiveFactory.Open(unityPackageFullPath);
    #         if (archive == null)
    #         {
    #             return;
    #         }

    #         foreach (var volume in archive.Entries)
    #         {
    #             ProcessArchiveVolume(volume, assets);
    #         }
    #     }


    #     private static void ProcessArchiveVolume(IArchiveEntry volume, IList<string> assets)
    #     {
    #         Func<IArchiveEntry, string> getFirstLine = (entry) =>
    #         {
    #             var path = string.Empty;
    #             using (var sr = new StreamReader(entry.OpenEntryStream()))
    #             {
    #                 path = sr.ReadLine();
    #             }
    #             return path;
    #         };

    #         var volumeStreamFilePath = Path.GetTempFileName();
    #         try
    #         {
    #             using (var tempStream = File.Open(volumeStreamFilePath, FileMode.Open))
    #             {
    #                 volume.WriteTo(tempStream);
    #                 tempStream.Flush();

    #                 using (var tempArchive = ArchiveFactory.Open(tempStream))
    #                 {
    #                     var pathEntries = from entry in tempArchive.Entries.ToArray()
    #                                       where Path.GetFileName(entry.Key).Contains("pathname")
    #                                             && !entry.IsDirectory
    #                                       select entry;

    #                     var toExtract = pathEntries.ToDictionary(
    #                         pathEntry => Path.GetDirectoryName(pathEntry.Key),
    #                         pathEntry => getFirstLine(pathEntry));

    #                     var assetEntries = from entry in tempArchive.Entries.ToArray()
    #                                        where Path.GetFileName(entry.Key).Contains("asset")
    #                                              && !entry.IsDirectory
    #                                        select new
    #                                        {
    #                                            entry = entry,
    #                                            path = toExtract[Path.GetDirectoryName(entry.Key)]
    #                                        };


    #                     foreach (var asset in assetEntries)
    #                     {
    #                         assets.Add(asset.path);
    #                     }
    #                 }

    #             }
    #         }
    #         finally
    #         {
    #             if (volumeStreamFilePath != null && File.Exists(volumeStreamFilePath))
    #             {
    #                 File.Delete(volumeStreamFilePath);
    #             }
    #         }
    #     }