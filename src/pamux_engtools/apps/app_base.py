import os, sys

from PyQt6.QtWidgets import QApplication

appsDir = os.path.dirname(os.path.realpath(__file__))

pamux_engtools_dir = os.path.abspath(os.path.join(appsDir, '..'))
if pamux_engtools_dir not in sys.path:
    sys.path.append(pamux_engtools_dir)

src_dir = os.path.abspath(os.path.join(pamux_engtools_dir, '..'))
if src_dir not in sys.path:
    sys.path.append(src_dir)

from pamux_engtools.utils.config import Config
from pamux_engtools.utils.paths import Paths

class AppBase:
    def __init__(self):
        self.__config = Config(Paths.EngToolsUIConfig, Paths.EngToolsPrefixesConfig)
        self.__app = QApplication(sys.argv)

    def createMainWindowImpl(self):
        return None

    def run(self):
        self.__mainWindow = self.createMainWindowImpl()
        self.__mainWindow.show()

        sys.exit(self.__app.exec())

    @property
    def config(self):
        return self.__config
