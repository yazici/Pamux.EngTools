from unreal_materials.nodes.ports_base import PortsBase
from unreal_materials.nodes.node_base import NodeBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html
class LandscapeGrassOutput(NodeBase):
    class InputPorts(PortsBase):
        def __init__(self, names: list = [ "Dirt", "Grass", "HeavyMud", "StonyGround", "Fields", "PlowedSoil" ]):
            super().__init__(names)

    def __init__(self):
        super().__init__("LandscapeGrassOutput", LandscapeGrassOutput.InputPorts())

    def setFoliageMasks(self, foliageMask, layerFoliaceMasks):
        pass