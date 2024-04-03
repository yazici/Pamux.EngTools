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

from pamux_unreal_tools.base.material_function_builder_base import MaterialLayerFunctionBuilderBase
from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase
from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl

class MLF_ForestGround:
    class Dependencies:
        def __init__(self, builder: ContainerBuilderBase) -> None:
             pass

    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            pass

    class Builder(MaterialLayerFunctionBuilderBase):
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


MLF_ForestGround.Builder().get()