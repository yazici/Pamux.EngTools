import unreal

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.builders.material_function_builder import MaterialLayerFunctionBuilder
from pamux_unreal_tools.base.material_function.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.IForestGround import IForestGround

from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MLF_LayerX import MLF_LayerX
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.layer_inputs import LayerInputs
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.layer_build import LayerBuild


class MLF_ForestGround:
    class Inputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            # /Script/Engine.Texture2D'/Game/Megascans/Surfaces/ForestGround/T_ForestGround_RF.T_ForestGround_RF'
            pass

    class Builder(MaterialLayerFunctionBuilder):
        def __init__(self, MF_LandscapeBaseMaterial: MaterialFunctionImpl):
            super().__init__(
                "ForestGround",
                MF_LandscapeBaseMaterial,
                MaterialFunctionDependenciesBase,
                LayerInputs,
                MaterialFunctionOutputs.ResultAndHeight)
            pass

        def build(self):
            call_result = LayerBuild.call_and_connect_LandscapeBaseMaterial(self, True)

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