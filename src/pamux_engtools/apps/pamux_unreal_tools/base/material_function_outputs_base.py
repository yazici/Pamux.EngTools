
from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase
from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos
class MaterialFunctionOutputsBase:
    def __init__(self, builder: ContainerBuilderBase) -> None:
        CurrentNodePos.goto_outputs()

class MaterialFunctionOutputs:
    class Result(MaterialFunctionOutputsBase):
        def __init__(self, builder: ContainerBuilderBase) -> None:
            super().__init__(builder)
            self.Result = builder.makeFunctionOutput("Result", 0)

    class ResultAndHeight(Result):
        def __init__(self, builder: ContainerBuilderBase) -> None:
            super().__init__(builder)
            CurrentNodePos.y += NodePos.DeltaY
            self.Height = builder.makeFunctionOutput("Height", 1)
