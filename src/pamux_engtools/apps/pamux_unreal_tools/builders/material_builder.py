from pamux_unreal_tools.factories.material_factory import MaterialFactory
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase

class MaterialBuilder(ContainerBuilderBase):
    def __init__(self, container_path: str, dependencies_class, inputs_class, outputs_class):
        super().__init__(
            MaterialFunctionFactory(),
            MaterialFactory(),

            container_path,
            dependencies_class,
            inputs_class,
            outputs_class)