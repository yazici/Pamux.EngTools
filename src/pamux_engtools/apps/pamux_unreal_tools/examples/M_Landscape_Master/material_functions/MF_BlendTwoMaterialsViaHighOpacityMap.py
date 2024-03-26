from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_function_builder_base import MaterialFunctionBuilderBase

from pamux_unreal_tools.base.material_expression_container import *

class MF_BlendTwoMaterialsViaHighOpacityMap:
    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__("MF_BlendTwoMaterialsViaHighOpacityMap")

        def build(self):
           pass



# Call (HeightLerp
# FuzzyShading

# SpecularContrast = 0.15
# SpecularMax = 0.5
# Specular = 0.9

# EdgeSpecularCorrection = 0.25
# SPecLerp = 0.5
# EdgeSpecularCorrectionStartDistance = 1000
# EdgeSpecularCorrectionFadeDistance = 500
# EdgeSpecularFalloffPower = 4.0

# RotateAboutWorldAxis_cheap

# MakeFloat2

# Forest_FuzzCoreDarkness
# Forest_FuzzPower
# Forest_FuzzBridghtness

# MultiplyAdd
# Append

# Output: Result, Height, PuddleMask

# PuddleCOlor
# PuddleHeight
# PuddleDepth
# PuddleRoughness
# WetnessRoughness
# WetnessDarken
# WetnessSaturation
# 1-x
# Input MaterialAttributes, InMaterial

# LandscapeLayerWeight FoliageMask

# LandscapeLayerWeight Dirt (LayerX)
# Scalar DirtFoliageThreshold = 0.0
# DirtFoliageEnabled = True
# RuntimeVirtualTextureSampleParam LandscapeRVT

# UMaterialExpressionLandscapeGrassOutput

# MaterialExpressionFunctionInput MaterialA, MaterialB, Alpha

# MaterialExpressionFunctionInput LayerSample, FOliageMask, Threshold, Enabled
# RoughnessIntensity, ALbedo, etc.

# TextureBase, UVParams (vector4)
# Constant4Vector
# LandscapeLayerCoords