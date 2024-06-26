import unreal

from pamux_unreal_tools.utils.interface_types import *
from pamux_unreal_tools.utils.types import *

# Idea: these interfaces declaration can be used both to construct "Inputs" class and call the function from other Materials/MaterialFunctions

@material_function_interface("{asset_path_root}/Functions/Layers/MF_LandscapeBaseMaterial")
def ILandscapeBaseMaterial(
        albedo: TTextureObject = TTextureObject(),
        colorOverlay: Vec3f = Vec3f(1.0, 1.0, 1.0),
        colorOverlayIntensity: float = 1.0,
        contrast: float = 0.0,
        contrastVariation: float = 1.0,
        roughness: TTextureObject = TTextureObject(),
        roughnessIntensity: float = 1.0,
        normal: TTextureObject = TTextureObject(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL),
        normalIntensity: float = 0.0,
        displacement: TTextureObject = TTextureObject(),
        uvParams: Vec4f = Vec4f(1.0, 1.0, 0.5, 0.5),
        rotation: float = 0.0,
        doTextureBomb: bool = True,
        doRotationVariation: bool = False,
        bombCellScale: float = 1.0,
        bombPatternScale: float = 1.0,
        bombRandomOffset: float = 0.0,
        bombRotationVariation: float = 0.0,
        opacityStrength: float = 1.0,
        opacityAdd: float = 0.0,
        opacityContrast: float = 1.0) -> tuple[TResult, THeight]:
    pass