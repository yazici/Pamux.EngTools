import unreal

MEL = unreal.MaterialEditingLibrary

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.utils.types import *

from pamux_unreal_tools.base.material_expression_container import MaterialExpressionContainer
from pamux_unreal_tools.impl.in_socket_impl import InSocketImpl
from pamux_unreal_tools.impl.out_socket_impl import OutSocketImpl
class MaterialFunctionBase(MaterialExpressionContainer):
    def __init__(self, unrealAsset: unreal.MaterialFunction):
        super().__init__(unrealAsset,
                         MEL.create_material_expression_in_function,
                         MEL.delete_all_material_expressions_in_function,
                         MEL.layout_material_function_expressions)

        self.virtual_inputs: SocketNames = []
        self.virtual_outputs: SocketNames = []

    def call(self) -> MaterialFunctionCall:
        result = MaterialFunctionCall()
        result.material_function.set(self.unrealAsset)

        for name in self.virtual_inputs:
            inSocket = InSocketImpl(result, name, 'StructProperty')
            exec(f"result.{self.builder.get_field_name(name)} = inSocket", locals())

        for name in self.virtual_outputs:
            outSocket = OutSocketImpl(result, name, 'StructProperty')
            exec(f"result.{self.builder.get_field_name(name)} = outSocket", locals())

        self.call_result = result
        return result
