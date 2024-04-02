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

class MF_GlancingAngleSpecCorrection:
    class Inputs:
        def __init__(self, builder: MaterialFunctionBuilderBase):
            pass

    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_GlancingAngleSpecCorrection",
                MF_GlancingAngleSpecCorrection.Inputs,
                MaterialFunctionOutputs.Result)

        def build_dependencies(self):
            pass
    
        def build_process_nodes(self):
            pass

        def finalize_node_connections(self):
            pass
