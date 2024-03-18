from unreal_materials.nodes.ports_base import PortsBase
from unreal_materials.nodes.node_base import NodeBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerBlend.html

class LandscapeLayerBlend(NodeBase):
    class InputPorts(PortsBase):
        @staticmethod
        def getPortNames(layers):
            result = []
            for layer in layers:
                result.append(f"Layer {layer.name_suffix}")
                result.append(f"Height {layer.name_suffix}")
            return result

        def __init__(self, layers):
            super().__init__(LandscapeLayerBlend.InputPorts.getPortNames(layers))

    def __init__(self, layers: list):
        super().__init__("MaterialExpressionLandscapeLayerBlend", "LandscapeLayerBlend", inputPorts = LandscapeLayerBlend.InputPorts(layers))


