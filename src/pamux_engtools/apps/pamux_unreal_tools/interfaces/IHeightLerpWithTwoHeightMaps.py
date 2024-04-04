from pamux_unreal_tools.utils.types import *

class TAlpha:
    pass

@material_function_interface("{engineMaterialFunctionsRoot}02/Texturing/HeightLerpWithTwoHeightMaps")
def IHeightLerpWithTwoHeightMaps(transition_phase, height_texture_1, height_texture_2) -> tuple[ TAlpha ]:
    pass