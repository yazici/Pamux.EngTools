from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.base.material_function.material_function_builder_base import MaterialFunctionBuilderBase

class MaterialFunctionBuilder(MaterialFunctionBuilderBase):
    materialFunctionFactory = MaterialFunctionFactory()

    def __init__(self, container_path: str, dependencies_class, inputs_class, outputs_class = MaterialFunctionOutputs.Result) -> None:
        super().__init__(
            MaterialFunctionBuilder.materialFunctionFactory,
            container_path,
            dependencies_class,
            inputs_class,
            outputs_class)

class MaterialLayerFunctionBuilder(MaterialFunctionBuilder):
    def __init__(self, container_path: str, dependencies_class, inputs_class, outputs_class = MaterialFunctionOutputs.ResultAndHeight) -> None:
        super().__init__(container_path, dependencies_class, inputs_class, outputs_class)

