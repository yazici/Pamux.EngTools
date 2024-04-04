from pamux_unreal_tools.utils.interface_types import *

@material_function_interface("{engineMaterialFunctionsRoot}02/Texturing/CustomRotator")
def ICustomRotator(uVs, rotation_center, rotation_angle) -> TRotated_Values:
    pass