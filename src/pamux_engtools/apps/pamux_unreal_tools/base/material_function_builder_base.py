
from pamux_unreal_tools.material_function import MaterialFunction, MaterialFunctionFactory
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase

LandscapeMaterialFunctionPackage = "/Game/Materials/Pamux/Landscape/Functions"

class MaterialFunctionBuilderBase(ContainerBuilderBase):
    def __init__(self, container_name: str, package_name: str = LandscapeMaterialFunctionPackage):
        super().__init__(MaterialFunctionFactory(), None, container_name, package_name)

    def makeFunctionOutput(self, name, sort_priority):
        CurrentNodePos.goto_outputs()
        result = FunctionOutput()
        result.output_name.set(name)
        result.sort_priority.set(sort_priority)
        return result

    def makeFunctionOutput_Result(self):
        return self.makeFunctionOutput("Result", 0)
    
    def makeFunctionOutput_Height(self):
        return self.makeFunctionOutput("Height", 1)

LandscapeMaterialLayerFunctionPackage = f"{LandscapeMaterialFunctionPackage}/Layers"

class MaterialLayerFunctionBuilderBase(MaterialFunctionBuilderBase):
    def __init__(self, container_name: str, package_name: str = LandscapeMaterialLayerFunctionPackage):
        super().__init__(container_name, package_name)

    def makeLayerFunctionOutputs(self):
        return self.makeFunctionOutput_Result(), self.makeFunctionOutput_Height()
