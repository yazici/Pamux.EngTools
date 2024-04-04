from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase
from pamux_unreal_tools.base.material_function_outputs_base import MaterialFunctionOutputs

class MaterialFunctionBuilderBase(ContainerBuilderBase):
    def __init__(self, interface, container_path: str, dependencies_class, inputs_class, outputs_class = MaterialFunctionOutputs.Result) -> None:
        super().__init__(interface, MaterialFunctionFactory(), None, container_path, dependencies_class, inputs_class, outputs_class)

class MaterialLayerFunctionBuilderBase(MaterialFunctionBuilderBase):
    def __init__(self, interface, container_path: str, dependencies_class, inputs_class, outputs_class = MaterialFunctionOutputs.ResultAndHeight) -> None:
        super().__init__(interface, container_path, dependencies_class, inputs_class, outputs_class)

