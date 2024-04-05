import unreal

from pamux_unreal_tools.base.material_expression.material_expression_value_base import MaterialExpressionValueBase
from pamux_unreal_tools.base.material_expression.material_expression_base_base import MaterialExpressionBaseBase

class Socket(MaterialExpressionValueBase):
    def __init__(self, material_expression: MaterialExpressionBaseBase, name: str, type, is_output: bool = False):
        super().__init__(material_expression, name, type)
        self.is_output: bool = is_output

    @property
    def unrealAsset(self) -> unreal.MaterialExpression:
        return self.material_expression.unrealAsset

class InSocket(Socket):
    def __init__(self, material_expression: MaterialExpressionBaseBase, name: str, type):
        super().__init__(material_expression, name, type, False)

class OutSocket(Socket):
    def __init__(self, material_expression: MaterialExpressionBaseBase, name: str, type):
        super().__init__(material_expression, name, type, True)

    def add_rt(self, container_name:str = None, socket_name:str = None):
        raise Exception("add_rt must be implemented")