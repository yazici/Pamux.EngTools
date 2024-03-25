
from pamux_unreal_tools.material import Material
from pamux_engtools.apps.pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.examples.M_Landscape_Master.globals import *

LandscapeMaterialFunctionPackage = "/Game/Materials/Pamux/Landscape/Functions"

class ContainerBuilderBase:
    def __init__(self, container_name: str, package_name: str = LandscapeMaterialFunctionPackage):
        self.container_name = container_name
        self.package_name = package_name

    def build(self):
        raise "Implement and build container blueprint here"

    def loadOrCreate(self):
        raise "Implement and loadOrCreate container blueprint here"

    def get(self):
        result = self.loadOrCreate()

        Globals.BuildStack.push(result)
        self.build()
        result.save()
        Globals.BuildStack.pop()
        return result

    @property
    def current_container(self):
        return Globals.BuildStack.top()

    def callMaterialFunction(self, materialFunctionToCall: MaterialFunction):
        result = MaterialFunctionCall(self.current_container)
        result.material_function.set(materialFunctionToCall.asset)
        return result

    class TextureSampleSet:
        def __init__(self, container, baseColor, roughness, opacity, normal):
            self.baseColor = TextureSample(container)
            self.baseColor.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.baseColor.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
            self.baseColor.texture.set(unreal.load_asset(baseColor))

            self.roughness = TextureSample(container)
            self.roughness.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.roughness.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
            self.roughness.texture.set(unreal.load_asset(roughness))

            self.opacity = TextureSample(container)
            self.opacity.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.opacity.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
            self.opacity.texture.set(unreal.load_asset(opacity))

            self.normal = TextureSample(container)
            self.normal.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.normal.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)
            self.normal.texture.set(unreal.load_asset(normal))

        
