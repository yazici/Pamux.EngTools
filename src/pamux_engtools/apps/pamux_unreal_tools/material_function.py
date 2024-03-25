# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_blueprint_creator.py"

import unreal

MEL = unreal.MaterialEditingLibrary
ATH = unreal.AssetToolsHelpers
AT = ATH.get_asset_tools()
EAL = unreal.EditorAssetLibrary
AUL = unreal.EditorUtilityLibrary
from pamux_engtools.apps.pamux_unreal_tools.material_expression_container import MaterialExpressionContainer
# https://docs.unrealengine.com/5.3/en-US/PythonAPI/class/MaterialEditingLibrary.html
class MaterialFunction(MaterialExpressionContainer):
    def __init__(self, asset: unreal.MaterialFunction):
        super().__init__(asset)

    @staticmethod
    def load(asset_name, package_path, deleteAllMaterialExpressions = False):
        asset = EAL.load_asset(f"{package_path}/{asset_name}")
        if asset is None:
            raise f"Can't load material function: {package_path}/{asset_name}"
            
        result = MaterialFunction(asset)
        if deleteAllMaterialExpressions:
            result.deleteAllMaterialExpressions()
        return result
    
    @staticmethod
    def create(asset_name, package_path):
        return MaterialFunction(AT.create_asset(asset_name, package_path, unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew()))

    @staticmethod
    def loadOrCreate(asset_name, package_path, deleteAllMaterialExpressions = False):
        try:
            return MaterialFunction.load(asset_name, package_path, deleteAllMaterialExpressions)
        except:
            return MaterialFunction.create(asset_name, package_path)
        
    def deleteAllMaterialExpressions(self):
        MEL.delete_all_material_expressions_in_function(self.asset)

    def createMaterialExpression(self, expression_class, node_pos_x = 0, node_pos_y = 0):
        return MEL.create_material_expression_in_function(self.asset, expression_class, node_pos_x, node_pos_y)


    def save(self):
        MEL.layout_material_function_expressions(self.asset)
        EAL.save_loaded_asset(self.asset, False)