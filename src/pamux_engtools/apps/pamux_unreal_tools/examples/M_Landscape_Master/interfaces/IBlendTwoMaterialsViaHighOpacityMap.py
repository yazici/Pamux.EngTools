from pamux_unreal_tools.utils.interface_types import *

@material_function_interface("{asset_path_root}/Functions/MF_BlendTwoMaterialsViaHighOpacityMap")
def IBlendTwoMaterialsViaHighOpacityMap(materialA: TMaterialAttributes, materialB: TMaterialAttributes, alpha: float) -> TResult:
    pass