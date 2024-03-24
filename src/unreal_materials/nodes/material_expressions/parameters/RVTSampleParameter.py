
from unreal_materials.nodes.utils.node_base import PortsBase, GroupedParameterBase

# https://docs.unrealengine.com/5.3/en-US/runtime-virtual-texturing-in-unreal-engine/
# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionRuntimeVirtualTextureSampleParameter.html

class RVTSampleParameter(GroupedParameterBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__(names = [ "UVs", "WorldPosition", "MipValue" ])

    class OutputPorts(PortsBase):
        def __init__(self, names: list = [ "BaseColor", "Specular", "Rougness", "Normal", "WorldHeight", "Mask" ]):
            super().__init__(names)

    class Details(GroupedParameterBase.DetailsBase):
        class VirtualTexture:
            def __init__(self):
                self.name = None
                self.content = None
                self.enablePackedPageTable = True
                self.enableAdaptivePageTable = True
                self.enableFeedback = True

        class TextureSample:
            def __init__(self):
                self.mipValueMode = "Default"
                self.addressMode = "Clamp"

        def __init__(self):
            super().__init__()
            self.virtualTexture = RVTSampleParameter.Details.VirtualTexture()
            self.textureSample = RVTSampleParameter.Details.TextureSample()
            
    def __init__(self, name: str):
        super().__init__("RuntimeVirtualTextureSampleParameter", name, self.Details(), self.InputPorts(), self.OutputPorts())
