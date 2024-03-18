from unreal_materials.nodes.node_base import NodeBase, DefaultInputPorts
from unreal_materials.nodes.ports_base import PortsBase

class GetMaterialAttributes(NodeBase):
    class OutputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "MaterialAttributes", "BaseColor", "Specular", "Roughness", "Normal" ])

    class Details(NodeBase.DetailsBase):
        def __init__(self, attributeTypes: list):
            super().__init__()

            self.attributeTypes = attributeTypes

    def __init__(self, details: Details = Details()):
        super().__init__("GetMaterialAttributes", details = details, inputPorts = DefaultInputPorts(), outputPorts = GetMaterialAttributes.OutputPorts())
