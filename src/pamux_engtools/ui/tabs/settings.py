from pamux_engtools.ui.tabs.tab_base import TabBase

class SettingsTab(TabBase):
    def __init__(self, mainWindow):
        super().__init__(mainWindow, mainWindow.tabSettings)


# Defaults
        # os.path.join(Paths.RoamingAppData, "Unity", "Asset Store-5.x")

        # os.path.join(Paths.EngData, "UnityAssetStore")

        self.mainWindow.editUnityAssetMetadataRoot.setText(self.config.unityAssetMetadataRoot, )
        self.mainWindow.editUnityAssetDownloadRoot.setText(self.config.unityAssetDownloadRoot)
