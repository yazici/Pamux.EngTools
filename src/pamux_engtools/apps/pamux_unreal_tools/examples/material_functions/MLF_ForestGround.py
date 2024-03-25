from pamux_unreal_tools.material_function import MaterialFunction
from pamux_engtools.apps.pamux_unreal_tools.material_function_builder_base import MaterialFunctionBuilderBase
from pamux_unreal_tools.material_expressions.parameters.scalar_parameter import ScalarParameter
from pamux_unreal_tools.material import Material
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_engtools.apps.pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_engtools.apps.pamux_unreal_tools.material_expression_container import *
from pamux_unreal_tools.material_script_helpers import *

# self.weight = LLWeightParameter(f"{name}")
# self.foliageThreshold = ScalarParameter(f"{name}FoliageThreshold")
# self.foliageEnabled = StaticBoolParameter(f"{name}FoliageEnabled", foliageEnabledDefaultValue)

class MLF_ForestGround:
    @staticmethod
    def build():
        return MF_FoliageMask.Builder().get()
    
    class Builder(MaterialFunctionBuilderBase):
        def __init__(self, layer_name: str, MF_LandscapeBaseMaterial: MaterialFunction):
            super().__init__(f"MLF_{layer_name}")

            self.layer_name = layer_name
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial

        def build(self, material_function: MaterialFunction):
            roughness = ScalarParameter(material_function, "Roughness", 0.5)
            roughness.connectMaterialProperty(material_function.MaterialProperty.MP_ROUGHNESS)


# def MLF_ForestGround():
#         result, height = MaterialFunctions.landscapeBaseMaterial(Params.ForestGround, Params.ForestGround.Opacity)

#         materialAttributes = Nodes.getMaterialAttributes(result)

#         fuzzyShading = Nodes.fuzzyShading(
#             materialAttributes.baseColor,
#             materialAttributes.normal,
#             Params.ForestGround.FuzzCoreDarkness,
#             Params.ForestGround.FuzzPower,
#             Params.ForestGround.FuzzBrightness
#         )

#         rouhgnessB = Nodes.mask(materialAttributes.rouhgness, "B")

#         lerped = Nodes.lerp(materialAttributes.baseColor, fuzzyShading, rouhgnessB)

#         return Nodes.setMaterialAttributes(
#             lerped,
#             materialAttributes.normal,
#             materialAttributes.specular,
#             materialAttributes.roughness
#         ), height
