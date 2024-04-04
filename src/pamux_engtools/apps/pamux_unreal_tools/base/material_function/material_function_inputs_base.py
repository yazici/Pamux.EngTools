
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.utils.node_pos import CurrentNodePos

class MaterialFunctionInputsBase:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            CurrentNodePos.goto_inputs()
