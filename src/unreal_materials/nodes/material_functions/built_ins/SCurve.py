from unreal_materials.nodes.utils.node_base import PortsBase, NodeBase

class SCurve(NodeBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "InputVector", "Power" ])

    def __init__(self):
        super().__init__("SCurve", SCurve.InputPorts())


