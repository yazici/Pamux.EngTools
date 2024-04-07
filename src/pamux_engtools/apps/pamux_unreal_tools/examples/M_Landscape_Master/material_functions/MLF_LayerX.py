from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.builders.material_function_builder import MaterialLayerFunctionBuilder
from pamux_unreal_tools.base.material_function.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.ILayerX import ILayerX
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.layer_inputs import LayerInputs
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.layer_build import LayerBuild
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_LandscapeBaseMaterial import MF_LandscapeBaseMaterial

class MLF_LayerX:
    @staticmethod
    def load_MF(builder, layer_name):
        return  builder.load_MF(f"/Game/Materials/Pamux/Landscape/Functions/Layers/MLF_{layer_name}",
                                LayerInputs.get(layer_name),
                                ["Result", "Height"])


    class Dependencies:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial.load_MF(builder)

    class Inputs(LayerInputs):
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            super().__init__(builder, "R")

    class Builder(MaterialLayerFunctionBuilder):
        def __init__(self, layer_name: str):
            super().__init__(
                layer_name,
                MLF_LayerX.Dependencies,
                MLF_LayerX.Inputs,
                MaterialFunctionOutputs.ResultAndHeight)
            pass

        def build(self):
            call = LayerBuild.call_and_connect_LandscapeBaseMaterial(self)
            call.outputs.result.connectTo(self.outputs.result)
