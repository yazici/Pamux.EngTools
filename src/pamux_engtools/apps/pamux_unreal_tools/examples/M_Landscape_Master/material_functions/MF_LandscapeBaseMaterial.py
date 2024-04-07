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
    @staticmethod
    def load_MF(builder):
        return  builder.load_MF("/Game/Materials/Pamux/Landscape/Functions/MF_LandscapeBaseMaterial",
                                ["Albedo", "ColorOverlay", "ColorOverlayIntensity", "Contrast", "ContrastVariation", "Roughness", "RoughnessIntensity", "NormalIntensity", "Normal", "Displacement", "Rotation", "DoTextureBomb", "DoRotationVariation", "BombCellScale", "BombPatternScale", "BombRandomOffset", "BombRotationVariation", "OpacityStrength", "OpacityAdd", "OpacityContrast"],
                                ["Result", "Height"])

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

            self.MF_TextureCellBombing_Landscape    = MF_TextureCellBombing_Landscape.load_MF(builder)

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
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_LandscapeBaseMaterial",
                MF_LandscapeBaseMaterial.Dependencies,
                MF_LandscapeBaseMaterial.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)
            

        def __build_cellBombing(self, map, uvParams):
            call = self.dependencies.MF_TextureCellBombing_Landscape.call()
            call.outputs.result.add_rt()
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


        def __build_switched(self, uvParams, cellBombed):
            textureSample = TextureSample()
            textureSample.RGB.add_rt()
            textureSample.UVs.comesFrom(uvParams)
            textureSample.tex.comesFrom(cellBombed)
            textureSample.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            textureSample.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
            textureSample.automatic_view_mip_bias.set(True)

            return StaticSwitch(
                cellBombed.outputs.result,
                textureSample.RGB,
                self.inputs.doTextureBomb)
        
        def __build_qualitySwitchAlbedo(self, switchedAlbedo):
            call = self.dependencies.blend_Overlay.call()
            call.inputs.base.comesFrom(switchedAlbedo)
            call.inputs.blend.comesFrom(self.inputs.colorOverlay)

            qualitySwitch = QualitySwitch()
            qualitySwitch.add_rt()
            qualitySwitch.default.comesFrom(call.outputs.result)
            qualitySwitch.low.comesFrom(Multiply(switchedAlbedo, self.inputs.colorOverlay))

            return qualitySwitch.output
        
        def __build_finalAlbedo(self, lerpedAlbedo, switchedDisplacement):
            cheapContrast_RGB = self.dependencies.cheapContrast_RGB.call()
            cheapContrast_RGB.inputs._in.comesFrom(lerpedAlbedo)
            cheapContrast_RGB.inputs.contrast.comesFrom(self.inputs.contrast)

            heightLerp = self.dependencies.heightLerp.call()
            heightLerp.inputs.a.comesFrom(lerpedAlbedo)
            heightLerp.inputs.b.comesFrom(cheapContrast_RGB)
            heightLerp.inputs.transitionPhase.comesFrom(self.inputs.contrastVariation)
            heightLerp.inputs.heightTexture.comesFrom(switchedDisplacement)

            qualitySwitch = QualitySwitch()
            qualitySwitch.add_rt()
            qualitySwitch.default.comesFrom(heightLerp.outputs.results)
            qualitySwitch.low.comesFrom(lerpedAlbedo)

            return qualitySwitch

        def build(self):
            qualitySwitch = QualitySwitch()
            qualitySwitch.add_rt()
            qualitySwitch.default.comesFrom(self.inputs.doTextureBomb)
            qualitySwitch.low.comesFrom(StaticBool(False))

            uvParams = self.__build_uvParams()

            albedo = self.__build_cellBombing(self.inputs.albedo, uvParams)
            switchedAlbedo = self.__build_switched(uvParams, albedo)
            qualitySwitchedAlbedo = self.__build_qualitySwitchAlbedo(switchedAlbedo)
            lerpedAlbedo = LinearInterpolate(switchedAlbedo, qualitySwitchedAlbedo, self.inputs.colorOverlayIntensity)

            roughness = self.__build_cellBombing(self.inputs.roughness, uvParams)
            switchedRoughness = self.__build_switched(uvParams, roughness)
            finalRoughness = Multiply(switchedRoughness, self.inputs.roughnessIntensity)

            displacement = self.__build_cellBombing(self.inputs.displacement, uvParams)
            switchedDisplacement = self.__build_switched(uvParams, displacement)
            finalDisplacement = Add(Multiply(Power(switchedDisplacement, self.inputs.opacityContrast), self.inputs.opacityStrength), self.inputs.opacityAdd)

            normal = self.__build_cellBombing(self.inputs.normal, uvParams)
            switchedNormal = self.__build_switched(uvParams, normal)
            
            call = self.dependencies.multiplyAdd.call()
            call.inputs.base.comesFrom(switchedNormal)
            call.inputs.add.comesFrom(AppendVector(AppendVector(self.inputs.normalIntensity, self.inputs.normalIntensity), Constant(0.0)))
            finalNormal = call.outputs.result

            finalAlbedo = self.__build_finalAlbedo(lerpedAlbedo, switchedDisplacement)

            makeMaterialAttributes = MakeMaterialAttributes()
            makeMaterialAttributes.baseColor.comesFrom(finalAlbedo)
            makeMaterialAttributes.roughness.comesFrom(finalRoughness)
            makeMaterialAttributes.normal.comesFrom(finalNormal)
            makeMaterialAttributes.opacity.comesFrom(finalDisplacement)

            breakMaterialAttributes = BreakMaterialAttributes(makeMaterialAttributes)

            componentMask = ComponentMask(breakMaterialAttributes.opacity, "R")

            makeMaterialAttributes.connectTo(self.outputs.result)
            componentMask.connectTo(self.outputs.height)
