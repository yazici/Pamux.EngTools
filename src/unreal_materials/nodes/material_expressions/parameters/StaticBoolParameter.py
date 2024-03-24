from unreal_materials.nodes.utils.node_base import GroupedParameterBase

class StaticBoolParameter(GroupedParameterBase):    
    class Details(GroupedParameterBase.DetailsBase):
        class BoolParameter:
            def __init__(self):
                self.defaultValue = False
                self.dynamicBranch = False
                
        def __init__(self):            
            super().__init__()
            self.boolParameter = StaticBoolParameter.Details.BoolParameter()

    def __init__(self, name: str):
        super().__init__("MaterialExpressionStaticBoolParameter", name, StaticBoolParameter.Details())
