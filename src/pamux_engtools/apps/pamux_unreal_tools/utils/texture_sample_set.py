import unreal

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.utils.asset_cache import AssetCache

class TMaterialTextures:
    def __init__(self, baseColor = None, roughness = None, opacity = None, normal = None, displacement = None):
        self.baseColor = baseColor
        self.roughness = roughness
        self.opacity = opacity
        self.normal = normal
        self.displacement = displacement

class TextureSampleSet:
    def __init__(self, tss: TMaterialTextures):
        self.baseColor = TextureSample()
        self.baseColor.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
        self.baseColor.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
        self.baseColor.texture.set(AssetCache.get(tss.baseColor))

        self.roughness = TextureSample()
        self.roughness.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
        self.roughness.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
        self.roughness.texture.set(AssetCache.get(tss.roughness))

        self.opacity = TextureSample()
        self.opacity.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
        self.opacity.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
        self.opacity.texture.set(AssetCache.get(tss.opacity))

        self.normal = TextureSample()
        self.normal.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
        self.normal.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)
        self.normal.texture.set(AssetCache.get(tss.normal))
