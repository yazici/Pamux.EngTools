from pamux_unreal_tools.base.material_expression_value_base import MaterialExpressionValueBase
from pamux_unreal_tools.base.material_expression_base_base import MaterialExpressionBaseBase

class MaterialExpressionEditorPropertyBase(MaterialExpressionValueBase):
    def __init__(self, materialExpression: MaterialExpressionBaseBase, name: str, type):
        super().__init__(materialExpression, name, type)