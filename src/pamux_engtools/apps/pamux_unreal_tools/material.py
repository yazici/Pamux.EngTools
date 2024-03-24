# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_blueprint_creator.py"

import unreal

MEL = unreal.MaterialEditingLibrary
ATH = unreal.AssetToolsHelpers
AT = ATH.get_asset_tools()
EAL = unreal.EditorAssetLibrary
AUL = unreal.EditorUtilityLibrary

from pamux_unreal_tools.material_expression_container import MaterialExpressionContainer
# https://docs.unrealengine.com/5.3/en-US/PythonAPI/class/MaterialEditingLibrary.html
class Material(MaterialExpressionContainer):
    def __init__(self, asset: unreal.Material):
        super().__init__(asset)

    @staticmethod
    def load(asset_name, package_path, deleteAllMaterialExpressions = False):
        asset = EAL.load_asset(f"{package_path}/{asset_name}")
        if asset is None:
            raise f"Can't load material: {package_path}/{asset_name}"

        result = Material(asset)
        if deleteAllMaterialExpressions:
            result.deleteAllMaterialExpressions()
        return result
    
    @staticmethod
    def create(asset_name, package_path):
        return Material(AT.create_asset(asset_name, package_path, unreal.Material, unreal.MaterialFactoryNew()))

    @staticmethod
    def loadOrCreate(asset_name, package_path, deleteAllMaterialExpressions = False):
        try:
            return Material.load(asset_name, package_path, deleteAllMaterialExpressions)
        except:
            return Material.create(asset_name, package_path)

    def deleteAllMaterialExpressions(self):
        MEL.delete_all_material_expressions(self.asset)

    def createMaterialExpression(self, expression_class, node_pos_x = 0, node_pos_y = 0):
        return MEL.create_material_expression(self.asset, expression_class, node_pos_x, node_pos_y)

    def save(self):
        MEL.layout_material_expressions(self.asset)
        MEL.recompile_material(self.asset)
        EAL.save_loaded_asset(self.asset, False)

    def getDefaultScalarParameterValue(self, parameterName):
        return MEL.get_material_default_scalar_parameter_value(self.asset, parameterName)
    
    def getDefaultStaticSwitchParameterValue(self, parameterName):
        return MEL.get_material_default_static_switch_parameter_value(self.asset, parameterName)
    
    def getDefaultTextureParameterValue(self, parameterName):
        return MEL.get_material_default_texture_parameter_value(self.asset, parameterName)
        