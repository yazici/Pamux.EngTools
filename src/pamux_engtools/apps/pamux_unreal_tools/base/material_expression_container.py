# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_blueprint_creator.py"

import unreal

from multipledispatch import dispatch
from collections import deque

MEL = unreal.MaterialEditingLibrary
ATH = unreal.AssetToolsHelpers
AT = ATH.get_asset_tools()
EAL = unreal.EditorAssetLibrary
AUL = unreal.EditorUtilityLibrary

# Assertion failed: Outputs.Num() == AttributeGetTypes.Num() + 1 [File:D:\build\++UE5\Sync\Engine\Source\Runtime\Engine\Private\Materials\MaterialExpressions.cpp] [Line: 7213]

# https://docs.unrealengine.com/5.3/en-US/PythonAPI/class/MaterialEditingLibrary.html
class MaterialExpressionContainer:
    def __init__(self, asset):
        self.asset = asset
        
    def createMaterialExpression(self, expression_class, node_pos_x = 0, node_pos_y = 0):
        raise "implement createMaterialExpression"


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