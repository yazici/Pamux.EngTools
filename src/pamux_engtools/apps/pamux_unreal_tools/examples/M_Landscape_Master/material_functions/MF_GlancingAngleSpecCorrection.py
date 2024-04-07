from pamux_unreal_tools.utils.types import *

from pamux_unreal_tools.builders.material_function_builder import MaterialFunctionBuilder
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_function.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.IGlancingAngleSpecCorrection import IGlancingAngleSpecCorrection
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.factories.material_expression_factories import MakeMaterialAttributesFactory

class MF_GlancingAngleSpecCorrection:
    @staticmethod
    def load_MF(builder):
        return  builder.load_MF("/Game/Materials/Pamux/Landscape/Functions/MF_GlancingAngleSpecCorrection",
                                ["MaterialAttributes", "EdgeSpecularFalloffPower", "EdgeSpecularCorrectionStartDistance", "EdgeSpecularCorrectionFadeDistance", "EdgeSpecularCorrection", "SpecLerp"],
                                ["Result"])
    class Inputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            self.materialAttributes = builder.build_FunctionInput("In", 0,  TMaterialAttributes(), False, False)

            self.pixelDepth = PixelDepth()
            self.pixelDepth.add_rt()

            self.edgeSpecularFalloffPower = ScalarParameter("EdgeSpecularFalloffPower", 4.0)
            self.edgeSpecularFalloffPower.add_rt()

            self.edgeSpecularCorrectionStartDistance = ScalarParameter("EdgeSpecularCorrectionStartDistance", 1000.0)
            self.edgeSpecularCorrectionStartDistance.add_rt()

            self.edgeSpecularCorrectionFadeDistance = ScalarParameter("EdgeSpecularCorrectionFadeDistance", 500.0)
            self.edgeSpecularCorrectionFadeDistance.add_rt()

            self.edgeSpecularCorrection = ScalarParameter("EdgeSpecularCorrection", 0.25)
            self.edgeSpecularCorrection.add_rt()

            self.specLerp = ScalarParameter("SpecLerp", 0.5)
            self.specLerp.add_rt()


    class Builder(MaterialFunctionBuilder):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_GlancingAngleSpecCorrection",
                MaterialFunctionDependenciesBase,
                MF_GlancingAngleSpecCorrection.Inputs,
                MaterialFunctionOutputs.Result)

        def build(self):
            breakMaterialAttributes = BreakMaterialAttributes(self.inputs.materialAttributes)
            breakMaterialAttributes.normal.add_rt()
            breakMaterialAttributes.specular.add_rt()

            transform = Transform(breakMaterialAttributes.normal.rt)

            fresnel = Fresnel()
            fresnel.exponentIn.comesFrom(self.inputs.edgeSpecularFalloffPower.output.rt)
            fresnel.base_reflect_fraction.set(0.04)
            fresnel.normal.comesFrom(transform)

            saturate1 = Saturate(fresnel)

            subtract = Subtract(self.inputs.pixelDepth, self.inputs.edgeSpecularCorrectionStartDistance.output.rt)

            divide = Divide(subtract, self.inputs.edgeSpecularCorrectionFadeDistance.output.rt)

            saturate2 = Saturate(divide)

            multiply1 = Multiply(saturate1, saturate2)

            multiply2 = Multiply(breakMaterialAttributes.specular.rt, self.inputs.edgeSpecularCorrection.output.rt)

            lerp = LinearInterpolate(breakMaterialAttributes.specular.rt, multiply2, multiply1)

            makeMaterialAttributes = MakeMaterialAttributesFactory.create(breakMaterialAttributes)
            makeMaterialAttributes.specular.comesFrom(lerp)

            self.outputs.result.comesFrom(makeMaterialAttributes)

#MF_GlancingAngleSpecCorrection.Builder().get()
