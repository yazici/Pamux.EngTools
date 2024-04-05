import unreal
import inspect
import logging
logger = logging.getLogger(__name__)

MEL = unreal.MaterialEditingLibrary

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.builders.material_function_builder import MaterialLayerFunctionBuilder
from pamux_unreal_tools.base.material_function.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.ILayerX import ILayerX

class MLF_LayerX:
    class Inputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            self.albedo = TextureObjectParameter(f"{builder.layer_name}Albedo")
            self.colorOverlay = VectorParameter(f"{builder.layer_name}ColorOverlay", unreal.LinearColor(0.5, 0.5, 0.5, 1.0))
            self.colorOverlayIntensity = ScalarParameter(f"{builder.layer_name}ColorOverlayIntensity", 0.0)

            self.contrast = ScalarParameter(f"{builder.layer_name}Contrast", 1.0)
            self.contrastVariation = ScalarParameter(f"{builder.layer_name}ContrastVariation", 0.0)

            self.roughness = TextureObjectParameter(f"{builder.layer_name}Roughness")
            self.roughnessIntensity = ScalarParameter(f"{builder.layer_name}RoughnessVariation", 1.0)

            self.normalIntensity = ScalarParameter(f"{builder.layer_name}NormalVariation", 0.0)
            self.normal = TextureObjectParameter(f"{builder.layer_name}Normal", None)
            self.normal.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)

            self.displacement = TextureObjectParameter(f"{builder.layer_name}Displacement")

            self.uvParams =  VectorParameter(f"{builder.layer_name}UVParams", unreal.LinearColor(1.0, 1.0, 0.5, 0.5))

            self.rotation = ScalarParameter(f"{builder.layer_name}Rotation", 0.0)

            self.doTextureBomb = StaticBoolParameter(f"{builder.layer_name}DoTextureBomb", True)
            self.doRotationVariation = StaticBoolParameter(f"{builder.layer_name}DoRotationVariation", True)

            self.bombCellScale = ScalarParameter(f"{builder.layer_name}BombCellScale", 0.0)
            self.bombPatternScale = ScalarParameter(f"{builder.layer_name}BombPatternScale", 0.0)
            self.bombRandomOffset = ScalarParameter(f"{builder.layer_name}BombRandomOffset", 0.0)
            self.bombRotationVariation = ScalarParameter(f"{builder.layer_name}BombRotationVariation", 0.0)

            self.opacityStrength = ScalarParameter(f"{builder.layer_name}OpacityStrength", 1.0)
            self.opacityAdd = ScalarParameter(f"{builder.layer_name}OpacityAdd", 0.0)
            self.opacityContrast = ScalarParameter(f"{builder.layer_name}OpacityContrast", 1.0)

    class Builder(MaterialLayerFunctionBuilder):
        def __init__(self, layer_name: str, MF_LandscapeBaseMaterial):
            super().__init__(
                layer_name,
                MF_LandscapeBaseMaterial,
                MaterialFunctionDependenciesBase,
                MLF_LayerX.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)
            pass

        def build(self):
            appendVector = AppendVector(self.inputs.uvParams, self.inputs.uvParams.a)
            appendVector.add_rt()

            call_result = self.MF_LandscapeBaseMaterial.call()
            #print(self.MF_LandscapeBaseMaterial)
            #print(call_result)
            #print(inspect.getmembers(call_result))

            #call_result.output.connectTo(result.a)
            #call_result.height.connectTo(height.a)

            # MaterialFunctions.landscapeBaseMaterial(Params.Dirt)

            # self.inputs.albedo.connectTo(call_result.inputs.albedo)

            # self.inputs.albedo.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.albedo)
            # self.inputs.colorOverlay.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.colorOverlay)
            # self.inputs.colorOverlayIntensity.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.colorOverlayIntensity)
            # self.inputs.contrast.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.contrast)
            # self.inputs.contrastVariation.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.contrastVariation)
            # self.inputs.roughness.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.roughness)
            # self.inputs.roughnessIntensity.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.roughnessIntensity)
            # self.inputs.normalIntensity.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.normalIntensity)
            # self.inputs.normal.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.normal)
            # self.inputs.displacement.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.displacement)
            # self.inputs.uvParams.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.uvParams)
            # self.inputs.rotation.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.rotation)
            # self.inputs.doTextureBomb.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.doTextureBomb)
            # self.inputs.doRotationVariation.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.doRotationVariation)
            # self.inputs.bombCellScale.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.bombCellScale)
            # self.inputs.bombPatternScale.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.bombPatternScale)
            # self.inputs.bombRandomOffset.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.bombRandomOffset)
            # self.inputs.bombRotationVariation.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.bombRotationVariation)
            # self.inputs.opacityStrength.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.opacityStrength)
            # self.inputs.opacityAdd.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.opacityAdd)
            # self.inputs.opacityContrast.connectTo(self.MF_LandscapeBaseMaterial.builder.inputs.opacityContrast)

            call_result.result.connectTo(self.outputs.result)
            call_result.height.connectTo(self.outputs.height)

        # def MLF_Dirt():
        #     return MaterialFunctions.landscapeBaseMaterial(Params.Dirt)

# MLF_LayerX.Builder().get()