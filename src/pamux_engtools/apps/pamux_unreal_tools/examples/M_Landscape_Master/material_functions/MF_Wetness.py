from pamux_unreal_tools.material_function import MaterialFunction
from pamux_unreal_tools.base.material_function_builder_base import MaterialFunctionBuilderBase
from pamux_unreal_tools.material import Material
from pamux_unreal_tools.material import MaterialAttributeGuids
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.wetness_base import WetnessBuilderBase
# material = util.load_asset('/Game/0_Root/Material/M_standard_shd_test.M_standard_shd_test')
# print(material) # Material
 
# node_set = unreal.MaterialEditingLibrary.get_material_selected_nodes(material)

class MF_Wetness:
    class Builder(WetnessBuilderBase):
        def __init__(self):
            super().__init__("MF_Wetness")

        # Blocks are based on the comments section in the original material
        class WetnessBlock:
            def build(self, materialAttributes: OutSocket, baseColor: OutSocket):
                self.wetnessSaturation = ScalarParameter("Wetness Saturation", -0.5)
                self.wetnessDarken = ScalarParameter("Wetness Darken", 0.5)
                self.wetnessRoughness = ScalarParameter("Wetness Roughness", 0.3)

                self.desaturation = Desaturation()
                self.desaturation.input.comesFrom(baseColor)
                self.desaturation.fraction.comesFrom(self.wetnessSaturation.output)

                self.saturate = Saturate()
                self.saturate.input.comesFrom(self.desaturation.output)

                self.multiply = Multiply()
                self.multiply.a.comesFrom(self.saturate.output)
                self.multiply.b.comesFrom(self.wetnessDarken.output)

                self.makeMaterialAttributes = MakeMaterialAttributes()
                self.makeMaterialAttributes.baseColor.comesFrom(self.multiply.output)
                self.makeMaterialAttributes.roughness.comesFrom(self.wetnessRoughness.output)

                return self.makeMaterialAttributes.output

        class HeightBlendBasedOnInputWetnessValueBlock:
            def build(self, prewettedMaterialAttributes: OutSocket, materialAttributes: OutSocket):
                self.breakMaterialAttributes = BreakMaterialAttributes()
                self.breakMaterialAttributes.input.comesFrom(materialAttributes)

                self.constWetness = Constant()
                self.constWetness.r.set(1.0)

                self.wetness = FunctionInput()
                self.wetness.input_name.set("Wetness")
                self.wetness.input_type.set(unreal.FunctionInputType.FUNCTION_INPUT_SCALAR)
                self.wetness.preview.comesFrom(self.constWetness.output)


                self.multiply = Multiply()
                self.multiply.a.comesFrom(self.wetness.output)
                self.multiply.const_b.set(2.0)

                self.constSubtract = Constant()

                self.subtract = Subtract()
                self.subtract.a.comesFrom(self.breakMaterialAttributes.opacity)
                self.subtract.b.comesFrom(self.constSubtract.output)

                self.add = Add()
                self.add.a.comesFrom(self.subtract.output)
                self.add.b.comesFrom(self.multiply.output)

                self.saturate = Saturate()
                self.saturate.input.comesFrom(self.add.output)

                self.blendMaterialAttributes = BlendMaterialAttributes()
                self.blendMaterialAttributes.a.comesFrom(prewettedMaterialAttributes)
                self.blendMaterialAttributes.b.comesFrom(materialAttributes)
                self.blendMaterialAttributes.alpha.comesFrom(self.saturate.output)

                return self.blendMaterialAttributes.output

        def build(self):
            materialAttributesOutput = self.getMaterialAttributesOutput()

            self.breakMaterialAttributes = BreakMaterialAttributes()
            self.breakMaterialAttributes.input.comesFrom(materialAttributesOutput)

            self.wetness = MF_Wetness.Builder.WetnessBlock().build(materialAttributesOutput, self.breakMaterialAttributes.baseColor)
            
            self.heightBlendBasedOnInputWetnessValue = MF_Wetness.Builder.HeightBlendBasedOnInputWetnessValueBlock().build(
                materialAttributesOutput,
                self.wetness)

            self.result = self.makeFunctionOutput("Result", 0)

            MEL.connect_material_expressions(self.heightBlendBasedOnInputWetnessValue.materialExpression.asset, "", self.result.asset, "")

            # self.heightBlendBasedOnInputWetnessValue.connectToFunctionOutput(self.result)

            
