
from pamux_engtools.ui.tabs.tab_base import TabBase

class HomeTab(TabBase):
    def __init__(self, mainWindow):
        super().__init__(mainWindow, mainWindow.tabHome)
