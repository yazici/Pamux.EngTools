from pamux_unreal_tools.base.material_expression_editor_property_base import MaterialExpressionEditorPropertyBase
from pamux_unreal_tools.base.material_expression_base import MaterialExpressionBase

class MaterialExpressionEditorPropertyImpl(MaterialExpressionEditorPropertyBase):
    def __init__(self, materialExpression: MaterialExpressionBase, name: str, type: str):
        super().__init__(materialExpression, name, type)

    def set(self, val):
        self.material_expression.unrealAsset.set_editor_property(self.name, val)

    def get(self):
        return self.material_expression.unrealAsset.get_editor_property(self.name)
