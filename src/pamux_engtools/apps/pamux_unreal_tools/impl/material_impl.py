import unreal

from pamux_unreal_tools.base.material.material_base import MaterialBase

class MaterialImpl(MaterialBase):
    def __init__(self, unrealAsset: unreal.Material):
        super().__init__(unrealAsset)

