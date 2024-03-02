from PyQt6.QtWidgets import QTableWidgetItem

from pamux_engtools.model.pamux_asset_library import PamuxAssetLibrary

from pamux_engtools.ui.tabs.tab_base import TabBase

class AssetLibraryTab(TabBase):
    def __init__(self, mainWindow):
        super().__init__(mainWindow, mainWindow.tabAssetLibrary)

        self.__pal = PamuxAssetLibrary(mainWindow.config)

        self.__tableAssetContainers = mainWindow.tableAssetContainers
        self.__tableAssetContainers.setColumnWidth(0, 100)

        self.refreshAssetContainersTable()

    def refreshAssetContainersTable(self, queryText: str = ""):
        filteredAssetContainers = self.__pal.query(queryText)

        self.__tableAssetContainers.setRowCount(len(filteredAssetContainers))

        row = 0
        for assetContainer in filteredAssetContainers:
            self.__tableAssetContainers.setItem(row, 0, QTableWidgetItem(assetContainer.name))
            self.__tableAssetContainers.setItem(row, 1, QTableWidgetItem(assetContainer.company))
            self.__tableAssetContainers.setItem(row, 2, QTableWidgetItem(assetContainer.category))
            row = row + 1
