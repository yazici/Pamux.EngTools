import unreal

from pamux_unreal_tools.material_expression import MaterialExpression
from pamux_unreal_tools.material_expression_container import MaterialExpressionContainer

class Ports:
    R = "r"

class Constant(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, r, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionConstant, node_pos_x, node_pos_y)

        self.R = r

    @property
    def R(self):
        return self.asset.get_editor_property(Ports.R)

    @R.setter
    def R(self, value):
        self.asset.set_editor_property(Ports.R, value)


class Constant2Vector(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionConstant2Vector, node_pos_x, node_pos_y)

class Constant3Vector(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionConstant3Vector, node_pos_x, node_pos_y)

class Constant4Vector(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionConstant4Vector, node_pos_x, node_pos_y)
