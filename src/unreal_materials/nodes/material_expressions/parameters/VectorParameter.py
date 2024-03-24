from unreal_materials.nodes.utils.node_base import GroupedParameterBase
from unreal_materials.nodes.utils.rgba import RGBA

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html
class VectorParameter(GroupedParameterBase):    
    class Details(GroupedParameterBase.DetailsBase):
        class VectorParameter:
            def __init__(self):
                self.defaultValue = RGBA(0.0, 0.0, 0.0, 0.0)

        class CustomPrimitiveData:
            def __init__(self):
                self.useCustomPrimitiveData = False
                self.primitiveDataIndex = 0
                
        def __init__(self):
            super().__init__()
            self.vectorParameter = VectorParameter.Details.VectorParameter()
            self.customPrimitiveData = VectorParameter.Details.CustomPrimitiveData()

    def __init__(self, name: str):
        super().__init__("MaterialExpressionVectorParameter", name, VectorParameter.Details())
