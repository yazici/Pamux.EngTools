import unreal
EAL = unreal.EditorAssetLibrary
ATH = unreal.AssetToolsHelpers
AT = ATH.get_asset_tools()

from pamux_unreal_tools.generated.material_expression_wrappers import NamedRerouteDeclaration

from pamux_unreal_tools.base.material_base import MaterialBase
from pamux_unreal_tools.base.material_function_base import MaterialFunctionBase
from pamux_unreal_tools.base.material_expression_container import MaterialExpressionContainer

from pamux_unreal_tools.utils.build_stack import BuildStack
from pamux_unreal_tools.utils.pamux_asset_utils import PamuxAssetUtils
from pamux_unreal_tools.utils.types import *

# Assertion failed: Outputs.Num() == AttributeGetTypes.Num() + 1 [File:D:\build\++UE5\Sync\Engine\Source\Runtime\Engine\Private\Materials\MaterialExpressions.cpp] [Line: 7213]

class MaterialExpressionContainerFactory:
    # container_wrapper_class: type[MaterialBase | MaterialFunctionBase]
    def __init__(self, asset_class: unreal.Class, asset_factory: unreal.Factory, container_wrapper_class) -> None:
        self.asset_class = asset_class
        self.asset_factory = asset_factory
        self.container_wrapper_class = container_wrapper_class

    #  -> MaterialBase | MaterialFunctionBase
    def load(self, builder, container_path: str, virtual_inputs: SocketNames, virtual_outputs: SocketNames) -> MaterialExpressionContainer:
        return self.__load_wrapped_asset(builder, container_path, virtual_inputs, virtual_outputs)

    #  -> MaterialBase | MaterialFunctionBase
    def loadAndClean(self, builder, container_path, virtual_inputs: SocketNames, virtual_outputs: SocketNames) -> MaterialExpressionContainer:
        result = self.__load_wrapped_asset(builder, container_path, virtual_inputs, virtual_outputs)
        result.deleteAllMaterialExpressions()
        return result

    #  -> MaterialBase | MaterialFunctionBase
    def loadAndCleanOrCreate(self, builder, container_path, virtual_inputs: SocketNames, virtual_outputs: SocketNames) -> MaterialExpressionContainer:
        try:
            return self.loadAndClean(builder, container_path, virtual_inputs, virtual_outputs)
        except:
            return self.__create_wrapped_asset(builder, container_path, virtual_inputs, virtual_outputs)

    #  -> MaterialBase | MaterialFunctionBase
    def __load_wrapped_asset(self, builder, asset_path: str, virtual_inputs: SocketNames, virtual_outputs: SocketNames) -> MaterialExpressionContainer:
        result = self.__load_and_wrap_asset(asset_path)
        result.builder = builder
        result.virtual_inputs = virtual_inputs
        result.virtual_outputs = virtual_outputs
        return result

    #  -> MaterialBase | MaterialFunctionBase
    def __create_wrapped_asset(self, builder, asset_path: str, virtual_inputs: SocketNames, virtual_outputs: SocketNames) -> MaterialExpressionContainer:
        result = self.__create_and_wrap_asset(asset_path)
        result.builder = builder
        result.virtual_inputs = virtual_inputs
        result.virtual_outputs = virtual_outputs
        return result

    #  -> MaterialBase | MaterialFunctionBase
    def __load_and_wrap_asset(self, asset_path: str) -> MaterialExpressionContainer:
        unrealAsset = EAL.load_asset(asset_path)
        if unrealAsset is None:
            raise Exception(f"Can't load asset: {asset_path}")
        return self.container_wrapper_class(unrealAsset)

    #  -> MaterialBase | MaterialFunctionBase
    def __create_and_wrap_asset(self, asset_path: str) -> MaterialExpressionContainer:
        package_path, asset_name = PamuxAssetUtils.split_asset_path(asset_path)
        
        unrealAsset = AT.create_asset(asset_name, package_path, self.asset_class, self.asset_factory)
        if unrealAsset is None:
            raise Exception(f"Can't create asset: {asset_path}")
        return self.container_wrapper_class(unrealAsset)

# class MaterialExpressionValue:
#     def __init__(self, materialExpression, name, type):
#         self.materialExpression = materialExpression
#         self.name = name
#         self.type = type

# class Property(MaterialExpressionValue):
#     def __init__(self, material_expression, name, type):
#         super().__init__(material_expression, name, type)

#     def set(self, val):
#         self.materialExpression.unrealAsset.set_editor_property(self.name, val)

#     def get(self):
#         return self.materialExpression.unrealAsset.get_editor_property(self.name)
