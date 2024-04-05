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

from pamux_unreal_tools.builders.material_function_builder import MaterialLayerFunctionBuilder
from pamux_unreal_tools.base.material_function.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.IForestGround import IForestGround

class MLF_ForestGround:
    class Inputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            pass

    class Builder(MaterialLayerFunctionBuilder):
        def __init__(self, MF_LandscapeBaseMaterial: MaterialFunctionImpl):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/Layers/MLF_ForestGround",
                MaterialFunctionDependenciesBase,
                MLF_ForestGround.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)

            self.layer_name = "ForestGround"
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial

        def build(self):
            pass

            # roughness = ScalarParameter(material_function)
            # roughness.parameter_name.set("Roughness")
            # roughness.default_value.set(0.5)

            # roughness.connectTo(unreal.MaterialProperty.MP_ROUGHNESS)


# def MLF_ForestGround():
#         result, height = MaterialFunctions.landscapeBaseMaterial(Params.ForestGround, Params.ForestGround.Opacity)

#         materialAttributes = Nodes.breakMaterialAttributes(result)

#         fuzzyShading = Nodes.fuzzyShading(
#             materialAttributes.baseColor,
#             materialAttributes.normal,
#             Params.ForestGround.FuzzCoreDarkness,
#             Params.ForestGround.FuzzPower,
#             Params.ForestGround.FuzzBrightness
#         )

#         rouhgnessB = Nodes.mask(materialAttributes.rouhgness, "B")

#         lerped = Nodes.lerp(materialAttributes.baseColor, fuzzyShading, rouhgnessB)

#         return Nodes.makeMaterialAttributes(
#             lerped,
#             materialAttributes.normal,
#             materialAttributes.specular,
#             materialAttributes.roughness
#         ), height


# MLF_ForestGround.Builder().get()