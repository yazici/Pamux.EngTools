
from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase
from pamux_unreal_tools.base.material_function_outputs_base import MaterialFunctionOutputs

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

