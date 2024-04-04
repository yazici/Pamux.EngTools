from pamux_unreal_tools.utils.types import *

class TXYZAxes:
    pass

@material_function_interface("{engineMaterialFunctionsRoot}02/WorldPositionOffset/RotateAboutWorldAxis_cheap")
def IRotateAboutWorldAxis_cheap(rotation_amount, pivotPoint, worldPosition) -> TXYZAxes:
    pass
