from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.utils.interface_types import *
from pamux_unreal_tools.base.texture_sample_set import TextureSampleSet

@material_function_interface("{asset_path_root}/Functions/MF_Puddles")
def IPuddles(
    materialAttributes: TextureSampleSet,
    puddle_color: TVectorParam = TVectorParam(0.057292, 0.051375, 0.034017, 1.0),
    puddle_height: TFloatParam = 1.0,
    puddle_slope: TFloatParam = 0.25,
    puddle_depth: TFloatParam = 0.25,
    puddle_roughness: TFloatParam = 0.15) -> TResult:
    pass