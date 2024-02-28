import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QDockWidget, QTabWidget, QGridLayout, QPushButton, QFileDialog, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import uic

from model.pamux_asset_library import PamuxAssetLibrary
from utils.paths import Paths
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
    
    # def loadImages(self):
    #     folderPath = QFileDialog.getExistingDirectory(self, "Select Folder")
    #     if folderPath:
    #         # Clear existing widgets/images from the layout
    #         for i in reversed(range(1, self.layout.count())): 
    #             widget = self.layout.itemAt(i).widget()
    #             if widget is not None:
    #                 widget.deleteLater()

    #         row, col = 1, 0
    #         for filename in os.listdir(folderPath):
    #             if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
    #                 imagePath = os.path.join(folderPath, filename)
    #                 pixmap = QPixmap(imagePath)
    #                 label = QLabel(self)
    #                 label.setPixmap(pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
    #                 self.layout.addWidget(label, row, col)
    #                 col += 1
    #                 if col % 4 == 0:  # Adjust based on your grid needs
    #                     row += 1
    #                     col = 0