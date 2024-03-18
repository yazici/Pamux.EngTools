from unreal_materials.nodes.material_functions.commons.material_function_call import PortsBase, MaterialFunctionCallBase

class UnaryFunctionCall(MaterialFunctionCallBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "Value" ])

    def __init__(self, name: str, inputPorts: PortsBase = InputPorts()):
        super().__init__(name = name, inputPorts = inputPorts)


class Saturate(UnaryFunctionCall):
    def __init__(self):
        super().__init__("Saturate")
