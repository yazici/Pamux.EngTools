import unreal

from pamux_unreal_tools.base.material_expression_editor_property_base import MaterialExpressionEditorPropertyBase
from pamux_unreal_tools.base.material_expression_sockets_base import InSocket, OutSocket
from pamux_unreal_tools.base.material_expression_base_base import MaterialExpressionBaseBase

from pamux_unreal_tools.utils.build_stack import BuildStack
from pamux_unreal_tools.utils.node_pos import NodePos

class MaterialExpressionBase(MaterialExpressionBaseBase):
    def __init__(self, expression_class: unreal.Class, node_pos: NodePos = None) -> None:
        self.container = BuildStack.top()
        self.expression_class: unreal.Class = expression_class

        self.unrealAsset: unreal.MaterialExpression = self.container.createMaterialExpression(self.expression_class, node_pos)

        self.desc: MaterialExpressionEditorPropertyBase = None
        self.material_expression_editor_x: MaterialExpressionEditorPropertyBase = None
        self.material_expression_editor_y: MaterialExpressionEditorPropertyBase = None

        self.input: InSocket = None

        self.output: OutSocket = None

    def comesFrom(self, param1) -> bool:
        return self.input.comesFrom(param1)
    
    def connectTo(self, param1) -> bool:
        return self.output.connectTo(param1)
    
    @property
    def rt(self):
        return self.output.rt

    def add_rt(self):
        return self.output.add_rt()