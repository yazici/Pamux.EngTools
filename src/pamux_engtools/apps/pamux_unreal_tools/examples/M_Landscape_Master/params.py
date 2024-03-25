from pamux_unreal_tools.generated.material_expression_wrappers import *

class LandscapeBaseMaterialParams:

    # self.DoTextureBomb = True
    # self.Albedo = Texture Object
    # self.Bomb.DoRotationVariation = false
    # self.Bomb.DoCellScale = 1.0
    # self.Bomb.PatternScale = 1.0
    # self.Bomb.RandomOffset = 0.0
    # self.Bomb.RotationVariation = 0
    # self.UVParams (1,1,.5,.5)
    # self.Rotation = 0.0
    # self.ColorOverlay = (1,1,1)
    # self.Contrast = 0.0
    # self.Contrast.Variation = 1.0
    
    def __init__(self):
        self.Albedo = None
        self.ColorOverlay = None
        self.ColorOverlay_Intensity = None

        self.Contrast = None
        self.Contrast_Variation = None

        self.Roughness = None
        self.Roughness_Intensity = None

        self.Normal_Intensity = None
        self.Normal = None

        self.Displacement = None

        self.UVParams = None # Append(Result, RotCenterY -A-)

        self.Rotation = None

        self.DoTextureBomb = None
        self.Bomb_DoRotationVariation = None
        self.Bomb_DoCellScale = None
        self.Bomb_PatternScale = None
        self.Bomb_RandomOffset = None
        self.Bomb_RotationVariation = None

        self.Opacity_Strength = None
        self.Opacity_Add = None
        self.Opacity_Contrast = None

class LandscapeLayerParams(LandscapeBaseMaterialParams):
    def __init__(self, layer_name):
        self.layer_name = layer_name

class Params:
    def __init__(self, material):
        self.Wetness = ScalarParameter(material)
        self.LandscapeRVT = ScalarParameter(material)
        self.LandscapeVisibilityMask = ScalarParameter(material)

        self.Dirt = LandscapeLayerParams("Dirt")
        self.Grass = LandscapeLayerParams("Grass")
        self.Mud = LandscapeLayerParams("Mud")
        self.StonyGround = LandscapeLayerParams("StonyGround")
        self.Fields = LandscapeLayerParams("Fields")
        self.PlowedGround = LandscapeLayerParams("PlowedGround")
        self.ForestGround = LandscapeLayerParams("ForestGround")
        self.HeavyMud = LandscapeLayerParams("HeavyMud")
