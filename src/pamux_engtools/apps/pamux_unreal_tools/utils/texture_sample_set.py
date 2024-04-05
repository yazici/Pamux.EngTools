import unreal

from pamux_unreal_tools.generated.material_expression_wrappers import *

class TTextureSampleSet:
    def __init__(self, baseColor, roughness, opacity, normal):
        self.baseColor = baseColor
        self.roughness = roughness
        self.opacity = opacity
        self.normal = normal

class TextureSampleSet:
    def __init__(self, tss: TTextureSampleSet):
        self.baseColor = TextureSample()
        self.baseColor.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
        self.baseColor.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
        self.baseColor.texture.set(unreal.load_asset(tss.baseColor))

        self.roughness = TextureSample()
        self.roughness.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
        self.roughness.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
        self.roughness.texture.set(unreal.load_asset(tss.roughness))

        self.opacity = TextureSample()
        self.opacity.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
        self.opacity.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
        self.opacity.texture.set(unreal.load_asset(tss.opacity))

        self.normal = TextureSample()
        self.normal.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
        self.normal.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)
        self.normal.texture.set(unreal.load_asset(tss.normal))
