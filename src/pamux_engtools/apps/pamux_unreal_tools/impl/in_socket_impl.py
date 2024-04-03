
import unreal
MEL = unreal.MaterialEditingLibrary

from pamux_unreal_tools.base.material_expression_sockets_base import InSocket, OutSocket
from pamux_unreal_tools.base.material_expression_base_base import MaterialExpressionBaseBase

class InSocketImpl(InSocket):
    def __init__(self, material_expression: MaterialExpressionBaseBase, name: str, type: str) -> None:
        super().__init__(material_expression, name, type)

    def comesFrom(self, param) -> bool:
        if isinstance(param, OutSocket):
            return self.__comesFrom_OutSocket(param)
        
        if isinstance(param, MaterialExpressionBaseBase):
            return self.__comesFrom_MaterialExpressionBase(param)

        raise Exception("Don't know how to call comesFrom for type: " + str(param))

    def __comesFrom_OutSocket(self, sourceOutSocket: OutSocket) -> bool:
        if hasattr(sourceOutSocket, "rt"):
            return self.comesFrom(sourceOutSocket.rt)
        else:
            return self.__comesFrom_impl(sourceOutSocket.material_expression, sourceOutSocket.name)

    def __comesFrom_MaterialExpressionBase(self, sourceMaterialExpression: MaterialExpressionBaseBase) -> bool:
        return self.__comesFrom_impl(sourceMaterialExpression, "")

    def __comesFrom_impl(self, sourceMaterialExpression: MaterialExpressionBaseBase, sourceOutSocketName: str) -> bool:
        self.material_expression.gotoRightOf(sourceMaterialExpression)
        return MEL.connect_material_expressions(sourceMaterialExpression.unrealAsset, sourceOutSocketName, self.material_expression.unrealAsset, self.name)
