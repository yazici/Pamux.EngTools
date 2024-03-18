from unreal_materials.nodes.utils.node_base import PortsBase, NodeBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html
class RVTOutput(NodeBase):
    class InputPorts(PortsBase):
        def __init__(self, names: list = [ "BaseColor", "Specular", "Rougness", "Normal", "WorldHeight", "Opacity", "Mask" ]):
            super().__init__(names)

    def __init__(self):
        super().__init__("RuntimeVirtualTextureOutput", RVTOutput.InputPorts())
