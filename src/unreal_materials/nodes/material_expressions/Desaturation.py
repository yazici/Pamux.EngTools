from unreal_materials.nodes.utils.node_base import MaterialExpressionBase, PortsBase
from unreal_materials.nodes.utils.rgba import RGBA

class Desaturation(MaterialExpressionBase):    
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__(names = [ "Input", "Fraction" ])

    class Details(MaterialExpressionBase.DetailsBase):
        def __init__(self):
            self.luminanceFactors = RGBA(0.3, 0.59, 0.11, 0.0)

    def __init__(self):
        super().__init__("MaterialExpressionDesaturation", "Desaturation". self.Details(), self.InputPorts())
 