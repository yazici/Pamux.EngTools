import unreal
from pathlib import Path
import sys
import os
import shutil

sys.path.append(str(Path(__file__).parent.parent.parent.parent.parent.resolve()))

from importlib import * 

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)

from pamux_unreal_tools.base.material_function_builder_base import MaterialFunctionBuilderBase

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.material_function import MaterialFunctionFactory

class MF_BlendTwoMaterialsViaHighOpacityMap:
    class Inputs:
        def __init__(self, builder: MaterialFunctionBuilderBase):
            preview_value = unreal.Vector4f()
            preview_value.set_editor_property("w", 1.0)


            self.alpha = builder.build_FunctionInput("Alpha", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR)
            self.alpha.preview_value.set(preview_value)
            self.alpha.sort_priority.set(2)
            self.alpha.use_preview_value_as_default.set(False)

            self.materialA = builder.build_FunctionInput("MaterialA", unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES)
            self.materialA.preview_value.set(preview_value)
            self.materialA.sort_priority.set(0)
            self.materialA.use_preview_value_as_default.set(False)

            self.materialB = builder.build_FunctionInput("MaterialB", unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES)
            self.materialB.preview_value.set(preview_value)
            self.materialB.sort_priority.set(1)
            self.materialB.use_preview_value_as_default.set(False)

    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__("MF_BlendTwoMaterialsViaHighOpacityMap")

        def build_dependencies(self):
            factory = MaterialFunctionFactory()
            self.heightLerpWithTwoHeightMaps = factory.load("HeightLerpWithTwoHeightMaps", "/Engine/Functions/Engine_MaterialFunctions02/Texturing")

        def build_input_nodes(self):
            self.inputs = MF_BlendTwoMaterialsViaHighOpacityMap.Inputs(self)

        def build_process_nodes(self):
            breakMaterialAttributesA = BreakMaterialAttributes(self.inputs.materialA.rt)
            breakMaterialAttributesB = BreakMaterialAttributes(self.inputs.materialB.rt)

            # Transistion is misspelled in the built in function
            lerp = self.callMaterialFunction(self.heightLerpWithTwoHeightMaps, [ "Transistion Phase", "Height Texture 1", "Height Texture 2" ], [ "Alpha" ])
            lerp.transistionPhase.comesFrom(self.inputs.alpha.rt)
            lerp.heightTexture1.comesFrom(breakMaterialAttributesA.opacity)
            lerp.heightTexture2.comesFrom(breakMaterialAttributesB.opacity)

            self.blendMaterialAttributes = BlendMaterialAttributes(self.inputs.materialA.rt, self.inputs.materialB.rt, lerp.alpha)

        def finalize_node_connections(self):
            return self.blendMaterialAttributes.output.connectToFunctionOutput(self.outputs.Result)


folder = "C:/src/Unreal Projects/PamuxSurvival/Content/Materials/Pamux"
if os.path.isdir(folder):
    shutil.rmtree(folder)

MF_BlendTwoMaterialsViaHighOpacityMap.Builder().get()


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