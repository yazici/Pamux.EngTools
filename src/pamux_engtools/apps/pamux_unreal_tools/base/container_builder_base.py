from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import InSocket, OutSocket
from pamux_unreal_tools.material_expression_factories import *

from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.utils.build_stack import BuildStack
from pamux_unreal_tools.material_function import MaterialFunction, MaterialFunctionFactory
from pamux_unreal_tools.utils.pamux_asset_utils import PamuxAssetUtils

class ContainerBuilderBase:
    def __init__(self,
                 container_factory: MaterialExpressionContainerFactory,
                 params_factory,
                 container_path: str,
                 inputs_class = None,
                 outputs_class = None):

        self.container_factory = container_factory
        self.params_factory = params_factory
        self.container_path = container_path
        self.inputs_class = inputs_class
        self.outputs_class = outputs_class

        self.material_function_factory = MaterialFunctionFactory()

    def load_MF(self, function_path, virtual_inputs, virtual_outputs) -> MaterialFunction:
        return self.material_function_factory.load(self, function_path, virtual_inputs, virtual_outputs)

    def build_dependencies(self):
        pass

    def build_input_nodes(self):
        self.inputs = self.inputs_class(self)

    def build_process_nodes(self):
        pass

    def build_output_nodes(self):
        self.outputs = self.outputs_class(self)

    def finalize_node_connections(self):
        pass

    def build_FunctionInput(self, input_name, input_type, preview = None) -> FunctionInput:
        result = FunctionInputFactory.create(input_name, input_type, preview)
        result.use_preview_value_as_default.set(True)

        CurrentNodePos.x += NodePos.DeltaX
        result.rt = NamedRerouteDeclaration(f"rt{input_name}", result)

        CurrentNodePos.x = 0
        CurrentNodePos.y += NodePos.DeltaY

        return result

    def __loadAndCleanOrCreate(self, virtual_inputs, virtual_outputs):
        result = self.container_factory.loadAndCleanOrCreate(self, self.container_path, virtual_inputs, virtual_outputs)
        BuildStack.push(result)
        print("pushed")

        if self.params_factory is None:
            self.params = None
        else:
            self.params = self.params_factory(result)
        return result

    def get(self, virtual_inputs = [], virtual_outputs = []):
        result = self.__loadAndCleanOrCreate(virtual_inputs, virtual_outputs)
        self.build_dependencies()

        CurrentNodePos.goto_inputs()
        self.build_input_nodes()

        CurrentNodePos.goto_process()
        self.build_process_nodes()

        CurrentNodePos.goto_outputs()
        self.build_output_nodes()

        self.finalize_node_connections()
        result.save()

        BuildStack.pop()
        print("popped")
        return result

    @property
    def current_container(self):
        return BuildStack.top()
    
    def get_field_name(self, name):
        if name == "X-Axis":
            return "xAxis"
        if name == "Y-Axis":
            return "yAxis"
        if name == "Z-Axis":
            return "zAxis"
        _name = name.replace(" ", "")
        return _name[0].lower() + _name[1:]

    # def callMaterialFunction(self, materialFunctionToCall: MaterialFunction, virtual_inputs, virtual_outputs) -> MaterialFunctionCall:
    #     result = MaterialFunctionCall()
    #     result.material_function.set(materialFunctionToCall.asset)

    #     for name in materialFunctionToCall.virtual_inputs:
    #         inSocket = InSocket(result, name, 'StructProperty')
    #         exec(f"result.{self.__get_field_name(name)} = inSocket", locals())

    #     for name in materialFunctionToCall.virtual_outputs:
    #         outSocket = OutSocket(result, name, 'StructProperty')
    #         exec(f"result.{self.__get_field_name(name)} = outSocket", locals())

    #     return result
