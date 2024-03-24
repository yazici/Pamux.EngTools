from unreal_materials.nodes.utils.node_base import PortsBase
from unreal_materials.nodes.material_functions.commons.ternary_function_call import TernaryFunctionCall

class MF_BlendTwoMaterialsViaHeightOpacityMap(TernaryFunctionCall):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "MaterialA", "MaterialB", "Alpha"  ])

    def __init__(self):
        super().__init__("MF_BlendTwoMaterialsViaHeightOpacityMap", MF_BlendTwoMaterialsViaHeightOpacityMap.InputPorts())
