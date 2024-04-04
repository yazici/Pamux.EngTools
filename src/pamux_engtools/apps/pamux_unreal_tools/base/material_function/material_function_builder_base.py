from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.base.material_function.material_function_factory_base import MaterialFunctionFactoryBase

class MaterialFunctionBuilderBase(MaterialExpressionContainerBuilderBase):
    def __init__(self, 
                 materialFunctionFactory: MaterialFunctionFactoryBase,
                 container_path: str,
                 dependencies_class,
                 inputs_class,
                 outputs_class = MaterialFunctionOutputs.Result) -> None:
        super().__init__(
            materialFunctionFactory,
            materialFunctionFactory,
            container_path,
            dependencies_class,
            inputs_class,
            outputs_class)

