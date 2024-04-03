
import unreal
import inspect
MEL = unreal.MaterialEditingLibrary

from pamux_unreal_tools.base.material_expression_sockets_base import InSocket, OutSocket

from pamux_unreal_tools.base.material_expression_base import MaterialExpressionBase
from pamux_unreal_tools.utils.node_pos import NodePos

class OutSocketImpl(OutSocket):
    def __init__(self, material_expression: MaterialExpressionBase, name: str, type: str) -> None:
        super().__init__(material_expression, name, type)

    def connectTo(self, param) -> bool:
        if isinstance(param, InSocket):
            return self.__connectToInSocket(param)
        
        if isinstance(param, unreal.MaterialProperty):
            return self.__connectToMaterialProperty(param)

        raise Exception("Don't know how to call connectTo for type: " + str(param))
    
    def __connectToInSocket(self, inSocket: InSocket) -> bool:
        self.material_expression.material_expression_editor_x.set(inSocket.material_expression.material_expression_editor_x.get() - NodePos.DeltaX)
        return MEL.connect_material_expressions(self.material_expression.unrealAsset, self.name, inSocket.material_expression.unrealAsset, inSocket.name)
    
    def __connectToMaterialProperty(self, materialProperty: unreal.MaterialProperty) -> bool:
        return MEL.connect_material_property(self.material_expression.unrealAsset, self.name, materialProperty)

    def connectToFunctionOutput(self, function_output) -> bool:
        self.material_expression.material_expression_editor_x.set(function_output.material_expression_editor_x.get() - NodePos.DeltaX)
        return MEL.connect_material_expressions(self.material_expression.unrealAsset, self.name, function_output.unrealAsset, "")

    def add_rt(self):
        frame = inspect.currentframe()
        frame = inspect.getouterframes(frame)[1]
        string = inspect.getframeinfo(frame[0]).code_context[0].strip()
        if not string.endswith(".add_rt()"):
            raise Exception("Cannot find string ending with .add_rt() in call stack to set the name of the reroute")

        parts = string[0:-len(".add_rt()")].split(".")
        name = "rt"
        for part in parts:
            name += part[0:1].upper() + part[1:]

        return self.material_expression.container.add_rt(name, self)
