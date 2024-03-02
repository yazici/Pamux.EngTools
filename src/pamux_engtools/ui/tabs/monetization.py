from pamux_engtools.ui.tabs.tab_base import TabBase

class MonetizationTab(TabBase):
    def __init__(self, mainWindow):
        super().__init__(mainWindow, mainWindow.tabMonetization)
