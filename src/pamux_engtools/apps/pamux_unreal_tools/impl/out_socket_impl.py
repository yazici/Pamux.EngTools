from multipledispatch import dispatch

import unreal
MEL = unreal.MaterialEditingLibrary

from pamux_unreal_tools.base.material_expression_sockets_base import InSocket, OutSocket
from pamux_unreal_tools.base.material_expression_base import MaterialExpressionBase
from pamux_unreal_tools.utils.node_pos import NodePos

class OutSocketImpl(OutSocket):
    def __init__(self, materialExpression: MaterialExpressionBase, name: str, type: str) -> None:
        super().__init__(materialExpression, name, type)

    @dispatch(InSocket)
    def connectTo(self, inSocket: InSocket) -> bool:
        self.material_expression.material_expression_editor_x.set(inSocket.material_expression.material_expression_editor_x.get() - NodePos.DeltaX)
        return MEL.connect_material_expressions(self.material_expression.unrealAsset, self.name, inSocket.material_expression.unrealAsset, inSocket.name)
    
    @dispatch(unreal.MaterialProperty)
    def connectTo(self, materialProperty: unreal.MaterialProperty) -> bool:
        return MEL.connect_material_property(self.material_expression.unrealAsset, self.name, materialProperty)

    def connectToFunctionOutput(self, function_output) -> bool:
        self.material_expression.material_expression_editor_x.set(function_output.material_expression_editor_x.get() - NodePos.DeltaX)
        return MEL.connect_material_expressions(self.material_expression.unrealAsset, self.name, function_output.unrealAsset, "")