# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_blueprint_creator.py"

import unreal

MEL = unreal.MaterialEditingLibrary
ATH = unreal.AssetToolsHelpers
AT = ATH.get_asset_tools()
EAL = unreal.EditorAssetLibrary
AUL = unreal.EditorUtilityLibrary

from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.utils.build_stack import NodePos

# https://docs.unrealengine.com/5.3/en-US/PythonAPI/class/MaterialEditingLibrary.html

class MaterialFunction(MaterialExpressionContainer):
    def __init__(self, asset: unreal.MaterialFunction):
        super().__init__(asset,
                         MEL.create_material_expression_in_function,
                         MEL.delete_all_material_expressions_in_function,
                         MEL.layout_material_function_expressions)

class MaterialFunctionFactory(MaterialExpressionContainerFactory):
    def load(self, asset_name, package_path, deleteAllMaterialExpressions = False):
        asset = EAL.load_asset(f"{package_path}/{asset_name}")
        if asset is None:
            raise f"Can't load asset: {package_path}/{asset_name}"
            
        result = MaterialFunction(asset)
        if deleteAllMaterialExpressions:
            result.deleteAllMaterialExpressions()
        return result

    def create(self, asset_name, package_path):
        return MaterialFunction(AT.create_asset(asset_name, package_path, unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew()))
