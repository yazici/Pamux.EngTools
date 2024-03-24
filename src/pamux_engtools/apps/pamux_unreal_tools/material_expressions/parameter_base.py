import unreal

from pamux_unreal_tools.material_expression import MaterialExpression
from pamux_unreal_tools.material_expression_container import MaterialExpressionContainer

class Ports:
    ParameterName = "ParameterName"
    DefaultValue = "DefaultValue"

class ParameterBase(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, expression_class, parameterName, defaultValue, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, expression_class, node_pos_x, node_pos_y)

        self.ParameterName = parameterName
        self.DefaultValue = defaultValue

    @property
    def ParameterName(self):
        return self.asset.get_editor_property(Ports.ParameterName)

    @ParameterName.setter
    def ParameterName(self, value):
        self.asset.set_editor_property(Ports.ParameterName, value)

    @property
    def DefaultValue(self):
        return self.asset.get_editor_property(Ports.DefaultValue)

    @DefaultValue.setter
    def DefaultValue(self, value):
        self.asset.set_editor_property(Ports.DefaultValue, value)