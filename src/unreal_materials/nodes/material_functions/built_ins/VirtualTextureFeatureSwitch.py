from unreal_materials.nodes.ports_base import PortsBase
from unreal_materials.nodes.node_base import NodeBase

class VirtualTextureFeatureSwitch(NodeBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "No", "Yes" ])

    def __init__(self):
        super().__init__("VirtualTextureFeatureSwitch", VirtualTextureFeatureSwitch.InputPorts())


