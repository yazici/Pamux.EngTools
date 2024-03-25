from pamux_unreal_tools.material_function import MaterialFunction
from pamux_unreal_tools.material_function_builder_base import MaterialLayerFunctionBuilderBase
from pamux_unreal_tools.material import Material
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.material_expression_container import *

# self.weight = LLWeightParameter(f"{name}")
# self.foliageThreshold = ScalarParameter(f"{name}FoliageThreshold")
# self.foliageEnabled = StaticBoolParameter(f"{name}FoliageEnabled", foliageEnabledDefaultValue)

class MLF_ForestGround:
    class Builder(MaterialLayerFunctionBuilderBase):
        def __init__(self, MF_LandscapeBaseMaterial: MaterialFunction):
            super().__init__(f"MLF_ForestGround")

            self.layer_name = "ForestGround"
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial

        def build(self):
            result, height = self.makeLayerFunctionOutputs()

            # roughness = ScalarParameter(material_function)
            # roughness.parameter_name.set("Roughness")
            # roughness.default_value.set(0.5)

            # roughness.connectTo(unreal.MaterialProperty.MP_ROUGHNESS)


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
