import os
import shutil
import logging
logger = logging.getLogger(__name__)

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.utils.types import *

from pamux_unreal_tools.base.material_function.material_function_base import MaterialFunctionBase

from pamux_unreal_tools.factories.material_expression_factories import FunctionInputFactory

from pamux_unreal_tools.utils.build_stack import BuildStack
from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos
from pamux_unreal_tools.utils.texture_sample_set import TMaterialTextures, TextureSampleSet
from pamux_unreal_tools.base.material_function.material_function_factory_base import MaterialFunctionFactoryBase
from pamux_unreal_tools.base.material_expression.material_expression_container_factory_base import MaterialExpressionContainerFactoryBase

class MaterialExpressionContainerBuilderBase:
    container_path: str
    container_name: str
    material_function_factory: MaterialFunctionFactoryBase
    container_factory: MaterialExpressionContainerFactoryBase
    dependencies_class: type
    inputs_class: type
    outputs_class: type

    DefaultTexture_Color = unreal.load_asset("/Engine/EngineResources/DefaultTexture")
    DefaultTexture_Normal = unreal.load_asset("/Engine/EngineMaterials/DefaultNormal")


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
        self.container_name = container_path[container_path.rindex("/")+1:]
        self.container_name = self.container_name[self.container_name.index("_")+1:]
        self.dependencies_class = dependencies_class
        self.inputs_class = inputs_class
        self.outputs_class = outputs_class

        self.unitW = unreal.Vector4f()
        self.unitW.set_editor_property("w", 1.0)

    def load_MF(self, function_path: str, virtual_inputs: SocketNames, virtual_outputs: SocketNames) -> MaterialFunctionBase:
        return self.material_function_factory.load(self, function_path, virtual_inputs, virtual_outputs)
    
    def load_SCurve(self):
        return self.load_MF("/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment/SCurve",
                            [ "In", "Power" ],
                            [ "Result" ])
    
    def load_Blend_Overlay(self):
        return self.load_MF("/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Overlay",
                            [ "Base", "Blend" ],
                            [ "Result" ])

    def load_CheapContrast_RGB(self):
        return self.load_MF("/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment/CheapContrast_RGB",
                            [ "In", "Contrast" ],
                            [ "Result" ])

    def load_HeightLerp(self):
        return self.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Texturing/HeightLerp",
                            [ "A", "B", "Transition Phase", "Height Texture", "Contrast" ],
                            [ "Results", "Alpha", "Lerp Alpha No Contrast" ])

    def load_MultiplyAdd(self):
        return self.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Math/MultiplyAdd",
                            [ "Base", "Add" ],
                            [ "Result" ])

    def load_BreakOutFloat4Components(self):
        return self.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat4Components",
                            [ "Float4" ],
                            [ "R", "G", "B", "A" ])

    def load_CustomRotator(self):
        return self.load_MF("/Engine/Functions/Engine_MaterialFunctions02/Texturing/CustomRotator",
                            [ "UVs", "Rotation Center", "Rotation Angle" ],
                            [ "Rotated Values" ])


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
                preview = TextureObject(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR, MaterialExpressionContainerBuilderBase.DefaultTexture_Color)
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
                preview = TextureObject(unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL, MaterialExpressionContainerBuilderBase.DefaultTexture_Normal)
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

        if isinstance(preview, TMaterialTextures):
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
        result: FunctionInput = FunctionInputFactory.create(input_name, input_type, preview)
        
        result.add_rt(input_name)

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
    
    def __load(self, virtual_inputs: SocketNames, virtual_outputs: SocketNames):
        result = self.container_factory.load(self, self.container_path, virtual_inputs, virtual_outputs)
        BuildStack.push(result)
        return result

    def get(self, virtual_inputs: SocketNames = [], virtual_outputs: SocketNames = []):
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
    
    def load(self, virtual_inputs: SocketNames = [], virtual_outputs: SocketNames = []):
        result = self.__load(virtual_inputs, virtual_outputs)
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
        if name == "In":
            return "_in"
        if name == "X-Axis":
            return "xAxis"
        if name == "Y-Axis":
            return "yAxis"
        if name == "Z-Axis":
            return "zAxis"
        _name = name.replace(" ", "")
        return _name[0].lower() + _name[1:]
