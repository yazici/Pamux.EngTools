# This file is generated. Please do NOT modify.
import unreal
from pamux_unreal_tools.impl.material_expression_impl import MaterialExpressionImpl
from pamux_unreal_tools.tools.material_expression_wrapper_generator.custom_base_classes import *
from pamux_unreal_tools.impl.material_expression_editor_property_impl import MaterialExpressionEditorPropertyImpl
from pamux_unreal_tools.impl.in_socket_impl import InSocketImpl
from pamux_unreal_tools.impl.out_socket_impl import OutSocketImpl
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.utils.node_pos import NodePos

class Abs(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionAbs, node_pos)

class AbsorptionMediumMaterialOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionAbsorptionMediumMaterialOutput, node_pos)

class ActorPositionWS(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionActorPositionWS, node_pos)

        self.origin_type = MaterialExpressionEditorPropertyImpl(self, 'origin_type', 'PositionOrigin')

class Add(MaterialExpressionImpl):
    def __init__(self, a, b, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionAdd, node_pos)

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if a is not None:
            if isinstance(a, float):
                self.const_a.set(a)
            else:
                self.a.comesFrom(a)
        if b is not None:
            if isinstance(b, float):
                self.const_b.set(b)
            else:
                self.b.comesFrom(b)

class AntialiasedTextureMask(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionAntialiasedTextureMask, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.channel = MaterialExpressionEditorPropertyImpl(self, 'channel', 'TextureColorChannel')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')
        self.threshold = MaterialExpressionEditorPropertyImpl(self, 'threshold', 'float')

        self.UVs = InSocketImpl(self, 'UVs', 'StructProperty')
        self.applyViewMipBias = InSocketImpl(self, 'ApplyViewMipBias', 'StructProperty')

class AppendVector(MaterialExpressionImpl):
    def __init__(self, a, b, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionAppendVector, node_pos)

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if a is not None:
            self.a.comesFrom(a)
        if b is not None:
            self.b.comesFrom(b)

class Arccosine(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionArccosine, node_pos)

class ArccosineFast(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionArccosineFast, node_pos)

class Arcsine(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionArcsine, node_pos)

class ArcsineFast(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionArcsineFast, node_pos)

class Arctangent(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionArctangent, node_pos)

class Arctangent2(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionArctangent2, node_pos)

        self.y = InSocketImpl(self, 'Y', 'StructProperty')
        self.x = InSocketImpl(self, 'X', 'StructProperty')

class Arctangent2Fast(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionArctangent2Fast, node_pos)

        self.y = InSocketImpl(self, 'Y', 'StructProperty')
        self.x = InSocketImpl(self, 'X', 'StructProperty')

class ArctangentFast(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionArctangentFast, node_pos)

class AtmosphericFogColor(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionAtmosphericFogColor, node_pos)

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')

class AtmosphericLightColor(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionAtmosphericLightColor, node_pos)

class AtmosphericLightVector(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionAtmosphericLightVector, node_pos)

class BentNormalCustomOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionBentNormalCustomOutput, node_pos)

class BinaryOp(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionBinaryOp, node_pos)

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

class BlackBody(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionBlackBody, node_pos)

        self.temp = InSocketImpl(self, 'Temp', 'StructProperty')

class BlendMaterialAttributes(MaterialExpressionImpl):
    def __init__(self, a, b, alpha, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionBlendMaterialAttributes, node_pos)

        self.pixel_attribute_blend_type = MaterialExpressionEditorPropertyImpl(self, 'pixel_attribute_blend_type', 'MaterialAttributeBlend')
        self.vertex_attribute_blend_type = MaterialExpressionEditorPropertyImpl(self, 'vertex_attribute_blend_type', 'MaterialAttributeBlend')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        self.alpha = InSocketImpl(self, 'Alpha', 'StructProperty')
        if a is not None:
            self.a.comesFrom(a)
        if b is not None:
            self.b.comesFrom(b)
        if alpha is not None:
            self.alpha.comesFrom(alpha)

class BreakMaterialAttributes(MaterialExpressionImpl):
    def __init__(self, input, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionBreakMaterialAttributes, node_pos)

        self.materialAttributes = InSocketImpl(self, 'MaterialAttributes', 'StructProperty')

        self.baseColor = OutSocketImpl(self, 'BaseColor', 'StructProperty')
        self.metallic = OutSocketImpl(self, 'Metallic', 'StructProperty')
        self.specular = OutSocketImpl(self, 'Specular', 'StructProperty')
        self.roughness = OutSocketImpl(self, 'Roughness', 'StructProperty')
        self.anisotropy = OutSocketImpl(self, 'Anisotropy', 'StructProperty')
        self.emissiveColor = OutSocketImpl(self, 'EmissiveColor', 'StructProperty')
        self.opacity = OutSocketImpl(self, 'Opacity', 'StructProperty')
        self.opacityMask = OutSocketImpl(self, 'OpacityMask', 'StructProperty')
        self.normal = OutSocketImpl(self, 'Normal', 'StructProperty')
        self.tangent = OutSocketImpl(self, 'Tangent', 'StructProperty')
        self.worldPositionOffset = OutSocketImpl(self, 'WorldPositionOffset', 'StructProperty')
        self.subsurfaceColor = OutSocketImpl(self, 'SubsurfaceColor', 'StructProperty')
        self.clearCoat = OutSocketImpl(self, 'ClearCoat', 'StructProperty')
        self.clearCoatRoughness = OutSocketImpl(self, 'ClearCoatRoughness', 'StructProperty')
        self.ambientOcclusion = OutSocketImpl(self, 'AmbientOcclusion', 'StructProperty')
        self.refraction = OutSocketImpl(self, 'Refraction', 'StructProperty')
        self.customizedUV0 = OutSocketImpl(self, 'CustomizedUV0', 'StructProperty')
        self.customizedUV1 = OutSocketImpl(self, 'CustomizedUV1', 'StructProperty')
        self.customizedUV2 = OutSocketImpl(self, 'CustomizedUV2', 'StructProperty')
        self.customizedUV3 = OutSocketImpl(self, 'CustomizedUV3', 'StructProperty')
        self.customizedUV4 = OutSocketImpl(self, 'CustomizedUV4', 'StructProperty')
        self.customizedUV5 = OutSocketImpl(self, 'CustomizedUV5', 'StructProperty')
        self.customizedUV6 = OutSocketImpl(self, 'CustomizedUV6', 'StructProperty')
        self.customizedUV7 = OutSocketImpl(self, 'CustomizedUV7', 'StructProperty')
        self.pixelDepthOffset = OutSocketImpl(self, 'PixelDepthOffset', 'StructProperty')
        self.shadingModel = OutSocketImpl(self, 'ShadingModel', 'StructProperty')
        self.displacement = OutSocketImpl(self, 'Displacement', 'StructProperty')
        if input is not None:
            self.input.comesFrom(input)

class BumpOffset(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionBumpOffset, node_pos)

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint32')
        self.height_ratio = MaterialExpressionEditorPropertyImpl(self, 'height_ratio', 'float')
        self.reference_plane = MaterialExpressionEditorPropertyImpl(self, 'reference_plane', 'float')

        self.coordinate = InSocketImpl(self, 'Coordinate', 'StructProperty')
        self.height = InSocketImpl(self, 'Height', 'StructProperty')
        self.heightRatioInput = InSocketImpl(self, 'HeightRatioInput', 'StructProperty')

class CameraPositionWS(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionCameraPositionWS, node_pos)

class CameraVectorWS(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionCameraVectorWS, node_pos)

class Ceil(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionCeil, node_pos)

class ChannelMaskParameter(MaterialExpressionImpl):
    def __init__(self, parameter_name, default_value, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionChannelMaskParameter, node_pos)

        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'LinearColor')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.mask_channel = MaterialExpressionEditorPropertyImpl(self, 'mask_channel', 'ChannelMaskParameterColor')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.primitive_data_index = MaterialExpressionEditorPropertyImpl(self, 'primitive_data_index', 'uint8')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = MaterialExpressionEditorPropertyImpl(self, 'use_custom_primitive_data', 'bool')

        self.defaultValue = InSocketImpl(self, 'DefaultValue', 'StructProperty')
        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class Clamp(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionClamp, node_pos)

        self.clamp_mode = MaterialExpressionEditorPropertyImpl(self, 'clamp_mode', 'ClampMode')
        self.max_default = MaterialExpressionEditorPropertyImpl(self, 'max_default', 'float')
        self.min_default = MaterialExpressionEditorPropertyImpl(self, 'min_default', 'float')

        self.min = InSocketImpl(self, 'Min', 'StructProperty')
        self.max = InSocketImpl(self, 'Max', 'StructProperty')

class ClearCoatNormalCustomOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionClearCoatNormalCustomOutput, node_pos)

class CloudSampleAttribute(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionCloudSampleAttribute, node_pos)

class CollectionParameter(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionCollectionParameter, node_pos)

        self.collection = MaterialExpressionEditorPropertyImpl(self, 'collection', 'MaterialParameterCollection')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')

        self.parameterId = InSocketImpl(self, 'ParameterId', 'StructProperty')

class Comment(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionComment, node_pos)

        self.color_comment_bubble = MaterialExpressionEditorPropertyImpl(self, 'color_comment_bubble', 'bool')
        self.comment_bubble_visible_in_details_panel = MaterialExpressionEditorPropertyImpl(self, 'comment_bubble_visible_in_details_panel', 'bool')
        self.comment_color = MaterialExpressionEditorPropertyImpl(self, 'comment_color', 'LinearColor')
        self.font_size = MaterialExpressionEditorPropertyImpl(self, 'font_size', 'int32')
        self.group_mode = MaterialExpressionEditorPropertyImpl(self, 'group_mode', 'bool')
        self.text = MaterialExpressionEditorPropertyImpl(self, 'text', 'str')

        self.commentColor = InSocketImpl(self, 'CommentColor', 'StructProperty')

class ComponentMask(MaterialExpressionImpl):
    def __init__(self, input, rgbaMask, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionComponentMask, node_pos)

        self.a = MaterialExpressionEditorPropertyImpl(self, 'a', 'bool')
        self.b = MaterialExpressionEditorPropertyImpl(self, 'b', 'bool')
        self.g = MaterialExpressionEditorPropertyImpl(self, 'g', 'bool')
        self.r = MaterialExpressionEditorPropertyImpl(self, 'r', 'bool')
        if input is not None:
            self.input.comesFrom(input)
        if rgbaMask is not None:
            __mask = rgbaMask.lower()
            self.r.set('r' in __mask)
            self.g.set('g' in __mask)
            self.b.set('b' in __mask)
            self.a.set('a' in __mask)
        else:
            self.r.set(True)
            self.g.set(True)
            self.b.set(False)
            self.a.set(False)

class Composite(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionComposite, node_pos)

        self.subgraph_name = MaterialExpressionEditorPropertyImpl(self, 'subgraph_name', 'str')

class Constant(MaterialExpressionImpl):
    def __init__(self, r, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionConstant, node_pos)

        self.r = MaterialExpressionEditorPropertyImpl(self, 'r', 'float')
        if r is not None:
            self.r.set(r)

class Constant2Vector(MaterialExpressionImpl):
    def __init__(self, constant, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionConstant2Vector, node_pos)

        self.g = MaterialExpressionEditorPropertyImpl(self, 'g', 'float')
        self.r = MaterialExpressionEditorPropertyImpl(self, 'r', 'float')

        self.r = OutSocketImpl(self, 'r', 'StructProperty')
        self.g = OutSocketImpl(self, 'g', 'StructProperty')
        if constant is not None:
            self.constant.set(constant)

class Constant3Vector(MaterialExpressionImpl):
    def __init__(self, constant, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionConstant3Vector, node_pos)

        self.constant = MaterialExpressionEditorPropertyImpl(self, 'constant', 'LinearColor')

        self.r = OutSocketImpl(self, 'r', 'StructProperty')
        self.g = OutSocketImpl(self, 'g', 'StructProperty')
        self.b = OutSocketImpl(self, 'b', 'StructProperty')
        if constant is not None:
            self.constant.set(constant)

class Constant4Vector(MaterialExpressionImpl):
    def __init__(self, constant, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionConstant4Vector, node_pos)

        self.constant = MaterialExpressionEditorPropertyImpl(self, 'constant', 'LinearColor')

        self.r = OutSocketImpl(self, 'r', 'StructProperty')
        self.g = OutSocketImpl(self, 'g', 'StructProperty')
        self.b = OutSocketImpl(self, 'b', 'StructProperty')
        self.a = OutSocketImpl(self, 'a', 'StructProperty')
        if constant is not None:
            self.constant.set(constant)

class ConstantBiasScale(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionConstantBiasScale, node_pos)

        self.bias = MaterialExpressionEditorPropertyImpl(self, 'bias', 'float')
        self.scale = MaterialExpressionEditorPropertyImpl(self, 'scale', 'float')

class ConstantDouble(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionConstantDouble, node_pos)

        self.value = MaterialExpressionEditorPropertyImpl(self, 'value', 'double')

class Cosine(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionCosine, node_pos)

        self.period = MaterialExpressionEditorPropertyImpl(self, 'period', 'float')

class CrossProduct(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionCrossProduct, node_pos)

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')

class CurveAtlasRowParameter(MaterialExpressionImpl):
    def __init__(self, parameter_name, default_value, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionCurveAtlasRowParameter, node_pos)

        self.atlas = MaterialExpressionEditorPropertyImpl(self, 'atlas', 'CurveLinearColorAtlas')
        self.curve = MaterialExpressionEditorPropertyImpl(self, 'curve', 'CurveLinearColor')
        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'float')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.primitive_data_index = MaterialExpressionEditorPropertyImpl(self, 'primitive_data_index', 'uint8')
        self.slider_max = MaterialExpressionEditorPropertyImpl(self, 'slider_max', 'float')
        self.slider_min = MaterialExpressionEditorPropertyImpl(self, 'slider_min', 'float')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = MaterialExpressionEditorPropertyImpl(self, 'use_custom_primitive_data', 'bool')

        self.inputTime = InSocketImpl(self, 'InputTime', 'StructProperty')
        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class Custom(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionCustom, node_pos)

        self.additional_defines = MaterialExpressionEditorPropertyImpl(self, 'additional_defines', 'Array[CustomDefine]')
        self.additional_outputs = MaterialExpressionEditorPropertyImpl(self, 'additional_outputs', 'Array[CustomOutput]')
        self.code = MaterialExpressionEditorPropertyImpl(self, 'code', 'str')
        self.description = MaterialExpressionEditorPropertyImpl(self, 'description', 'str')
        self.include_file_paths = MaterialExpressionEditorPropertyImpl(self, 'include_file_paths', 'Array[str]')
        self.inputs = MaterialExpressionEditorPropertyImpl(self, 'inputs', 'Array[CustomInput]')
        self.output_type = MaterialExpressionEditorPropertyImpl(self, 'output_type', 'CustomMaterialOutputType')

class CustomOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionCustomOutput, node_pos)

class DBufferTexture(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDBufferTexture, node_pos)

        self.d_buffer_texture_id = MaterialExpressionEditorPropertyImpl(self, 'd_buffer_texture_id', 'DBufferTextureId')

class DDX(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDDX, node_pos)

        self.value = InSocketImpl(self, 'Value', 'StructProperty')

class DDY(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDDY, node_pos)

        self.value = InSocketImpl(self, 'Value', 'StructProperty')

class DataDrivenShaderPlatformInfoSwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDataDrivenShaderPlatformInfoSwitch, node_pos)

        self.ddspi_property_names = MaterialExpressionEditorPropertyImpl(self, 'ddspi_property_names', 'Array[DataDrivenShaderPlatformInfoInput]')

class DecalColor(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDecalColor, node_pos)

class DecalDerivative(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDecalDerivative, node_pos)

class DecalLifetimeOpacity(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDecalLifetimeOpacity, node_pos)

class DecalMipmapLevel(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDecalMipmapLevel, node_pos)

        self.const_height = MaterialExpressionEditorPropertyImpl(self, 'const_height', 'float')
        self.const_width = MaterialExpressionEditorPropertyImpl(self, 'const_width', 'float')

        self.textureSize = InSocketImpl(self, 'TextureSize', 'StructProperty')

class DeltaTime(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDeltaTime, node_pos)

class DepthFade(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDepthFade, node_pos)

        self.fade_distance_default = MaterialExpressionEditorPropertyImpl(self, 'fade_distance_default', 'float')
        self.opacity_default = MaterialExpressionEditorPropertyImpl(self, 'opacity_default', 'float')

        self.inOpacity = InSocketImpl(self, 'InOpacity', 'StructProperty')
        self.fadeDistance = InSocketImpl(self, 'FadeDistance', 'StructProperty')

class DepthOfFieldFunction(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDepthOfFieldFunction, node_pos)

        self.function_value = MaterialExpressionEditorPropertyImpl(self, 'function_value', 'DepthOfFieldFunctionValue')

        self.depth = InSocketImpl(self, 'Depth', 'StructProperty')

class DeriveNormalZ(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDeriveNormalZ, node_pos)

        self.inXY = InSocketImpl(self, 'InXY', 'StructProperty')

class Desaturation(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDesaturation, node_pos)

        self.luminance_factors = MaterialExpressionEditorPropertyImpl(self, 'luminance_factors', 'LinearColor')

        self.fraction = InSocketImpl(self, 'Fraction', 'StructProperty')

class Distance(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDistance, node_pos)

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')

class DistanceCullFade(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDistanceCullFade, node_pos)

class DistanceFieldApproxAO(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDistanceFieldApproxAO, node_pos)

        self.base_distance_default = MaterialExpressionEditorPropertyImpl(self, 'base_distance_default', 'float')
        self.num_steps = MaterialExpressionEditorPropertyImpl(self, 'num_steps', 'uint32')
        self.radius_default = MaterialExpressionEditorPropertyImpl(self, 'radius_default', 'float')
        self.step_scale_default = MaterialExpressionEditorPropertyImpl(self, 'step_scale_default', 'float')

class DistanceFieldGradient(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDistanceFieldGradient, node_pos)

        self.position = InSocketImpl(self, 'Position', 'StructProperty')

class DistanceFieldsRenderingSwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDistanceFieldsRenderingSwitch, node_pos)

        self.no = InSocketImpl(self, 'No', 'StructProperty')
        self.yes = InSocketImpl(self, 'Yes', 'StructProperty')

class DistanceToNearestSurface(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDistanceToNearestSurface, node_pos)

        self.position = InSocketImpl(self, 'Position', 'StructProperty')

class Divide(MaterialExpressionImpl):
    def __init__(self, a, b, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDivide, node_pos)

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if a is not None:
            if isinstance(a, float):
                self.const_a.set(a)
            else:
                self.a.comesFrom(a)
        if b is not None:
            if isinstance(b, float):
                self.const_b.set(b)
            else:
                self.b.comesFrom(b)

class DotProduct(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDotProduct, node_pos)

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')

class DoubleVectorParameter(MaterialExpressionImpl):
    def __init__(self, parameter_name, default_value, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDoubleVectorParameter, node_pos)

        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'Vector4d')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class DynamicParameter(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionDynamicParameter, node_pos)

        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'LinearColor')
        self.param_names = MaterialExpressionEditorPropertyImpl(self, 'param_names', 'Array[str]')
        self.parameter_index = MaterialExpressionEditorPropertyImpl(self, 'parameter_index', 'uint32')

        self.defaultValue = InSocketImpl(self, 'DefaultValue', 'StructProperty')

class ExecBegin(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionExecBegin, node_pos)

class ExecEnd(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionExecEnd, node_pos)

class Exponential(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionExponential, node_pos)

class Exponential2(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionExponential2, node_pos)

class EyeAdaptation(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionEyeAdaptation, node_pos)

class EyeAdaptationInverse(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionEyeAdaptationInverse, node_pos)

class FeatureLevelSwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionFeatureLevelSwitch, node_pos)

        self.default = InSocketImpl(self, 'Default', 'StructProperty')

class Floor(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionFloor, node_pos)

class Fmod(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionFmod, node_pos)

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')

class FontSample(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionFontSample, node_pos)

        self.font = MaterialExpressionEditorPropertyImpl(self, 'font', 'Font')
        self.font_texture_page = MaterialExpressionEditorPropertyImpl(self, 'font_texture_page', 'int32')

class FontSampleParameter(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionFontSampleParameter, node_pos)

        self.font = MaterialExpressionEditorPropertyImpl(self, 'font', 'Font')
        self.font_texture_page = MaterialExpressionEditorPropertyImpl(self, 'font_texture_page', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')

class ForLoop(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionForLoop, node_pos)

class Frac(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionFrac, node_pos)

class Fresnel(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionFresnel, node_pos)

        self.base_reflect_fraction = MaterialExpressionEditorPropertyImpl(self, 'base_reflect_fraction', 'float')
        self.exponent = MaterialExpressionEditorPropertyImpl(self, 'exponent', 'float')

        self.exponentIn = InSocketImpl(self, 'ExponentIn', 'StructProperty')
        self.baseReflectFractionIn = InSocketImpl(self, 'BaseReflectFractionIn', 'StructProperty')
        self.normal = InSocketImpl(self, 'Normal', 'StructProperty')

class FunctionInput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionFunctionInput, node_pos)

        self.description = MaterialExpressionEditorPropertyImpl(self, 'description', 'str')
        self.input_name = MaterialExpressionEditorPropertyImpl(self, 'input_name', 'Name')
        self.input_type = MaterialExpressionEditorPropertyImpl(self, 'input_type', 'FunctionInputType')
        self.preview_value = MaterialExpressionEditorPropertyImpl(self, 'preview_value', 'Vector4f')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.use_preview_value_as_default = MaterialExpressionEditorPropertyImpl(self, 'use_preview_value_as_default', 'bool')

        self.preview = InSocketImpl(self, 'Preview', 'StructProperty')
        self.ID = InSocketImpl(self, 'ID', 'StructProperty')
        self.previewValue = InSocketImpl(self, 'PreviewValue', 'StructProperty')

class FunctionOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionFunctionOutput, node_pos)

        self.description = MaterialExpressionEditorPropertyImpl(self, 'description', 'str')
        self.output_name = MaterialExpressionEditorPropertyImpl(self, 'output_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.ID = InSocketImpl(self, 'ID', 'StructProperty')

class GIReplace(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionGIReplace, node_pos)

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.staticIndirect = InSocketImpl(self, 'StaticIndirect', 'StructProperty')
        self.dynamicIndirect = InSocketImpl(self, 'DynamicIndirect', 'StructProperty')

class GenericConstant(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionGenericConstant, node_pos)

class GetLocal(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionGetLocal, node_pos)

        self.local_name = MaterialExpressionEditorPropertyImpl(self, 'local_name', 'Name')

class GetMaterialAttributes(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionGetMaterialAttributes, node_pos)

        self.attribute_get_types = MaterialExpressionEditorPropertyImpl(self, 'attribute_get_types', 'Array[Guid]')

        self.materialAttributes = InSocketImpl(self, 'MaterialAttributes', 'StructProperty')

        self.materialAttributes = OutSocketImpl(self, 'MaterialAttributes', 'StructProperty')
        self.baseColor = OutSocketImpl(self, 'BaseColor', 'StructProperty')
        self.metallic = OutSocketImpl(self, 'Metallic', 'StructProperty')
        self.specular = OutSocketImpl(self, 'Specular', 'StructProperty')
        self.roughness = OutSocketImpl(self, 'Roughness', 'StructProperty')
        self.anisotropy = OutSocketImpl(self, 'Anisotropy', 'StructProperty')
        self.emissiveColor = OutSocketImpl(self, 'EmissiveColor', 'StructProperty')
        self.opacity = OutSocketImpl(self, 'Opacity', 'StructProperty')
        self.opacityMask = OutSocketImpl(self, 'OpacityMask', 'StructProperty')
        self.normal = OutSocketImpl(self, 'Normal', 'StructProperty')
        self.tangent = OutSocketImpl(self, 'Tangent', 'StructProperty')
        self.worldPositionOffset = OutSocketImpl(self, 'WorldPositionOffset', 'StructProperty')
        self.worldDisplacement = OutSocketImpl(self, 'WorldDisplacement', 'StructProperty')
        self.tessellationMultiplier = OutSocketImpl(self, 'TessellationMultiplier', 'StructProperty')
        self.subsurfaceColor = OutSocketImpl(self, 'SubsurfaceColor', 'StructProperty')
        self.clearCoat = OutSocketImpl(self, 'ClearCoat', 'StructProperty')
        self.clearCoatRoughness = OutSocketImpl(self, 'ClearCoatRoughness', 'StructProperty')
        self.ambientOcclusion = OutSocketImpl(self, 'AmbientOcclusion', 'StructProperty')
        self.refraction = OutSocketImpl(self, 'Refraction', 'StructProperty')
        self.customizedUVs = OutSocketImpl(self, 'CustomizedUVs', 'StructProperty')
        self.pixelDepthOffset = OutSocketImpl(self, 'PixelDepthOffset', 'StructProperty')
        self.shadingModel = OutSocketImpl(self, 'ShadingModel', 'StructProperty')

class HairAttributes(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionHairAttributes, node_pos)

        self.use_tangent_space = MaterialExpressionEditorPropertyImpl(self, 'use_tangent_space', 'bool')

class HairColor(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionHairColor, node_pos)

        self.melanin = InSocketImpl(self, 'Melanin', 'StructProperty')
        self.redness = InSocketImpl(self, 'Redness', 'StructProperty')
        self.dyeColor = InSocketImpl(self, 'DyeColor', 'StructProperty')

class HeightfieldMinMaxTexture(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionHeightfieldMinMaxTexture, node_pos)

        self.min_max_texture = MaterialExpressionEditorPropertyImpl(self, 'min_max_texture', 'HeightfieldMinMaxTexture')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')

class HsvToRgb(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionHsvToRgb, node_pos)

class If(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionIf, node_pos)

        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')
        self.equals_threshold = MaterialExpressionEditorPropertyImpl(self, 'equals_threshold', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        self.aGreaterThanB = InSocketImpl(self, 'AGreaterThanB', 'StructProperty')
        self.aEqualsB = InSocketImpl(self, 'AEqualsB', 'StructProperty')
        self.aLessThanB = InSocketImpl(self, 'ALessThanB', 'StructProperty')

class IfThenElse(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionIfThenElse, node_pos)

class InverseLinearInterpolate(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionInverseLinearInterpolate, node_pos)

        self.clamp_result = MaterialExpressionEditorPropertyImpl(self, 'clamp_result', 'bool')
        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')
        self.const_value = MaterialExpressionEditorPropertyImpl(self, 'const_value', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        self.value = InSocketImpl(self, 'Value', 'StructProperty')

class IsOrthographic(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionIsOrthographic, node_pos)

class LandscapeGrassOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLandscapeGrassOutput, node_pos)

        self.grass_types = MaterialExpressionEditorPropertyImpl(self, 'grass_types', 'Array[GrassInput]')

class LandscapeLayerBlend(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLandscapeLayerBlend, node_pos)

        self.layers = MaterialExpressionEditorPropertyImpl(self, 'layers', 'Array[LayerBlendInput]')

class LandscapeLayerCoords(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLandscapeLayerCoords, node_pos)

        self.custom_uv_type = MaterialExpressionEditorPropertyImpl(self, 'custom_uv_type', 'LandscapeCustomizedCoordType')
        self.mapping_pan_u = MaterialExpressionEditorPropertyImpl(self, 'mapping_pan_u', 'float')
        self.mapping_pan_v = MaterialExpressionEditorPropertyImpl(self, 'mapping_pan_v', 'float')
        self.mapping_rotation = MaterialExpressionEditorPropertyImpl(self, 'mapping_rotation', 'float')
        self.mapping_scale = MaterialExpressionEditorPropertyImpl(self, 'mapping_scale', 'float')
        self.mapping_type = MaterialExpressionEditorPropertyImpl(self, 'mapping_type', 'TerrainCoordMappingType')

class LandscapeLayerSample(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLandscapeLayerSample, node_pos)

        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.preview_weight = MaterialExpressionEditorPropertyImpl(self, 'preview_weight', 'float')

class LandscapeLayerSwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLandscapeLayerSwitch, node_pos)

        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.preview_used = MaterialExpressionEditorPropertyImpl(self, 'preview_used', 'bool')

class LandscapeLayerWeight(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLandscapeLayerWeight, node_pos)

        self.const_base = MaterialExpressionEditorPropertyImpl(self, 'const_base', 'Vector')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.preview_weight = MaterialExpressionEditorPropertyImpl(self, 'preview_weight', 'float')

class LandscapePhysicalMaterialOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLandscapePhysicalMaterialOutput, node_pos)

        self.inputs = MaterialExpressionEditorPropertyImpl(self, 'inputs', 'Array[PhysicalMaterialInput]')

class LandscapeVisibilityMask(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLandscapeVisibilityMask, node_pos)

class Length(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLength, node_pos)

class Less(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLess, node_pos)

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

class LightVector(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLightVector, node_pos)

class LightmapUVs(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLightmapUVs, node_pos)

class LightmassReplace(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLightmassReplace, node_pos)

        self.realtime = InSocketImpl(self, 'Realtime', 'StructProperty')
        self.lightmass = InSocketImpl(self, 'Lightmass', 'StructProperty')

class LinearInterpolate(MaterialExpressionImpl):
    def __init__(self, a, b, alpha, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLinearInterpolate, node_pos)

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        self.alpha = InSocketImpl(self, 'Alpha', 'StructProperty')
        if a is not None:
            self.a.comesFrom(a)
        if b is not None:
            self.b.comesFrom(b)
        if alpha is not None:
            self.alpha.comesFrom(alpha)

class Logarithm(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLogarithm, node_pos)

class Logarithm10(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLogarithm10, node_pos)

        self.x = InSocketImpl(self, 'X', 'StructProperty')

class Logarithm2(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionLogarithm2, node_pos)

        self.x = InSocketImpl(self, 'X', 'StructProperty')

class MakeMaterialAttributes(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMakeMaterialAttributes, node_pos)

        self.baseColor = InSocketImpl(self, 'BaseColor', 'StructProperty')
        self.metallic = InSocketImpl(self, 'Metallic', 'StructProperty')
        self.specular = InSocketImpl(self, 'Specular', 'StructProperty')
        self.roughness = InSocketImpl(self, 'Roughness', 'StructProperty')
        self.anisotropy = InSocketImpl(self, 'Anisotropy', 'StructProperty')
        self.emissiveColor = InSocketImpl(self, 'EmissiveColor', 'StructProperty')
        self.opacity = InSocketImpl(self, 'Opacity', 'StructProperty')
        self.opacityMask = InSocketImpl(self, 'OpacityMask', 'StructProperty')
        self.normal = InSocketImpl(self, 'Normal', 'StructProperty')
        self.tangent = InSocketImpl(self, 'Tangent', 'StructProperty')
        self.worldPositionOffset = InSocketImpl(self, 'WorldPositionOffset', 'StructProperty')
        self.subsurfaceColor = InSocketImpl(self, 'SubsurfaceColor', 'StructProperty')
        self.clearCoat = InSocketImpl(self, 'ClearCoat', 'StructProperty')
        self.clearCoatRoughness = InSocketImpl(self, 'ClearCoatRoughness', 'StructProperty')
        self.ambientOcclusion = InSocketImpl(self, 'AmbientOcclusion', 'StructProperty')
        self.refraction = InSocketImpl(self, 'Refraction', 'StructProperty')
        self.customizedUV_0 = InSocketImpl(self, 'CustomizedUV_0', 'StructProperty')
        self.customizedUV_1 = InSocketImpl(self, 'CustomizedUV_1', 'StructProperty')
        self.customizedUV_2 = InSocketImpl(self, 'CustomizedUV_2', 'StructProperty')
        self.customizedUV_3 = InSocketImpl(self, 'CustomizedUV_3', 'StructProperty')
        self.customizedUV_4 = InSocketImpl(self, 'CustomizedUV_4', 'StructProperty')
        self.customizedUV_5 = InSocketImpl(self, 'CustomizedUV_5', 'StructProperty')
        self.customizedUV_6 = InSocketImpl(self, 'CustomizedUV_6', 'StructProperty')
        self.customizedUV_7 = InSocketImpl(self, 'CustomizedUV_7', 'StructProperty')
        self.pixelDepthOffset = InSocketImpl(self, 'PixelDepthOffset', 'StructProperty')
        self.shadingModel = InSocketImpl(self, 'ShadingModel', 'StructProperty')
        self.displacement = InSocketImpl(self, 'Displacement', 'StructProperty')

class MapARPassthroughCameraUV(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMapARPassthroughCameraUV, node_pos)

        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')

class MaterialAttributeLayers(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialAttributeLayers, node_pos)

        self.default_layers = MaterialExpressionEditorPropertyImpl(self, 'default_layers', 'MaterialLayersFunctions')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        self.defaultLayers = InSocketImpl(self, 'DefaultLayers', 'StructProperty')

class MaterialFunctionCall(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialFunctionCall, node_pos)

        self.material_function = MaterialExpressionEditorPropertyImpl(self, 'material_function', 'MaterialFunctionInterface')

        self.functionParameterInfo = InSocketImpl(self, 'FunctionParameterInfo', 'StructProperty')

class MaterialLayerOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialLayerOutput, node_pos)

        self.description = MaterialExpressionEditorPropertyImpl(self, 'description', 'str')
        self.output_name = MaterialExpressionEditorPropertyImpl(self, 'output_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.ID = InSocketImpl(self, 'ID', 'StructProperty')

class MaterialProxyReplace(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialProxyReplace, node_pos)

        self.realtime = InSocketImpl(self, 'Realtime', 'StructProperty')
        self.materialProxy = InSocketImpl(self, 'MaterialProxy', 'StructProperty')

class MaterialXAppend3Vector(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXAppend3Vector, node_pos)

class MaterialXAppend4Vector(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXAppend4Vector, node_pos)

class MaterialXBurn(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXBurn, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXDifference(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXDifference, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXDisjointOver(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXDisjointOver, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXDodge(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXDodge, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXFractal3D(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXFractal3D, node_pos)

        self.const_amplitude = MaterialExpressionEditorPropertyImpl(self, 'const_amplitude', 'float')
        self.const_diminish = MaterialExpressionEditorPropertyImpl(self, 'const_diminish', 'float')
        self.const_lacunarity = MaterialExpressionEditorPropertyImpl(self, 'const_lacunarity', 'float')
        self.const_octaves = MaterialExpressionEditorPropertyImpl(self, 'const_octaves', 'int32')
        self.levels = MaterialExpressionEditorPropertyImpl(self, 'levels', 'int32')
        self.output_max = MaterialExpressionEditorPropertyImpl(self, 'output_max', 'float')
        self.output_min = MaterialExpressionEditorPropertyImpl(self, 'output_min', 'float')
        self.scale = MaterialExpressionEditorPropertyImpl(self, 'scale', 'float')
        self.turbulence = MaterialExpressionEditorPropertyImpl(self, 'turbulence', 'bool')

class MaterialXIn(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXIn, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXLuminance(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXLuminance, node_pos)

        self.luminance_factors = MaterialExpressionEditorPropertyImpl(self, 'luminance_factors', 'LinearColor')
        self.luminance_mode = MaterialExpressionEditorPropertyImpl(self, 'luminance_mode', 'MaterialXLuminanceMode')

class MaterialXMask(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXMask, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXMatte(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXMatte, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXMinus(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXMinus, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXOut(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXOut, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXOver(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXOver, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXOverlay(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXOverlay, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXPlace2D(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXPlace2D, node_pos)

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_rotation_angle = MaterialExpressionEditorPropertyImpl(self, 'const_rotation_angle', 'float')

class MaterialXPlus(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXPlus, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXPremult(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXPremult, node_pos)

class MaterialXRamp4(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXRamp4, node_pos)

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')

class MaterialXRampLeftRight(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXRampLeftRight, node_pos)

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')

class MaterialXRampTopBottom(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXRampTopBottom, node_pos)

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')

class MaterialXRemap(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXRemap, node_pos)

        self.input_high_default = MaterialExpressionEditorPropertyImpl(self, 'input_high_default', 'float')
        self.input_low_default = MaterialExpressionEditorPropertyImpl(self, 'input_low_default', 'float')
        self.target_high_default = MaterialExpressionEditorPropertyImpl(self, 'target_high_default', 'float')
        self.target_low_default = MaterialExpressionEditorPropertyImpl(self, 'target_low_default', 'float')

class MaterialXRotate2D(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXRotate2D, node_pos)

        self.const_rotation_angle = MaterialExpressionEditorPropertyImpl(self, 'const_rotation_angle', 'float')

class MaterialXScreen(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXScreen, node_pos)

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')

class MaterialXSplitLeftRight(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXSplitLeftRight, node_pos)

        self.const_center = MaterialExpressionEditorPropertyImpl(self, 'const_center', 'float')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')

class MaterialXSplitTopBottom(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXSplitTopBottom, node_pos)

        self.const_center = MaterialExpressionEditorPropertyImpl(self, 'const_center', 'float')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')

class MaterialXSwizzle(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXSwizzle, node_pos)

        self.channels = MaterialExpressionEditorPropertyImpl(self, 'channels', 'str')

class MaterialXTextureSampleParameterBlur(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXTextureSampleParameterBlur, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.filter = MaterialExpressionEditorPropertyImpl(self, 'filter', 'MaterialXTextureSampleBlurFilter')
        self.filter_offset = MaterialExpressionEditorPropertyImpl(self, 'filter_offset', 'float')
        self.filter_size = MaterialExpressionEditorPropertyImpl(self, 'filter_size', 'float')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.kernel_size = MaterialExpressionEditorPropertyImpl(self, 'kernel_size', 'MAterialXTextureSampleBlurKernel')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

class MaterialXUnpremult(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMaterialXUnpremult, node_pos)

class Max(MaterialExpressionImpl):
    def __init__(self, a, b, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMax, node_pos)

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if a is not None:
            if isinstance(a, float):
                self.const_a.set(a)
            else:
                self.a.comesFrom(a)
        if b is not None:
            if isinstance(b, float):
                self.const_b.set(b)
            else:
                self.b.comesFrom(b)

class Min(MaterialExpressionImpl):
    def __init__(self, a, b, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMin, node_pos)

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if a is not None:
            if isinstance(a, float):
                self.const_a.set(a)
            else:
                self.a.comesFrom(a)
        if b is not None:
            if isinstance(b, float):
                self.const_b.set(b)
            else:
                self.b.comesFrom(b)

class Multiply(MaterialExpressionImpl):
    def __init__(self, a, b, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionMultiply, node_pos)

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if a is not None:
            if isinstance(a, float):
                self.const_a.set(a)
            else:
                self.a.comesFrom(a)
        if b is not None:
            if isinstance(b, float):
                self.const_b.set(b)
            else:
                self.b.comesFrom(b)

class NamedRerouteBase(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionNamedRerouteBase, node_pos)

class NamedRerouteDeclaration(NamedRerouteDeclarationBase):
    def __init__(self, name, input, nodeColor = None, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionNamedRerouteDeclaration, node_pos)

        self.name = MaterialExpressionEditorPropertyImpl(self, 'name', 'Name')
        self.nodeNolor = MaterialExpressionEditorPropertyImpl(self, 'nodeNolor', 'LinearColor')
        self.variableGuid = MaterialExpressionEditorPropertyImpl(self, 'variableGuid', 'Guid')

        self.variableGuid = InSocketImpl(self, 'VariableGuid', 'StructProperty')
        if name is not None:
            self.name.set(name)
        if input is not None:
            self.input.comesFrom(input)
            input.rt = self
        if nodeColor is not None:
            self.nodeColor.set(nodeColor)

class NamedRerouteUsage(MaterialExpressionImpl):
    def __init__(self, declarationGuid, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionNamedRerouteUsage, node_pos)

        self.declarationGuid = MaterialExpressionEditorPropertyImpl(self, 'declarationGuid', 'Guid')
        if declarationGuid is not None:
            self.declarationGuid.set(declarationGuid)

class NaniteReplace(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionNaniteReplace, node_pos)

class Noise(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionNoise, node_pos)

        self.level_scale = MaterialExpressionEditorPropertyImpl(self, 'level_scale', 'float')
        self.levels = MaterialExpressionEditorPropertyImpl(self, 'levels', 'int32')
        self.noise_function = MaterialExpressionEditorPropertyImpl(self, 'noise_function', 'NoiseFunction')
        self.output_max = MaterialExpressionEditorPropertyImpl(self, 'output_max', 'float')
        self.output_min = MaterialExpressionEditorPropertyImpl(self, 'output_min', 'float')
        self.quality = MaterialExpressionEditorPropertyImpl(self, 'quality', 'int32')
        self.repeat_size = MaterialExpressionEditorPropertyImpl(self, 'repeat_size', 'uint32')
        self.scale = MaterialExpressionEditorPropertyImpl(self, 'scale', 'float')
        self.tiling = MaterialExpressionEditorPropertyImpl(self, 'tiling', 'bool')
        self.turbulence = MaterialExpressionEditorPropertyImpl(self, 'turbulence', 'bool')

        self.position = InSocketImpl(self, 'Position', 'StructProperty')
        self.filterWidth = InSocketImpl(self, 'FilterWidth', 'StructProperty')

class Normalize(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionNormalize, node_pos)

        self.vectorInput = InSocketImpl(self, 'VectorInput', 'StructProperty')

class ObjectBounds(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionObjectBounds, node_pos)

class ObjectLocalBounds(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionObjectLocalBounds, node_pos)

class ObjectOrientation(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionObjectOrientation, node_pos)

class ObjectPositionWS(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionObjectPositionWS, node_pos)

        self.origin_type = MaterialExpressionEditorPropertyImpl(self, 'origin_type', 'PositionOrigin')

class ObjectRadius(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionObjectRadius, node_pos)

class OneMinus(MaterialExpressionImpl):
    def __init__(self, input, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionOneMinus, node_pos)
        if input is not None:
            self.input.comesFrom(input)

class Panner(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPanner, node_pos)

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint32')
        self.fractional_part = MaterialExpressionEditorPropertyImpl(self, 'fractional_part', 'bool')
        self.speed_x = MaterialExpressionEditorPropertyImpl(self, 'speed_x', 'float')
        self.speed_y = MaterialExpressionEditorPropertyImpl(self, 'speed_y', 'float')

        self.coordinate = InSocketImpl(self, 'Coordinate', 'StructProperty')
        self.time = InSocketImpl(self, 'Time', 'StructProperty')
        self.speed = InSocketImpl(self, 'Speed', 'StructProperty')

class Parameter(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParameter, node_pos)

        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')

class ParticleColor(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleColor, node_pos)

class ParticleDirection(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleDirection, node_pos)

class ParticleMacroUV(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleMacroUV, node_pos)

class ParticleMotionBlurFade(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleMotionBlurFade, node_pos)

class ParticlePositionWS(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticlePositionWS, node_pos)

        self.origin_type = MaterialExpressionEditorPropertyImpl(self, 'origin_type', 'PositionOrigin')

class ParticleRadius(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleRadius, node_pos)

class ParticleRandom(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleRandom, node_pos)

class ParticleRelativeTime(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleRelativeTime, node_pos)

class ParticleSize(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleSize, node_pos)

class ParticleSpeed(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleSpeed, node_pos)

class ParticleSpriteRotation(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleSpriteRotation, node_pos)

class ParticleSubUV(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleSubUV, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.blend = MaterialExpressionEditorPropertyImpl(self, 'blend', 'bool')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')

class ParticleSubUVProperties(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionParticleSubUVProperties, node_pos)

class PathTracingBufferTexture(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPathTracingBufferTexture, node_pos)

        self.path_tracing_buffer_texture_id = MaterialExpressionEditorPropertyImpl(self, 'path_tracing_buffer_texture_id', 'PathTracingBufferTextureId')

class PathTracingQualitySwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPathTracingQualitySwitch, node_pos)

class PathTracingRayTypeSwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPathTracingRayTypeSwitch, node_pos)

class PerInstanceCustomData(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPerInstanceCustomData, node_pos)

        self.const_default_value = MaterialExpressionEditorPropertyImpl(self, 'const_default_value', 'float')
        self.data_index = MaterialExpressionEditorPropertyImpl(self, 'data_index', 'uint32')

        self.defaultValue = InSocketImpl(self, 'DefaultValue', 'StructProperty')

class PerInstanceCustomData3Vector(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPerInstanceCustomData3Vector, node_pos)

        self.const_default_value = MaterialExpressionEditorPropertyImpl(self, 'const_default_value', 'LinearColor')
        self.data_index = MaterialExpressionEditorPropertyImpl(self, 'data_index', 'uint32')

class PerInstanceFadeAmount(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPerInstanceFadeAmount, node_pos)

class PerInstanceRandom(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPerInstanceRandom, node_pos)

class PinBase(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPinBase, node_pos)

        self.reroute_pins = MaterialExpressionEditorPropertyImpl(self, 'reroute_pins', 'Array[CompositeReroute]')

class PixelDepth(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPixelDepth, node_pos)

class PixelNormalWS(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPixelNormalWS, node_pos)

class Power(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPower, node_pos)

        self.const_exponent = MaterialExpressionEditorPropertyImpl(self, 'const_exponent', 'float')

        self.base = InSocketImpl(self, 'Base', 'StructProperty')
        self.exponent = InSocketImpl(self, 'Exponent', 'StructProperty')

class PreSkinnedLocalBounds(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPreSkinnedLocalBounds, node_pos)

class PreSkinnedNormal(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPreSkinnedNormal, node_pos)

class PreSkinnedPosition(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPreSkinnedPosition, node_pos)

class PrecomputedAOMask(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPrecomputedAOMask, node_pos)

class PreviousFrameSwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionPreviousFrameSwitch, node_pos)

        self.currentFrame = InSocketImpl(self, 'CurrentFrame', 'StructProperty')
        self.previousFrame = InSocketImpl(self, 'PreviousFrame', 'StructProperty')

class QualitySwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionQualitySwitch, node_pos)

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.low = InSocketImpl(self, 'Low', 'StructProperty')
        self.high = InSocketImpl(self, 'High', 'StructProperty')
        self.medium = InSocketImpl(self, 'Medium', 'StructProperty')
        self.epic = InSocketImpl(self, 'Epic', 'StructProperty')

class RayTracingQualitySwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionRayTracingQualitySwitch, node_pos)

        self.normal = InSocketImpl(self, 'Normal', 'StructProperty')
        self.rayTraced = InSocketImpl(self, 'RayTraced', 'StructProperty')

class ReflectionCapturePassSwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionReflectionCapturePassSwitch, node_pos)

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.reflection = InSocketImpl(self, 'Reflection', 'StructProperty')

class ReflectionVectorWS(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionReflectionVectorWS, node_pos)

        self.normalize_custom_world_normal = MaterialExpressionEditorPropertyImpl(self, 'normalize_custom_world_normal', 'bool')

        self.customWorldNormal = InSocketImpl(self, 'CustomWorldNormal', 'StructProperty')

class Reroute(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionReroute, node_pos)

class RerouteBase(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionRerouteBase, node_pos)

class RgbToHsv(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionRgbToHsv, node_pos)

class RotateAboutAxis(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionRotateAboutAxis, node_pos)

        self.period = MaterialExpressionEditorPropertyImpl(self, 'period', 'float')

        self.normalizedRotationAxis = InSocketImpl(self, 'NormalizedRotationAxis', 'StructProperty')
        self.rotationAngle = InSocketImpl(self, 'RotationAngle', 'StructProperty')
        self.pivotPoint = InSocketImpl(self, 'PivotPoint', 'StructProperty')
        self.position = InSocketImpl(self, 'Position', 'StructProperty')

class Rotator(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionRotator, node_pos)

        self.center_x = MaterialExpressionEditorPropertyImpl(self, 'center_x', 'float')
        self.center_y = MaterialExpressionEditorPropertyImpl(self, 'center_y', 'float')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint32')
        self.speed = MaterialExpressionEditorPropertyImpl(self, 'speed', 'float')

        self.coordinate = InSocketImpl(self, 'Coordinate', 'StructProperty')
        self.time = InSocketImpl(self, 'Time', 'StructProperty')

class Round(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionRound, node_pos)

class RuntimeVirtualTextureOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionRuntimeVirtualTextureOutput, node_pos)

        self.baseColor = InSocketImpl(self, 'BaseColor', 'StructProperty')
        self.specular = InSocketImpl(self, 'Specular', 'StructProperty')
        self.roughness = InSocketImpl(self, 'Roughness', 'StructProperty')
        self.normal = InSocketImpl(self, 'Normal', 'StructProperty')
        self.worldHeight = InSocketImpl(self, 'WorldHeight', 'StructProperty')
        self.opacity = InSocketImpl(self, 'Opacity', 'StructProperty')
        self.mask = InSocketImpl(self, 'Mask', 'StructProperty')

class RuntimeVirtualTextureReplace(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionRuntimeVirtualTextureReplace, node_pos)

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.virtualTextureOutput = InSocketImpl(self, 'VirtualTextureOutput', 'StructProperty')

class RuntimeVirtualTextureSample(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionRuntimeVirtualTextureSample, node_pos)

        self.adaptive = MaterialExpressionEditorPropertyImpl(self, 'adaptive', 'bool')
        self.enable_feedback = MaterialExpressionEditorPropertyImpl(self, 'enable_feedback', 'bool')
        self.material_type = MaterialExpressionEditorPropertyImpl(self, 'material_type', 'RuntimeVirtualTextureMaterialType')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'RuntimeVirtualTextureMipValueMode')
        self.single_physical_space = MaterialExpressionEditorPropertyImpl(self, 'single_physical_space', 'bool')
        self.texture_address_mode = MaterialExpressionEditorPropertyImpl(self, 'texture_address_mode', 'RuntimeVirtualTextureTextureAddressMode')
        self.virtual_texture = MaterialExpressionEditorPropertyImpl(self, 'virtual_texture', 'RuntimeVirtualTexture')

        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')
        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')
        self.mipValue = InSocketImpl(self, 'MipValue', 'StructProperty')

class RuntimeVirtualTextureSampleParameter(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionRuntimeVirtualTextureSampleParameter, node_pos)

        self.adaptive = MaterialExpressionEditorPropertyImpl(self, 'adaptive', 'bool')
        self.enable_feedback = MaterialExpressionEditorPropertyImpl(self, 'enable_feedback', 'bool')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.material_type = MaterialExpressionEditorPropertyImpl(self, 'material_type', 'RuntimeVirtualTextureMaterialType')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'RuntimeVirtualTextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.single_physical_space = MaterialExpressionEditorPropertyImpl(self, 'single_physical_space', 'bool')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture_address_mode = MaterialExpressionEditorPropertyImpl(self, 'texture_address_mode', 'RuntimeVirtualTextureTextureAddressMode')
        self.virtual_texture = MaterialExpressionEditorPropertyImpl(self, 'virtual_texture', 'RuntimeVirtualTexture')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')
        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')
        self.mipValue = InSocketImpl(self, 'MipValue', 'StructProperty')

class SamplePhysicsIntegerField(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSamplePhysicsIntegerField, node_pos)

        self.field_target = MaterialExpressionEditorPropertyImpl(self, 'field_target', 'FieldIntegerType')

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')

class SamplePhysicsScalarField(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSamplePhysicsScalarField, node_pos)

        self.field_target = MaterialExpressionEditorPropertyImpl(self, 'field_target', 'FieldScalarType')

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')

class SamplePhysicsVectorField(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSamplePhysicsVectorField, node_pos)

        self.field_target = MaterialExpressionEditorPropertyImpl(self, 'field_target', 'FieldVectorType')

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')

class Saturate(MaterialExpressionImpl):
    def __init__(self, input, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSaturate, node_pos)
        if input is not None:
            self.input.comesFrom(input)

class ScalarParameter(MaterialExpressionImpl):
    def __init__(self, parameter_name, default_value, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionScalarParameter, node_pos)

        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'float')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.primitive_data_index = MaterialExpressionEditorPropertyImpl(self, 'primitive_data_index', 'uint8')
        self.slider_max = MaterialExpressionEditorPropertyImpl(self, 'slider_max', 'float')
        self.slider_min = MaterialExpressionEditorPropertyImpl(self, 'slider_min', 'float')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = MaterialExpressionEditorPropertyImpl(self, 'use_custom_primitive_data', 'bool')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class SceneColor(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSceneColor, node_pos)

        self.const_input = MaterialExpressionEditorPropertyImpl(self, 'const_input', 'Vector2D')
        self.input_mode = MaterialExpressionEditorPropertyImpl(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        self.offsetFraction = InSocketImpl(self, 'OffsetFraction', 'StructProperty')
        self.constInput = InSocketImpl(self, 'ConstInput', 'StructProperty')

class SceneDepth(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSceneDepth, node_pos)

        self.const_input = MaterialExpressionEditorPropertyImpl(self, 'const_input', 'Vector2D')
        self.input_mode = MaterialExpressionEditorPropertyImpl(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')
        self.constInput = InSocketImpl(self, 'ConstInput', 'StructProperty')

class SceneDepthWithoutWater(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSceneDepthWithoutWater, node_pos)

        self.const_input = MaterialExpressionEditorPropertyImpl(self, 'const_input', 'Vector2D')
        self.fallback_depth = MaterialExpressionEditorPropertyImpl(self, 'fallback_depth', 'float')
        self.input_mode = MaterialExpressionEditorPropertyImpl(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        self.constInput = InSocketImpl(self, 'ConstInput', 'StructProperty')

class SceneTexelSize(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSceneTexelSize, node_pos)

class SceneTexture(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSceneTexture, node_pos)

        self.filtered = MaterialExpressionEditorPropertyImpl(self, 'filtered', 'bool')
        self.scene_texture_id = MaterialExpressionEditorPropertyImpl(self, 'scene_texture_id', 'SceneTextureId')

        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')

class ScreenPosition(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionScreenPosition, node_pos)

class SetLocal(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSetLocal, node_pos)

        self.local_name = MaterialExpressionEditorPropertyImpl(self, 'local_name', 'Name')

class SetMaterialAttributes(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSetMaterialAttributes, node_pos)

        self.attribute_set_types = MaterialExpressionEditorPropertyImpl(self, 'attribute_set_types', 'Array[Guid]')

        self.materialAttributes = InSocketImpl(self, 'MaterialAttributes', 'StructProperty')
        self.baseColor = InSocketImpl(self, 'BaseColor', 'StructProperty')
        self.metallic = InSocketImpl(self, 'Metallic', 'StructProperty')
        self.specular = InSocketImpl(self, 'Specular', 'StructProperty')
        self.roughness = InSocketImpl(self, 'Roughness', 'StructProperty')
        self.anisotropy = InSocketImpl(self, 'Anisotropy', 'StructProperty')
        self.emissiveColor = InSocketImpl(self, 'EmissiveColor', 'StructProperty')
        self.opacity = InSocketImpl(self, 'Opacity', 'StructProperty')
        self.opacityMask = InSocketImpl(self, 'OpacityMask', 'StructProperty')
        self.normal = InSocketImpl(self, 'Normal', 'StructProperty')
        self.tangent = InSocketImpl(self, 'Tangent', 'StructProperty')
        self.worldPositionOffset = InSocketImpl(self, 'WorldPositionOffset', 'StructProperty')
        self.worldDisplacement = InSocketImpl(self, 'WorldDisplacement', 'StructProperty')
        self.tessellationMultiplier = InSocketImpl(self, 'TessellationMultiplier', 'StructProperty')
        self.subsurfaceColor = InSocketImpl(self, 'SubsurfaceColor', 'StructProperty')
        self.clearCoat = InSocketImpl(self, 'ClearCoat', 'StructProperty')
        self.clearCoatRoughness = InSocketImpl(self, 'ClearCoatRoughness', 'StructProperty')
        self.ambientOcclusion = InSocketImpl(self, 'AmbientOcclusion', 'StructProperty')
        self.refraction = InSocketImpl(self, 'Refraction', 'StructProperty')
        self.customizedUVs = InSocketImpl(self, 'CustomizedUVs', 'StructProperty')
        self.pixelDepthOffset = InSocketImpl(self, 'PixelDepthOffset', 'StructProperty')
        self.shadingModel = InSocketImpl(self, 'ShadingModel', 'StructProperty')

class ShaderStageSwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionShaderStageSwitch, node_pos)

        self.pixelShader = InSocketImpl(self, 'PixelShader', 'StructProperty')
        self.vertexShader = InSocketImpl(self, 'VertexShader', 'StructProperty')

class ShadingModel(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionShadingModel, node_pos)

        self.shading_model = MaterialExpressionEditorPropertyImpl(self, 'shading_model', 'MaterialShadingModel')

class ShadingPathSwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionShadingPathSwitch, node_pos)

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.inputs = InSocketImpl(self, 'Inputs', 'StructProperty')

class ShadowReplace(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionShadowReplace, node_pos)

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.shadow = InSocketImpl(self, 'Shadow', 'StructProperty')

class Sign(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSign, node_pos)

class Sine(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSine, node_pos)

        self.period = MaterialExpressionEditorPropertyImpl(self, 'period', 'float')

class SingleLayerWaterMaterialOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSingleLayerWaterMaterialOutput, node_pos)

        self.scatteringCoefficients = InSocketImpl(self, 'ScatteringCoefficients', 'StructProperty')
        self.absorptionCoefficients = InSocketImpl(self, 'AbsorptionCoefficients', 'StructProperty')
        self.phaseG = InSocketImpl(self, 'PhaseG', 'StructProperty')
        self.colorScaleBehindWater = InSocketImpl(self, 'ColorScaleBehindWater', 'StructProperty')

class SkyAtmosphereAerialPerspective(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSkyAtmosphereAerialPerspective, node_pos)

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')

class SkyAtmosphereDistantLightScatteredLuminance(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSkyAtmosphereDistantLightScatteredLuminance, node_pos)

class SkyAtmosphereLightDirection(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSkyAtmosphereLightDirection, node_pos)

        self.light_index = MaterialExpressionEditorPropertyImpl(self, 'light_index', 'int32')

class SkyAtmosphereLightDiskLuminance(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSkyAtmosphereLightDiskLuminance, node_pos)

        self.light_index = MaterialExpressionEditorPropertyImpl(self, 'light_index', 'int32')

class SkyAtmosphereLightIlluminance(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSkyAtmosphereLightIlluminance, node_pos)

        self.light_index = MaterialExpressionEditorPropertyImpl(self, 'light_index', 'int32')

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')

class SkyAtmosphereViewLuminance(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSkyAtmosphereViewLuminance, node_pos)

class SkyLightEnvMapSample(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSkyLightEnvMapSample, node_pos)

class SmoothStep(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSmoothStep, node_pos)

        self.const_max = MaterialExpressionEditorPropertyImpl(self, 'const_max', 'float')
        self.const_min = MaterialExpressionEditorPropertyImpl(self, 'const_min', 'float')
        self.const_value = MaterialExpressionEditorPropertyImpl(self, 'const_value', 'float')

        self.min = InSocketImpl(self, 'Min', 'StructProperty')
        self.max = InSocketImpl(self, 'Max', 'StructProperty')
        self.value = InSocketImpl(self, 'Value', 'StructProperty')

class Sobol(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSobol, node_pos)

        self.const_index = MaterialExpressionEditorPropertyImpl(self, 'const_index', 'uint32')
        self.const_seed = MaterialExpressionEditorPropertyImpl(self, 'const_seed', 'Vector2D')

        self.cell = InSocketImpl(self, 'Cell', 'StructProperty')
        self.index = InSocketImpl(self, 'Index', 'StructProperty')
        self.seed = InSocketImpl(self, 'Seed', 'StructProperty')
        self.constSeed = InSocketImpl(self, 'ConstSeed', 'StructProperty')

class SparseVolumeTextureBase(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSparseVolumeTextureBase, node_pos)

        self.sparse_volume_texture = MaterialExpressionEditorPropertyImpl(self, 'sparse_volume_texture', 'SparseVolumeTexture')

class SparseVolumeTextureObject(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSparseVolumeTextureObject, node_pos)

        self.sparse_volume_texture = MaterialExpressionEditorPropertyImpl(self, 'sparse_volume_texture', 'SparseVolumeTexture')

class SparseVolumeTextureObjectParameter(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSparseVolumeTextureObjectParameter, node_pos)

        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.sparse_volume_texture = MaterialExpressionEditorPropertyImpl(self, 'sparse_volume_texture', 'SparseVolumeTexture')

class SparseVolumeTextureSample(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSparseVolumeTextureSample, node_pos)

        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sparse_volume_texture = MaterialExpressionEditorPropertyImpl(self, 'sparse_volume_texture', 'SparseVolumeTexture')

class SparseVolumeTextureSampleParameter(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSparseVolumeTextureSampleParameter, node_pos)

        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.sparse_volume_texture = MaterialExpressionEditorPropertyImpl(self, 'sparse_volume_texture', 'SparseVolumeTexture')

class SpeedTree(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSpeedTree, node_pos)

        self.accurate_wind_velocities = MaterialExpressionEditorPropertyImpl(self, 'accurate_wind_velocities', 'bool')
        self.billboard_threshold = MaterialExpressionEditorPropertyImpl(self, 'billboard_threshold', 'float')
        self.geometry_type = MaterialExpressionEditorPropertyImpl(self, 'geometry_type', 'SpeedTreeGeometryType')
        self.lod_type = MaterialExpressionEditorPropertyImpl(self, 'lod_type', 'SpeedTreeLODType')
        self.wind_type = MaterialExpressionEditorPropertyImpl(self, 'wind_type', 'SpeedTreeWindType')

        self.geometryInput = InSocketImpl(self, 'GeometryInput', 'StructProperty')
        self.windInput = InSocketImpl(self, 'WindInput', 'StructProperty')
        self.lODInput = InSocketImpl(self, 'LODInput', 'StructProperty')
        self.extraBendWS = InSocketImpl(self, 'ExtraBendWS', 'StructProperty')

class SphereMask(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSphereMask, node_pos)

        self.attenuation_radius = MaterialExpressionEditorPropertyImpl(self, 'attenuation_radius', 'float')
        self.hardness_percent = MaterialExpressionEditorPropertyImpl(self, 'hardness_percent', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        self.radius = InSocketImpl(self, 'Radius', 'StructProperty')
        self.hardness = InSocketImpl(self, 'Hardness', 'StructProperty')

class SphericalParticleOpacity(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSphericalParticleOpacity, node_pos)

        self.constant_density = MaterialExpressionEditorPropertyImpl(self, 'constant_density', 'float')

        self.density = InSocketImpl(self, 'Density', 'StructProperty')

class SpriteTextureSampler(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSpriteTextureSampler, node_pos)

        self.additional_slot_index = MaterialExpressionEditorPropertyImpl(self, 'additional_slot_index', 'int32')
        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sample_additional_textures = MaterialExpressionEditorPropertyImpl(self, 'sample_additional_textures', 'bool')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.slot_display_name = MaterialExpressionEditorPropertyImpl(self, 'slot_display_name', 'Text')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

class SquareRoot(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSquareRoot, node_pos)

class StaticBool(MaterialExpressionImpl):
    def __init__(self, value, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStaticBool, node_pos)

        self.value = MaterialExpressionEditorPropertyImpl(self, 'Value', 'bool')
        if value is not None:
            self.value.set(value)

class StaticBoolParameter(MaterialExpressionImpl):
    def __init__(self, parameter_name, default_value, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStaticBoolParameter, node_pos)

        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'bool')
        self.dynamic_branch = MaterialExpressionEditorPropertyImpl(self, 'dynamic_branch', 'bool')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class StaticComponentMaskParameter(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStaticComponentMaskParameter, node_pos)

        self.default_a = MaterialExpressionEditorPropertyImpl(self, 'default_a', 'bool')
        self.default_b = MaterialExpressionEditorPropertyImpl(self, 'default_b', 'bool')
        self.default_g = MaterialExpressionEditorPropertyImpl(self, 'default_g', 'bool')
        self.default_r = MaterialExpressionEditorPropertyImpl(self, 'default_r', 'bool')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')

class StaticSwitch(MaterialExpressionImpl):
    def __init__(self, true, false, value, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStaticSwitch, node_pos)

        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'bool')

        self.true = InSocketImpl(self, 'True', 'StructProperty')
        self.false = InSocketImpl(self, 'False', 'StructProperty')
        self.value = InSocketImpl(self, 'Value', 'StructProperty')
        if true is not None:
            self.true.comesFrom(true)
        if false is not None:
            self.false.comesFrom(false)
        if value is not None:
            self.value.comesFrom(value)

class StaticSwitchParameter(MaterialExpressionImpl):
    def __init__(self, parameter_name, default_value, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStaticSwitchParameter, node_pos)

        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'bool')
        self.dynamic_branch = MaterialExpressionEditorPropertyImpl(self, 'dynamic_branch', 'bool')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class Step(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStep, node_pos)

        self.const_x = MaterialExpressionEditorPropertyImpl(self, 'const_x', 'float')
        self.const_y = MaterialExpressionEditorPropertyImpl(self, 'const_y', 'float')

        self.y = InSocketImpl(self, 'Y', 'StructProperty')
        self.x = InSocketImpl(self, 'X', 'StructProperty')

class StrataAdd(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataAdd, node_pos)

        self.use_parameter_blending = MaterialExpressionEditorPropertyImpl(self, 'use_parameter_blending', 'bool')

class StrataBSDF(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataBSDF, node_pos)

class StrataConvertToDecal(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataConvertToDecal, node_pos)

class StrataEyeBSDF(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataEyeBSDF, node_pos)

        self.subsurface_profile = MaterialExpressionEditorPropertyImpl(self, 'subsurface_profile', 'SubsurfaceProfile')

class StrataHairBSDF(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataHairBSDF, node_pos)

class StrataHazinessToSecondaryRoughness(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataHazinessToSecondaryRoughness, node_pos)

class StrataHorizontalMixing(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataHorizontalMixing, node_pos)

        self.use_parameter_blending = MaterialExpressionEditorPropertyImpl(self, 'use_parameter_blending', 'bool')

class StrataLegacyConversion(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataLegacyConversion, node_pos)

        self.subsurface_profile = MaterialExpressionEditorPropertyImpl(self, 'subsurface_profile', 'SubsurfaceProfile')

class StrataLightFunction(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataLightFunction, node_pos)

class StrataMetalnessToDiffuseAlbedoF0(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataMetalnessToDiffuseAlbedoF0, node_pos)

class StrataPostProcess(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataPostProcess, node_pos)

class StrataSimpleClearCoatBSDF(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataSimpleClearCoatBSDF, node_pos)

class StrataSingleLayerWaterBSDF(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataSingleLayerWaterBSDF, node_pos)

class StrataSlabBSDF(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataSlabBSDF, node_pos)

        self.specular_profile = MaterialExpressionEditorPropertyImpl(self, 'specular_profile', 'SpecularProfile')
        self.subsurface_profile = MaterialExpressionEditorPropertyImpl(self, 'subsurface_profile', 'SubsurfaceProfile')
        self.use_sss_diffusion = MaterialExpressionEditorPropertyImpl(self, 'use_sss_diffusion', 'bool')

class StrataThinFilm(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataThinFilm, node_pos)

class StrataTransmittanceToMFP(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataTransmittanceToMFP, node_pos)

class StrataUI(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataUI, node_pos)

class StrataUnlitBSDF(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataUnlitBSDF, node_pos)

class StrataUtilityBase(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataUtilityBase, node_pos)

class StrataVerticalLayering(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataVerticalLayering, node_pos)

        self.use_parameter_blending = MaterialExpressionEditorPropertyImpl(self, 'use_parameter_blending', 'bool')

class StrataVolumetricFogCloudBSDF(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataVolumetricFogCloudBSDF, node_pos)

class StrataWeight(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionStrataWeight, node_pos)

class SubsurfaceMediumMaterialOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSubsurfaceMediumMaterialOutput, node_pos)

class Subtract(MaterialExpressionImpl):
    def __init__(self, a, b, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSubtract, node_pos)

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if a is not None:
            if isinstance(a, float):
                self.const_a.set(a)
            else:
                self.a.comesFrom(a)
        if b is not None:
            if isinstance(b, float):
                self.const_b.set(b)
            else:
                self.b.comesFrom(b)

class Switch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionSwitch, node_pos)

        self.const_default = MaterialExpressionEditorPropertyImpl(self, 'const_default', 'float')
        self.const_switch_value = MaterialExpressionEditorPropertyImpl(self, 'const_switch_value', 'float')
        self.description = MaterialExpressionEditorPropertyImpl(self, 'description', 'str')
        self.inputs = MaterialExpressionEditorPropertyImpl(self, 'inputs', 'Array[SwitchCustomInput]')

class Tangent(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTangent, node_pos)

        self.period = MaterialExpressionEditorPropertyImpl(self, 'period', 'float')

class TangentOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTangentOutput, node_pos)

class TemporalSobol(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTemporalSobol, node_pos)

        self.const_index = MaterialExpressionEditorPropertyImpl(self, 'const_index', 'uint32')
        self.const_seed = MaterialExpressionEditorPropertyImpl(self, 'const_seed', 'Vector2D')

        self.index = InSocketImpl(self, 'Index', 'StructProperty')
        self.seed = InSocketImpl(self, 'Seed', 'StructProperty')
        self.constSeed = InSocketImpl(self, 'ConstSeed', 'StructProperty')

class TextureBase(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureBase, node_pos)

        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

class TextureCoordinate(MaterialExpressionImpl):
    def __init__(self, u_tiling, v_tiling, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureCoordinate, node_pos)

        self.coordinate_index = MaterialExpressionEditorPropertyImpl(self, 'coordinate_index', 'int32')
        self.u_tiling = MaterialExpressionEditorPropertyImpl(self, 'u_tiling', 'float')
        self.un_mirror_u = MaterialExpressionEditorPropertyImpl(self, 'un_mirror_u', 'bool')
        self.un_mirror_v = MaterialExpressionEditorPropertyImpl(self, 'un_mirror_v', 'bool')
        self.v_tiling = MaterialExpressionEditorPropertyImpl(self, 'v_tiling', 'float')
        if u_tiling is not None:
            self.u_tiling.set(u_tiling)
        if v_tiling is not None:
            self.v_tiling.set(v_tiling)

class TextureObject(MaterialExpressionImpl):
    def __init__(self, sampler_type, texture, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureObject, node_pos)

        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')
        if sampler_type is not None:
            self.sampler_type.set(sampler_type)
        if texture is not None:
            self.texture.set(texture)

class TextureObjectParameter(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureObjectParameter, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')

class TextureProperty(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureProperty, node_pos)

        self.property_ = MaterialExpressionEditorPropertyImpl(self, 'property_', 'MaterialExposedTextureProperty')

        self.textureObject = InSocketImpl(self, 'TextureObject', 'StructProperty')

class TextureSample(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureSample, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

        self.UVs = InSocketImpl(self, 'UVs', 'StructProperty')
        self.tex = InSocketImpl(self, 'Tex', 'StructProperty')
        self.applyViewMipBias = InSocketImpl(self, 'ApplyViewMipBias', 'StructProperty')

        self.RGB = OutSocketImpl(self, 'RGB', 'StructProperty')
        self.r = OutSocketImpl(self, 'R', 'StructProperty')
        self.g = OutSocketImpl(self, 'G', 'StructProperty')
        self.b = OutSocketImpl(self, 'B', 'StructProperty')
        self.a = OutSocketImpl(self, 'A', 'StructProperty')
        self.RGBA = OutSocketImpl(self, 'RGBA', 'StructProperty')

class TextureSampleParameter(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureSampleParameter, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')

class TextureSampleParameter2D(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureSampleParameter2D, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')

class TextureSampleParameter2DArray(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureSampleParameter2DArray, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')

class TextureSampleParameterCube(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureSampleParameterCube, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')

class TextureSampleParameterCubeArray(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureSampleParameterCubeArray, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

class TextureSampleParameterSubUV(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureSampleParameterSubUV, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.blend = MaterialExpressionEditorPropertyImpl(self, 'blend', 'bool')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')

class TextureSampleParameterVolume(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTextureSampleParameterVolume, node_pos)

        self.automatic_view_mip_bias = MaterialExpressionEditorPropertyImpl(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_mip_value = MaterialExpressionEditorPropertyImpl(self, 'const_mip_value', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = MaterialExpressionEditorPropertyImpl(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')

class ThinTranslucentMaterialOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionThinTranslucentMaterialOutput, node_pos)

        self.transmittanceColor = InSocketImpl(self, 'TransmittanceColor', 'StructProperty')

class Time(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTime, node_pos)

        self.ignore_pause = MaterialExpressionEditorPropertyImpl(self, 'ignore_pause', 'bool')
        self.override_period = MaterialExpressionEditorPropertyImpl(self, 'override_period', 'bool')
        self.period = MaterialExpressionEditorPropertyImpl(self, 'period', 'float')

class Transform(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTransform, node_pos)

        self.transform_source_type = MaterialExpressionEditorPropertyImpl(self, 'transform_source_type', 'MaterialVectorCoordTransformSource')
        self.transform_type = MaterialExpressionEditorPropertyImpl(self, 'transform_type', 'MaterialVectorCoordTransform')

class TransformPosition(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTransformPosition, node_pos)

        self.transform_source_type = MaterialExpressionEditorPropertyImpl(self, 'transform_source_type', 'MaterialPositionTransformSource')
        self.transform_type = MaterialExpressionEditorPropertyImpl(self, 'transform_type', 'MaterialPositionTransformSource')

class Truncate(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTruncate, node_pos)

class TruncateLWC(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTruncateLWC, node_pos)

class TwoSidedSign(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionTwoSidedSign, node_pos)

class VectorNoise(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVectorNoise, node_pos)

        self.noise_function = MaterialExpressionEditorPropertyImpl(self, 'noise_function', 'VectorNoiseFunction')
        self.quality = MaterialExpressionEditorPropertyImpl(self, 'quality', 'int32')
        self.tile_size = MaterialExpressionEditorPropertyImpl(self, 'tile_size', 'uint32')
        self.tiling = MaterialExpressionEditorPropertyImpl(self, 'tiling', 'bool')

        self.position = InSocketImpl(self, 'Position', 'StructProperty')

class VectorParameter(MaterialExpressionImpl):
    def __init__(self, parameter_name, default_value, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVectorParameter, node_pos)

        self.channel_names = MaterialExpressionEditorPropertyImpl(self, 'channel_names', 'ParameterChannelNames')
        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'LinearColor')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.primitive_data_index = MaterialExpressionEditorPropertyImpl(self, 'primitive_data_index', 'uint8')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = MaterialExpressionEditorPropertyImpl(self, 'use_custom_primitive_data', 'bool')

        self.defaultValue = InSocketImpl(self, 'DefaultValue', 'StructProperty')
        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')

        self.r = OutSocketImpl(self, 'r', 'StructProperty')
        self.g = OutSocketImpl(self, 'g', 'StructProperty')
        self.b = OutSocketImpl(self, 'b', 'StructProperty')
        self.a = OutSocketImpl(self, 'a', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class VertexColor(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVertexColor, node_pos)

class VertexInterpolator(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVertexInterpolator, node_pos)

class VertexNormalWS(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVertexNormalWS, node_pos)

class VertexTangentWS(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVertexTangentWS, node_pos)

class ViewProperty(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionViewProperty, node_pos)

        self.property_ = MaterialExpressionEditorPropertyImpl(self, 'property_', 'MaterialExposedViewProperty')

class ViewSize(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionViewSize, node_pos)

class VirtualTextureFeatureSwitch(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVirtualTextureFeatureSwitch, node_pos)

        self.no = InSocketImpl(self, 'No', 'StructProperty')
        self.yes = InSocketImpl(self, 'Yes', 'StructProperty')

class VolumetricAdvancedMaterialInput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVolumetricAdvancedMaterialInput, node_pos)

class VolumetricAdvancedMaterialOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVolumetricAdvancedMaterialOutput, node_pos)

        self.clamp_multi_scattering_contribution = MaterialExpressionEditorPropertyImpl(self, 'clamp_multi_scattering_contribution', 'bool')
        self.const_multi_scattering_contribution = MaterialExpressionEditorPropertyImpl(self, 'const_multi_scattering_contribution', 'float')
        self.const_multi_scattering_eccentricity = MaterialExpressionEditorPropertyImpl(self, 'const_multi_scattering_eccentricity', 'float')
        self.const_multi_scattering_occlusion = MaterialExpressionEditorPropertyImpl(self, 'const_multi_scattering_occlusion', 'float')
        self.const_phase_blend = MaterialExpressionEditorPropertyImpl(self, 'const_phase_blend', 'float')
        self.const_phase_g = MaterialExpressionEditorPropertyImpl(self, 'const_phase_g', 'float')
        self.const_phase_g2 = MaterialExpressionEditorPropertyImpl(self, 'const_phase_g2', 'float')
        self.gray_scale_material = MaterialExpressionEditorPropertyImpl(self, 'gray_scale_material', 'bool')
        self.ground_contribution = MaterialExpressionEditorPropertyImpl(self, 'ground_contribution', 'bool')
        self.multi_scattering_approximation_octave_count = MaterialExpressionEditorPropertyImpl(self, 'multi_scattering_approximation_octave_count', 'uint32')
        self.per_sample_phase_evaluation = MaterialExpressionEditorPropertyImpl(self, 'per_sample_phase_evaluation', 'bool')
        self.ray_march_volume_shadow = MaterialExpressionEditorPropertyImpl(self, 'ray_march_volume_shadow', 'bool')

        self.phaseG = InSocketImpl(self, 'PhaseG', 'StructProperty')
        self.phaseG2 = InSocketImpl(self, 'PhaseG2', 'StructProperty')
        self.phaseBlend = InSocketImpl(self, 'PhaseBlend', 'StructProperty')
        self.multiScatteringContribution = InSocketImpl(self, 'MultiScatteringContribution', 'StructProperty')
        self.multiScatteringOcclusion = InSocketImpl(self, 'MultiScatteringOcclusion', 'StructProperty')
        self.multiScatteringEccentricity = InSocketImpl(self, 'MultiScatteringEccentricity', 'StructProperty')
        self.conservativeDensity = InSocketImpl(self, 'ConservativeDensity', 'StructProperty')

class VolumetricCloudEmptySpaceSkippingInput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVolumetricCloudEmptySpaceSkippingInput, node_pos)

class VolumetricCloudEmptySpaceSkippingOutput(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionVolumetricCloudEmptySpaceSkippingOutput, node_pos)

class WhileLoop(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionWhileLoop, node_pos)

class WorldPosition(MaterialExpressionImpl):
    def __init__(self, node_pos: NodePos = None) -> None:
        super().__init__(unreal.MaterialExpressionWorldPosition, node_pos)

        self.world_position_shader_offset = MaterialExpressionEditorPropertyImpl(self, 'world_position_shader_offset', 'WorldPositionIncludedOffsets')