from pamux_unreal_tools.utils.interface_types import *

@material_function_interface("{engineMaterialFunctionsRoot}02/Texturing/HeightLerp")
def IHeightLerp(a, b, transition_phase, height_texture, contrast) -> tuple[ TResults, TAlpha, TLerp_Alpha_No_Contrast ]:
    pass