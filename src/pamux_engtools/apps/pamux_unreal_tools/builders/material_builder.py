from pamux_unreal_tools.factories.material_factory import MaterialFactory
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase

class MaterialBuilder(MaterialExpressionContainerBuilderBase):
    def __init__(self, container_path: str, dependencies_class, inputs_class, outputs_class):
        super().__init__(
            MaterialFunctionFactory(),
            MaterialFactory(),
            container_path,
            dependencies_class,
            inputs_class,
            outputs_class)