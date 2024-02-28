
from PyQt6 import uic

from utils.paths import Paths

class UI:
    @staticmethod
    def load(obj):
        uic.loadUi(Paths.getUiPath(obj.__class__.__name__), obj)