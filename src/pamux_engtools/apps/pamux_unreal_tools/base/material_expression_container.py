# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_blueprint_creator.py"

import unreal

from multipledispatch import dispatch
from pamux_unreal_tools.utils.build_stack import *

MEL = unreal.MaterialEditingLibrary
ATH = unreal.AssetToolsHelpers
AT = ATH.get_asset_tools()
EAL = unreal.EditorAssetLibrary
AUL = unreal.EditorUtilityLibrary

from pamux_unreal_tools.utils.pamux_asset_utils import PamuxAssetUtils
# from pamux_unreal_tools.generated.material_expression_wrappers import NamedRerouteDeclaration
from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos
# Assertion failed: Outputs.Num() == AttributeGetTypes.Num() + 1 [File:D:\build\++UE5\Sync\Engine\Source\Runtime\Engine\Private\Materials\MaterialExpressions.cpp] [Line: 7213]

# https://docs.unrealengine.com/5.3/en-US/PythonAPI/class/MaterialEditingLibrary.html
class MaterialExpressionContainer:
    # unreal.Material | unreal.MaterialFunction
    def __init__(self, unrealAsset, f_create_material_expression, f_delete_all_material_expression, f_layout_expression, should_recompile: bool = False) -> None:
        self.unrealAsset: unreal.Material | unreal.MaterialFunction = unrealAsset
        self.f_create_material_expression = f_create_material_expression
        self.f_delete_all_material_expression = f_delete_all_material_expression
        self.f_layout_expression = f_layout_expression
        self.should_recompile = should_recompile

    def deleteAllMaterialExpressions(self) -> None:
        self.f_delete_all_material_expression(self.unrealAsset)

    def createMaterialExpression(self, expression_class: unreal.Class, node_pos: NodePos = None) -> unreal.MaterialExpression:
        if node_pos is None:
            node_pos = CurrentNodePos
        return self.f_create_material_expression(self.unrealAsset, expression_class, node_pos.x, node_pos.y)

    def save(self) -> None:
        # self.f_layout_expression(self.unrealAsset)
        if self.should_recompile:
            MEL.recompile_material(self.unrealAsset)
        EAL.save_loaded_asset(self.unrealAsset, False)

    def getDefaultScalarParameterValue(self, parameter_name: str) -> float:
        return MEL.get_material_default_scalar_parameter_value(self.unrealAsset, parameter_name)
    
    def getDefaultStaticSwitchParameterValue(self, parameter_name: str) -> bool:
        return MEL.get_material_default_static_switch_parameter_value(self.unrealAsset, parameter_name)
    
    def getDefaultTextureParameterValue(self, parameter_name: str) -> unreal.Texture:
        return MEL.get_material_default_texture_parameter_value(self.unrealAsset, parameter_name)

