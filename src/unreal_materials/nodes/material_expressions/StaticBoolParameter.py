from unreal_materials.nodes.node_base import NodeBase
from unreal_materials.nodes.material_expressions.MaterialExpressionParameterBase import MaterialExpressionParameterBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html
class MaterialExpressionStaticBoolParameter(MaterialExpressionParameterBase):    
    class Details(NodeBase.DetailsBase):
        class BoolParameter:
            def __init__(self, defaultValue: bool = False, dynamicBranch: bool = False):
                self.defaultValue = defaultValue
                self.dynamicBranch = dynamicBranch

                
        def __init__(
                self,
                group: str = "Globals",
                sortPriority: int = 32, 
                dynamicBranch: bool = False, 
                defaultValue: bool = False):
            
            self.materialExpression = MaterialExpressionStaticBoolParameter.Details.MaterialExpression(group, sortPriority)
            self.boolParameter = MaterialExpressionStaticBoolParameter.Details.BoolParameter(defaultValue, dynamicBranch)

    def __init__(self, name: str, defaultValue: bool = False, dynamicBranch: bool = False):
        super().__init__("MaterialExpressionStaticBoolParameter", name, details = MaterialExpressionStaticBoolParameter.Details(defaultValue, dynamicBranch))
