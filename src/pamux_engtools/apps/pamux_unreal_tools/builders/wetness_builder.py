

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.utils.texture_sample_set import TMaterialTextures
from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.builders.material_function_builder import MaterialFunctionBuilder

class WetnessBuilder(MaterialFunctionBuilder):
    def __init__(self, container_path: str, dependencies_class, inputs_class, outputs_class = MaterialFunctionOutputs.Result):
        super().__init__(container_path, dependencies_class, inputs_class, outputs_class)

        self.textureSampleSet = TMaterialTextures("GrassyLayer_A", "GrassyLayer_R", "GrassyLayer_D", "GrassyLayer_N")