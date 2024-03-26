# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_blueprint_creator.py"

import unreal

from multipledispatch import dispatch
from pamux_unreal_tools.utils.build_stack import *

MEL = unreal.MaterialEditingLibrary
ATH = unreal.AssetToolsHelpers
AT = ATH.get_asset_tools()
EAL = unreal.EditorAssetLibrary
AUL = unreal.EditorUtilityLibrary

# Assertion failed: Outputs.Num() == AttributeGetTypes.Num() + 1 [File:D:\build\++UE5\Sync\Engine\Source\Runtime\Engine\Private\Materials\MaterialExpressions.cpp] [Line: 7213]

# https://docs.unrealengine.com/5.3/en-US/PythonAPI/class/MaterialEditingLibrary.html
class MaterialExpressionContainer:
    def __init__(self, asset, f_create_material_expression, f_delete_all_material_expression, f_layout_expression, should_recompile = False):
        self.asset = asset
        self.f_create_material_expression = f_create_material_expression
        self.f_delete_all_material_expression = f_delete_all_material_expression
        self.f_layout_expression = f_layout_expression
        self.should_recompile = should_recompile

    def deleteAllMaterialExpressions(self):
        self.f_delete_all_material_expression(self.asset)

    def createMaterialExpression(self, expression_class, node_pos: NodePos = None):
        if node_pos is None:
            node_pos = CurrentNodePos
        return self.f_create_material_expression(self.asset, expression_class, node_pos.x, node_pos.y)

    def save(self):
        self.f_layout_expression(self.asset)
        if self.should_recompile:
            MEL.recompile_material(self.asset)
        EAL.save_loaded_asset(self.asset, False)

    def getDefaultScalarParameterValue(self, parameterName):
        return MEL.get_material_default_scalar_parameter_value(self.asset, parameterName)
    
    def getDefaultStaticSwitchParameterValue(self, parameterName):
        return MEL.get_material_default_static_switch_parameter_value(self.asset, parameterName)
    
    def getDefaultTextureParameterValue(self, parameterName):
        return MEL.get_material_default_texture_parameter_value(self.asset, parameterName)

class MaterialExpressionContainerFactory:
    def load(self, asset_name, package_path, deleteAllMaterialExpressions = False):
        raise "implement load"
    
    def create(self, asset_name, package_path):
        raise "implement create"
    
    def loadOrCreate(self, asset_name, package_path, deleteAllMaterialExpressions = False):
        try:
            return self.load(asset_name, package_path, deleteAllMaterialExpressions)
        except:
            return self.create(asset_name, package_path)
    
class MaterialExpressionValue:
    def __init__(self, materialExpression, name, type):
        self.materialExpression = materialExpression
        self.name = name
        self.type = type

class Property(MaterialExpressionValue):
    def __init__(self, materialExpression, name, type):
        super().__init__(materialExpression, name, type)

    def set(self, val):
        self.materialExpression.asset.set_editor_property(self.name, val)

    def get(self):
        return self.materialExpression.asset.get_editor_property(self.name)

class Socket(MaterialExpressionValue):
    def __init__(self, materialExpression, name, type, is_output = False):
        super().__init__(materialExpression, name, type)
        self.is_output = is_output

class InSocket(Socket):
    def __init__(self, materialExpression, name, type):
        super().__init__(materialExpression, name, type, False)

    def comesFrom(self, source) -> bool:
        if isinstance(source, Socket):
            return MEL.connect_material_expressions(source.materialExpression.asset, source.name, self.materialExpression.asset, self.name)
        else:    
            return MEL.connect_material_expressions(source.asset, "", self.materialExpression.asset, self.name)

class OutSocket(Socket):
    def __init__(self, materialExpression, name, type):
        super().__init__(materialExpression, name, type, True)

    @dispatch(InSocket)
    def connectTo(self, inSocket: InSocket) -> bool:
        return MEL.connect_material_expressions(self.materialExpression.asset, self.name, inSocket.materialExpression.asset, inSocket.name)
    
    @dispatch(unreal.MaterialProperty)
    def connectTo(self, materialProperty: unreal.MaterialProperty) -> bool:
        return MEL.connect_material_property(self.materialExpression.asset, self.name, materialProperty)

    def connectToFunctionOutput(self, function_output) -> bool:
        return MEL.connect_material_expressions(self.materialExpression.asset, self.name, function_output.asset, function_output.output_name.get())