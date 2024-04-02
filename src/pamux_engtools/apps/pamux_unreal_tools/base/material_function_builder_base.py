
from pamux_unreal_tools.material_function import MaterialFunction, MaterialFunctionFactory
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase

class MaterialFunctionOutputs:
    class Result:
        def __init__(self, builder: ContainerBuilderBase) -> None:
            CurrentNodePos.goto_outputs()
            self.Result = builder.makeFunctionOutput("Result", 0)

    class ResultAndHeight(Result):
        def __init__(self, builder: ContainerBuilderBase) -> None:
            super().__init__(builder)
            CurrentNodePos.y += NodePos.DeltaY
            self.Height = builder.makeFunctionOutput("Height", 1)

class MaterialFunctionBuilderBase(ContainerBuilderBase):
    def __init__(self, container_path: str, inputs_class, outputs_class = MaterialFunctionOutputs.Result) -> None:
        super().__init__(MaterialFunctionFactory(), None, container_path, inputs_class, outputs_class)

    def makeFunctionOutput(self, name, sort_priority) -> FunctionOutput:
        result = FunctionOutput()
        result.output_name.set(name)
        result.sort_priority.set(sort_priority)
        return result


class MaterialLayerFunctionBuilderBase(MaterialFunctionBuilderBase):
    def __init__(self, container_path: str, inputs_class, outputs_class = MaterialFunctionOutputs.ResultAndHeight) -> None:
        super().__init__(container_path, inputs_class, outputs_class)

