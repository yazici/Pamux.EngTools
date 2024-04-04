import unreal

SocketNames = list[str]



class VecFBase:
    def __init__(self):
        self.linearColor = unreal.LinearColor()
        self.functionInputType = None

class Vec2f(VecFBase):
    def __init__(self, x: float, y: float):
        super().__init__()

        self.x = x
        self.y = y
        self.linearColor.r = self.x
        self.linearColor.g = self.y
        self.functionInputType = unreal.FunctionInputType.FUNCTION_INPUT_VECTOR2

class Vec3f(Vec2f):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y)
        self.z = z
        self.linearColor.b = self.z
        self.functionInputType = unreal.FunctionInputType.FUNCTION_INPUT_VECTOR3

class Vec4f(Vec3f):
    def __init__(self, x: float, y: float, z: float, w: float):
        super().__init__(x, y, z)
        self.w = w
        self.linearColor.a = self.w
        self.functionInputType = unreal.FunctionInputType.FUNCTION_INPUT_VECTOR4
