from unreal_materials.nodes.utils.node_base import MaterialExpressionBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html

# https://docs.unrealengine.com/5.0/en-US/landscape-material-layer-blending-in-unreal-engine/#creatinglandscapeholematerials
# https://docs.unrealengine.com/5.0/en-US/landscape-material-layer-blending-in-unreal-engine/#landscapevisibilitymasknode
# The LandscapeVisibilityMask node removes visible parts of your Landscape, so you can create holes in your landscape to, for example, create caves.


class LandscapeVisibilityMask(MaterialExpressionBase):    
    def __init__(self):
        super().__init__("MaterialExpressionLandscapeVisibilityMask", "LandscapeVisibilityMask")
