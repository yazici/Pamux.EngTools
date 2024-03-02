from PyQt6.QtWidgets import QWidget

class TabBase:
    def __init__(self, mainWindow, tab: QWidget):
        self.__mainWindow = mainWindow
        self.__tab = tab
        self.__config = self.__mainWindow.config

    def setCurrentTab(self):
        self.__mainWindow.tabWidget.setCurrentIndex(self.__mainWindow.tabWidget.indexOf(self.__tab))

    @property
    def config(self):
        return self.__config
    
    @property
    def mainWindow(self):
        return self.__mainWindow