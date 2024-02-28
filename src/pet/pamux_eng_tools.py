# python 3.9.13
# 
# pip install userpaths
# https://pypi.org/project/PyQt6/    pip install PyQt6
# https://pypi.org/project/pyqt6-tools/   pip install pyqt6-tools

import sys
import os

from PyQt6.QtWidgets import QApplication

from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())
