import unreal

from pamux_unreal_tools.base.material_expression.material_expression_base import MaterialExpressionBase

from pamux_unreal_tools.utils.node_pos import NodePos
from pamux_unreal_tools.impl.in_socket_impl import InSocketImpl
from pamux_unreal_tools.impl.out_socket_impl import OutSocketImpl
from pamux_unreal_tools.impl.material_expression_editor_property_impl import MaterialExpressionEditorPropertyImpl

MEL = unreal.MaterialEditingLibrary

class MaterialExpressionImpl(MaterialExpressionBase):
    def __init__(self, expression_class: unreal.Class, node_pos: NodePos = None) -> None:
        super().__init__(expression_class, node_pos)

        self.desc = MaterialExpressionEditorPropertyImpl(self, 'desc', 'str')

        self.material_expression_editor_x = MaterialExpressionEditorPropertyImpl(self, 'material_expression_editor_x', 'int32')
        self.material_expression_editor_y = MaterialExpressionEditorPropertyImpl(self, 'material_expression_editor_y', 'int32')

        self.input = InSocketImpl(self, '', 'StructProperty')

        self.output = OutSocketImpl(self, '', 'StructProperty')


    def gotoRightOf(self, sourceMaterialExpression: MaterialExpressionBase):
        self.material_expression_editor_x.set(sourceMaterialExpression.material_expression_editor_x.get() + NodePos.DeltaX)
