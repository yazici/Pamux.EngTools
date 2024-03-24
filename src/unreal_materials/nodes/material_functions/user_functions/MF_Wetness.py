from unreal_materials.nodes.utils.node_base import PortsBase
from unreal_materials.nodes.material_functions.commons.binary_function_call import BinaryFunctionCall

class MF_Wetness(BinaryFunctionCall):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "InMaterial", "Wetness" ])

    def __init__(self):
        super().__init__(type = "MF_Wetness", inputPorts = MF_Wetness.InputPorts())