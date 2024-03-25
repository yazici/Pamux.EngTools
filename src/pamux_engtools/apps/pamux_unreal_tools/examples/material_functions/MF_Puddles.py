from pamux_unreal_tools.material_function import MaterialFunction

from pamux_engtools.apps.pamux_unreal_tools.material_function_builder_base import MaterialFunctionBuilderBase
from pamux_unreal_tools.material import Material
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_engtools.apps.pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_engtools.apps.pamux_unreal_tools.material_expression_container import *
from pamux_unreal_tools.material_script_helpers import *

class MF_Puddles:
    @staticmethod
    def build():
        return MF_FoliageMask.Builder().get()
    
    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__("MF_Puddles")

        def build(self, material_function: MaterialFunction):
            pass