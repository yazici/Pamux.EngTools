from unreal_materials.nodes.ports_base import PortsBase
from unreal_materials.nodes.node_base import NodeBase, DefaultInputPorts, DefaultOutputPorts 

class MaterialFunctionCallBase(NodeBase):
    def __init__(self, name: str, inputPorts: PortsBase = DefaultInputPorts(), outputPorts: PortsBase = DefaultOutputPorts()):
        super().__init__("MaterialExpressionMaterialFunctionCall", name = name, inputPorts = inputPorts, outputPorts = outputPorts)
