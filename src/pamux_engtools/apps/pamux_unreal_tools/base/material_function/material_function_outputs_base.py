
from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos

class MaterialFunctionOutputsBase:
    def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
        CurrentNodePos.goto_outputs()

class MaterialFunctionOutputs:
    class Result(MaterialFunctionOutputsBase):
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            super().__init__(builder)
            self.result = builder.makeFunctionOutput("Result", 0)

    class ResultAndHeight(Result):
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            super().__init__(builder)
            CurrentNodePos.y += NodePos.DeltaY
            self.height = builder.makeFunctionOutput("Height", 1)
