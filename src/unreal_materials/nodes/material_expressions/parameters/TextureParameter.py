from unreal_materials.nodes.utils.node_base import PortsBase, DefaultInputPorts, DefaultOutputPorts, GroupedParameterBase

class TextureParameter(GroupedParameterBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "UVs", "ApplyMipBias" ])

    class Details(GroupedParameterBase.DetailsBase):
        def __init__(self):
            super().__init__()

            self.mipValueMode = "None"
            self.samplerSource = "FromTextureAsset"
            self.samplerType = "Color"
            self.isDefaultMeshpaintTexture = False
            self.textureName = None
            #self.textureName = "T_DrySoil_A"
            
    def __init__(self, name: str, inputPorts = InputPorts(), outputPorts = DefaultOutputPorts()):
        super().__init__("MaterialExpressionTextureBase", name, TextureParameter.Details(), inputPorts, outputPorts)
