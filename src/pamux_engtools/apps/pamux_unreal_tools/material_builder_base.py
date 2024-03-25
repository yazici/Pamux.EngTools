
from pamux_unreal_tools.material import Material
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.material_function import MaterialFunction
from pamux_unreal_tools.container_builder_base import ContainerBuilderBase

from pamux_unreal_tools.examples.M_Landscape_Master.globals import *

class MaterialBuilderBase(ContainerBuilderBase):
    def __init__(self, paramsClass, container_name: str, package_name: str):
        super().__init__(container_name, package_name)
        self.paramsClass = paramsClass

    def loadOrCreate(self):
        result = Material.loadOrCreate(self.material_name, self.package_name, True)
        self.params = self.paramsClass(result)
        return result
