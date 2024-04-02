
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase
from pamux_unreal_tools.utils.node_pos import CurrentNodePos


class MaterialFunctionInputsBase:
        def __init__(self, builder: ContainerBuilderBase) -> None:
            CurrentNodePos.goto_inputs()
