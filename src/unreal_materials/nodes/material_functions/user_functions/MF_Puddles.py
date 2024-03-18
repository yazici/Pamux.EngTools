from unreal_materials.nodes.material_functions.commons.material_function_call import MaterialFunctionCallBase, PortsBase, NodeBase

class MF_Puddles(MaterialFunctionCallBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "MaterialAttributes" ])

    class OutputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "Result", "PuddleMask" ])

    def __init__(self):
        super().__init__("MF_Puddles", NodeBase.DetailsBase(), MF_Puddles.InputPorts(), MF_Puddles.OutputPorts())
