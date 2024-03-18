from unreal_materials.nodes.material_functions.commons.material_function_call import PortsBase, MaterialFunctionCallBase, NodeBase, DefaultOutputPorts

class TernaryFunctionCall(MaterialFunctionCallBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "A", "B", "C" ])

    def __init__(self, name: str, inputPorts: PortsBase = InputPorts()):
        super().__init__(name, NodeBase.DetailsBase(), inputPorts, DefaultOutputPorts())


