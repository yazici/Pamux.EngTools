import unreal
from pamux_unreal_tools.utils.interface_types import *
from pamux_unreal_tools.utils.types import *

@material_function_interface("{asset_path_root}/Functions/MF_TextureCellBombing_Landscape")
def ITextureCellBombing_Landscape(
      texture: TTextureObject = TTextureObject(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR),
      UVs: TTextureCoordinate = TTextureCoordinate(1.0, 1.0),
      cellScale: float = 2.0,
      patternScale: float = 10.0,
      doRotationVariation: bool = False,
      randomOffsetVariation: float = 1.0,
      randomRotationVariation: float = 1.0,
      isNormalMap: bool = False
) -> TResult:
    pass
