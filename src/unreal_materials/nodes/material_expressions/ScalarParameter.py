from unreal_materials.nodes.node_base import NodeBase
from unreal_materials.nodes.material_expressions.MaterialExpressionParameterBase import MaterialExpressionParameterBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html
class MaterialExpressionScalarParameter(MaterialExpressionParameterBase):    
    class Details(NodeBase.DetailsBase):
        class ScalarParameter:
            def __init__(self, defaultValue: float = 0.0, sliderMin: float = 0.0, sliderMax: float = 0.0):
                self.defaultValue = defaultValue
                self.sliderMin = sliderMin
                self.sliderMax = sliderMax

        class CustomPrimitiveData:
            def __init__(self, useCustomPrimitiveData: bool = False, primitiveDataIndex: int = 0):
                self.useCustomPrimitiveData = useCustomPrimitiveData
                self.primitiveDataIndex = primitiveDataIndex
                
        def __init__(
                self,
                group: str = "Globals",
                sortPriority: int = 32, 
                scalarParameter: ScalarParameter = ScalarParameter(), 
                customPrimitiveData: CustomPrimitiveData = CustomPrimitiveData()):
            
            self.materialExpression = MaterialExpressionScalarParameter.Details.MaterialExpression(group, sortPriority)
            self.scalarParameter = scalarParameter
            self.customPrimitiveData = customPrimitiveData

    def __init__(self, name: str, details: Details = Details()):
        super().__init__("MaterialExpressionScalarParameter", name, details)
