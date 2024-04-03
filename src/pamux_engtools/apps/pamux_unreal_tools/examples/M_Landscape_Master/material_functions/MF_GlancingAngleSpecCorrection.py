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
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.factories.material_expression_factories import FunctionInputFactory
from pamux_unreal_tools.base.material_expression_base import MaterialExpressionBase

class MF_GlancingAngleSpecCorrection:
    class Dependencies:
        def __init__(self, builder: ContainerBuilderBase) -> None:
             pass

    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            self.materialAttributes = builder.build_FunctionInput("In", unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES)

            preview_value = unreal.Vector4f()
            preview_value.set_editor_property("w", 1.0)
            self.materialAttributes.preview_value.set(preview_value)


    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_GlancingAngleSpecCorrection",
                MaterialFunctionDependenciesBase,
                MF_GlancingAngleSpecCorrection.Inputs,
                MaterialFunctionOutputs.Result)

        def build(self):
            breakMaterialAttributes = BreakMaterialAttributes(self.inputs.materialAttributes)
            # self.add_rt(breakMaterialAttributes.normal)
            # "rtBreakMaterialAttributes.Normal"
            breakMaterialAttributes.normal.add_rt()

            # breakMaterialAttributes.specular

            transform = Transform(breakMaterialAttributes.normal)

MF_GlancingAngleSpecCorrection.Builder().get()
