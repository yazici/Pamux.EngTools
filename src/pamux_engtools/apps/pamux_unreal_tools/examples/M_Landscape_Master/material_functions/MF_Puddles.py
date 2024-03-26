from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.base.material_function_builder_base import MaterialFunctionBuilderBase
from pamux_unreal_tools.material import Material
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.wetness_base import WetnessBuilderBase

class MF_Puddles:
    class Builder(WetnessBuilderBase):
        def __init__(self):
            super().__init__("MF_Puddles")

        def build(self):
            materialAttributesOutput = self.getMaterialAttributesOutput()

            breakMaterialAttributes = BreakMaterialAttributes()
            breakMaterialAttributes.input.comesFrom(materialAttributesOutput)

            puddleColor = VectorParameter("Puddle Color", unreal.LinearColor(0.057292, 0.051375, 0.034017, 1.0))
            puddleHeight = ScalarParameter("Puddle Height", 1.0)
            puddleSlope = ScalarParameter("Puddle Slope", 0.25)
            puddleDepth = ScalarParameter("Puddle Depth", 0.75)
            puddleRoughness = ScalarParameter("Puddle Roughness", 0.15)
            puddleSpecular = OneMinus()
            puddleSpecular.input.comesFrom(puddleRoughness.output)

            puddleNormal = Constant3Vector()
            puddleNormal.constant = Property(puddleNormal, 'constant', 'LinearColor') # TODO No Input
            puddleNormal.constant.set(unreal.LinearColor(0.0, 0.0, 1.0))

            puddleOpacity = Constant()
            puddleOpacity.r.set(1.0)

            puddleColorMultiply = Multiply()
            puddleColorMultiply.a.comesFrom(puddleColor.output)
            puddleColorMultiply.b.comesFrom(puddleColor.a)

            lerp = LinearInterpolate()
            lerp.a.comesFrom(breakMaterialAttributes.baseColor)
            lerp.b.comesFrom(puddleColorMultiply.output)
            lerp.alpha.comesFrom(puddleDepth.output)

            makeMaterialAttributes = MakeMaterialAttributes()
            makeMaterialAttributes.baseColor.comesFrom(lerp.output)
            makeMaterialAttributes.metallic.comesFrom(breakMaterialAttributes.metallic)
            makeMaterialAttributes.specular.comesFrom(puddleSpecular.output)
            makeMaterialAttributes.roughness.comesFrom(puddleRoughness.output)
            makeMaterialAttributes.anisotropy.comesFrom(breakMaterialAttributes.anisotropy)
            makeMaterialAttributes.emissiveColor.comesFrom(breakMaterialAttributes.emissiveColor)
            makeMaterialAttributes.opacity.comesFrom(puddleOpacity.output)
            makeMaterialAttributes.opacityMask.comesFrom(breakMaterialAttributes.opacityMask)
            makeMaterialAttributes.normal.comesFrom(puddleNormal.output)
            makeMaterialAttributes.tangent.comesFrom(breakMaterialAttributes.tangent)
            makeMaterialAttributes.worldPositionOffset.comesFrom(breakMaterialAttributes.worldPositionOffset)
            makeMaterialAttributes.subsurfaceColor.comesFrom(breakMaterialAttributes.subsurfaceColor)
            makeMaterialAttributes.clearCoat.comesFrom(breakMaterialAttributes.clearCoat)
            makeMaterialAttributes.clearCoatRoughness.comesFrom(breakMaterialAttributes.clearCoatRoughness)
            makeMaterialAttributes.ambientOcclusion.comesFrom(breakMaterialAttributes.ambientOcclusion)
            makeMaterialAttributes.refraction.comesFrom(breakMaterialAttributes.refraction)
            makeMaterialAttributes.customizedUV_0.comesFrom(breakMaterialAttributes.customizedUV0)
            makeMaterialAttributes.customizedUV_1.comesFrom(breakMaterialAttributes.customizedUV1)
            makeMaterialAttributes.customizedUV_2.comesFrom(breakMaterialAttributes.customizedUV2)
            makeMaterialAttributes.customizedUV_3.comesFrom(breakMaterialAttributes.customizedUV3)
            makeMaterialAttributes.customizedUV_4.comesFrom(breakMaterialAttributes.customizedUV4)
            makeMaterialAttributes.customizedUV_5.comesFrom(breakMaterialAttributes.customizedUV5)
            makeMaterialAttributes.customizedUV_6.comesFrom(breakMaterialAttributes.customizedUV6)
            makeMaterialAttributes.customizedUV_7.comesFrom(breakMaterialAttributes.customizedUV7)
            makeMaterialAttributes.pixelDepthOffset.comesFrom(breakMaterialAttributes.pixelDepthOffset)
            makeMaterialAttributes.shadingModel.comesFrom(breakMaterialAttributes.shadingModel)
            makeMaterialAttributes.displacement.comesFrom(breakMaterialAttributes.displacement)

            componentMask = ComponentMask()
            componentMask.input.comesFrom(breakMaterialAttributes.opacity)
            componentMask.r.set(True)
            componentMask.g.set(False)
            componentMask.b.set(False)
            componentMask.a.set(False)

            saturate1 = Saturate(
                            Divide(
                                Subtract(componentMask.output, puddleHeight.output).output,
                                puddleSlope.output
                            ).output)

            saturate2 = Saturate(OneMinus(saturate1.output).output)

            blendMaterialAttributes = BlendMaterialAttributes()
            blendMaterialAttributes.a.comesFrom(materialAttributesOutput)
            blendMaterialAttributes.b.comesFrom(makeMaterialAttributes.output)
            blendMaterialAttributes.alpha.comesFrom(saturate2.output)


            result = self.makeFunctionOutput("Result", 0)
            MEL.connect_material_expressions(blendMaterialAttributes.asset, "", result.asset, "")

            puddleMask = self.makeFunctionOutput("PuddleMask", 1)
            MEL.connect_material_expressions(saturate2.asset, "", puddleMask.asset, "")
