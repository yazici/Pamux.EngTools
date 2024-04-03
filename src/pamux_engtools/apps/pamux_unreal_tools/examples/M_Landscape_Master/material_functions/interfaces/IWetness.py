
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.utils.types import *
from pamux_unreal_tools.base.texture_sample_set import TextureSampleSet

@material_function_interface("{asset_path_root}/Functions/MF_Wetness")
def IWetness(
    materialAttributes: TextureSampleSet,
    wetness_saturation: TFloatParam = -0.5,
    wetness_darken: TFloatParam = 0.5,
    wetness_roughness: TFloatParam = 0.3,
    wtness: float = 1.0) -> TResult:
    pass
