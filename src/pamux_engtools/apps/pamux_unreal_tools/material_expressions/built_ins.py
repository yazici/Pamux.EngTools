import unreal

from pamux_unreal_tools.material_expression import MaterialExpression
from pamux_unreal_tools.material_expression_container import MaterialExpressionContainer


class GetMaterialAttributes(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionGetMaterialAttributes, node_pos_x, node_pos_y)


class SetMaterialAttributes(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionSetMaterialAttributes, node_pos_x, node_pos_y)


class VirtualTextureFeatureSwitch(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionVirtualTextureFeatureSwitch, node_pos_x, node_pos_y)


class QualitySwitch(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionQualitySwitch, node_pos_x, node_pos_y)

class Switch(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionSwitch, node_pos_x, node_pos_y)

class SCurve(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionSCurve, node_pos_x, node_pos_y)

class BlendMaterialAttributes(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionBlendMaterialAttributes, node_pos_x, node_pos_y)

# ???
class HeightLerp(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionHeightLerpWithTwoHeightMaps, node_pos_x, node_pos_y)

class HeightLerpWithTwoHeightMaps(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionHeightLerpWithTwoHeightMaps, node_pos_x, node_pos_y)

class Saturate(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionSaturate, node_pos_x, node_pos_y)

class Transform(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionTransform, node_pos_x, node_pos_y)

class CustomRotator(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionCustomRotator, node_pos_x, node_pos_y)

class Blend_Overlay(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionBlend_Overlay, node_pos_x, node_pos_y)



class CheapContrast_RGB(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionCheapContrast_RGB, node_pos_x, node_pos_y)



class Mask(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionMask, node_pos_x, node_pos_y)

class MakeMaterialAttributes(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionMakeMaterialAttributes, node_pos_x, node_pos_y)

class LandscapeLayerWeight(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionLandscapeLayerWeight, node_pos_x, node_pos_y)

class LandscapeLayerSwitch(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionLandscapeLayerSwitch, node_pos_x, node_pos_y)


class LandscapeLayerSample(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionLandscapeLayerSample, node_pos_x, node_pos_y)

class LandscapeLayerCoords(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionLandscapeLayerSample, node_pos_x, node_pos_y)

class LandscapeGrassOutput(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionLandscapeLayerSample, node_pos_x, node_pos_y)

class LandscapeVisibilityMask(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionLandscapeVisibilityMask, node_pos_x, node_pos_y)

class RuntimeVirtualTextureSampleParameter(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.RuntimeVirtualTextureSampleParameter, node_pos_x, node_pos_y)

class TextureBase(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionTextureBase, node_pos_x, node_pos_y)

class Fresnel(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionFresnel, node_pos_x, node_pos_y)

