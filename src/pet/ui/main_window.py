from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from model.pamux_asset_library import PamuxAssetLibrary
from utils.ui_helper import UI

# app = QApplication.instance()
# https://doc.qt.io/qt-6/qlineedit.html

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__pal = PamuxAssetLibrary()

        UI.load(self)

        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabAssetLibrary))
        self.editQuery.textChanged.connect(self.onQueryTextChanged)
        self.tableAssetContainers.setColumnWidth(0, 100)
        self.refreshAssetContainersTable()

    def onQueryTextChanged(self, queryText = None):
        if queryText is None:
            queryText = str(self.editQuery.text())
        else:
            queryText = str(queryText)

        self.refreshAssetContainersTable(queryText.lower())

    def refreshAssetContainersTable(self, queryText: str = ""):
        assetContainers = self.__pal.query(queryText)
        row = 0
        self.tableAssetContainers.setRowCount(len(assetContainers))
        for assetContainer in assetContainers:
            self.tableAssetContainers.setItem(row, 0, QTableWidgetItem(assetContainer.name))
            self.tableAssetContainers.setItem(row, 1, QTableWidgetItem(assetContainer.company))
            self.tableAssetContainers.setItem(row, 2, QTableWidgetItem(assetContainer.category))
            row = row + 1
