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

from pamux_unreal_tools.base.material_function_builder_base import *

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase

from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.wetness_base import WetnessBuilderBase
from pamux_unreal_tools.factories.material_expression_factories import *
from pamux_unreal_tools.base.material_expression_sockets_base import OutSocket

class MF_Wetness:
    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            self.materialAttributes = builder.getMaterialAttributes()
            self.materialAttributes.add_rt()

            self.wetnessSaturation = ScalarParameter("Wetness Saturation", -0.5)
            self.wetnessSaturation.add_rt()

            self.wetnessDarken = ScalarParameter("Wetness Darken", 0.5)
            self.wetnessDarken.add_rt()

            self.wetnessRoughness = ScalarParameter("Wetness Roughness", 0.3)
            self.wetnessRoughness.add_rt()

            self.wetness = builder.build_FunctionInput("Wetness", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(1.0))
            self.wetness.add_rt()

    class Builder(WetnessBuilderBase):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_Wetness",
                MaterialFunctionDependenciesBase,
                MF_Wetness.Inputs,
                MaterialFunctionOutputs.Result)

        def build(self):
            breakMaterialAttributes = BreakMaterialAttributes(self.inputs.materialAttributes)
            breakMaterialAttributes.baseColor.add_rt()

            desaturation = Desaturation()
            desaturation.input.comesFrom(breakMaterialAttributes.baseColor)
            desaturation.fraction.comesFrom(self.inputs.wetnessSaturation)

            saturate1 = Saturate(desaturation)

            multiply1 = Multiply(saturate1, self.inputs.wetnessDarken)

            makeMaterialAttributes = MakeMaterialAttributesFactory.create(breakMaterialAttributes)
            makeMaterialAttributes.baseColor.comesFrom(multiply1)
            makeMaterialAttributes.roughness.comesFrom(self.inputs.wetnessRoughness)

            breakMaterialAttributes = BreakMaterialAttributes(makeMaterialAttributes)

            subtract = Subtract(breakMaterialAttributes.opacity, Constant(1.0))
            multiply2 = Multiply(self.inputs.wetness, 2.0)
            add = Add(subtract, multiply2)
            saturate2 = Saturate(add)

            blend = BlendMaterialAttributes(self.inputs.materialAttributes, makeMaterialAttributes.output, saturate2)

            blend.connectTo(self.outputs.result)
               
        
            

#MF_Wetness.Builder().get()
