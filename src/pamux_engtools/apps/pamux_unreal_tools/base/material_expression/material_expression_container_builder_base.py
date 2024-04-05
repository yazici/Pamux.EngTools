import os
import shutil

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.utils.types import *

from pamux_unreal_tools.base.material_function.material_function_base import MaterialFunctionBase

from pamux_unreal_tools.factories.material_expression_factories import FunctionInputFactory

from pamux_unreal_tools.utils.build_stack import BuildStack
from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos
from pamux_unreal_tools.utils.texture_sample_set import TTextureSampleSet, TextureSampleSet
from pamux_unreal_tools.base.material_function.material_function_factory_base import MaterialFunctionFactoryBase
from pamux_unreal_tools.base.material_expression.material_expression_container_factory_base import MaterialExpressionContainerFactoryBase

class MaterialExpressionContainerBuilderBase:
    def __init__(self,
                 material_function_factory: MaterialFunctionFactoryBase,
                 container_factory: MaterialExpressionContainerFactoryBase,
                 container_path: str,
                 dependencies_class = None,
                 inputs_class = None,
                 outputs_class = None):

        self.material_function_factory = material_function_factory
        self.container_factory = container_factory

        self.container_path = container_path
        self.dependencies_class = dependencies_class
        self.inputs_class = inputs_class
        self.outputs_class = outputs_class

        self.unitW = unreal.Vector4f()
        self.unitW.set_editor_property("w", 1.0)

    def load_MF(self, function_path: str, virtual_inputs: SocketNames, virtual_outputs: SocketNames) -> MaterialFunctionBase:
        return self.material_function_factory.load(self, function_path, virtual_inputs, virtual_outputs)

    def build(self):
        pass

    def build_FunctionInput(self, input_name: str, sort_priority: int, preview, use_preview_input: bool, use_preview_value_as_default: bool) -> FunctionInput:
        if isinstance(preview, float):
            if use_preview_input:
                preview = Constant(preview)
            else:
                preview = None

            return self.__build_FunctionInput_impl(
                input_name,
                unreal.FunctionInputType.FUNCTION_INPUT_SCALAR,
                sort_priority,
                preview,
                use_preview_value_as_default)

        if isinstance(preview, bool):
            if use_preview_input:
                preview = StaticBool(preview)
            else:
                preview = None

            return self.__build_FunctionInput_impl(
                input_name,
                unreal.FunctionInputType.FUNCTION_INPUT_STATIC_BOOL,
                sort_priority,
                preview,
                use_preview_value_as_default)

        if isinstance(preview, VecFBase):
            if preview is None:
                functionInputType = None
            else:
                functionInputType = preview.functionInputType

            if use_preview_input:
                preview = preview.linearColor
            else:
                preview = None

            return self.__build_FunctionInput_impl(
                input_name,
                functionInputType,
                sort_priority,
                preview,
                use_preview_value_as_default)
        
        if isinstance(preview, TTextureObject_Color):
            if use_preview_input:
                preview = TextureObject()
            else:
                preview = None

            return self.__build_FunctionInput_impl(
                input_name,
                unreal.FunctionInputType.FUNCTION_INPUT_TEXTURE2D,
                sort_priority,
                preview,
                use_preview_value_as_default)

        if isinstance(preview, TTextureObject_Normal):
            if use_preview_input:
                preview = TextureObject(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)
            else:
                preview = None

            return self.__build_FunctionInput_impl(
                input_name,
                unreal.FunctionInputType.FUNCTION_INPUT_TEXTURE2D,
                sort_priority,
                preview,
                use_preview_value_as_default)

        if isinstance(preview, TTextureCoordinate):
            if use_preview_input:
                preview = TextureCoordinate(preview.x, preview.y)
            else:
                preview = None

            return self.__build_FunctionInput_impl(
                input_name,
                unreal.FunctionInputType.FUNCTION_INPUT_VECTOR2,
                sort_priority,
                preview,
                use_preview_value_as_default)

        if isinstance(preview, MakeMaterialAttributes):
            if not use_preview_input:
                preview = None

            return self.__build_FunctionInput_impl(
                input_name,
                unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES,
                sort_priority,
                preview,
                use_preview_value_as_default)

        if isinstance(preview, TTextureSampleSet):
            if use_preview_input:
                preview = TextureSampleSet(preview)
                makeMaterialAttributes = MakeMaterialAttributes()
                makeMaterialAttributes.baseColor.comesFrom(preview.baseColor.RGB)
                makeMaterialAttributes.roughness.comesFrom(preview.roughness.RGB)
                makeMaterialAttributes.opacity.comesFrom(preview.opacity.RGB)
                makeMaterialAttributes.normal.comesFrom(preview.normal.RGB)
                preview = makeMaterialAttributes
            else:
                preview = None

            return self.__build_FunctionInput_impl(
                input_name,
                unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES,
                sort_priority,
                preview,
                use_preview_value_as_default)
        
        if isinstance(preview, TMaterialAttributes):
            if not use_preview_input:
                preview = None

            return self.__build_FunctionInput_impl(
                input_name,
                unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES,
                sort_priority,
                preview,
                use_preview_value_as_default)

        raise Exception(f"Unsupported preview type calling build_FunctionInput with input_name: {input_name}")

    def __build_FunctionInput_impl(self, input_name: str, input_type: str, sort_priority: int, preview, use_preview_value_as_default: bool) -> FunctionInput:
        result = FunctionInputFactory.create(input_name, input_type, preview)
        result.add_rt()
        result.sort_priority.set(sort_priority)

        result.preview_value.set(self.unitW)
        result.use_preview_value_as_default.set(use_preview_value_as_default)
        
        CurrentNodePos.x = 0
        CurrentNodePos.y += NodePos.DeltaY

        return result

    def __loadAndCleanOrCreate(self, virtual_inputs: SocketNames, virtual_outputs: SocketNames):
        result = self.container_factory.loadAndCleanOrCreate(self, self.container_path, virtual_inputs, virtual_outputs)
        BuildStack.push(result)
        return result

    def get(self, virtual_inputs: SocketNames = [], virtual_outputs: SocketNames = [], purge = False):
        if purge:
            folder = "C:/src/Unreal Projects/PamuxSurvival/Content/Materials/Pamux"
            if os.path.isdir(folder):
                shutil.rmtree(folder)
            
        result = self.__loadAndCleanOrCreate(virtual_inputs, virtual_outputs)
        result.builder = self

        self.dependencies = self.dependencies_class(self)

        CurrentNodePos.goto_inputs()
        self.inputs = self.inputs_class(self)

        CurrentNodePos.goto_outputs()
        self.outputs = self.outputs_class(self)

        CurrentNodePos.goto_process()
        self.build()

        result.save()

        BuildStack.pop()

        return result

    def makeFunctionOutput(self, name, sort_priority) -> FunctionOutput:
        result = FunctionOutput()
        result.output_name.set(name)
        result.sort_priority.set(sort_priority)
        return result

    @property
    def current_container(self):
        return BuildStack.top()
    
    def get_field_name(self, name: str):
        if name == "X-Axis":
            return "xAxis"
        if name == "Y-Axis":
            return "yAxis"
        if name == "Z-Axis":
            return "zAxis"
        _name = name.replace(" ", "")
        return _name[0].lower() + _name[1:]

    def __create_interface_dependencies_object(self):
        print(self.interface)