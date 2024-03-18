from unreal_materials.nodes.material_functions.commons.material_function_call import MaterialFunctionCallBase
from unreal_materials.nodes.utils.node_base import PortsBase, NodeBase

class BinaryFunctionCall(MaterialFunctionCallBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "A", "B" ])

    def __init__(self, name: str, inputPorts: PortsBase = InputPorts()):
        super().__init__(name, NodeBase.DetailsBase(), inputPorts)

class Divide(BinaryFunctionCall):
    def __init__(self):
        super().__init__("Divide")

class Multiply(BinaryFunctionCall):
    def __init__(self):
        super().__init__("Multiply")

class Subtract(BinaryFunctionCall):
    def __init__(self):
        super().__init__("Subtract")
