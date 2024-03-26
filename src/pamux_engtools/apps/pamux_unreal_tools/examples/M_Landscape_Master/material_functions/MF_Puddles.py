from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.wetness_base import WetnessBuilderBase

class MF_Puddles:
    class Builder(WetnessBuilderBase):
        def __init__(self):
            super().__init__("MF_Puddles")

        def build(self):
            materialAttributes = self.getMaterialAttributes()

            breakMaterialAttributes = BreakMaterialAttributes(materialAttributes)

            puddleColor = VectorParameter("Puddle Color", unreal.LinearColor(0.057292, 0.051375, 0.034017, 1.0))
            puddleHeight = ScalarParameter("Puddle Height", 1.0)
            puddleSlope = ScalarParameter("Puddle Slope", 0.25)
            puddleDepth = ScalarParameter("Puddle Depth", 0.75)
            puddleRoughness = ScalarParameter("Puddle Roughness", 0.15)
            puddleSpecular = OneMinus(puddleRoughness.output)

            puddleNormal = Constant3Vector()
            puddleNormal.constant = Property(puddleNormal, 'constant', 'LinearColor') # TODO No Input
            puddleNormal.constant.set(unreal.LinearColor(0.0, 0.0, 1.0))

            puddleOpacity = Constant(1.0)
            puddleColorMultiply = Multiply(puddleColor.output, puddleColor.a)

            lerp = LinearInterpolate(breakMaterialAttributes.baseColor, puddleColorMultiply.output, puddleDepth.output)

            makeMaterialAttributes = MakeMaterialAttributes.create(breakMaterialAttributes)
            makeMaterialAttributes.baseColor.comesFrom(lerp.output)
            makeMaterialAttributes.specular.comesFrom(puddleSpecular.output)
            makeMaterialAttributes.roughness.comesFrom(puddleRoughness.output)
            makeMaterialAttributes.opacity.comesFrom(puddleOpacity.output)
            makeMaterialAttributes.normal.comesFrom(puddleNormal.output)

            componentMask = ComponentMask(breakMaterialAttributes.opacity)
            componentMask.r.set(True)
            componentMask.g.set(False)
            componentMask.b.set(False)
            componentMask.a.set(False)

            saturate = Saturate(OneMinus(Saturate(Divide(Subtract(componentMask, puddleHeight), puddleSlope))))

            blendMaterialAttributes = BlendMaterialAttributes(materialAttributes, makeMaterialAttributes, saturate)

            result = self.makeFunctionOutput("Result", 0)
            MEL.connect_material_expressions(blendMaterialAttributes.asset, "", result.asset, "")

            puddleMask = self.makeFunctionOutput("PuddleMask", 1)
            MEL.connect_material_expressions(saturate.asset, "", puddleMask.asset, "")
