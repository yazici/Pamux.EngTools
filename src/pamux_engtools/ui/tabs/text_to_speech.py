from pamux_engtools.ui.tabs.tab_base import TabBase

class TextToSpeechTab(TabBase):
    def __init__(self, mainWindow):
        super().__init__(mainWindow, mainWindow.tabTextToSpeech)
