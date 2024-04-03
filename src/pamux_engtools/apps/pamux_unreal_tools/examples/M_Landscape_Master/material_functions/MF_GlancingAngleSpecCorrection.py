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

from pamux_unreal_tools.base.material_function_builder_base import MaterialFunctionBuilderBase
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_function_outputs_base import MaterialFunctionOutputs

class MF_GlancingAngleSpecCorrection:
    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            self.materialAttributes = builder.build_FunctionInput("In", unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES)
            self.materialAttributes.add_rt()

            preview_value = unreal.Vector4f()
            preview_value.set_editor_property("w", 1.0)
            self.materialAttributes.preview_value.set(preview_value)

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


    class Builder(MaterialFunctionBuilderBase):
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

            # self.inputs.materialAttributes
            makeMaterialAttributes = MakeMaterialAttributes()
            makeMaterialAttributes.specular.comesFrom(lerp)

            self.outputs.Result.comesFrom(makeMaterialAttributes)

#MF_GlancingAngleSpecCorrection.Builder().get()
