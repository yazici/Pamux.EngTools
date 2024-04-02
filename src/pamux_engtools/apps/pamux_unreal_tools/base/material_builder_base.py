
from pamux_unreal_tools.material import MaterialFactory
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase

class MaterialBuilderBase(ContainerBuilderBase):
    def __init__(self, params_factory, container_path: str):
        super().__init__(MaterialFactory(), params_factory, container_path)