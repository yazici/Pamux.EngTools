import unreal

from pamux_unreal_tools.material_expressions.parameter_base import ParameterBase
from pamux_unreal_tools.material_expression_container import MaterialExpressionContainer

class StaticBoolParameter(ParameterBase):
    def __init__(self, parent: MaterialExpressionContainer, parameterName, defaultValue, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionStaticBoolParameter, parameterName, defaultValue, node_pos_x, node_pos_y)
