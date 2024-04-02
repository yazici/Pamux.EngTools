
from pamux_unreal_tools.material_function import MaterialFunction, MaterialFunctionFactory
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase

class MaterialFunctionOutputs:
    class Result:
        def __init__(self, builder):
            CurrentNodePos.y = 0
            self.Result = builder.makeFunctionOutput_Result()

    class ResultAndHeight(Result):
        def __init__(self, builder):
            super().__init__(builder)
            self.Height = builder.makeFunctionOutput_Height()

class MaterialFunctionBuilderBase(ContainerBuilderBase):
    def __init__(self, container_path: str, inputs_class, outputs_class):
        super().__init__(MaterialFunctionFactory(), None, container_path, inputs_class, outputs_class)

    def makeFunctionOutput(self, name, sort_priority):
        CurrentNodePos.goto_outputs()
        result = FunctionOutput()
        result.output_name.set(name)
        result.sort_priority.set(sort_priority)
        return result

    def makeFunctionOutput_Result(self):
        return self.makeFunctionOutput("Result", 0)
    
    def makeFunctionOutput_Height(self):
        return self.makeFunctionOutput("Height", 1)
    
    def build_dependencies(self):
        pass
    
    def build_input_nodes(self):
        pass

    def build_output_nodes(self):
        self.outputs = MaterialFunctionOutputs.Result(self)

    def finalize_node_connections(self):
        pass

class MaterialLayerFunctionBuilderBase(MaterialFunctionBuilderBase):
    def __init__(self, container_path: str):
        super().__init__(container_path)

    def build_output_nodes(self):
        CurrentNodePos.y = 0
        self.Result = self.makeFunctionOutput_Result()

        CurrentNodePos.y += NodePos.DeltaY
        self.Height = self.makeFunctionOutput_Height()
