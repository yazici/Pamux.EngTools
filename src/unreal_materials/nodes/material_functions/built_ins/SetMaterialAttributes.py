from unreal_materials.nodes.utils.node_base import PortsBase
from unreal_materials.nodes.utils.node_base import NodeBase

class SetMaterialAttributes(NodeBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "MaterialAttributes", "BaseColor", "Specular", "Roughness", "Normal", "OpacityMask" ])

    class Details(NodeBase.DetailsBase):
        def __init__(self):
            super().__init__()

            self.attributeTypes = None

    def __init__(self):
        super().__init__(
            "SetMaterialAttributes",            
            SetMaterialAttributes.DetailsBase(),
            SetMaterialAttributes.InputPorts())


