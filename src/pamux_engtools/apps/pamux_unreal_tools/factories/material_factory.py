import unreal

from pamux_unreal_tools.factories.material_expression_container_factory import MaterialExpressionContainerFactory

from pamux_unreal_tools.impl.material_impl import MaterialImpl

class MaterialFactory(MaterialExpressionContainerFactory):
    def __init__(self):
        super().__init__(unreal.Material, unreal.MaterialFactoryNew(), MaterialImpl)
