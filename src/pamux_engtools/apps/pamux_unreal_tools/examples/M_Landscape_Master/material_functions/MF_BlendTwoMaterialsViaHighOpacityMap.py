import unreal
from pathlib import Path
import sys
# import os
# import shutil

# sys.path.append(str(Path(__file__).parent.parent.parent.parent.parent.resolve()))

# from importlib import * 

# reloads = []
# for  k, v in sys.modules.items():
#     if k.startswith("pamux_unreal_tools"):
#         reloads.append(v)

# for module in reloads:
#     reload(module)

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.utils.types import *

from pamux_unreal_tools.builders.material_function_builder import MaterialFunctionBuilder
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs

from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase

from pamux_unreal_tools.interfaces.IHeightLerpWithTwoHeightMaps import IHeightLerpWithTwoHeightMaps
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.IBlendTwoMaterialsViaHighOpacityMap import IBlendTwoMaterialsViaHighOpacityMap
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory

class MF_BlendTwoMaterialsViaHighOpacityMap:
    class Dependencies:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
             self.heightLerpWithTwoHeightMaps = builder.load_MF(
                "/Engine/Functions/Engine_MaterialFunctions02/Texturing/HeightLerpWithTwoHeightMaps",
                [ "Transistion Phase", "Height Texture 1", "Height Texture 2" ],
                [ "Alpha" ])

    class Inputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            # No Preview
            self.alpha      = builder.build_FunctionInput("Alpha",      2, 0.0,                     False, False)
            self.materialA  = builder.build_FunctionInput("MaterialA",  0, TMaterialAttributes(),   False, False)
            self.materialB  = builder.build_FunctionInput("MaterialB",  1, TMaterialAttributes(),   False, False)

    class Builder(MaterialFunctionBuilder):
        def __init__(self) -> None:
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_BlendTwoMaterialsViaHighOpacityMap",
                MF_BlendTwoMaterialsViaHighOpacityMap.Dependencies,
                MF_BlendTwoMaterialsViaHighOpacityMap.Inputs,
                MaterialFunctionOutputs.Result)

        def build(self):
            breakMaterialAttributesA = BreakMaterialAttributes(self.inputs.materialA)
            breakMaterialAttributesB = BreakMaterialAttributes(self.inputs.materialB)

            # Transistion is misspelled in the built in function
            lerp = self.dependencies.heightLerpWithTwoHeightMaps.call()
            lerp.transistionPhase.comesFrom(self.inputs.alpha)
            lerp.heightTexture1.comesFrom(breakMaterialAttributesA.opacity)
            lerp.heightTexture2.comesFrom(breakMaterialAttributesB.opacity)

            self.blendMaterialAttributes = BlendMaterialAttributes(self.inputs.materialA, self.inputs.materialB, lerp.alpha)

            self.blendMaterialAttributes.connectTo(self.outputs.result)

# MF_BlendTwoMaterialsViaHighOpacityMap.Builder().get()
