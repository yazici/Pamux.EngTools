# python 3.9.13
# 
# pip install userpaths
# https://pypi.org/project/PyQt6/    pip install PyQt6
# https://pypi.org/project/pyqt6-tools/   pip install pyqt6-tools

from app_base import AppBase

from pamux_engtools.ui.main_window import MainWindow

class App(AppBase):
    def createMainWindowImpl(self):
        return MainWindow(self)

if __name__ == '__main__':
    app = App()
    app.run()
