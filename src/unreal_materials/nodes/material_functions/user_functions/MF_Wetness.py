from src.unreal_materials.nodes.material_functions.commons.binary_function_call import BinaryFunctionCall, PortsBase, NodeBase

class MF_Wetness(BinaryFunctionCall):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "InMaterial", "Wetness" ])

    def __init__(self):
        super().__init__("MF_Wetness", NodeBase.DetailsBase(), MF_Wetness.InputPorts())
