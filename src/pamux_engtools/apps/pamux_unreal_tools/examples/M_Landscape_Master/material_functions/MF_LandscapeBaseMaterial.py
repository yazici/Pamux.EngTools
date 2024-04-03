from importlib import * 
import os
import shutil

from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.base.material_function_builder_base import MaterialLayerFunctionBuilderBase
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.examples.M_Landscape_Master.params import *
from pamux_unreal_tools.examples.M_Landscape_Master.globals import *
from pamux_unreal_tools.factories.material_expression_factories import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_TextureCellBombing_Landscape import MF_TextureCellBombing_Landscape
from pamux_unreal_tools.base.material_function_builder_base import *
from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos
from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase

class MF_LandscapeBaseMaterial:
    class Dependencies:
        def __init__(self, builder: ContainerBuilderBase) -> None:
            self.blend_Overlay = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Overlay", [ "Base", "Blend" ], [ "Result" ])
            self.cheapContrast_RGB = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment/CheapContrast_RGB", [ "In", "Contrast" ], [ "Result" ])
            self.heightLerp = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Texturing/HeightLerp", [ "A", "B", "Transition Phase", "Height Texture", "Contrast" ], [ "Results", "Alpha", "Lerp Alpha No Contrast" ])
            self.multiplyAdd = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Math/MultiplyAdd", [ "Base", "Add" ], [ "Result" ])
            self.breakOutFloat4Components = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat4Components", [ "Float4" ], [ "R", "G", "B", "A" ])
            self.customRotator = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Texturing/CustomRotator", [ "UVs", "Rotation Center", "Rotation Angle" ], [ "Rotated Values" ])

            self.MF_TextureCellBombing_Landscape = MF_TextureCellBombing_Landscape.Builder().get()
            # 
            self.call_MF_TextureCellBombing_Landscape = {}

    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            CurrentNodePos.x = 0

            self.rotation = builder.build_FunctionInput("Rotation", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(0.0))
            self.rotation.add_rt()

            self.bombDoRotationVariation = builder.build_FunctionInput("BombDoRotationVariation", unreal.FunctionInputType.FUNCTION_INPUT_STATIC_BOOL, StaticBool(False))
            self.bombDoRotationVariation.add_rt()

            self.bombCellScale = builder.build_FunctionInput("BombCellScale", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(1.0))
            self.bombCellScale.add_rt()

            self.bombPatternScale = builder.build_FunctionInput("BombPatternScale", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(1.0))
            self.bombPatternScale.add_rt()

            self.bombRandomOffset = builder.build_FunctionInput("BombRandomOffset", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(0.0))
            self.bombRandomOffset.add_rt()

            self.displacement = builder.build_FunctionInput("Displacement", unreal.FunctionInputType.FUNCTION_INPUT_TEXTURE2D, TextureBase())
            self.displacement.add_rt()

            self.doTextureBomb = FunctionInputFactory.create("DoTextureBomb", unreal.FunctionInputType.FUNCTION_INPUT_STATIC_BOOL, StaticBool(True))
            self.doTextureBomb.add_rt()

            CurrentNodePos.y += NodePos.DeltaY
            CurrentNodePos.y -= NodePos.DeltaY
            CurrentNodePos.x += NodePos.DeltaX/4*3

            self.qualitySwitch = QualitySwitch()
            self.qualitySwitch.add_rt()

            self.qualitySwitch.default.comesFrom(self.doTextureBomb)
            self.qualitySwitch.low.comesFrom(StaticBool(False))
            
            #MEL.connect_material_expressions(StaticBool(False).output.materialExpression.unrealAsset, "", qualitySwitch.unrealAsset, "Low")

            CurrentNodePos.y += NodePos.DeltaY
            CurrentNodePos.x = 0
            
            self.uvParams = builder.build_FunctionInput("UVParams", unreal.FunctionInputType.FUNCTION_INPUT_VECTOR4, unreal.LinearColor(1.0, 1.0, 0.5, 0.5))
            self.uvParams.add_rt()

            self.albedo = builder.build_FunctionInput("Albedo", unreal.FunctionInputType.FUNCTION_INPUT_TEXTURE2D, TextureObject())
            self.albedo.add_rt()

            self.colorOverlay = builder.build_FunctionInput("ColorOverlay", unreal.FunctionInputType.FUNCTION_INPUT_VECTOR3, unreal.LinearColor(1.0, 1.0, 1.0))
            self.colorOverlay.add_rt()

            self.roughness = builder.build_FunctionInput("Roughness", unreal.FunctionInputType.FUNCTION_INPUT_TEXTURE2D, TextureObject())
            self.roughness.add_rt()

            self.normal = builder.build_FunctionInput("Normal", unreal.FunctionInputType.FUNCTION_INPUT_TEXTURE2D, TextureObject(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL))
            self.normal.add_rt()

    class Builder(MaterialLayerFunctionBuilderBase):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/Layers/MF_LandscapeBaseMaterial",
                MF_LandscapeBaseMaterial.Dependencies,
                MF_LandscapeBaseMaterial.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)

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
        #     #     commonParams.Bomb.DoCellScale,
        #     #     commonParams.Bomb.PatternScale,
        #     #     commonParams.Bomb.DoRotationVariation,
        #     #     commonParams.Bomb.RandomOffset, # Variation??
        #     #     commonParams.Bomb.RotationVariation,
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


        def __build_cellBombing(self, map_name):
            return
            call = self.MF_TextureCellBombing_Landscape.call()

            self.call_MF_TextureCellBombing_Landscape[map_name] = call
            
            # eval(f"map = self.{map_name}")

            call.texture.comesFrom(map)
            call.UVs.comesFrom(map)
            call.cellScale.comesFrom(map)
            call.patternScale.comesFrom(map)
            call.doRotationVariation.comesFrom(map)
            call.randomOffsetVariation.comesFrom(map)
            call.randomRotationVariation.comesFrom(map)

            call.isNormalMap.comesFrom(Constant(map_name == "normal"))

            call.Result.rt = NamedRerouteDeclaration(f"rtMF_TextureCellBombing_Landscape_{map_name}", call.Result)

        def build(self):
            # commonParams = LandscapeBaseMaterialParams()

            self.landscapeLayerCoords = LandscapeLayerCoords()
            self.landscapeLayerCoords.mapping_type.set(unreal.TerrainCoordMappingType.TCMT_AUTO)
            self.landscapeLayerCoords.custom_uv_type.set(unreal.LandscapeCustomizedCoordType.LCCT_NONE)

            self.breakOutFloat4Components.call()
            # self.breakOutFloat4Components.call_result.float4.comesFrom(self.uvParams)
            # self.uvParamsRG = AppendVector(self.breakOutFloat4Components.call_result.r, self.breakOutFloat4Components.call_result.g)
            # self.uvParamsBA = AppendVector(self.breakOutFloat4Components.call_result, self.breakOutFloat4Components.call_result.a)

            # self.multiply = Multiply(self.landscapeLayerCoords, self.uvParamsRG)

            self.customRotator.call()
            # self.customRotator.call_result.UVs.comesFrom(self.multiply)
            # self.customRotator.call_result.rotationCenter.comesFrom(self.uvParamsBA)
            # self.customRotator.call_result.rotationAngle.comesFrom(self.rotation.rt)

            
            self.__build_cellBombing("albedo")
            self.__build_cellBombing("roughness")
            self.__build_cellBombing("displacement")
            self.__build_cellBombing("normal")

            self.componentMask = ComponentMask()
            self.componentMask.g.set(False)

            self.makeMaterialAttributes = MakeMaterialAttributes()
            
            # #makeMaterialAttributes.baseColor.comesFrom(qualitySwitch)

            # self.multiply = Multiply()
            # self.makeMaterialAttributes.roughness.comesFrom(self.multiply)

            self.multiplyAdd.call()
            # self.multiplyAdd.call_result.a.comesFrom(switched)
            # self.multiplyAdd.call_result.b.comesFrom(computedIntensity)


            # # makeMaterialAttributes.normal.comesFrom(multiplyAdd)

            # self.add = Add()
            # self.makeMaterialAttributes.opacity.comesFrom(self.add)
            
            self.breakMaterialAttributes = BreakMaterialAttributes(self.makeMaterialAttributes)

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

            self.makeMaterialAttributes.output.connectToFunctionOutput(self.Result)
            self.componentMask.output.connectToFunctionOutput(self.Height)

            #             MEL.connect_material_expressions(
            #     breakMaterialAttributes.unrealAsset,
            #     breakMaterialAttributes.input.name,
            #     self.Result.unrealAsset,
            #     f"")

            # MEL.connect_material_expressions(componentMask.unrealAsset, "", self.Height.unrealAsset, f"")

            # MEL.connect_material_expressions(self.call_BreakOutFloat4Components.output.materialExpression.unrealAsset, "", self.uvParams.unrealAsset, "Low")

MF_LandscapeBaseMaterial.Builder().get()
