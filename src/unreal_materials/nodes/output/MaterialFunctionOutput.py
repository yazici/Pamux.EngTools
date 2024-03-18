from unreal_materials.nodes.utils.node_base import PortsBase, NodeBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html

class MaterialFunctionOutput(NodeBase):
    def __init__(self):
        super().__init__("MaterialExpressionFunctionOutput", "Output Result")
        self.sortPriority = 0

class MaterialFunctionHeightOutput(NodeBase):
    class OutputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "Height" ])

    def __init__(self):
        super().__init__("MaterialExpressionFunctionOutput", "Output Height")
        self.sortPriority = 1
