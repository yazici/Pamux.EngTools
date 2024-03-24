import unreal

from pamux_unreal_tools.material_expression import MaterialExpression
from pamux_unreal_tools.material_expression_container import MaterialExpressionContainer

class Ports:
    UTiling = "UTiling"
    VTiling = "VTiling"

class TextureCoordinate(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, uTiling = 1.0, vTiling = 1.0, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionTextureCoordinate, node_pos_x, node_pos_y)

        self.UTiling = uTiling
        self.VTiling = vTiling

    @property
    def UTiling(self):
        return self.asset.get_editor_property(Ports.UTiling)

    @UTiling.setter
    def UTiling(self, value):
        self.asset.set_editor_property(Ports.UTiling, value)

    @property
    def VTiling(self):
        return self.asset.get_editor_property(Ports.VTiling)

    @VTiling.setter
    def VTiling(self, value):
        self.asset.set_editor_property(Ports.VTiling, value)