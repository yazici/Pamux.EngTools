import unreal
from typing import Any

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.utils.asset_cache import AssetCache

class LayerInputs:
    @staticmethod
    def get(layer_name = ""):
        return [
            f"{layer_name}Albedo",
            f"{layer_name}ColorOverlay",
            f"{layer_name}ColorOverlayIntensity",
            f"{layer_name}Contrast",
            f"{layer_name}ContrastVariation",
            f"{layer_name}Roughness",
            f"{layer_name}RoughnessIntensity",
            f"{layer_name}NormalIntensity",
            f"{layer_name}Normal",
            f"{layer_name}Displacement",
            f"{layer_name}UVParams",
            f"{layer_name}Rotation",
            f"{layer_name}DoTextureBomb",
            f"{layer_name}DoRotationVariation",
            f"{layer_name}BombCellScale",
            f"{layer_name}BombPatternScale",
            f"{layer_name}BombRandomOffset",
            f"{layer_name}BombRotationVariation",
            f"{layer_name}OpacityStrength",
            f"{layer_name}OpacityAdd",
            f"{layer_name}OpacityContrast"
        ]

    def __init__(self, builder: MaterialExpressionContainerBuilderBase, roughnessTextureTypeSuffix = "R"):
        self.albedo = TextureObjectParameter(f"{builder.layer_name}Albedo")
        self.albedo.texture.set(AssetCache.get_layer_texture(builder.layer_name, "A"))
        self.colorOverlay = VectorParameter(f"{builder.layer_name}ColorOverlay", unreal.LinearColor(0.5, 0.5, 0.5, 1.0))
        self.colorOverlayIntensity = ScalarParameter(f"{builder.layer_name}ColorOverlayIntensity", 0.0)

        self.contrast = ScalarParameter(f"{builder.layer_name}Contrast", 1.0)
        self.contrastVariation = ScalarParameter(f"{builder.layer_name}ContrastVariation", 0.0)

        self.roughness = TextureObjectParameter(f"{builder.layer_name}Roughness")
        self.roughness.texture.set(AssetCache.get_layer_texture(builder.layer_name, roughnessTextureTypeSuffix))

        self.roughnessIntensity = ScalarParameter(f"{builder.layer_name}RoughnessVariation", 1.0)

        self.normalIntensity = ScalarParameter(f"{builder.layer_name}NormalIntensity", 0.0)
        self.normal = TextureObjectParameter(f"{builder.layer_name}Normal", None)
        self.normal.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)
        self.normal.texture.set(AssetCache.get_layer_texture(builder.layer_name, "N"))

        self.displacement = TextureObjectParameter(f"{builder.layer_name}Displacement")
        self.displacement.texture.set(AssetCache.get_layer_texture(builder.layer_name, "D"))

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
