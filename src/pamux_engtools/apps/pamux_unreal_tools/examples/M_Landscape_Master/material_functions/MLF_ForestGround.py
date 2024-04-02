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
from pamux_unreal_tools.material_function import MaterialFunction


from pamux_unreal_tools.base.material_function_builder_base import MaterialLayerFunctionBuilderBase





# self.weight = LLWeightParameter(f"{name}")
# self.foliageThreshold = ScalarParameter(f"{name}FoliageThreshold")
# self.foliageEnabled = StaticBoolParameter(f"{name}FoliageEnabled", foliageEnabledDefaultValue)

class MLF_ForestGround:
    class Inputs:
        def __init__(self, builder: MaterialFunctionBuilderBase):
            pass

    class Builder(MaterialLayerFunctionBuilderBase):
        def __init__(self, MF_LandscapeBaseMaterial: MaterialFunction):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/Layers/MLF_ForestGround",
                MLF_ForestGround.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)

            self.layer_name = "ForestGround"
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial

        def build_dependencies(self):
            pass
    
        def build_process_nodes(self):
            pass
        
        def build_output_nodes(self):
            pass

        def finalize_node_connections(self):
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
