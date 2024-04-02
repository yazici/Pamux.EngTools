import unreal
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.utils.node_pos import NodePos
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl

from pamux_unreal_tools.factories.material_expression_container_factory import MaterialExpressionContainerFactory

class MaterialFunctionFactory(MaterialExpressionContainerFactory):
    def __init__(self):
        super().__init__(unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew(), MaterialFunctionImpl)
