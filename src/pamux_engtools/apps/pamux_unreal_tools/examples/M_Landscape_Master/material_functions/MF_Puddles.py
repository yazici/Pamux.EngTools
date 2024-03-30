from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.wetness_base import WetnessBuilderBase

class MF_Puddles:
    class Builder(WetnessBuilderBase):
        def __init__(self):
            super().__init__("MF_Puddles")

        def build_dependencies(self):
            pass

        def build_input_nodes(self):
            pass

        def build_process_nodes(self):
            self.materialAttributes = self.getMaterialAttributes()

            self.breakMaterialAttributes = BreakMaterialAttributes(self.materialAttributes)

            self.puddleColor = VectorParameter("Puddle Color", unreal.LinearColor(0.057292, 0.051375, 0.034017, 1.0))
            self.puddleHeight = ScalarParameter("Puddle Height", 1.0)
            self.puddleSlope = ScalarParameter("Puddle Slope", 0.25)
            self.puddleDepth = ScalarParameter("Puddle Depth", 0.75)
            self.puddleRoughness = ScalarParameter("Puddle Roughness", 0.15)
            self.puddleSpecular = OneMinus(self.puddleRoughness.output)

            self.puddleNormal = Constant3Vector()
            self.puddleNormal.constant = Property(self.puddleNormal, 'constant', 'LinearColor') # TODO No Input
            self.puddleNormal.constant.set(unreal.LinearColor(0.0, 0.0, 1.0))

            self.puddleOpacity = Constant(1.0)
            self.puddleColorMultiply = Multiply(self.puddleColor.output, self.puddleColor.a)

            self.lerp = LinearInterpolate(self.breakMaterialAttributes.baseColor, self.puddleColorMultiply.output, self.puddleDepth.output)

            self.makeMaterialAttributes = MakeMaterialAttributes.create(self.breakMaterialAttributes)
            self.makeMaterialAttributes.baseColor.comesFrom(self.lerp.output)
            self.makeMaterialAttributes.specular.comesFrom(self.puddleSpecular.output)
            self.makeMaterialAttributes.roughness.comesFrom(self.puddleRoughness.output)
            self.makeMaterialAttributes.opacity.comesFrom(self.puddleOpacity.output)
            self.makeMaterialAttributes.normal.comesFrom(self.puddleNormal.output)

            self.componentMask = ComponentMask(self.breakMaterialAttributes.opacity)
            self.componentMask.r.set(True)
            self.componentMask.g.set(False)
            self.componentMask.b.set(False)
            self.componentMask.a.set(False)

            self.saturate = Saturate(OneMinus(Saturate(Divide(Subtract(self.componentMask, self.puddleHeight), self.puddleSlope))))

            self.blendMaterialAttributes = BlendMaterialAttributes(self.materialAttributes, self.makeMaterialAttributes, self.saturate)


        def build_output_nodes(self):
            self.Result = self.makeFunctionOutput("Result", 0)
            self.PuddleMask = self.makeFunctionOutput("PuddleMask", 1)

        def finalize_node_connections(self):
            MEL.connect_material_expressions(self.blendMaterialAttributes.asset, "", self.Result.asset, "")
            MEL.connect_material_expressions(self.saturate.asset, "", self.PuddleMask.asset, "")
