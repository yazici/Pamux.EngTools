from unreal_materials.nodes.utils.node_base import GroupedParameterBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html
class ScalarParameter(GroupedParameterBase):    
    class Details(GroupedParameterBase.DetailsBase):
        class ScalarParameter:
            def __init__(self):
                self.defaultValue = 0.0
                self.sliderMin = 0.0
                self.sliderMax = 0.0

        class CustomPrimitiveData:
            def __init__(self):
                self.useCustomPrimitiveData = False
                self.primitiveDataIndex = 0
                
        def __init__(self):
            super().__init__()
            self.scalarParameter = ScalarParameter.Details.ScalarParameter()
            self.customPrimitiveData = ScalarParameter.Details.CustomPrimitiveData()

    def __init__(self, name: str):
        super().__init__("MaterialExpressionScalarParameter", name, ScalarParameter.Details())
