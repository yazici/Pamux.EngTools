import unreal
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

SocketNames = list[str]
TFloatParam = float

class InterfaceTypeBase:
    pass

class TResult(InterfaceTypeBase):
    pass

class THeight(InterfaceTypeBase):
    pass

class TAlpha(InterfaceTypeBase):
    pass

class TPixelDepth(InterfaceTypeBase):
    pass

class TMaterialAttributes(InterfaceTypeBase):
    pass

class TResults(InterfaceTypeBase):
    pass

class TLerp_Alpha_No_Contrast(InterfaceTypeBase):
    pass

class TVec4Components(InterfaceTypeBase):
    pass

class TRotated_Values(InterfaceTypeBase):
    pass

class TXYZAxes(InterfaceTypeBase):
    pass

class TVectorParam(InterfaceTypeBase):
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class TTextureCoordinate(InterfaceTypeBase):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TTextureObject(InterfaceTypeBase):
    materialSamplerType: unreal.MaterialSamplerType

    def __init__(self, materialSamplerType: unreal.MaterialSamplerType = unreal.MaterialSamplerType.SAMPLERTYPE_COLOR):
        self.materialSamplerType = materialSamplerType
