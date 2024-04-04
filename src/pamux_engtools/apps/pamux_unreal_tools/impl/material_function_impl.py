import unreal

from pamux_engtools.apps.pamux_unreal_tools.base.material_function.material_function_base import MaterialFunctionBase

class MaterialFunctionImpl(MaterialFunctionBase):
    def __init__(self, unrealAsset: unreal.MaterialFunction):
        super().__init__(unrealAsset)
