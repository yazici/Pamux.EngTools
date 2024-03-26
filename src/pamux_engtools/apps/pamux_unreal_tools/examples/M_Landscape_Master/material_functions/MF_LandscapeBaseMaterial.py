from importlib import * 

from pamux_unreal_tools.material_function import MaterialFunctionFactory
from pamux_unreal_tools.base.material_function_builder_base import MaterialLayerFunctionBuilderBase
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.examples.M_Landscape_Master.params import *
from pamux_unreal_tools.examples.M_Landscape_Master.globals import *



# from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_TextureCellBombing_Landscape import *

class MF_LandscapeBaseMaterial:
    class Builder(MaterialLayerFunctionBuilderBase):
        def __init__(self):
            super().__init__("MF_LandscapeBaseMaterial")

        # def baseColorPath(self, qualitySwitched, commonParams, rotatedUVs, heightTexture):
        #         switched = self.doStuffWithTexture(material_function, commonParams.Albedo, False, qualitySwitched, commonParams, rotatedUVs)        

        #         switchedAndMultipliedColorOverlay = Multiply(material_function, switched, commonParams.ColorOverlay)

        #         blend_Overlay = MaterialFunctionFactory().load("Blend_Overlay", "/Engine/Functions/Engine_MaterialFunctions03/Blends", True)
        #         call_Blend_Overlay = self.callMaterialFunction(blend_Overlay)
        #         call_Blend_Overlay.base = switched
        #         call_Blend_Overlay.blend = commonParams.ColorOverlay
        #         # blendOverlay = Blend_Overlay(material_function, switched, commonParams.ColorOverlay)


        #         qualitySwitched2 = QualitySwitch(material_function, call_Blend_Overlay.Result, switchedAndMultipliedColorOverlay)

        #         lerpedColorOverlay = LinearInterpolate(material_function, switched, qualitySwitched2, commonParams.ColorOverlay.Intensity)

        #         cheapContrast_RGB = MaterialFunctionFactory().load("CheapContrast_RGB", "/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment", True)
        #         call_CheapContrast_RGB = self.callMaterialFunction(cheapContrast_RGB)
        #         call_CheapContrast_RGB.In = lerpedColorOverlay
        #         call_CheapContrast_RGB.Contrast = commonParams.Contrast

        #         heightLerp = MaterialFunctionFactory().load("HeightLerp", "/Engine/Functions/Engine_MaterialFunctions02/Texturing", True)
        #         call_HeightLerp = self.callMaterialFunction(heightLerp)
        #         call_HeightLerp.A = lerpedColorOverlay
        #         call_HeightLerp.B = call_CheapContrast_RGB.Result
        #         call_HeightLerp.TransitionPhase = commonParams.Contrast.Variation
        #         call_HeightLerp.HeightTexture = heightTexture

        #         return QualitySwitch(heightLerp, lerpedColorOverlay)

        # def roughnessPath(self, qualitySwitched, commonParams, rotatedUVs):
        #     switched = self.doStuffWithTexture(material_function, commonParams.Roughness, False, qualitySwitched, commonParams, rotatedUVs)        

        #     return Multiply(material_function, switched, commonParams.Roughness.Intensity)

        # def normalPath(self, qualitySwitched, commonParams, rotatedUVs):
        #     multiplyAdd = MaterialFunctionFactory().load("MultiplyAdd", "/Engine/Functions/Engine_MaterialFunctions02/Math", True)

        #     switched = self.doStuffWithTexture(material_function, commonParams.Normal, True, qualitySwitched, commonParams, rotatedUVs)

        #     computedIntensity = AppendVector(material_function, commonParams.Normal.Intensity, commonParams.Normal.Intensity)
        #     constZero = 0
        #     computedIntensity = AppendVector(material_function, computedIntensity, constZero)

        #     call_multiplyAdd = self.callMaterialFunction(multiplyAdd)
        #     call_multiplyAdd.a.comesFrom(switched)
        #     call_multiplyAdd.b.comesFrom(computedIntensity)

        #     return call_multiplyAdd.Result
        
        # def heightTexture(self, qualitySwitched, commonParams, rotatedUVs):
        #     return self.doStuffWithTexture(material_function, commonParams.Displacement, False, qualitySwitched, commonParams, rotatedUVs)
            
        # def doStuffWithTexture(self, texture, isNormalMap, qualitySwitched, commonParams, rotatedUVs):
        #     MF_TextureCellBombing_Landscape = MF_TextureCellBombing_Landscape.Builder().get()
        #     call_textureCellBombing_Landscape = MaterialFunctionCall(material_function, MF_TextureCellBombing_Landscape)

        #     # textureCellBombing_LandscapeResult = MaterialFunctions.textureCellBombing_Landscape(
        #     #     texture,
        #     #     rotatedUVs,
        #     #     commonParams.Bomb.DoCellScale,
        #     #     commonParams.Bomb.PatternScale,
        #     #     commonParams.Bomb.DoRotationVariation,
        #     #     commonParams.Bomb.RandomOffset, # Variation??
        #     #     commonParams.Bomb.RotationVariation,
        #     #     isNormalMap)
            
        #     textureSample = TextureSample(material_function, uvs = rotatedUVs, tex = texture)

        #     return Switch(material_function, call_textureCellBombing_Landscape, textureSample, qualitySwitched)



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

        #     computedIntensity = Power(material_function, heightTexture, commonParams.Opacity.Contrast)
        #     computedIntensity = Multiply(material_function, computedIntensity, commonParams.Opacity.Strength)
        #     computedIntensity = Add(material_function, computedIntensity, commonParams.Opacity.Add)

        #     return MultiplyAdd(material_function, heightTexture, computedIntensity)

        def build(self):
            commonParams = LandscapeBaseMaterialParams()

            breakOutFloat4Components = MaterialFunctionFactory().load("BreakOutFloat4Components", "/Engine/Functions/Engine_MaterialFunctions02/Utility", True)
            call_BreakOutFloat4Components = self.callMaterialFunction(breakOutFloat4Components)
            # call_BreakOutFloat4Components.float4.comesFrom(commonParams.UVParams)

            componentMask = ComponentMask()
            componentMask.g.set(False)

            makeMaterialAttributes = MakeMaterialAttributes()
            qualitySwitch = QualitySwitch()
            makeMaterialAttributes.baseColor.comesFrom(qualitySwitch)

            multiply = Multiply()
            makeMaterialAttributes.roughness.comesFrom(multiply)

            multiplyAdd = MaterialFunctionFactory().load("MultiplyAdd", "/Engine/Functions/Engine_MaterialFunctions02/Math", True)

            call_multiplyAdd = self.callMaterialFunction(multiplyAdd)
            # call_multiplyAdd.a.comesFrom(switched)
            # call_multiplyAdd.b.comesFrom(computedIntensity)


            # makeMaterialAttributes.normal.comesFrom(multiplyAdd)

            add = Add()
            makeMaterialAttributes.opacity.comesFrom(add)
            
            breakMaterialAttributes = BreakMaterialAttributes(makeMaterialAttributes)

            result, height = self.makeLayerFunctionOutputs()

            MEL.connect_material_expressions(
                breakMaterialAttributes.asset,
                breakMaterialAttributes.input.name,
                result.asset,
                f"")

            MEL.connect_material_expressions(componentMask.asset, "", height.asset, f"")

            # uvParamsRG = AppendVector(material_function, call_BreakOutFloat4Components.r, call_BreakOutFloat4Components.g)
            # uvParamsBA = AppendVector(material_function, call_BreakOutFloat4Components.b, call_BreakOutFloat4Components.a)

            # landscapeLayerCoords = LandscapeLayerCoords(material_function)

            # multiply = Multiply(material_function)
            # multiply.a = landscapeLayerCoords
            # multiply.b = uvParamsRG

            # customRotator = MaterialFunctionFactory().load("CustomRotator", "/Engine/Functions/Engine_MaterialFunctions02/Texturing", True)
            # call_CustomRotator = self.callMaterialFunction(customRotator)

            # call_CustomRotator.
            # uvParamsBA, 
            # commonParams.Rotation
            # rotatedUVs = call_CustomRotator.output
            # customRotator(material_function, multiply.output, )

            # qualitySwitched = QualitySwitch(material_function, commonParams.DoTextureBomb, False)

            # heightTexture = HeightTexture(material_function, qualitySwitched, commonParams, rotatedUVs)

            # baseColor = self.baseColorPath(material_function, qualitySwitched, commonParams, rotatedUVs, heightTexture)
            # roughness = self.roughnessPath(material_function, qualitySwitched, commonParams, rotatedUVs)        
            # opacity = self.opacityPath(material_function, heightTexture, commonParams)
            # normal = self.normalPath(material_function, qualitySwitched, commonParams, rotatedUVs)

            # sma = MakeMaterialAttributes(material_function, baseColor, roughness, normal, opacity)
            # gma = BreakMaterialAttributes(material_function, sma)

            # gmaOpacityR = Mask(material_function, gma.Opacity, "R")

            # return gma, gmaOpacityR
