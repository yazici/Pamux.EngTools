import unreal

from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl
from pamux_unreal_tools.base.material_function.material_function_factory_base import MaterialFunctionFactoryBase

class MaterialFunctionFactory(MaterialFunctionFactoryBase):
    def __init__(self):
        super().__init__(unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew(), MaterialFunctionImpl)
