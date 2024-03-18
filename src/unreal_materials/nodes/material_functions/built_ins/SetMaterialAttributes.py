from unreal_materials.nodes.ports_base import PortsBase
from unreal_materials.nodes.node_base import NodeBase

class SetMaterialAttributes(NodeBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "MaterialAttributes", "BaseColor", "Specular", "Roughness", "Normal", "OpacityMask" ])


    class Details(NodeBase.DetailsBase):
        def __init__(self, attributeTypes: list):
            super().__init__()

            self.attributeTypes = attributeTypes

    def __init__(self):
        super().__init__("SetMaterialAttributes", SetMaterialAttributes.DetailsBase(), SetMaterialAttributes.InputPorts())


