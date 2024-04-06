import unreal

import logging
logger = logging.getLogger(__name__)

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.utils.types import *
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase

from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_TextureCellBombing_Landscape import MF_TextureCellBombing_Landscape

from pamux_unreal_tools.builders.material_function_builder import MaterialFunctionBuilder
from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs

from pamux_unreal_tools.interfaces.IBlend_Overlay import IBlend_Overlay
from pamux_unreal_tools.interfaces.ICheapContrast_RGB import ICheapContrast_RGB
from pamux_unreal_tools.interfaces.IHeightLerp import IHeightLerp
from pamux_unreal_tools.interfaces.IMultiplyAdd import IMultiplyAdd
from pamux_unreal_tools.interfaces.IBreakOutFloat4Components import IBreakOutFloat4Components
from pamux_unreal_tools.interfaces.ICustomRotator import ICustomRotator

from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.ILandscapeBaseMaterial import ILandscapeBaseMaterial
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.ITextureCellBombing_Landscape import ITextureCellBombing_Landscape
from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl

class MF_LandscapeBaseMaterial:
    class Dependencies:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            self.blend_Overlay                      = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Overlay",
                                                                      [ "Base", "Blend" ],
                                                                      [ "Result" ])

            self.cheapContrast_RGB                  = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment/CheapContrast_RGB",
                                                                      [ "In", "Contrast" ],
                                                                      [ "Result" ])

            self.heightLerp                         = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Texturing/HeightLerp",
                                                                      [ "A", "B", "Transition Phase", "Height Texture", "Contrast" ],
                                                                      [ "Results", "Alpha", "Lerp Alpha No Contrast" ])

            self.multiplyAdd                        = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Math/MultiplyAdd",
                                                                      [ "Base", "Add" ],
                                                                      [ "Result" ])

            self.breakOutFloat4Components           = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat4Components",
                                                                      [ "Float4" ],
                                                                      [ "R", "G", "B", "A" ])

            self.customRotator                      = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Texturing/CustomRotator",
                                                                      [ "UVs", "Rotation Center", "Rotation Angle" ],
                                                                      [ "Rotated Values" ])

    class Inputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            self.albedo                     = builder.build_FunctionInput("Albedo",                         0,      TTextureObject_Color(),    True,   True)
            self.colorOverlay               = builder.build_FunctionInput("ColorOverlay",                   1,      Vec3f(1.0, 1.0, 1.0),      True,   True)
            self.colorOverlayIntensity      = builder.build_FunctionInput("ColorOverlayIntensity",          2,      1.0,                       True,   True)
            self.contrast                   = builder.build_FunctionInput("Contrast",                       3,      0.0,                       True,   True)
            self.contrastVariation          = builder.build_FunctionInput("ContrastVariation",              4,      1.0,                       True,   True)
            self.roughness                  = builder.build_FunctionInput("Roughness",                      5,      TTextureObject_Color(),    True,   True)
            self.roughnessIntensity         = builder.build_FunctionInput("RoughnessIntensity",             6,      1.0,                       True,   True)
            self.normal                     = builder.build_FunctionInput("Normal",                         7,      TTextureObject_Normal(),   True,   True)
            self.normalIntensity            = builder.build_FunctionInput("NormalIntensity",                8,      0.0,                       True,   True)
            self.displacement               = builder.build_FunctionInput("Displacement",                   9,      TTextureObject_Color(),    True,   True)
            self.uvParams                   = builder.build_FunctionInput("UVParams",                       10,     Vec4f(1.0, 1.0, 0.5, 0.5), True,   True)
            self.rotation                   = builder.build_FunctionInput("Rotation",                       11,     0.0,                       True,   True)
            self.doTextureBomb              = builder.build_FunctionInput("DoTextureBomb",                  12,     True,                      True,   True)
            self.doRotationVariation        = builder.build_FunctionInput("DoRotationVariation",            13,     False,                     True,   True)
            self.bombCellScale              = builder.build_FunctionInput("BombCellScale",                  14,     1.0,                       True,   True)
            self.bombPatternScale           = builder.build_FunctionInput("BombPatternScale",               15,     1.0,                       True,   True)
            self.bombRandomOffset           = builder.build_FunctionInput("BombRandomOffset",               16,     0.0,                       True,   True)
            self.bombRotationVariation      = builder.build_FunctionInput("BombRotationVariation",          17,     0.0,                       True,   True)
            self.opacityStrength            = builder.build_FunctionInput("OpacityStrength",                18,     1.0,                       True,   True)
            self.opacityAdd                 = builder.build_FunctionInput("OpacityAdd",                     19,     0.0,                       True,   True)
            self.opacityContrast            = builder.build_FunctionInput("OpacityContrast",                20,     1.0,                       True,   True)

    class Builder(MaterialFunctionBuilder):
        def __init__(self, MF_TextureCellBombing_Landscape: MaterialFunctionImpl):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_LandscapeBaseMaterial",
                MF_LandscapeBaseMaterial.Dependencies,
                MF_LandscapeBaseMaterial.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)
            self.MF_TextureCellBombing_Landscape = MF_TextureCellBombing_Landscape

        def __build_cellBombing(self, map, uvParams):
            call = self.MF_TextureCellBombing_Landscape.call()
            call.inputs.texture.comesFrom(map)
            call.inputs.uVs.comesFrom(uvParams)
            call.inputs.cellScale.comesFrom(self.inputs.bombCellScale)
            call.inputs.patternScale.comesFrom(self.inputs.bombPatternScale)
            call.inputs.doRotationVariation.comesFrom(self.inputs.doRotationVariation)
            call.inputs.randomOffsetVariation.comesFrom(self.inputs.bombRandomOffset)
            call.inputs.randomRotationVariation.comesFrom(self.inputs.bombRotationVariation)
            if map == self.inputs.normal:
                call.inputs.isNormalMap.comesFrom(StaticBool(True))
            return call

        def __build_uvParams(self):
            call = self.dependencies.breakOutFloat4Components.call()
            call.inputs.float4.comesFrom(self.inputs.uvParams)

            uvParamsRG = AppendVector(call.outputs.r, call.outputs.g)
            uvParamsBA = AppendVector(call.outputs.b, call.outputs.a)

            landscapeLayerCoords = LandscapeLayerCoords()
            landscapeLayerCoords.mapping_type.set(unreal.TerrainCoordMappingType.TCMT_AUTO)
            landscapeLayerCoords.custom_uv_type.set(unreal.LandscapeCustomizedCoordType.LCCT_NONE)

            multiply = Multiply(landscapeLayerCoords, uvParamsRG)

            call = self.dependencies.customRotator.call()
            call.add_rt()
            call.inputs.uVs.comesFrom(multiply)
            call.inputs.rotationCenter.comesFrom(uvParamsBA)
            call.inputs.rotationAngle.comesFrom(self.inputs.rotation)

            return call


        def build(self):
                qualitySwitch = QualitySwitch()
                qualitySwitch.add_rt()
                qualitySwitch.default.comesFrom(self.inputs.doTextureBomb)
                qualitySwitch.low.comesFrom(StaticBool(False))

                uvParams = self.__build_uvParams()

                self.__build_cellBombing(self.inputs.albedo, uvParams)
                self.__build_cellBombing(self.inputs.roughness, uvParams)
                self.__build_cellBombing(self.inputs.displacement, uvParams)
                self.__build_cellBombing(self.inputs.normal, uvParams)

                componentMask = ComponentMask()
                componentMask.g.set(False)

                makeMaterialAttributes = MakeMaterialAttributes()
                
                
                makeMaterialAttributes.baseColor.comesFrom(qualitySwitch)

                #multiply2 = Multiply()
                #makeMaterialAttributes.roughness.comesFrom(multiply2)
                
                computedIntensity = AppendVector(self.inputs.normalIntensity, self.inputs.normalIntensity)
                return
                multiplyAddCall = self.dependencies.multiplyAdd.call()
                multiplyAddCall.inputs.a.comesFrom(qualitySwitch)
                multiplyAddCall.inputs.b.comesFrom(computedIntensity)

                


                # # makeMaterialAttributes.normal.comesFrom(multiplyAdd)

                # self.add = Add()
                # self.makeMaterialAttributes.opacity.comesFrom(self.add)
                
                breakMaterialAttributes = BreakMaterialAttributes(makeMaterialAttributes)

                # call_CustomRotator.
                # uvParamsBA, 
                # commonParams.Rotation
                # rotatedUVs = call_CustomRotator.output
                # customRotator(multiply.output, )

                # qualitySwitched = QualitySwitch(commonParams.DoTextureBomb, False)

                # heightTexture = HeightTexture(qualitySwitched, commonParams, rotatedUVs)

                # baseColor = self.baseColorPath(qualitySwitched, commonParams, rotatedUVs, heightTexture)
                # roughness = self.roughnessPath(qualitySwitched, commonParams, rotatedUVs)        
                # opacity = self.opacityPath(heightTexture, commonParams)
                # normal = self.normalPath(qualitySwitched, commonParams, rotatedUVs)

                # sma = MakeMaterialAttributes(baseColor, roughness, normal, opacity)
                # gma = BreakMaterialAttributes(sma)

                # gmaOpacityR = Mask(gma.Opacity, "R")

                # return gma, gmaOpacityR

                makeMaterialAttributes.connectTo(self.outputs.result)
                componentMask.connectTo(self.outputs.height)

                #             MEL.connect_material_expressions(
                #     breakMaterialAttributes.unrealAsset,
                #     breakMaterialAttributes.input.name,
                #     self.Result.unrealAsset,
                #     f"")

                # MEL.connect_material_expressions(componentMask.unrealAsset, "", self.Height.unrealAsset, f"")

                # MEL.connect_material_expressions(self.call_BreakOutFloat4Components.output.materialExpression.unrealAsset, "", self.uvParams.unrealAsset, "Low")

            # def baseColorPath(self, qualitySwitched, commonParams, rotatedUVs, heightTexture):
            #         switched = self.doStuffWithTexture(commonParams.Albedo, False, qualitySwitched, commonParams, rotatedUVs)

            #         switchedAndMultipliedColorOverlay = Multiply(switched, commonParams.ColorOverlay)

            #         
            #         call_Blend_Overlay = self.blend_Overlay(self)
            #         call_Blend_Overlay.base = switched
            #         call_Blend_Overlay.blend = commonParams.ColorOverlay
            #         # blendOverlay = Blend_Overlay(switched, commonParams.ColorOverlay)


            #         qualitySwitched2 = QualitySwitch(call_Blend_Overlay.Result, switchedAndMultipliedColorOverlay)

            #         lerpedColorOverlay = LinearInterpolate(switched, qualitySwitched2, commonParams.ColorOverlay.Intensity)

            #         
            #         call_CheapContrast_RGB = cheapContrast_RGB.call()
            #         call_CheapContrast_RGB.In = lerpedColorOverlay
            #         call_CheapContrast_RGB.Contrast = commonParams.Contrast
            #         call_HeightLerp = heightLerp.call()
            #         call_HeightLerp.A = lerpedColorOverlay
            #         call_HeightLerp.B = call_CheapContrast_RGB.Result
            #         call_HeightLerp.TransitionPhase = commonParams.Contrast.Variation
            #         call_HeightLerp.HeightTexture = heightTexture

            #         return QualitySwitch(heightLerp, lerpedColorOverlay)

            # def roughnessPath(self, qualitySwitched, commonParams, rotatedUVs):
            #     switched = self.doStuffWithTexture(commonParams.Roughness, False, qualitySwitched, commonParams, rotatedUVs)        

            #     return Multiply(switched, commonParams.Roughness.Intensity)

            # def normalPath(self, qualitySwitched, commonParams, rotatedUVs):
                

            #     switched = self.doStuffWithTexture(commonParams.Normal, True, qualitySwitched, commonParams, rotatedUVs)

            #     computedIntensity = AppendVector(commonParams.Normal.Intensity, commonParams.Normal.Intensity)
            #     constZero = 0
            #     computedIntensity = AppendVector(computedIntensity, constZero)

            #     call_multiplyAdd = multiplyAdd.call()
            #     call_multiplyAdd.a.comesFrom(switched)
            #     call_multiplyAdd.b.comesFrom(computedIntensity)

            #     return call_multiplyAdd.Result
            
            # def heightTexture(self, qualitySwitched, commonParams, rotatedUVs):
            #     return self.doStuffWithTexture(commonParams.Displacement, False, qualitySwitched, commonParams, rotatedUVs)
                
            # def doStuffWithTexture(self, texture, isNormalMap, qualitySwitched, commonParams, rotatedUVs):
            #     MF_TextureCellBombing_Landscape = MF_TextureCellBombing_Landscape.Builder().get()
            #     call_textureCellBombing_Landscape = MaterialFunctionCall(MF_TextureCellBombing_Landscape)

            #     # textureCellBombing_LandscapeResult = MaterialFunctions.textureCellBombing_Landscape(
            #     #     texture,
            #     #     rotatedUVs,
            #     #     commonParams.cellScale,
            #     #     commonParams.patternScale,
            #     #     commonParams.doRotationVariation,
            #     #     commonParams.bombRandomOffset, # Variation??
            #     #     commonParams.bombRotationVariation,
            #     #     isNormalMap)
                
            #     textureSample = TextureSample(uvs = rotatedUVs, tex = texture)

            #     return StaticSwitch(call_textureCellBombing_Landscape, textureSample, qualitySwitched)

            # def opacityPath(self, heightTexture, commonParams):
            #     # # commonParams.D.Intensity = 1
                
            #     # isNormalMap = True

            #     # textureCellBombing_LandscapeResult = MaterialFunctions.textureCellBombing_Landscape(
            #     #     commonParams.Displacement,
            #     #     rotatedUVs,
            #     #     commonParams.Bomb.DoCellScale,
            #     #     commonParams.Bomb.PatternScale,
            #     #     commonParams.Bomb.DoRotationVariation,
            #     #     commonParams.Bomb.RandomOffset, # Variation??
            #     #     commonParams.Bomb.RotationVariation,
            #     #     isNormalMap)
                
            #     # textureSample = Nodes.TextureSample(uvs = rotatedUVs, tex = commonParams.Normal)

            #     # switched = Nodes.switch(textureCellBombing_LandscapeResult, textureSample, qualitySwitched)

            #     computedIntensity = Power(heightTexture, commonParams.Opacity.Contrast)
            #     computedIntensity = Multiply(computedIntensity, commonParams.Opacity.Strength)
            #     computedIntensity = Add(computedIntensity, commonParams.Opacity.Add)

            #     return MultiplyAdd(heightTexture, computedIntensity)


           
        