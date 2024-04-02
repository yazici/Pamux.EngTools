import unreal
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.utils.node_pos import NodePos
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.impl.material_impl import MaterialImpl
from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos
class MaterialFactory(MaterialExpressionContainerFactory):
    def __init__(self):
        super().__init__(unreal.Material, unreal.MaterialFactoryNew(), MaterialImpl)

