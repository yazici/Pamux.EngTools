import unreal
from multipledispatch import dispatch
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.utils.build_stack import BuildStack
from pamux_unreal_tools.utils.build_stack import NodePos

# in cmd: "C:\Program Files\Epic Games\UE_5.3\Engine\Binaries\ThirdParty\Python3\Win64\python.exe" -m pip install multipledispatch

BPFactory = unreal.BlueprintFactory()
AT = unreal.AssetToolsHelpers.get_asset_tools()
EAL = unreal.EditorAssetLibrary
EUL = unreal.EditorUtilityLibrary # https://docs.unrealengine.com/4.27/en-US/PythonAPI/class/EditorUtilityLibrary.html
MEL = unreal.MaterialEditingLibrary

# EUL.get_selected_assets()
# EUL.get_selected_blueprint_classes()

class MaterialExpressionBase:
    def __init__(self, expression_class, node_pos: NodePos = None):
        print("top")
        print(BuildStack.top())
        self.parent = BuildStack.top()
        self.expression_class = expression_class

        print(expression_class)

        self.asset = self.parent.createMaterialExpression(self.expression_class, node_pos)

class MaterialExpression(MaterialExpressionBase):
    def __init__(self, expression_class, node_pos: NodePos = None):
        super().__init__(expression_class, node_pos)

    @dispatch(unreal.MaterialProperty)
    def connectTo(self, materialProperty: unreal.MaterialProperty) -> bool:
        return MEL.connect_material_property(self.asset, "", materialProperty)

    @dispatch(str, MaterialExpressionBase, str)
    def connectTo(self, outPortName: str, materialExpression: MaterialExpressionBase, inPortName: str) -> bool:
        return MEL.connect_material_expressions(self.asset, outPortName, materialExpression.asset, inPortName)
    
    # @dispatch(MaterialExpressionBase, str)
    # def connectTo(self, OutSocket) -> bool:
    #     return MEL.connect_material_expressions(self.asset, "", materialExpression.asset, inPortName)
