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

from pamux_unreal_tools.base.material_function_builder_base import *

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.material_function import MaterialFunctionFactory





from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.wetness_base import WetnessBuilderBase
from pamux_unreal_tools.material_expression_factories import *
# material = util.load_asset('/Game/0_Root/Material/M_standard_shd_test.M_standard_shd_test')
# print(material) # Material
 
# node_set = unreal.MaterialEditingLibrary.get_material_selected_nodes(material)

class MF_Wetness:
    class Inputs:
        def __init__(self, builder: MaterialFunctionBuilderBase):
            pass

    class Builder(WetnessBuilderBase):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_Wetness",
                MF_Wetness.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)

        # Blocks are based on the comments section in the original material
        class WetnessBlock:
            def build(self, materialAttributes: OutSocket, baseColor: OutSocket):
                wetnessSaturation = ScalarParameter("Wetness Saturation", -0.5)
                wetnessDarken = ScalarParameter("Wetness Darken", 0.5)
                wetnessRoughness = ScalarParameter("Wetness Roughness", 0.3)

                desaturation = Desaturation()
                desaturation.input.comesFrom(baseColor)
                desaturation.fraction.comesFrom(wetnessSaturation.output)

                saturate = Saturate(desaturation)

                makeMaterialAttributes = MakeMaterialAttributesFactory.create(materialAttributes)
                makeMaterialAttributes.baseColor.comesFrom(Multiply(saturate, wetnessDarken))
                makeMaterialAttributes.roughness.comesFrom(wetnessRoughness)

                return makeMaterialAttributes.output

        class HeightBlendBasedOnInputWetnessValueBlock:
            def build(self, prewettedMaterialAttributes: OutSocket, materialAttributes: OutSocket):
                breakMaterialAttributes = BreakMaterialAttributes(materialAttributes)

                # wetness = FunctionInput()
                wetness = FunctionInputFactory.create("Wetness", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(1.0))
                # wetness.input_name.set("Wetness")
                # wetness.input_type.set(unreal.FunctionInputType.FUNCTION_INPUT_SCALAR)
                # wetness.preview.comesFrom(Constant(1.0))

                saturate = Saturate(Add(Subtract(breakMaterialAttributes.opacity, Constant(1.0)), Multiply(wetness, 2.0)))

                return BlendMaterialAttributes(prewettedMaterialAttributes, materialAttributes, saturate).output

        def build_dependencies(self):
            pass

        def build_input_nodes(self):
            self.inputs = MF_Wetness.Inputs(self)

        def build_process_nodes(self):
            materialAttributes = self.getMaterialAttributes()

            breakMaterialAttributes = BreakMaterialAttributes(materialAttributes)

            wetness = MF_Wetness.Builder.WetnessBlock().build(breakMaterialAttributes, breakMaterialAttributes.baseColor)
            
            heightBlendBasedOnInputWetnessValue = MF_Wetness.Builder.HeightBlendBasedOnInputWetnessValueBlock().build(
                materialAttributes,
                wetness)

            result = self.makeFunctionOutput("Result", 0)

            MEL.connect_material_expressions(heightBlendBasedOnInputWetnessValue.materialExpression.asset, "", result.asset, "")

            # self.heightBlendBasedOnInputWetnessValue.connectToFunctionOutput(self.result)
        
        def build_output_nodes(self):
            pass

        def finalize_node_connections(self):
            #             MEL.connect_material_expressions(
            #     breakMaterialAttributes.asset,
            #     breakMaterialAttributes.input.name,
            #     self.Result.asset,
            #     f"")

            # MEL.connect_material_expressions(componentMask.asset, "", self.Height.asset, f"")
        
            self.breakMaterialAttributes.connectToFunctionOutput(self.Result)
            self.componentMask.connectToFunctionOutput(self.Height)

            
