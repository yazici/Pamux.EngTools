from unreal_materials.nodes.utils.node_base import PortsBase, NodeBase, DefaultInputPorts

class GetMaterialAttributes(NodeBase):
    class OutputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "MaterialAttributes", "BaseColor", "Specular", "Roughness", "Normal" ])

    class Details(NodeBase.DetailsBase):
        def __init__(self, attributeTypes: list):
            super().__init__()

            self.attributeTypes = attributeTypes

    def __init__(self):
        super().__init__(
            "GetMaterialAttributes",
            details = GetMaterialAttributes.Details(),
            inputPorts = DefaultInputPorts(),
            outputPorts = GetMaterialAttributes.OutputPorts())
