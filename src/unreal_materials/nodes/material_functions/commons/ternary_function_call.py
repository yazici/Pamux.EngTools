from unreal_materials.nodes.material_functions.commons.material_function_call import MaterialFunctionCallBase
from unreal_materials.nodes.utils.node_base import PortsBase, DefaultOutputPorts, NodeBase

class TernaryFunctionCall(MaterialFunctionCallBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "A", "B", "C" ])

    def __init__(self, name: str, inputPorts: PortsBase = InputPorts()):
        super().__init__(name, NodeBase.DetailsBase(), inputPorts, DefaultOutputPorts())


class Lerp(TernaryFunctionCall):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "A", "B", "Alpha"  ])

    def __init__(self):
        super().__init__("Lerp", Lerp.InputPorts())
