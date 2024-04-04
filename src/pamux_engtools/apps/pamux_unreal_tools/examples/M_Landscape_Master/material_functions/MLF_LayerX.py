import unreal
from pathlib import Path
import sys
from importlib import * 

sys.path.append(str(Path(__file__).parent.parent.parent.parent.parent.resolve()))

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl
from pamux_unreal_tools.base.material_function_builder_base import MaterialLayerFunctionBuilderBase
from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.ILayerX import ILayerX

class MLF_LayerX:
    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            self.Albedo = None
            self.ColorOverlay = None
            self.ColorOverlay_Intensity = None

            self.Contrast = None
            self.Contrast_Variation = None

            self.Roughness = None
            self.Roughness_Intensity = None

            self.Normal_Intensity = None
            self.Normal = None

            self.Displacement = None

            self.UVParams = None # Append(Result, RotCenterY -A-)

            self.Rotation = None

            self.DoTextureBomb = None
            self.Bomb_DoRotationVariation = None
            self.Bomb_DoCellScale = None
            self.Bomb_PatternScale = None
            self.Bomb_RandomOffset = None
            self.Bomb_RotationVariation = None

            self.Opacity_Strength = None
            self.Opacity_Add = None
            self.Opacity_Contrast = None
            
            self.albedo = TextureObjectParameter(f"{builder.layer_name}Albedo")
            self.roughness = ScalarParameter("Roughness", 0.5)

    class Builder(MaterialLayerFunctionBuilderBase):
        def __init__(self, layer_name: str, MF_LandscapeBaseMaterial: MaterialFunctionImpl):
            super().__init__(
                ILayerX,
                f"/Game/Materials/Pamux/Landscape/Functions/Layers/MLF_{layer_name}",
                MaterialFunctionDependenciesBase,
                MLF_LayerX.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)

            self.layer_name = layer_name
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial


        def build(self):
            call_result = self.MF_LandscapeBaseMaterial.call()

            #call_result.output.connectTo(result.a)
            #call_result.height.connectTo(height.a)

            # MaterialFunctions.landscapeBaseMaterial(Params.Dirt)

            call_result.result.connectTo(self.outputs.result)
            call_result.result.connectTo(self.outputs.height)


        # def MLF_Dirt():
        #     return MaterialFunctions.landscapeBaseMaterial(Params.Dirt)

MLF_LayerX.Builder().get()