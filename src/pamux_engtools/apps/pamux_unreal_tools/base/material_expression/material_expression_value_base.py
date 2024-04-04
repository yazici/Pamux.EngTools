from pamux_unreal_tools.base.material_expression.material_expression_base_base import MaterialExpressionBaseBase

class MaterialExpressionValueBase:
    def __init__(self, material_expression: MaterialExpressionBaseBase, name: str, type):
        self.material_expression: MaterialExpressionBaseBase = material_expression
        self.name: str = name
        self.type = type
