from unreal_materials.nodes.node_base import ParameterBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html
class MaterialExpressionLandscapeLayerWeightParameter(ParameterBase):    
    class Details:
        def __init__(self, previewWeight: float = 0.0):
            self.previewWeight = previewWeight
            
    def __init__(self, name: str, desc: str = None, details: Details = Details()):
        super().__init__("MaterialExpressionLandscapeLayerWeight", name, desc, details)
