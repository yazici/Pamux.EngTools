from unreal_materials.nodes.utils.node_base import PortsBase, NodeBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html
class MasterMaterialOutput(NodeBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "MaterialAttributes" ])

    class Details(NodeBase.DetailsBase):
        class PhysicalMaterial:
            class Mask:
                def __init__(self):
                    pass

            class Map:
                def __init__(self):
                    pass

            def __init__(self):
                pass

        class Material:
            def __init__(self):
                pass

        class Nanite:
            def __init__(self):
                pass

        class Translucency:
            class SelfShadowing:
                def __init__(self):
                    pass
            def __init__(self):
                pass

        class Usage:
            def __init__(self):
                pass

        class Mobile:
            def __init__(self):
                pass

        class ForwardShading:
            def __init__(self):
                pass

        class PostProcessMaterial:
            def __init__(self):
                pass

        class Refraction:
            def __init__(self):
                pass

        class WorldPositionOffset:
            def __init__(self):
                pass

        class Lightmass:
            class Settings:
                def __init__(self):
                    pass

            def __init__(self):
                pass

        class Previewing:
            def __init__(self):
                pass

        class ImportSettings:
            def __init__(self):
                pass

        def __init__(self, name: str, desc: str = None):
            super().__init__(name, desc)

            self.physicalMaterial = self.PhysicalMaterial()
            self.material = self.Material()
            self.nanite = self.Nanite()
            self.translucency = self.Translucency()                
            self.usage = self.Usage()
            self.mobile = self.Mobile()
            self.forwardShading = self.ForwardShading()
            self.postProcessMaterial = self.PostProcessMaterial()
            self.refraction = self.Refraction()
            self.worldPositionOffset = self.WorldPositionOffset()
            self.lightmass = self.Lightmass()
            self.previewing = self.Previewing()
            self.importSettings = self.ImportSettings()

    def __init__(self, type):
        super().__init__(type = type, details = MasterMaterialOutput.Details(), inputPorts = MasterMaterialOutput.InputPorts())
