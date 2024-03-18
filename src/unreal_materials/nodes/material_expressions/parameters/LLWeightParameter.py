from unreal_materials.nodes.utils.node_base import GroupedParameterBase

class LLWeightParameter(GroupedParameterBase):
    class Details(GroupedParameterBase.DetailsBase):
        def __init__(self):
            super().__init__()

            self.previewWeight = 0.0
            
    def __init__(self, name: str):
        super().__init__("MaterialExpressionLandscapeLayerWeight", name, LLWeightParameter.Details())
