from multipledispatch import dispatch

import unreal
MEL = unreal.MaterialEditingLibrary

from pamux_unreal_tools.base.material_expression_sockets_base import InSocket, OutSocket
from pamux_unreal_tools.base.material_expression_base import MaterialExpressionBase

class InSocketImpl(InSocket):
    def __init__(self, materialExpression: MaterialExpressionBase, name: str, type: str) -> None:
        super().__init__(materialExpression, name, type)

    @dispatch(OutSocket)
    def comesFrom(self, sourceOutSocket: OutSocket) -> bool:
        return self.__comesFrom_impl(sourceOutSocket.material_expression, sourceOutSocket.name)

    @dispatch(MaterialExpressionBase)
    def comesFrom(self, sourceMaterialExpression: MaterialExpressionBase) -> bool:
        return self.__comesFrom_impl(sourceMaterialExpression, "")

    def __comesFrom_impl(self, sourceMaterialExpression: MaterialExpressionBase, sourceOutSocketName: str) -> bool:
        self.material_expression.gotoRightOf(sourceMaterialExpression)
        return MEL.connect_material_expressions(sourceMaterialExpression.unrealAsset, sourceOutSocketName, self.material_expression.unrealAsset, self.name)
