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

class Int2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Float3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class Float4:
    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class Transform:
    def __init__(self, pos: Float3, rot: Float4, scale: Float3):
        self.pos = pos
        self.rot = rot
        self.scale = scale

class AbstractNoise:
    def __init__(self, seed):
        self.seed = seed

class PerlinNoise(AbstractNoise):
    def __init__(self, seed):
        super().__init__(seed)

class HeightMapNoise(PerlinNoise):
    def __init__(self, seed):
        self.seed = seed

class Stamp:
    def __init__(self, name, transform: Transform):
        self.name = name
        self.transform = transform

class Biome:
    def __init__(self, name, transform: Transform):
        self.name = name
        self.transform = transform

class Object:
    def __init__(self, name, transform: Transform):
        self.name = name
        self.transform = transform

class BiomeInstance:
    def __init__(self, name, transform: Transform):
        self.name = name
        self.transform = transform

class Material:
    def __init__(self, name):
        self.name = name


        
class Layer:
    def __init__(self, name):
        self.name = name

class Distribution:
    def __init__(self, name):
        self.name = name

class Erosion:
    def __init__(self):
        super().__init__()

class HeightMap:
    def __init__(self):
        super().__init__()



class Container:
    def __init__(self):
        self.__items = []

class Stamps(Container):
    def __init__(self):
        super().__init__()

class Biomes(Container):
    def __init__(self):
        super().__init__()

class BiomeInstances(Container):
    def __init__(self):
        super().__init__()

class Objects(Container):
    def __init__(self):
        super().__init__()

class Materials(Container):
    def __init__(self):
        super().__init__()


class Trees(Container):
    def __init__(self):
        super().__init__()

class Undergrowth(Container):
    def __init__(self):
        super().__init__()

class Terrain:
    ChunkSize = 512
    
    def __init__(self):
        self.sizeX = 1024
        self.sizeY = 1024

        self.seed = 1

        self.maxHeight = 1024

        self.heightMap = HeightMap()

        self.stamps = Stamps()
        self.noise = HeightMapNoise()
        self.erosion  = Erosion()
        
        # object
        self.biomes = Biomes()
        self.biomeInstances = BiomeInstances()
        self.trees = Trees()
        self.undergrowth = Undergrowth()

    def generate(self):

        self.stamps.apply()
        self.noise.apply()
        self.erosion.apply()
