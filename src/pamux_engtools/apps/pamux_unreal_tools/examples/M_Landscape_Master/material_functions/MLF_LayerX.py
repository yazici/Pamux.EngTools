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


from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl
from pamux_unreal_tools.base.material_function_builder_base import MaterialLayerFunctionBuilderBase
from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase

# self.weight = LLWeightParameter(f"{name}")
# self.foliageThreshold = ScalarParameter(f"{name}FoliageThreshold")
# self.foliageEnabled = StaticBoolParameter(f"{name}FoliageEnabled", foliageEnabledDefaultValue)

class MLF_LayerX:
    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            self.alpha = builder.build_FunctionInput(f"{builder.layer_name}Albedo", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR)

    class Builder(MaterialLayerFunctionBuilderBase):
        def __init__(self, layer_name: str, MF_LandscapeBaseMaterial: MaterialFunctionImpl):
            super().__init__(
                f"/Game/Materials/Pamux/Landscape/Functions/Layers/MLF_{layer_name}",
                MaterialFunctionDependenciesBase,
                MLF_LayerX.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)

            self.layer_name = layer_name
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial


        def build(self):
            self.call_MF_LandscapeBaseMaterial = self.MF_LandscapeBaseMaterial.call()

            #self.call_MF_LandscapeBaseMaterial.output.connectTo(result.a)
            #call_MF_LandscapeBaseMaterial.height.connectTo(height.a)

            # MaterialFunctions.landscapeBaseMaterial(Params.Dirt)

            # roughness = ScalarParameter(material_function)
            # roughness.parameter_name.set("Roughness")
            # roughness.default_value.set(0.5)


            self.call_MF_LandscapeBaseMaterial.Result.connectToFunctionOutput(self.Result)
            self.call_MF_LandscapeBaseMaterial.Height.connectToFunctionOutput(self.Height)

            # MEL.connect_material_expressions(self.call_MF_LandscapeBaseMaterial.unrealAsset, "Result", self.Result.unrealAsset, f"")
            # MEL.connect_material_expressions(self.call_MF_LandscapeBaseMaterial.unrealAsset, "Height", self.Hesult.unrealAsset, f"")


        # def MLF_Dirt():
        #     return MaterialFunctions.landscapeBaseMaterial(Params.Dirt)

MLF_LayerX.Builder().get()