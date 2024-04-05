import unreal
from typing import Any

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase

class LayerInputs:
    def __init__(self, builder: MaterialExpressionContainerBuilderBase, roughnessTextureTypeSuffix = "R"):
        self.albedo = TextureObjectParameter(f"{builder.layer_name}Albedo")
        self.albedo.texture.set(self.__load_texture(builder.layer_name, "A"))
        self.colorOverlay = VectorParameter(f"{builder.layer_name}ColorOverlay", unreal.LinearColor(0.5, 0.5, 0.5, 1.0))
        self.colorOverlayIntensity = ScalarParameter(f"{builder.layer_name}ColorOverlayIntensity", 0.0)

        self.contrast = ScalarParameter(f"{builder.layer_name}Contrast", 1.0)
        self.contrastVariation = ScalarParameter(f"{builder.layer_name}ContrastVariation", 0.0)

        self.roughness = TextureObjectParameter(f"{builder.layer_name}Roughness")
        self.roughness.texture.set(self.__load_texture(builder.layer_name, roughnessTextureTypeSuffix))

        self.roughnessIntensity = ScalarParameter(f"{builder.layer_name}RoughnessVariation", 1.0)

        self.normalIntensity = ScalarParameter(f"{builder.layer_name}NormalVariation", 0.0)
        self.normal = TextureObjectParameter(f"{builder.layer_name}Normal", None)
        self.normal.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)
        self.normal.texture.set(self.__load_texture(builder.layer_name, "N"))

        self.displacement = TextureObjectParameter(f"{builder.layer_name}Displacement")
        self.displacement.texture.set(self.__load_texture(builder.layer_name, "D"))

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

    def __load_texture(self, layer_name: str, texture_type: str) -> Any:
        return unreal.load_asset(f"/Script/Engine.Texture2D'/Game/Megascans/Surfaces/{layer_name}/T_{layer_name}_{texture_type}.T_{layer_name}_{texture_type}'")