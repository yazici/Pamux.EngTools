from unreal_materials.nodes.utils.node_base import PortsBase, DefaultInputPorts, DefaultOutputPorts, NodeBase

class MaterialFunctionCallBase(NodeBase):
    def __init__(
        self,
        name: str,
        inputPorts: PortsBase = DefaultInputPorts(),
        outputPorts: PortsBase = DefaultOutputPorts()):

        super().__init__("MaterialExpressionMaterialFunctionCall", name = name, inputPorts = inputPorts, outputPorts = outputPorts)
