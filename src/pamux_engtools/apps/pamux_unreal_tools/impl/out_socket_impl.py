
import unreal
import inspect
MEL = unreal.MaterialEditingLibrary

from pamux_unreal_tools.base.material_expression_sockets_base import InSocket, OutSocket

from pamux_unreal_tools.base.material_expression_base import MaterialExpressionBase
from pamux_unreal_tools.utils.node_pos import NodePos

class OutSocketImpl(OutSocket):
    def __init__(self, material_expression: MaterialExpressionBase, name: str, type: str) -> None:
        super().__init__(material_expression, name, type)

    # def connectTo(self, param1, param2 = None, param3 = None) -> bool:
    #     if isinstance(param1, unreal.MaterialProperty):
    #         return self.__connectTo_MaterialProperty(param1)
        
    #     if isinstance(param1, str) and param1 is not None and isinstance(param2, MaterialExpressionBase) and isinstance(param3, str) and param3 is not None:
    #         return self.__comesFrom_MaterialExpressionBase(param1, param2, param3)

    #     raise Exception(f"Don't know how to call connectTo for type[s]: {str(param1)}, {str(param2)}")
    

    # def __connectTo_MaterialProperty(self, materialProperty: unreal.MaterialProperty) -> bool:
    #     return MEL.connect_material_property(self.unrealAsset, "", materialProperty)

    # def __comesFrom_MaterialExpressionBase(self, outPortName: str, material_expression: MaterialExpressionBase, inPortName: str) -> bool:
    #     return MEL.connect_material_expressions(self.unrealAsset, outPortName, material_expression.unrealAsset, inPortName)

    # @dispatch(MaterialExpressionBase, str)
    # def connectTo(self, OutSocket) -> bool:
    #     return MEL.connect_material_expressions(self.unrealAsset, "", materialExpression.unrealAsset, inPortName)

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
        requiredLineEnding = ".add_rt()"
        for frame in inspect.getouterframes(inspect.currentframe()):
            for line in frame.code_context:
                line = line.strip()
                if not line.endswith(requiredLineEnding):
                    continue
                if line == "return self.output.add_rt()":
                    continue

                line = line[0:-len(requiredLineEnding)]

                if line.startswith("self."):
                    line = line[len("self."):]

                name = "rt"
                if "." in line:
                    parts = line.split(".")
                    isFirst = True
                    for part in parts:
                        if isFirst:
                            isFirst = False
                        else:
                            name += "."
                        name += part[0:1].upper() + part[1:]
                else:
                    name += line[0:1].upper() + line[1:] + ".Output"

                return self.material_expression.container.add_rt(name, self)

        raise Exception(f"Cannot find string ending with .add_rt() in call stack to set the name of the reroute")
