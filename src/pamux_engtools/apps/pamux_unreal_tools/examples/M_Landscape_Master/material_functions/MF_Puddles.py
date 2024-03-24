from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.material_function_builder_base import MaterialFunctionBuilderBase
from pamux_unreal_tools.material import Material
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.material_expressions.material_expression_wrappers import *
from pamux_unreal_tools.material_expression_container import *
from pamux_unreal_tools.material_script_helpers import *

class MF_Puddles:
    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__("MF_Puddles")

        def build(self, material_function: MaterialFunction):
            pass