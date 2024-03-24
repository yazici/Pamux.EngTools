import unreal

from pamux_unreal_tools.material_expressions.parameter_base import ParameterBase
from pamux_unreal_tools.material_expression_container import MaterialExpressionContainer

class VectorParameter(ParameterBase):
    def __init__(self, parent: MaterialExpressionContainer, parameterName: str, defaultValue, node_pos_x: int = 0, node_pos_y: int = 0):
        super().__init__(parent, unreal.MaterialExpressionVectorParameter, parameterName, defaultValue, node_pos_x, node_pos_y)
