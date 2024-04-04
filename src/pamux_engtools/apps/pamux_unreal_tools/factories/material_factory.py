import unreal

from pamux_unreal_tools.impl.material_impl import MaterialImpl

from pamux_unreal_tools.base.material.material_factory_base import MaterialFactoryBase

class MaterialFactory(MaterialFactoryBase):
    def __init__(self):
        super().__init__(unreal.Material, unreal.MaterialFactoryNew(), MaterialImpl)
