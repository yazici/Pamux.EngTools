
import os

class Paths:
    MetadataExtension = "gdometa"

    ThisScriptDir = os.path.dirname(os.path.abspath(__file__))
    ProjectRootDir = os.path.dirname(ThisScriptDir)
    UiDir = os.path.join(ProjectRootDir, "ui")

    SystemDrive = os.environ["SystemDrive"]
    HomeDrive = os.environ["HOMEDRIVE"]

    ProgramFiles = os.environ["ProgramFiles"]
    ProgramFilesX86 = os.environ["ProgramFiles(x86)"]

    LocalAppData = os.environ["LOCALAPPDATA"]
    RoamingAppData = os.environ["APPDATA"]

    HomeDriveRoot = os.path.join( HomeDrive, os.path.sep)

    Src = os.path.join(HomeDriveRoot, "src")
    Apps = os.path.join(HomeDriveRoot, "apps")

    EngTools = os.path.join(Src, "Pamux.EngTools")
    EngData = os.path.join(EngTools, "Data")
    EngConfig = os.path.join(EngTools, "Config")
    EngToolsUIConfig = os.path.join(EngConfig, "petui.config.json")
    EngToolsPrefixesConfig = os.path.join(EngConfig, "petui.prefixes.txt")


    EngTemp = os.path.join(EngTools, "Temp")
    EngContent = os.path.join(EngTools, "Content")

    EngTempUnpackRoot = os.path.join(EngTemp, "UnPack")

    EngHarvestRoot = os.path.join(EngContent, "Harvest")

    LocalHtmlPath = os.path.join(EngData, "local.html")

    VoiceSaveDirectory = os.path.join(EngData, "Voice")

    GzipCli = os.path.join(Apps, "gzip-1.3.12-1-bin", "bin", "gzip.exe")
    SevenZipCli = os.path.join(ProgramFiles, "7-Zip", "7z.exe")

    UnityApp = os.path.join(ProgramFiles, "Unity")

    UnityAssetDownloadDefault = os.path.join(RoamingAppData, "Unity", "Asset Store-5.x")

    UnityAssetMetadataDefault = os.path.join(EngData, "UnityAssetStore")


    SketchupSearchUrl = "https://3dwarehouse.sketchup.com/search.html?backendClass=entity&q="

    @staticmethod
    def getUiPath(name: str):
        return os.path.join(Paths.UiDir, f"{name}.ui")