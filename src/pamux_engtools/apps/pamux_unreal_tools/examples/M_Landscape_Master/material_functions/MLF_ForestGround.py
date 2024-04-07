from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.builders.material_function_builder import MaterialLayerFunctionBuilder
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.IForestGround import IForestGround

from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.layer_inputs import LayerInputs
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.layer_build import LayerBuild
from pamux_unreal_tools.factories.material_expression_factories import MakeMaterialAttributesFactory
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_LandscapeBaseMaterial import MF_LandscapeBaseMaterial

class MLF_ForestGround:
    @staticmethod
    def load_MF(builder):
        return  builder.load_MF("/Game/Materials/Pamux/Landscape/Functions/Layers/MLF_ForestGround",
                                LayerInputs.get("ForestGround"),
                                ["Result", "Height"])
    
    class Dependencies:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            self.fuzzyShading = builder.load_FuzzyShading()

            self.MF_LandscapeBaseMaterial    = MF_LandscapeBaseMaterial.load_MF(builder)

    class Inputs(LayerInputs):
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            super().__init__(builder, "RF")
            self.fuzzCoreDarkness = ScalarParameter(f"Forest_FuzzCoreDarkness", 0.0)
            self.fuzzPower = ScalarParameter(f"Forest_FuzzPower", 1.0)
            self.fuzzEdgeBrightness = ScalarParameter(f"Forest_FuzzBrightness", 1.0)

    class Builder(MaterialLayerFunctionBuilder):
        def __init__(self):
            super().__init__(
                "ForestGround",
                MLF_ForestGround.Dependencies,
                MLF_ForestGround.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)

        def build(self):
            call = LayerBuild.call_and_connect_LandscapeBaseMaterial(self)
            self.inputs.opacityStrength.connectTo(call.inputs.opacityStrength)
            self.inputs.opacityAdd.connectTo(call.inputs.opacityAdd)
            self.inputs.opacityContrast.connectTo(call.inputs.opacityContrast)

            breakMaterialAttributes = BreakMaterialAttributes(call.outputs.result)
            call.outputs.result.connectTo(breakMaterialAttributes)

            fuzzShading =  self.dependencies.fuzzyShading.call()
            fuzzShading.inputs.baseColor.comesFrom(breakMaterialAttributes.baseColor)
            fuzzShading.inputs.normal.comesFrom(breakMaterialAttributes.normal)
            fuzzShading.inputs.coreDarkness.comesFrom(self.inputs.fuzzCoreDarkness)
            fuzzShading.inputs.power.comesFrom(self.inputs.fuzzPower)
            fuzzShading.inputs.edgeBrightness.comesFrom(self.inputs.fuzzEdgeBrightness)

            roughnessB = ComponentMask(breakMaterialAttributes.roughness, "B")
            lerp = LinearInterpolate(breakMaterialAttributes.baseColor, fuzzShading.outputs.result, roughnessB)

            makeMaterialAttributes = MakeMaterialAttributesFactory.create(breakMaterialAttributes)
            makeMaterialAttributes.baseColor.comesFrom(lerp.output)
            makeMaterialAttributes.normal.comesFrom(breakMaterialAttributes.normal)
            makeMaterialAttributes.specular.comesFrom(breakMaterialAttributes.specular)
            makeMaterialAttributes.roughness.comesFrom(breakMaterialAttributes.roughness)

            makeMaterialAttributes.output.connectTo(self.outputs.result)
