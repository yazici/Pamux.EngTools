# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_blueprint_creator.py"

import unreal

MEL = unreal.MaterialEditingLibrary
ATH = unreal.AssetToolsHelpers
AT = ATH.get_asset_tools()
EAL = unreal.EditorAssetLibrary
AUL = unreal.EditorUtilityLibrary

from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.utils.build_stack import NodePos
from pamux_unreal_tools.generated.material_expression_wrappers import *
# https://docs.unrealengine.com/5.3/en-US/PythonAPI/class/MaterialEditingLibrary.html

class MaterialFunction(MaterialExpressionContainer):
    def __init__(self, asset: unreal.MaterialFunction):
        super().__init__(asset,
                         MEL.create_material_expression_in_function,
                         MEL.delete_all_material_expressions_in_function,
                         MEL.layout_material_function_expressions)


    def call(self) -> MaterialFunctionCall:
        result = MaterialFunctionCall()
        result.material_function.set(self.asset)

        for name in self.virtual_inputs:
            inSocket = InSocket(result, name, 'StructProperty')
            exec(f"result.{self.builder.get_field_name(name)} = inSocket", locals())

        for name in self.virtual_outputs:
            outSocket = OutSocket(result, name, 'StructProperty')
            exec(f"result.{self.builder.get_field_name(name)} = outSocket", locals())

        self.call_result = result
        return result

class MaterialFunctionFactory(MaterialExpressionContainerFactory):
    def __init__(self):
        super().__init__(unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew(), MaterialFunction)
