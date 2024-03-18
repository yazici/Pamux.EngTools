from unreal_materials.nodes.ports_base import PortsBase
from unreal_materials.nodes.node_base import NodeBase

class QualitySwitch(NodeBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "Default", "Low", "High", "Medium", "Epic" ])

    def __init__(self):
        super().__init__("QualitySwitch", QualitySwitch.InputPorts())


