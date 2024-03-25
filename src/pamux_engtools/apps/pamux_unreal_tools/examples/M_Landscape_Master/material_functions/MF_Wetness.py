from pamux_unreal_tools.material_function import MaterialFunction
from pamux_unreal_tools.base.material_function_builder_base import MaterialFunctionBuilderBase
from pamux_unreal_tools.material import Material
from pamux_unreal_tools.material import MaterialAttributeGuids
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *

# material = util.load_asset('/Game/0_Root/Material/M_standard_shd_test.M_standard_shd_test')
# print(material) # Material
 
# node_set = unreal.MaterialEditingLibrary.get_material_selected_nodes(material)

class MF_Wetness:
    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__("MF_Wetness")

        # Blocks are based on the comments section in the original material
        class WetnessBlock:
            def build(self, material_function, materialAttributes: OutSocket, baseColor: OutSocket):
                self.wetnessSaturation = ScalarParameter(material_function, "Wetness Saturation", -0.5)
                self.wetnessDarken = ScalarParameter(material_function, "Wetness Darken", 0.5)
                self.wetnessRoughness = ScalarParameter(material_function, "Wetness Roughness", 0.3)

                self.desaturation = Desaturation(material_function)
                self.desaturation.input.comesFrom(baseColor)
                self.desaturation.fraction.comesFrom(self.wetnessSaturation.output)

                self.saturate = Saturate(material_function)
                self.saturate.input.comesFrom(self.desaturation.output)

                self.multiply = Multiply(material_function)
                self.multiply.a.comesFrom(self.saturate.output)
                self.multiply.b.comesFrom(self.wetnessDarken.output)

                self.setMaterialAttributes = SetMaterialAttributes(material_function)
                setMaterialAttributesArray = unreal.Array(unreal.Guid)
                setMaterialAttributesArray.append(MaterialAttributeGuids.BaseColor)
                setMaterialAttributesArray.append(MaterialAttributeGuids.Roughness)
                #self.setMaterialAttributes.attribute_set_types.set(setMaterialAttributesArray)

                self.setMaterialAttributes.materialAttributes.comesFrom(materialAttributes)
                self.setMaterialAttributes.baseColor.comesFrom(self.multiply.output)
                self.setMaterialAttributes.roughness.comesFrom(self.wetnessRoughness.output)

                return self.setMaterialAttributes.output

        class HeightBlendBasedOnInputWetnessValueBlock:
            def build(self, material_function, prewettedMaterialAttributes: OutSocket, materialAttributes: OutSocket):
                self.getMaterialAttributes = GetMaterialAttributes(material_function)
                self.getMaterialAttributes.input.comesFrom(materialAttributes)

                self.constWetness = Constant(material_function)
                self.constWetness.r.set(1.0)

                self.wetness = FunctionInput(material_function)
                self.wetness.input_name.set("Wetness")
                self.wetness.input_type.set(unreal.FunctionInputType.FUNCTION_INPUT_SCALAR)
                self.wetness.preview.comesFrom(self.constWetness.output)


                self.multiply = Multiply(material_function)
                self.multiply.a.comesFrom(self.wetness.output)
                self.multiply.const_b.set(2.0)

                self.constSubtract = Constant(material_function)

                self.subtract = Subtract(material_function)
                self.subtract.a.comesFrom(self.getMaterialAttributes.opacity)
                self.subtract.b.comesFrom(self.constSubtract.output)

                self.add = Add(material_function)
                self.add.a.comesFrom(self.subtract.output)
                self.add.b.comesFrom(self.multiply.output)

                self.saturate = Saturate(material_function)
                self.saturate.input.comesFrom(self.add.output)

                self.blendMaterialAttributes = BlendMaterialAttributes(material_function)
                self.blendMaterialAttributes.a.comesFrom(prewettedMaterialAttributes)
                self.blendMaterialAttributes.b.comesFrom(self.getMaterialAttributes.materialAttributes)
                self.blendMaterialAttributes.alpha.comesFrom(self.saturate.output)

                return self.blendMaterialAttributes.output

        def build(self):
            self.textureSampleSet = MaterialFunctionBuilderBase.TextureSampleSet(
                self.current_container, 
                "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_A", 
                "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_R", 
                "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_D", 
                "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_N")


            self.makeMaterialAttributes = MakeMaterialAttributes(self.current_container)
            self.makeMaterialAttributes.baseColor.comesFrom(self.textureSampleSet.baseColor.RGB)
            self.makeMaterialAttributes.roughness.comesFrom(self.textureSampleSet.roughness.RGB)
            self.makeMaterialAttributes.opacity.comesFrom(self.textureSampleSet.opacity.RGB)
            self.makeMaterialAttributes.normal.comesFrom(self.textureSampleSet.normal.RGB)

            self.inMaterial = FunctionInput(self.current_container)
            self.inMaterial.input_name.set("InMaterial")
            self.inMaterial.input_type.set(unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES)
            self.inMaterial.preview.comesFrom(self.makeMaterialAttributes.output)

            self.getMaterialAttributes = GetMaterialAttributes(self.current_container)
            
            getMaterialAttributesArray = unreal.Array(unreal.Guid)
            getMaterialAttributesArray.append(MaterialAttributeGuids.BaseColor)
            # self.getMaterialAttributes.attribute_get_types.set(getMaterialAttributesArray)

            
            self.getMaterialAttributes.input.comesFrom(self.inMaterial.output)

            self.wetness = MF_Wetness.Builder.WetnessBlock().build(
                self.current_container,
                self.getMaterialAttributes.materialAttributes,
                self.getMaterialAttributes.baseColor)
            
            self.heightBlendBasedOnInputWetnessValue = MF_Wetness.Builder.HeightBlendBasedOnInputWetnessValueBlock().build(
                self.current_container,
                self.getMaterialAttributes.materialAttributes,
                self.wetness)

            self.result = self.makeFunctionOutput("Result", 0)

            MEL.connect_material_expressions(self.heightBlendBasedOnInputWetnessValue.materialExpression.asset, "", self.result.asset, "")

            # self.heightBlendBasedOnInputWetnessValue.connectToFunctionOutput(self.result)

            
