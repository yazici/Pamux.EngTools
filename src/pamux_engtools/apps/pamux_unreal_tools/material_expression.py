import unreal
from multipledispatch import dispatch
from pamux_unreal_tools.material_expression_container import *

# in cmd: "C:\Program Files\Epic Games\UE_5.3\Engine\Binaries\ThirdParty\Python3\Win64\python.exe" -m pip install multipledispatch

MEL = unreal.MaterialEditingLibrary

class MaterialExpressionBase:
    def __init__(self, parent: MaterialExpressionContainer, expression_class, node_pos_x = 0, node_pos_y = 0):
        self.parent = parent
        self.expression_class = expression_class

        self.asset = self.parent.createMaterialExpression(self.expression_class, node_pos_x, node_pos_y)

class MaterialExpression(MaterialExpressionBase):
    def __init__(self, parent: MaterialExpressionContainer, expression_class, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, expression_class, node_pos_x, node_pos_y)

    @dispatch(unreal.MaterialProperty)
    def connectTo(self, materialProperty: unreal.MaterialProperty) -> bool:
        return MEL.connect_material_property(self.asset, "", materialProperty)

    @dispatch(str, MaterialExpressionBase, str)
    def connectTo(self, outPortName: str, materialExpression: MaterialExpressionBase, inPortName: str) -> bool:
        return MEL.connect_material_expressions(self.asset, outPortName, materialExpression.asset, inPortName)
    
    # @dispatch(MaterialExpressionBase, str)
    # def connectTo(self, OutSocket) -> bool:
    #     return MEL.connect_material_expressions(self.asset, "", materialExpression.asset, inPortName)
