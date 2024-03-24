from unreal_materials.nodes.utils.node_base import PortsBase, NodeBase

class VirtualTextureFeatureSwitch(NodeBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "No", "Yes" ])

    def __init__(self):
        super().__init__("VirtualTextureFeatureSwitch", VirtualTextureFeatureSwitch.InputPorts())


