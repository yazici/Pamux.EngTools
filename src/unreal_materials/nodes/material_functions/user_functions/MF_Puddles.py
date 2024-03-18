from unreal_materials.nodes.utils.node_base import PortsBase
from unreal_materials.nodes.material_functions.commons.material_function_call import MaterialFunctionCallBase

class MF_Puddles(MaterialFunctionCallBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "MaterialAttributes" ])

    class OutputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "Result", "PuddleMask" ])

    def __init__(self):
        super().__init__(type = "MF_Puddles", inputPorts = MF_Puddles.InputPorts(), outputPorts = MF_Puddles.OutputPorts())
