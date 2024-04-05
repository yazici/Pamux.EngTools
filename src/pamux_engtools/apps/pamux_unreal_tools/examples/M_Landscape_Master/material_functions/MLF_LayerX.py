from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.builders.material_function_builder import MaterialLayerFunctionBuilder
from pamux_unreal_tools.base.material_function.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.ILayerX import ILayerX
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.layer_inputs import LayerInputs
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.layer_build import LayerBuild

class MLF_LayerX:
    class Inputs(LayerInputs):
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            super().__init__(builder, "R")

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
            call = LayerBuild.call_and_connect_LandscapeBaseMaterial(self)

            call.outputs.result.connectTo(self.outputs.result)
