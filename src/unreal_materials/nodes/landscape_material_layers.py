from unreal_materials.nodes.ports_base import PortsBase
from unreal_materials.nodes.node_base import NodeBase, DefaultInputPorts

class MLF_LandscapeLayer(NodeBase):
    class OutputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "Result", "Height" ])

    def __init__(self, name_suffix: str):
        super().__init__(f"MLF_{name_suffix}", f"MLF_{name_suffix}", None, NodeBase.DetailsBase(), DefaultInputPorts(), MLF_LandscapeLayer.OutputPorts())
        self.name_suffix = name_suffix


class LandscapeMaterialLayers:
    ALL = [
        MLF_LandscapeLayer("Dirt"),
        MLF_LandscapeLayer("Grass"),
        MLF_LandscapeLayer("Mud"),
        MLF_LandscapeLayer("StonyGround"),
        MLF_LandscapeLayer("Fields"),
        MLF_LandscapeLayer("PlowedGround"),
        MLF_LandscapeLayer("ForestGrounds"),
        MLF_LandscapeLayer("HeavyMud")
    ]
