# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_blueprint_creator.py"

import unreal

from unreal import GuidLibrary

MEL = unreal.MaterialEditingLibrary
ATH = unreal.AssetToolsHelpers
AT = ATH.get_asset_tools()
EAL = unreal.EditorAssetLibrary
AUL = unreal.EditorUtilityLibrary

class MaterialAttributeGuids:
    BaseColor = GuidLibrary.parse_string_to_guid("69B8D33616ED4D499AA497292F050F7A")[0]
    SubsurfaceColor = GuidLibrary.parse_string_to_guid("5B8FC67951CE40829D777BEEF4F72C44")[0]
    Metallic = GuidLibrary.parse_string_to_guid("57C3A1617F064296B00B24A5A496F34C")[0]
    Specular = GuidLibrary.parse_string_to_guid("9FDAB39925564CC98CD2D572C12C8FED")[0]
    Roughness = GuidLibrary.parse_string_to_guid("D1DD967C4CAD47D39E6346FB08ECF210")[0]
    ClearCoat = GuidLibrary.parse_string_to_guid("9E502E693C8F48FA94645CFD28E5428D")[0]
    ClearCoatRoughness = GuidLibrary.parse_string_to_guid("BE4F2FFD12FC4296B0124EEA12C28D92")[0]
    Refraction = GuidLibrary.parse_string_to_guid("D0B0FA0314D74455A851BAC581A0788B")[0]
    Opacity = GuidLibrary.parse_string_to_guid("B8F50FBA2A754EC19EF672CFEB27BF51")[0]
    Normal = GuidLibrary.parse_string_to_guid("0FA2821A200F4A4AB719B789C1259C64")[0]
    ClearCoatBottomNormal = GuidLibrary.parse_string_to_guid("AA3D5C0416294716BBDEC8696A27DD72")[0]
    CustomEyeTangent = GuidLibrary.parse_string_to_guid("8EAB2CB273634A248CD14F473F9C8E55")[0]

from pamux_unreal_tools.base.material_expression_container import MaterialExpressionContainer
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
        