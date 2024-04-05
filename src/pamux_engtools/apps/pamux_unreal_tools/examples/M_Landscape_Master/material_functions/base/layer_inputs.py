import unreal

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase

class LayerInputs:
    def __init__(self, builder: MaterialExpressionContainerBuilderBase):
        self.albedo = TextureObjectParameter(f"{builder.layer_name}Albedo")
        self.colorOverlay = VectorParameter(f"{builder.layer_name}ColorOverlay", unreal.LinearColor(0.5, 0.5, 0.5, 1.0))
        self.colorOverlayIntensity = ScalarParameter(f"{builder.layer_name}ColorOverlayIntensity", 0.0)

        self.contrast = ScalarParameter(f"{builder.layer_name}Contrast", 1.0)
        self.contrastVariation = ScalarParameter(f"{builder.layer_name}ContrastVariation", 0.0)

        self.roughness = TextureObjectParameter(f"{builder.layer_name}Roughness")
        self.roughnessIntensity = ScalarParameter(f"{builder.layer_name}RoughnessVariation", 1.0)

        self.normalIntensity = ScalarParameter(f"{builder.layer_name}NormalVariation", 0.0)
        self.normal = TextureObjectParameter(f"{builder.layer_name}Normal", None)
        self.normal.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)

        self.displacement = TextureObjectParameter(f"{builder.layer_name}Displacement")

        self.uvParams =  VectorParameter(f"{builder.layer_name}UVParams", unreal.LinearColor(1.0, 1.0, 0.5, 0.5))

        self.rotation = ScalarParameter(f"{builder.layer_name}Rotation", 0.0)

        self.doTextureBomb = StaticBoolParameter(f"{builder.layer_name}DoTextureBomb", True)
        self.doRotationVariation = StaticBoolParameter(f"{builder.layer_name}DoRotationVariation", True)

        self.bombCellScale = ScalarParameter(f"{builder.layer_name}BombCellScale", 0.0)
        self.bombPatternScale = ScalarParameter(f"{builder.layer_name}BombPatternScale", 0.0)
        self.bombRandomOffset = ScalarParameter(f"{builder.layer_name}BombRandomOffset", 0.0)
        self.bombRotationVariation = ScalarParameter(f"{builder.layer_name}BombRotationVariation", 0.0)

        self.opacityStrength = ScalarParameter(f"{builder.layer_name}OpacityStrength", 1.0)
        self.opacityAdd = ScalarParameter(f"{builder.layer_name}OpacityAdd", 0.0)
        self.opacityContrast = ScalarParameter(f"{builder.layer_name}OpacityContrast", 1.0)