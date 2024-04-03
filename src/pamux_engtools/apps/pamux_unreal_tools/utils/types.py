from unreal import LinearColor, FunctionInputType

from typing import NewType
#from typing import TypeAlias

SocketNames = list[str]

class TResult:
    pass
class THeight:
    pass

class TMaterialAttributes:
    pass

TFloatParam = float


# https://realpython.com/primer-on-python-decorators/

def material_function_interface(path):
    pass

def parameter_name_prefix(prefix):
    pass

class VecFBase:
    def __init__(self):
        self.linearColor = LinearColor()
        self.functionInputType = None

class Vec2f(VecFBase):
    def __init__(self, x: float, y: float):
        super().__init__()

        self.x = x
        self.y = y
        self.linearColor.r = self.x
        self.linearColor.g = self.y
        self.functionInputType = FunctionInputType.FUNCTION_INPUT_VECTOR2

class Vec3f(Vec2f):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y)
        self.z = z
        self.linearColor.b = self.z
        self.functionInputType = FunctionInputType.FUNCTION_INPUT_VECTOR3

class Vec4f(Vec3f):
    def __init__(self, x: float, y: float, z: float, w: float):
        super().__init__(x, y, z)
        self.w = w
        self.linearColor.a = self.w
        self.functionInputType = FunctionInputType.FUNCTION_INPUT_VECTOR4
