import unreal
MEL = unreal.MaterialEditingLibrary

from pamux_unreal_tools.base.material_expression.material_expression_container_base import MaterialExpressionContainerBase

class MaterialBase(MaterialExpressionContainerBase):
    def __init__(self, unrealAsset: unreal.Material):
        super().__init__(unrealAsset,
                         MEL.create_material_expression,
                         MEL.delete_all_material_expressions,
                         MEL.layout_material_expressions,
                         True)
