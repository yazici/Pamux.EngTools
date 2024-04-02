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
from pamux_unreal_tools.material_function import MaterialFunctionFactory

class MF_FoliageMask:
    class Inputs:
        def __init__(self, builder: MaterialFunctionBuilderBase):
            self.layerSample = builder.build_FunctionInput("LayerSample", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR)
            self.foliageMask = builder.build_FunctionInput("FoliageMask", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR)
            self.threshold = builder.build_FunctionInput("Threshold", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR)
            self.enabled = builder.build_FunctionInput("Enabled", unreal.FunctionInputType.FUNCTION_INPUT_STATIC_BOOL, StaticBool(True))


    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_FoliageMask",
                MF_FoliageMask.Inputs,
                MaterialFunctionOutputs.Result)

        def build_process_nodes(self):
            pass

        def finalize_node_connections(self):
            pass
