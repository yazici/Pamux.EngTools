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

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_function_builder_base import MaterialFunctionBuilderBase
from pamux_unreal_tools.base.material_function_outputs_base import MaterialFunctionOutputs

from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase

class MF_BlendTwoMaterialsViaHighOpacityMap:
    class Dependencies:
        def __init__(self, builder: ContainerBuilderBase) -> None:
             self.heightLerpWithTwoHeightMaps = builder.load_MF(
                "/Engine/Functions/Engine_MaterialFunctions02/Texturing/HeightLerpWithTwoHeightMaps",
                [ "Transistion Phase", "Height Texture 1", "Height Texture 2" ],
                [ "Alpha" ])

    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            # No Preview
            self.alpha      = builder.build_FunctionInput("Alpha",      2, 0.0, False)
            self.materialA  = builder.build_FunctionInput("MaterialA",  0, unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES, False)
            self.materialB  = builder.build_FunctionInput("MaterialB",  1, unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES, False)

    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_BlendTwoMaterialsViaHighOpacityMap",
                MF_BlendTwoMaterialsViaHighOpacityMap.Dependencies,
                MF_BlendTwoMaterialsViaHighOpacityMap.Inputs,
                MaterialFunctionOutputs.Result)

        def build(self):
            breakMaterialAttributesA = BreakMaterialAttributes(self.inputs.materialA.rt)
            breakMaterialAttributesB = BreakMaterialAttributes(self.inputs.materialB.rt)

            # Transistion is misspelled in the built in function
            lerp = self.dependencies.heightLerpWithTwoHeightMaps.call()
            lerp.transistionPhase.comesFrom(self.inputs.alpha.rt)
            lerp.heightTexture1.comesFrom(breakMaterialAttributesA.opacity)
            lerp.heightTexture2.comesFrom(breakMaterialAttributesB.opacity)

            self.blendMaterialAttributes = BlendMaterialAttributes(self.inputs.materialA.rt, self.inputs.materialB.rt, lerp.alpha)

            self.blendMaterialAttributes.output.connectToFunctionOutput(self.outputs.Result)

# MF_BlendTwoMaterialsViaHighOpacityMap.Builder().get()
