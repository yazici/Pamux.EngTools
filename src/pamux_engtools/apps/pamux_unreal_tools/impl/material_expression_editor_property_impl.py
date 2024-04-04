from pamux_unreal_tools.base.material_expression_editor_property_base import MaterialExpressionEditorPropertyBase
from pamux_unreal_tools.base.material_expression.material_expression_base_base import MaterialExpressionBaseBase

class MaterialExpressionEditorPropertyImpl(MaterialExpressionEditorPropertyBase):
    def __init__(self, material_expression: MaterialExpressionBaseBase, name: str, type: str):
        super().__init__(material_expression, name, type)

    def set(self, val):
        self.material_expression.unrealAsset.set_editor_property(self.name, val)

    def get(self):
        return self.material_expression.unrealAsset.get_editor_property(self.name)
