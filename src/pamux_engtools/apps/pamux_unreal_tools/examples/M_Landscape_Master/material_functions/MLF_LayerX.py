from pamux_unreal_tools.material_function import MaterialFunction
from pamux_unreal_tools.base.material_function_builder_base import MaterialLayerFunctionBuilderBase
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *

# self.weight = LLWeightParameter(f"{name}")
# self.foliageThreshold = ScalarParameter(f"{name}FoliageThreshold")
# self.foliageEnabled = StaticBoolParameter(f"{name}FoliageEnabled", foliageEnabledDefaultValue)

class MLF_LayerX:
    class Builder(MaterialLayerFunctionBuilderBase):
        def __init__(self, layer_name: str, MF_LandscapeBaseMaterial: MaterialFunction):
            super().__init__(f"MLF_{layer_name}")

            self.layer_name = layer_name
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial

        def build_dependencies(self):
            pass
        
        def build_input_nodes(self):
            pass

        def build_process_nodes(self):
            self.call_MF_LandscapeBaseMaterial = self.callMaterialFunction(self.MF_LandscapeBaseMaterial, [], [ "Result", "Height" ])

            #self.call_MF_LandscapeBaseMaterial.output.connectTo(result.a)
            #call_MF_LandscapeBaseMaterial.height.connectTo(height.a)

            # MaterialFunctions.landscapeBaseMaterial(Params.Dirt)

            # roughness = ScalarParameter(material_function)
            # roughness.parameter_name.set("Roughness")
            # roughness.default_value.set(0.5)


        def finalize_node_connections(self):
            return 
            self.call_MF_LandscapeBaseMaterial.Result.connectToFunctionOutput(self.Result)
            self.call_MF_LandscapeBaseMaterial.Height.connectToFunctionOutput(self.Height)

            # MEL.connect_material_expressions(self.call_MF_LandscapeBaseMaterial.asset, "Result", self.Result.asset, f"")
            # MEL.connect_material_expressions(self.call_MF_LandscapeBaseMaterial.asset, "Height", self.Hesult.asset, f"")


        # def MLF_Dirt():
        #     return MaterialFunctions.landscapeBaseMaterial(Params.Dirt)
