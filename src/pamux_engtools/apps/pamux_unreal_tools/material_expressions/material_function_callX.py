import unreal

from pamux_unreal_tools.material_expression import MaterialExpression
from pamux_unreal_tools.material_expression_container import MaterialExpressionContainer
from pamux_unreal_tools.material_function import material_function

class Ports:
    MaterialFunction = "material_function"

class MaterialFunctionCallX(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, materialFunction: material_function.MaterialFunction, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionMaterialFunctionCall, node_pos_x, node_pos_y)

        self.MaterialFunction = materialFunction

    @property
    def MaterialFunction(self):
        return self.asset.get_editor_property(Ports.MaterialFunction)

    @MaterialFunction.setter
    def MaterialFunction(self, value):
        self.asset.set_editor_property(Ports.MaterialFunction, value.asset)