from pamux_unreal_tools.material_function import MaterialFunction
from pamux_unreal_tools.material_function_builder_base import MaterialLayerFunctionBuilderBase
from pamux_unreal_tools.material import Material
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.material_expression_container import *

# self.weight = LLWeightParameter(f"{name}")
# self.foliageThreshold = ScalarParameter(f"{name}FoliageThreshold")
# self.foliageEnabled = StaticBoolParameter(f"{name}FoliageEnabled", foliageEnabledDefaultValue)

class MLF_LayerX:
    class Builder(MaterialLayerFunctionBuilderBase):
        def __init__(self, layer_name: str, MF_LandscapeBaseMaterial: MaterialFunction):
            super().__init__(f"MLF_{layer_name}")

            self.layer_name = layer_name
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial

        def build(self):
            self.call_MF_LandscapeBaseMaterial = self.callMaterialFunction(self.MF_LandscapeBaseMaterial)

            result, height = self.makeLayerFunctionOutputs()

            MEL.connect_material_expressions(self.call_MF_LandscapeBaseMaterial.asset, "Result", result.asset, f"")
            MEL.connect_material_expressions(self.call_MF_LandscapeBaseMaterial.asset, "Height", height.asset, f"")

            #self.call_MF_LandscapeBaseMaterial.output.connectTo(result.a)
            #call_MF_LandscapeBaseMaterial.height.connectTo(height.a)

            # MaterialFunctions.landscapeBaseMaterial(Params.Dirt)

            # roughness = ScalarParameter(material_function)
            # roughness.parameter_name.set("Roughness")
            # roughness.default_value.set(0.5)




        # def MLF_Dirt():
        #     return MaterialFunctions.landscapeBaseMaterial(Params.Dirt)
