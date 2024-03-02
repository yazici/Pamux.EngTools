from PyQt6.QtWidgets import QMainWindow

from pamux_engtools.utils.ui_helper import UI

from pamux_engtools.ui.tabs.asset_library import AssetLibraryTab
from pamux_engtools.ui.tabs.distribution import DistributionTab
from pamux_engtools.ui.tabs.home import HomeTab
from pamux_engtools.ui.tabs.monetization import MonetizationTab
from pamux_engtools.ui.tabs.node_editor import NodeEditorTab
from pamux_engtools.ui.tabs.settings import SettingsTab
from pamux_engtools.ui.tabs.text_to_speech import TextToSpeechTab

# app = QApplication.instance()
# https://doc.qt.io/qt-6/qlineedit.html

# C:\src\Pamux.EngTools\.venv\Lib\site-packages\qt6_applications\Qt\bin\designer.exe
# C:\src\Pamux.EngTools\src\pamux_engtools\ui\MainWindow.ui
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.__app = app
        self.__config = self.__app.config

        UI.load(self)

        self.__assetLibraryTab = AssetLibraryTab(self)
        self.__distributionTab = DistributionTab(self)
        self.__homeTab = HomeTab(self)
        self.__monetizationTab = MonetizationTab(self)
        self.__nodeEditrTab = NodeEditorTab(self)
        self.__settingsTab = SettingsTab(self)
        self.__textToSpeechTab = TextToSpeechTab(self)

        self.editQuery.textChanged.connect(self.onQueryTextChanged)

        self.__assetLibraryTab.setCurrentTab()

    @property
    def config(self):
        return self.__config

    def onQueryTextChanged(self, queryText = None):
        if queryText is None:
            queryText = str(self.editQuery.text())
        else:
            queryText = str(queryText)

        self.__assetLibraryTab.refreshAssetContainersTable(queryText.lower())
