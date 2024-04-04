
from pamux_unreal_tools.utils.interface_types import *

@material_function_interface("{asset_path_root}/Functions/MF_GlancingAngleSpecCorrection")
def IGlancingAngleSpecCorrection(
    materialAttributes: TMaterialAttributes,
    pixelDepth: TPixelDepth = TPixelDepth(),
    edgeSpecularFalloffPower: TFloatParam = 4.0,
    edgeSpecularCorrectionStartDistance: TFloatParam = 1000.0,
    edgeSpecularCorrectionFadeDistance: TFloatParam = 500.0,
    edgeSpecularCorrection: TFloatParam = 0.25,
    specLerp: TFloatParam = 0.5) -> TResult:
    pass
