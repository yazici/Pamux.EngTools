from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import InSocket, OutSocket
from pamux_unreal_tools.material_expression_factories import *

from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.utils.build_stack import BuildStack

LandscapeMaterialFunctionPackage = "/Game/Materials/Pamux/Landscape/Functions"

class ContainerBuilderBase:
    def __init__(self, container_factory: MaterialExpressionContainerFactory, params_factory, container_name: str, package_name: str = LandscapeMaterialFunctionPackage):
        self.container_factory = container_factory
        self.params_factory = params_factory
        self.container_name = container_name
        self.package_name = package_name
  
    def build_dependencies(self):
        raise "Implement build_dependencies"
    
    def build_input_nodes(self):
        raise "Implement build_input_nodes"

    def build_process_nodes(self):
        raise "Implement build_process_nodes"
    
    def build_output_nodes(self):
        raise "Implement build_output_nodes"

    def finalize_node_connections(self):
        raise "Implement finalize_node_connections"

    def build_FunctionInput(self, input_name, input_type, preview = None) -> FunctionInput:
        result = FunctionInputFactory.create(input_name, input_type, preview)
        result.use_preview_value_as_default.set(True)

        CurrentNodePos.x += NodePos.DeltaX

        result.rt = NamedRerouteDeclaration(f"rt{input_name}", result)

        CurrentNodePos.x = 0
        CurrentNodePos.y += NodePos.DeltaY

        return result

    def loadOrCreate(self):
        result = self.container_factory.loadOrCreate(self.container_name, self.package_name)
        BuildStack.push(result)
        print("pushed")

        if self.params_factory is None:
            self.params = None
        else:
            self.params = self.params_factory(result)
        return result

    def get(self):
        result = self.loadOrCreate()
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
    
    def __get_field_name(self, name):
        if name == "X-Axis":
            return "xAxis"
        if name == "Y-Axis":
            return "yAxis"
        if name == "Z-Axis":
            return "zAxis"
        _name = name.replace(" ", "")
        return _name[0].lower() + _name[1:]

    def callMaterialFunction(self, materialFunctionToCall: MaterialFunction, virtual_inputs = [], virtual_outputs = []) -> MaterialFunctionCall:
        result = MaterialFunctionCall()
        result.material_function.set(materialFunctionToCall.asset)

        for name in virtual_inputs:
            
            inSocket = InSocket(result, name, 'StructProperty')
            exec(f"result.{self.__get_field_name(name)} = inSocket", locals())

        for name in virtual_outputs:
            outSocket = OutSocket(result, name, 'StructProperty')
            exec(f"result.{self.__get_field_name(name)} = outSocket", locals())

        return result

    class TextureSampleSet:
        def __init__(self, baseColor, roughness, opacity, normal):
            self.baseColor = TextureSample()
            self.baseColor.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.baseColor.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
            self.baseColor.texture.set(unreal.load_asset(baseColor))

            self.roughness = TextureSample()
            self.roughness.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.roughness.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
            self.roughness.texture.set(unreal.load_asset(roughness))

            self.opacity = TextureSample()
            self.opacity.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.opacity.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
            self.opacity.texture.set(unreal.load_asset(opacity))

            self.normal = TextureSample()
            self.normal.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.normal.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)
            self.normal.texture.set(unreal.load_asset(normal))

        
