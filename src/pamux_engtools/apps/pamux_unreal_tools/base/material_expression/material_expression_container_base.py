import unreal

MEL = unreal.MaterialEditingLibrary
EAL = unreal.EditorAssetLibrary

from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos
from pamux_unreal_tools.base.material_expression.material_expression_sockets_base import OutSocket
from pamux_unreal_tools.generated.material_expression_wrappers import NamedRerouteDeclaration

class MaterialExpressionContainerBase:
    # unreal.Material | unreal.MaterialFunction
    def __init__(self,
                 unrealAsset,
                 f_create_material_expression,
                 f_delete_all_material_expression,
                 f_layout_expression,
                 should_recompile: bool = False) -> None:
        self.builder = None
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

    def add_rt(self, name: str, outSocket: OutSocket):
        rt = NamedRerouteDeclaration(name, outSocket)
        rt.material_expression_editor_x.set(outSocket.material_expression.material_expression_editor_x.get() + NodePos.DeltaX)
