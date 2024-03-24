# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_blueprint_creator.py"

import unreal

from multipledispatch import dispatch
from pamux_unreal_tools.material_function import MaterialFunction
from pamux_unreal_tools.material_expressions.material_expression_wrappers import *

MEL = unreal.MaterialEditingLibrary
ATH = unreal.AssetToolsHelpers
AT = ATH.get_asset_tools()
EAL = unreal.EditorAssetLibrary
AUL = unreal.EditorUtilityLibrary

def callMaterialFunction(container: MaterialExpressionContainer, materialFunction: MaterialFunction):
    call = MaterialFunctionCall(container)
    call.material_function.set(materialFunction.asset)
    return call