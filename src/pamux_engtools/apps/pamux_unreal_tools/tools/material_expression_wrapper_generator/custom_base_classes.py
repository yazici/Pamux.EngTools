import unreal

from pamux_unreal_tools.utils.node_pos import NodePos
from pamux_unreal_tools.impl.material_expression_impl import MaterialExpressionImpl

from pamux_unreal_tools.impl.out_socket_impl import OutSocketImpl

class NamedRerouteDeclarationBase(MaterialExpressionImpl):
    def __init__(self, expression_class: unreal.Class, node_pos: NodePos = None) -> None:
        super().__init__(expression_class, node_pos)
