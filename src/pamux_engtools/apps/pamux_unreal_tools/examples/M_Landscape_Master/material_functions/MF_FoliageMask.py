import unreal
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent.parent.parent.resolve()))

from importlib import * 

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)

from pamux_unreal_tools.builders.material_function_builder import MaterialFunctionBuilder
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.IFoliageMask import IFoliageMask
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory

class MF_FoliageMask:
    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            # No Preview
            self.layerSample    = builder.build_FunctionInput("LayerSample",    0, 0.0, False) 
            self.foliageMask    = builder.build_FunctionInput("FoliageMask",    1, 0.0, False)
            self.threshold      = builder.build_FunctionInput("Threshold",      2, 0.0, False)
            self.enabled        = builder.build_FunctionInput("Enabled",        3, True)

    class Builder(MaterialFunctionBuilder):
        def __init__(self):
            super().__init__(
                MaterialFunctionFactory(),
                "/Game/Materials/Pamux/Landscape/Functions/MF_FoliageMask",
                MaterialFunctionDependenciesBase,
                MF_FoliageMask.Inputs,
                MaterialFunctionOutputs.Result)

        def build(self):
            divide = Divide(self.inputs.layerSample.rt, self.inputs.threshold.rt)
            floor = Floor(divide.output)
            lerp = LinearInterpolate(0.0, self.inputs.layerSample.rt, floor)
            subtract = Subtract(lerp.output, self.inputs.foliageMask.rt)
            saturate = Saturate(subtract.output)

            switch = StaticSwitch(saturate, Constant(0.0), self.inputs.enabled.rt)

            switch.output.connectTo(self.outputs.Result)

# MF_FoliageMask.Builder().get()
