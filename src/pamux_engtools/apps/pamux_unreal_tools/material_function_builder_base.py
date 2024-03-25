
from pamux_unreal_tools.material_function import MaterialFunction
from pamux_engtools.apps.pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.container_builder_base import ContainerBuilderBase
from pamux_unreal_tools.examples.M_Landscape_Master.globals import *

LandscapeMaterialFunctionPackage = "/Game/Materials/Pamux/Landscape/Functions"

class MaterialFunctionBuilderBase(ContainerBuilderBase):
    def __init__(self, container_name: str, package_name: str = LandscapeMaterialFunctionPackage):
        super().__init__(container_name, package_name)

    def loadOrCreate(self):
        return MaterialFunction.loadOrCreate(self.container_name, self.package_name, True)

    def makeFunctionOutput(self, name, sort_priority):
        result = FunctionOutput(self.current_container)
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