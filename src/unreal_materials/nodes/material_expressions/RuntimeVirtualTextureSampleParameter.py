from unreal_materials.nodes.ports_base import PortsBase

from unreal_materials.nodes.material_expressions.MaterialExpressionParameterBase import MaterialExpressionParameterBase

# https://docs.unrealengine.com/5.3/en-US/runtime-virtual-texturing-in-unreal-engine/
# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionRuntimeVirtualTextureSampleParameter.html

class RuntimeVirtualTextureSampleParameter(MaterialExpressionParameterBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__(names = [ "UVs", "WorldPosition", "MipValue" ])

    class OutputPorts(PortsBase):
        def __init__(self, names: list = [ "BaseColor", "Specular", "Rougness", "Normal", "WorldHeight", "Mask" ]):
            super().__init__(names)

    class Details(MaterialExpressionParameterBase.DetailsBase):
        class VirtualTexture:
            def __init__(self, name: str, content = str):
                self.name = name
                self.content = content
                self.enablePackedPageTable = True
                self.enableAdaptivePageTable = True
                self.enableFeedback = True

        class TextureSample:
            def __init__(self, mipValueMode: str = "Default", addressMode: str = "Clamp"):
                self.mipValueMode = mipValueMode
                self.addressMode = addressMode

        def __init__(
                self,
                materialExpression: MaterialExpressionParameterBase.DetailsBase.MaterialExpression,
                virtualTexture: VirtualTexture,
                textureSample: TextureSample):

            self.materialExpression = materialExpression
            self.virtualTexture = virtualTexture
            self.textureSample = textureSample
            
    def __init__(self, name: str, details: Details):
        super().__init__("RuntimeVirtualTextureSampleParameter", name, details, self.InputPorts(), self.OutputPorts())
