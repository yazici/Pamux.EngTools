from unreal_materials.nodes.ports_base import PortsBase
from unreal_materials.nodes.node_base import NodeBase
from unreal_materials.nodes.material_functions.commons.material_function_call import MaterialFunctionCallBase

class BinaryFunctionCall(MaterialFunctionCallBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "A", "B" ])

    def __init__(self, name: str, inputPorts: PortsBase = InputPorts()):
        super().__init__(name, NodeBase.DetailsBase(), inputPorts)

class Divide(BinaryFunctionCall):
    def __init__(self):
        super().__init__("Divide")

class Subtract(BinaryFunctionCall):
    def __init__(self):
        super().__init__("Subtract")
