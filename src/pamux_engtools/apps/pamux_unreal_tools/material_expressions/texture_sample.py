import unreal

from pamux_unreal_tools.material_expression import MaterialExpression
from pamux_unreal_tools.material_expression_container import MaterialExpressionContainer

class TextureSample(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionTextureSample, node_pos_x, node_pos_y)
