from unreal import LinearColor, FunctionInputType

from typing import NewType
#from typing import TypeAlias
from functools import wraps
import functools
from typing import Any, Callable

SocketNames = list[str]

class TResult:
    pass
class THeight:
    pass

class TMaterialAttributes:
    pass

TFloatParam = float


# https://realpython.com/primer-on-python-decorators/
import inspect
class material_function_interface:
    def __init__(self, asset_path):
        self.asset_path = asset_path

    def __call__(self, func):
        func._asset_path = self.asset_path
        return func

class parameter_name_prefix:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        func._parameter_name_prefix = self.prefix
        return func

class class_builder:
    def __init__(self, class_name):
        self.class_name = class_name

    def __call__(self, original_function):
        def wrapper(*args, **kwargs):
            _self = args[0]
            _self.begin_class(self.class_name)
            result = original_function(*args, **kwargs)
            _self.end_class()
            return result
        return wrapper


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
