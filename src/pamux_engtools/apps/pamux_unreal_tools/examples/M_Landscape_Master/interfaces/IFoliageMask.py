from pamux_unreal_tools.utils.interface_types import *

@material_function_interface("{asset_path_root}/Functions/MF_FoliageMask")
def IFoliageMask(layerSample: float, foliageMask: float, threshold: float, enabled: bool = True) -> TResult:
    pass
