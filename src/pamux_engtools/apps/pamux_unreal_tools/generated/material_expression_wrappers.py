# This file is generated. Please do NOT modify.
import unreal
from pamux_unreal_tools.material_expression import MaterialExpression
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.utils.build_stack import NodePos

class Abs(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class AbsorptionMediumMaterialOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ActorPositionWS(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.origin_type = Property(self, 'origin_type', 'PositionOrigin')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Add(MaterialExpression):
    def __init__(self, a, b) -> None:
        super().__init__()

        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
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

class AntialiasedTextureMask(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.channel = Property(self, 'channel', 'TextureColorChannel')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')
        self.threshold = Property(self, 'threshold', 'float')

        self.UVs = InSocket(self, 'UVs', 'StructProperty')
        self.applyViewMipBias = InSocket(self, 'ApplyViewMipBias', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class AppendVector(MaterialExpression):
    def __init__(self, a, b) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if a is not None:
            self.a.comesFrom(a)
        if b is not None:
            self.b.comesFrom(b)

class Arccosine(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ArccosineFast(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Arcsine(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ArcsineFast(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Arctangent(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Arctangent2(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.y = InSocket(self, 'Y', 'StructProperty')
        self.x = InSocket(self, 'X', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Arctangent2Fast(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.y = InSocket(self, 'Y', 'StructProperty')
        self.x = InSocket(self, 'X', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ArctangentFast(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class AtmosphericFogColor(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class AtmosphericLightColor(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class AtmosphericLightVector(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class BentNormalCustomOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class BinaryOp(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class BlackBody(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.temp = InSocket(self, 'Temp', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class BlendMaterialAttributes(MaterialExpression):
    def __init__(self, a, b, alpha) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.pixel_attribute_blend_type = Property(self, 'pixel_attribute_blend_type', 'MaterialAttributeBlend')
        self.vertex_attribute_blend_type = Property(self, 'vertex_attribute_blend_type', 'MaterialAttributeBlend')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.alpha = InSocket(self, 'Alpha', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if a is not None:
            self.a.comesFrom(a)
        if b is not None:
            self.b.comesFrom(b)
        if alpha is not None:
            self.alpha.comesFrom(alpha)

class BreakMaterialAttributes(MaterialExpression):
    def __init__(self, input) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.baseColor = OutSocket(self, 'BaseColor', 'StructProperty')
        self.metallic = OutSocket(self, 'Metallic', 'StructProperty')
        self.specular = OutSocket(self, 'Specular', 'StructProperty')
        self.roughness = OutSocket(self, 'Roughness', 'StructProperty')
        self.anisotropy = OutSocket(self, 'Anisotropy', 'StructProperty')
        self.emissiveColor = OutSocket(self, 'EmissiveColor', 'StructProperty')
        self.opacity = OutSocket(self, 'Opacity', 'StructProperty')
        self.opacityMask = OutSocket(self, 'OpacityMask', 'StructProperty')
        self.normal = OutSocket(self, 'Normal', 'StructProperty')
        self.tangent = OutSocket(self, 'Tangent', 'StructProperty')
        self.worldPositionOffset = OutSocket(self, 'WorldPositionOffset', 'StructProperty')
        self.subsurfaceColor = OutSocket(self, 'SubsurfaceColor', 'StructProperty')
        self.clearCoat = OutSocket(self, 'ClearCoat', 'StructProperty')
        self.clearCoatRoughness = OutSocket(self, 'ClearCoatRoughness', 'StructProperty')
        self.ambientOcclusion = OutSocket(self, 'AmbientOcclusion', 'StructProperty')
        self.refraction = OutSocket(self, 'Refraction', 'StructProperty')
        self.customizedUV0 = OutSocket(self, 'CustomizedUV0', 'StructProperty')
        self.customizedUV1 = OutSocket(self, 'CustomizedUV1', 'StructProperty')
        self.customizedUV2 = OutSocket(self, 'CustomizedUV2', 'StructProperty')
        self.customizedUV3 = OutSocket(self, 'CustomizedUV3', 'StructProperty')
        self.customizedUV4 = OutSocket(self, 'CustomizedUV4', 'StructProperty')
        self.customizedUV5 = OutSocket(self, 'CustomizedUV5', 'StructProperty')
        self.customizedUV6 = OutSocket(self, 'CustomizedUV6', 'StructProperty')
        self.customizedUV7 = OutSocket(self, 'CustomizedUV7', 'StructProperty')
        self.pixelDepthOffset = OutSocket(self, 'PixelDepthOffset', 'StructProperty')
        self.shadingModel = OutSocket(self, 'ShadingModel', 'StructProperty')
        self.displacement = OutSocket(self, 'Displacement', 'StructProperty')
        if input is not None:
            self.input.comesFrom(input)

class BumpOffset(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_coordinate = Property(self, 'const_coordinate', 'uint32')
        self.desc = Property(self, 'desc', 'str')
        self.height_ratio = Property(self, 'height_ratio', 'float')
        self.reference_plane = Property(self, 'reference_plane', 'float')

        self.coordinate = InSocket(self, 'Coordinate', 'StructProperty')
        self.height = InSocket(self, 'Height', 'StructProperty')
        self.heightRatioInput = InSocket(self, 'HeightRatioInput', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class CameraPositionWS(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class CameraVectorWS(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Ceil(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ChannelMaskParameter(MaterialExpression):
    def __init__(self, parameter_name, default_value) -> None:
        super().__init__()

        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.default_value = Property(self, 'default_value', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.mask_channel = Property(self, 'mask_channel', 'ChannelMaskParameterColor')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.primitive_data_index = Property(self, 'primitive_data_index', 'uint8')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = Property(self, 'use_custom_primitive_data', 'bool')

        self.defaultValue = InSocket(self, 'DefaultValue', 'StructProperty')
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class Clamp(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.clamp_mode = Property(self, 'clamp_mode', 'ClampMode')
        self.desc = Property(self, 'desc', 'str')
        self.max_default = Property(self, 'max_default', 'float')
        self.min_default = Property(self, 'min_default', 'float')

        self.input = InSocket(self, 'Input', 'StructProperty')
        self.min = InSocket(self, 'Min', 'StructProperty')
        self.max = InSocket(self, 'Max', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ClearCoatNormalCustomOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class CloudSampleAttribute(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class CollectionParameter(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.collection = Property(self, 'collection', 'MaterialParameterCollection')
        self.desc = Property(self, 'desc', 'str')
        self.parameter_name = Property(self, 'parameter_name', 'Name')

        self.parameterId = InSocket(self, 'ParameterId', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Comment(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.color_comment_bubble = Property(self, 'color_comment_bubble', 'bool')
        self.comment_bubble_visible_in_details_panel = Property(self, 'comment_bubble_visible_in_details_panel', 'bool')
        self.comment_color = Property(self, 'comment_color', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')
        self.font_size = Property(self, 'font_size', 'int32')
        self.group_mode = Property(self, 'group_mode', 'bool')
        self.text = Property(self, 'text', 'str')

        self.commentColor = InSocket(self, 'CommentColor', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ComponentMask(MaterialExpression):
    def __init__(self, input, rgbaMask) -> None:
        super().__init__()

        self.a = Property(self, 'a', 'bool')
        self.b = Property(self, 'b', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.g = Property(self, 'g', 'bool')
        self.r = Property(self, 'r', 'bool')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
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

class Composite(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.subgraph_name = Property(self, 'subgraph_name', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Constant(MaterialExpression):
    def __init__(self, r) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.r = Property(self, 'r', 'float')

        self.output = OutSocket(self, '', 'StructProperty')
        if r is not None:
            self.r.set(r)

class Constant2Vector(MaterialExpression):
    def __init__(self, constant) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.g = Property(self, 'g', 'float')
        self.r = Property(self, 'r', 'float')

        self.output = OutSocket(self, '', 'StructProperty')
        self.r = OutSocket(self, 'r', 'StructProperty')
        self.g = OutSocket(self, 'g', 'StructProperty')
        if constant is not None:
            self.constant.set(constant)

class Constant3Vector(MaterialExpression):
    def __init__(self, constant) -> None:
        super().__init__()

        self.constant = Property(self, 'constant', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')

        self.output = OutSocket(self, '', 'StructProperty')
        self.r = OutSocket(self, 'r', 'StructProperty')
        self.g = OutSocket(self, 'g', 'StructProperty')
        self.b = OutSocket(self, 'b', 'StructProperty')
        if constant is not None:
            self.constant.set(constant)

class Constant4Vector(MaterialExpression):
    def __init__(self, constant) -> None:
        super().__init__()

        self.constant = Property(self, 'constant', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')

        self.output = OutSocket(self, '', 'StructProperty')
        self.r = OutSocket(self, 'r', 'StructProperty')
        self.g = OutSocket(self, 'g', 'StructProperty')
        self.b = OutSocket(self, 'b', 'StructProperty')
        self.a = OutSocket(self, 'a', 'StructProperty')
        if constant is not None:
            self.constant.set(constant)

class ConstantBiasScale(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.bias = Property(self, 'bias', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.scale = Property(self, 'scale', 'float')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ConstantDouble(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.value = Property(self, 'value', 'double')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Cosine(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.period = Property(self, 'period', 'float')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class CrossProduct(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class CurveAtlasRowParameter(MaterialExpression):
    def __init__(self, parameter_name, default_value) -> None:
        super().__init__()

        self.atlas = Property(self, 'atlas', 'CurveLinearColorAtlas')
        self.curve = Property(self, 'curve', 'CurveLinearColor')
        self.default_value = Property(self, 'default_value', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.primitive_data_index = Property(self, 'primitive_data_index', 'uint8')
        self.slider_max = Property(self, 'slider_max', 'float')
        self.slider_min = Property(self, 'slider_min', 'float')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = Property(self, 'use_custom_primitive_data', 'bool')

        self.inputTime = InSocket(self, 'InputTime', 'StructProperty')
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class Custom(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.additional_defines = Property(self, 'additional_defines', 'Array[CustomDefine]')
        self.additional_outputs = Property(self, 'additional_outputs', 'Array[CustomOutput]')
        self.code = Property(self, 'code', 'str')
        self.desc = Property(self, 'desc', 'str')
        self.description = Property(self, 'description', 'str')
        self.include_file_paths = Property(self, 'include_file_paths', 'Array[str]')
        self.inputs = Property(self, 'inputs', 'Array[CustomInput]')
        self.output_type = Property(self, 'output_type', 'CustomMaterialOutputType')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class CustomOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DBufferTexture(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.d_buffer_texture_id = Property(self, 'd_buffer_texture_id', 'DBufferTextureId')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DDX(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.value = InSocket(self, 'Value', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DDY(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.value = InSocket(self, 'Value', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DataDrivenShaderPlatformInfoSwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.ddspi_property_names = Property(self, 'ddspi_property_names', 'Array[DataDrivenShaderPlatformInfoInput]')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DecalColor(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DecalDerivative(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DecalLifetimeOpacity(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DecalMipmapLevel(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_height = Property(self, 'const_height', 'float')
        self.const_width = Property(self, 'const_width', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.textureSize = InSocket(self, 'TextureSize', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DeltaTime(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DepthFade(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.fade_distance_default = Property(self, 'fade_distance_default', 'float')
        self.opacity_default = Property(self, 'opacity_default', 'float')

        self.inOpacity = InSocket(self, 'InOpacity', 'StructProperty')
        self.fadeDistance = InSocket(self, 'FadeDistance', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DepthOfFieldFunction(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.function_value = Property(self, 'function_value', 'DepthOfFieldFunctionValue')

        self.depth = InSocket(self, 'Depth', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DeriveNormalZ(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.inXY = InSocket(self, 'InXY', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Desaturation(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.luminance_factors = Property(self, 'luminance_factors', 'LinearColor')

        self.input = InSocket(self, '', 'StructProperty')
        self.fraction = InSocket(self, 'Fraction', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Distance(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DistanceCullFade(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DistanceFieldApproxAO(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.base_distance_default = Property(self, 'base_distance_default', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.num_steps = Property(self, 'num_steps', 'uint32')
        self.radius_default = Property(self, 'radius_default', 'float')
        self.step_scale_default = Property(self, 'step_scale_default', 'float')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DistanceFieldGradient(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.position = InSocket(self, 'Position', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DistanceFieldsRenderingSwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.no = InSocket(self, 'No', 'StructProperty')
        self.yes = InSocket(self, 'Yes', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DistanceToNearestSurface(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.position = InSocket(self, 'Position', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Divide(MaterialExpression):
    def __init__(self, a, b) -> None:
        super().__init__()

        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
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

class DotProduct(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class DoubleVectorParameter(MaterialExpression):
    def __init__(self, parameter_name, default_value) -> None:
        super().__init__()

        self.default_value = Property(self, 'default_value', 'Vector4d')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class DynamicParameter(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.default_value = Property(self, 'default_value', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')
        self.param_names = Property(self, 'param_names', 'Array[str]')
        self.parameter_index = Property(self, 'parameter_index', 'uint32')

        self.defaultValue = InSocket(self, 'DefaultValue', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ExecBegin(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ExecEnd(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Exponential(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Exponential2(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class EyeAdaptation(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class EyeAdaptationInverse(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class FeatureLevelSwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.default = InSocket(self, 'Default', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Floor(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Fmod(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class FontSample(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.font = Property(self, 'font', 'Font')
        self.font_texture_page = Property(self, 'font_texture_page', 'int32')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class FontSampleParameter(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.font = Property(self, 'font', 'Font')
        self.font_texture_page = Property(self, 'font_texture_page', 'int32')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ForLoop(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Frac(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Fresnel(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.base_reflect_fraction = Property(self, 'base_reflect_fraction', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.exponent = Property(self, 'exponent', 'float')

        self.exponentIn = InSocket(self, 'ExponentIn', 'StructProperty')
        self.baseReflectFractionIn = InSocket(self, 'BaseReflectFractionIn', 'StructProperty')
        self.normal = InSocket(self, 'Normal', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class FunctionInput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.description = Property(self, 'description', 'str')
        self.input_name = Property(self, 'input_name', 'Name')
        self.input_type = Property(self, 'input_type', 'FunctionInputType')
        self.preview_value = Property(self, 'preview_value', 'Vector4f')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.use_preview_value_as_default = Property(self, 'use_preview_value_as_default', 'bool')

        self.preview = InSocket(self, 'Preview', 'StructProperty')
        self.ID = InSocket(self, 'ID', 'StructProperty')
        self.previewValue = InSocket(self, 'PreviewValue', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        

         
         
         
         
        @
        s
        t
        a
        t
        i
        c
        m
        e
        t
        h
        o
        d
        

         
         
         
         
        d
        e
        f
         
        c
        r
        e
        a
        t
        e
        (
        i
        n
        p
        u
        t
        _
        n
        a
        m
        e
        ,
         
        i
        n
        p
        u
        t
        _
        t
        y
        p
        e
        ,
         
        p
        r
        e
        v
        i
        e
        w
         
        =
         
        N
        o
        n
        e
        )
        :
        

         
         
         
         
         
         
         
         
        i
        f
         
        i
        s
        i
        n
        s
        t
        a
        n
        c
        e
        (
        p
        r
        e
        v
        i
        e
        w
        ,
         
        f
        l
        o
        a
        t
        )
        :
        

         
         
         
         
         
         
         
         
         
         
         
         
        p
        r
        e
        v
        i
        e
        w
         
        =
         
        C
        o
        n
        s
        t
        a
        n
        t
        (
        p
        r
        e
        v
        i
        e
        w
        )
        

         
         
         
         
         
         
         
         
        e
        l
        i
        f
         
        i
        s
        i
        n
        s
        t
        a
        n
        c
        e
        (
        p
        r
        e
        v
        i
        e
        w
        ,
         
        u
        n
        r
        e
        a
        l
        .
        L
        i
        n
        e
        a
        r
        C
        o
        l
        o
        r
        )
        :
        

         
         
         
         
         
         
         
         
         
         
         
         
        p
        r
        e
        v
        i
        e
        w
         
        =
         
        C
        o
        n
        s
        t
        a
        n
        t
        4
        V
        e
        c
        t
        o
        r
        (
        p
        r
        e
        v
        i
        e
        w
        )
        

        

         
         
         
         
         
         
         
         
        C
        u
        r
        r
        e
        n
        t
        N
        o
        d
        e
        P
        o
        s
        .
        x
         
        +
        =
         
        N
        o
        d
        e
        P
        o
        s
        .
        D
        e
        l
        t
        a
        X
        

        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
         
        =
         
        F
        u
        n
        c
        t
        i
        o
        n
        I
        n
        p
        u
        t
        (
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        i
        n
        p
        u
        t
        _
        n
        a
        m
        e
        .
        s
        e
        t
        (
        i
        n
        p
        u
        t
        _
        n
        a
        m
        e
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        i
        n
        p
        u
        t
        _
        t
        y
        p
        e
        .
        s
        e
        t
        (
        i
        n
        p
        u
        t
        _
        t
        y
        p
        e
        )
        

         
         
         
         
         
         
         
         
        i
        f
         
        p
        r
        e
        v
        i
        e
        w
         
        i
        s
         
        n
        o
        t
         
        N
        o
        n
        e
        :
        

         
         
         
         
         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        p
        r
        e
        v
        i
        e
        w
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        p
        r
        e
        v
        i
        e
        w
        )
        

         
         
         
         
         
         
         
         
        r
        e
        t
        u
        r
        n
         
        r
        e
        s
        u
        l
        t
        


class FunctionOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.description = Property(self, 'description', 'str')
        self.output_name = Property(self, 'output_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.ID = InSocket(self, 'ID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class GIReplace(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.default = InSocket(self, 'Default', 'StructProperty')
        self.staticIndirect = InSocket(self, 'StaticIndirect', 'StructProperty')
        self.dynamicIndirect = InSocket(self, 'DynamicIndirect', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class GenericConstant(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class GetLocal(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.local_name = Property(self, 'local_name', 'Name')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class GetMaterialAttributes(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.attribute_get_types = Property(self, 'attribute_get_types', 'Array[Guid]')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.materialAttributes = OutSocket(self, 'MaterialAttributes', 'StructProperty')
        self.baseColor = OutSocket(self, 'BaseColor', 'StructProperty')
        self.metallic = OutSocket(self, 'Metallic', 'StructProperty')
        self.specular = OutSocket(self, 'Specular', 'StructProperty')
        self.roughness = OutSocket(self, 'Roughness', 'StructProperty')
        self.anisotropy = OutSocket(self, 'Anisotropy', 'StructProperty')
        self.emissiveColor = OutSocket(self, 'EmissiveColor', 'StructProperty')
        self.opacity = OutSocket(self, 'Opacity', 'StructProperty')
        self.opacityMask = OutSocket(self, 'OpacityMask', 'StructProperty')
        self.normal = OutSocket(self, 'Normal', 'StructProperty')
        self.tangent = OutSocket(self, 'Tangent', 'StructProperty')
        self.worldPositionOffset = OutSocket(self, 'WorldPositionOffset', 'StructProperty')
        self.worldDisplacement = OutSocket(self, 'WorldDisplacement', 'StructProperty')
        self.tessellationMultiplier = OutSocket(self, 'TessellationMultiplier', 'StructProperty')
        self.subsurfaceColor = OutSocket(self, 'SubsurfaceColor', 'StructProperty')
        self.clearCoat = OutSocket(self, 'ClearCoat', 'StructProperty')
        self.clearCoatRoughness = OutSocket(self, 'ClearCoatRoughness', 'StructProperty')
        self.ambientOcclusion = OutSocket(self, 'AmbientOcclusion', 'StructProperty')
        self.refraction = OutSocket(self, 'Refraction', 'StructProperty')
        self.customizedUVs = OutSocket(self, 'CustomizedUVs', 'StructProperty')
        self.pixelDepthOffset = OutSocket(self, 'PixelDepthOffset', 'StructProperty')
        self.shadingModel = OutSocket(self, 'ShadingModel', 'StructProperty')

class HairAttributes(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.use_tangent_space = Property(self, 'use_tangent_space', 'bool')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class HairColor(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.melanin = InSocket(self, 'Melanin', 'StructProperty')
        self.redness = InSocket(self, 'Redness', 'StructProperty')
        self.dyeColor = InSocket(self, 'DyeColor', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class HeightfieldMinMaxTexture(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.min_max_texture = Property(self, 'min_max_texture', 'HeightfieldMinMaxTexture')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class HsvToRgb(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class If(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.equals_threshold = Property(self, 'equals_threshold', 'float')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.aGreaterThanB = InSocket(self, 'AGreaterThanB', 'StructProperty')
        self.aEqualsB = InSocket(self, 'AEqualsB', 'StructProperty')
        self.aLessThanB = InSocket(self, 'ALessThanB', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class IfThenElse(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class InverseLinearInterpolate(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.clamp_result = Property(self, 'clamp_result', 'bool')
        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.const_value = Property(self, 'const_value', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.value = InSocket(self, 'Value', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class IsOrthographic(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LandscapeGrassOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.grass_types = Property(self, 'grass_types', 'Array[GrassInput]')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LandscapeLayerBlend(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.layers = Property(self, 'layers', 'Array[LayerBlendInput]')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LandscapeLayerCoords(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.custom_uv_type = Property(self, 'custom_uv_type', 'LandscapeCustomizedCoordType')
        self.desc = Property(self, 'desc', 'str')
        self.mapping_pan_u = Property(self, 'mapping_pan_u', 'float')
        self.mapping_pan_v = Property(self, 'mapping_pan_v', 'float')
        self.mapping_rotation = Property(self, 'mapping_rotation', 'float')
        self.mapping_scale = Property(self, 'mapping_scale', 'float')
        self.mapping_type = Property(self, 'mapping_type', 'TerrainCoordMappingType')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LandscapeLayerSample(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.preview_weight = Property(self, 'preview_weight', 'float')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LandscapeLayerSwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.preview_used = Property(self, 'preview_used', 'bool')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LandscapeLayerWeight(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_base = Property(self, 'const_base', 'Vector')
        self.desc = Property(self, 'desc', 'str')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.preview_weight = Property(self, 'preview_weight', 'float')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LandscapePhysicalMaterialOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.inputs = Property(self, 'inputs', 'Array[PhysicalMaterialInput]')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LandscapeVisibilityMask(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Length(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Less(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LightVector(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LightmapUVs(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LightmassReplace(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.realtime = InSocket(self, 'Realtime', 'StructProperty')
        self.lightmass = InSocket(self, 'Lightmass', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class LinearInterpolate(MaterialExpression):
    def __init__(self, a, b, alpha) -> None:
        super().__init__()

        self.const_a = Property(self, 'const_a', 'float')
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.alpha = InSocket(self, 'Alpha', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if a is not None:
            self.a.comesFrom(a)
        if b is not None:
            self.b.comesFrom(b)
        if alpha is not None:
            self.alpha.comesFrom(alpha)

class Logarithm(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Logarithm10(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.x = InSocket(self, 'X', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Logarithm2(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.x = InSocket(self, 'X', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MakeMaterialAttributes(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.baseColor = InSocket(self, 'BaseColor', 'StructProperty')
        self.metallic = InSocket(self, 'Metallic', 'StructProperty')
        self.specular = InSocket(self, 'Specular', 'StructProperty')
        self.roughness = InSocket(self, 'Roughness', 'StructProperty')
        self.anisotropy = InSocket(self, 'Anisotropy', 'StructProperty')
        self.emissiveColor = InSocket(self, 'EmissiveColor', 'StructProperty')
        self.opacity = InSocket(self, 'Opacity', 'StructProperty')
        self.opacityMask = InSocket(self, 'OpacityMask', 'StructProperty')
        self.normal = InSocket(self, 'Normal', 'StructProperty')
        self.tangent = InSocket(self, 'Tangent', 'StructProperty')
        self.worldPositionOffset = InSocket(self, 'WorldPositionOffset', 'StructProperty')
        self.subsurfaceColor = InSocket(self, 'SubsurfaceColor', 'StructProperty')
        self.clearCoat = InSocket(self, 'ClearCoat', 'StructProperty')
        self.clearCoatRoughness = InSocket(self, 'ClearCoatRoughness', 'StructProperty')
        self.ambientOcclusion = InSocket(self, 'AmbientOcclusion', 'StructProperty')
        self.refraction = InSocket(self, 'Refraction', 'StructProperty')
        self.customizedUV_0 = InSocket(self, 'CustomizedUV_0', 'StructProperty')
        self.customizedUV_1 = InSocket(self, 'CustomizedUV_1', 'StructProperty')
        self.customizedUV_2 = InSocket(self, 'CustomizedUV_2', 'StructProperty')
        self.customizedUV_3 = InSocket(self, 'CustomizedUV_3', 'StructProperty')
        self.customizedUV_4 = InSocket(self, 'CustomizedUV_4', 'StructProperty')
        self.customizedUV_5 = InSocket(self, 'CustomizedUV_5', 'StructProperty')
        self.customizedUV_6 = InSocket(self, 'CustomizedUV_6', 'StructProperty')
        self.customizedUV_7 = InSocket(self, 'CustomizedUV_7', 'StructProperty')
        self.pixelDepthOffset = InSocket(self, 'PixelDepthOffset', 'StructProperty')
        self.shadingModel = InSocket(self, 'ShadingModel', 'StructProperty')
        self.displacement = InSocket(self, 'Displacement', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        

         
         
         
         
        @
        s
        t
        a
        t
        i
        c
        m
        e
        t
        h
        o
        d
        

         
         
         
         
        d
        e
        f
         
        c
        r
        e
        a
        t
        e
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        )
        :
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
         
        =
         
        M
        a
        k
        e
        M
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        (
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        b
        a
        s
        e
        C
        o
        l
        o
        r
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        b
        a
        s
        e
        C
        o
        l
        o
        r
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        m
        e
        t
        a
        l
        l
        i
        c
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        m
        e
        t
        a
        l
        l
        i
        c
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        s
        p
        e
        c
        u
        l
        a
        r
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        s
        p
        e
        c
        u
        l
        a
        r
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        r
        o
        u
        g
        h
        n
        e
        s
        s
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        r
        o
        u
        g
        h
        n
        e
        s
        s
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        a
        n
        i
        s
        o
        t
        r
        o
        p
        y
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        a
        n
        i
        s
        o
        t
        r
        o
        p
        y
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        e
        m
        i
        s
        s
        i
        v
        e
        C
        o
        l
        o
        r
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        e
        m
        i
        s
        s
        i
        v
        e
        C
        o
        l
        o
        r
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        o
        p
        a
        c
        i
        t
        y
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        o
        p
        a
        c
        i
        t
        y
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        o
        p
        a
        c
        i
        t
        y
        M
        a
        s
        k
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        o
        p
        a
        c
        i
        t
        y
        M
        a
        s
        k
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        n
        o
        r
        m
        a
        l
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        n
        o
        r
        m
        a
        l
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        t
        a
        n
        g
        e
        n
        t
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        t
        a
        n
        g
        e
        n
        t
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        w
        o
        r
        l
        d
        P
        o
        s
        i
        t
        i
        o
        n
        O
        f
        f
        s
        e
        t
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        w
        o
        r
        l
        d
        P
        o
        s
        i
        t
        i
        o
        n
        O
        f
        f
        s
        e
        t
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        s
        u
        b
        s
        u
        r
        f
        a
        c
        e
        C
        o
        l
        o
        r
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        s
        u
        b
        s
        u
        r
        f
        a
        c
        e
        C
        o
        l
        o
        r
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        c
        l
        e
        a
        r
        C
        o
        a
        t
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        c
        l
        e
        a
        r
        C
        o
        a
        t
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        c
        l
        e
        a
        r
        C
        o
        a
        t
        R
        o
        u
        g
        h
        n
        e
        s
        s
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        c
        l
        e
        a
        r
        C
        o
        a
        t
        R
        o
        u
        g
        h
        n
        e
        s
        s
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        a
        m
        b
        i
        e
        n
        t
        O
        c
        c
        l
        u
        s
        i
        o
        n
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        a
        m
        b
        i
        e
        n
        t
        O
        c
        c
        l
        u
        s
        i
        o
        n
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        r
        e
        f
        r
        a
        c
        t
        i
        o
        n
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        r
        e
        f
        r
        a
        c
        t
        i
        o
        n
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        _
        0
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        0
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        _
        1
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        1
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        _
        2
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        2
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        _
        3
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        3
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        _
        4
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        4
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        _
        5
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        5
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        _
        6
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        6
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        _
        7
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        c
        u
        s
        t
        o
        m
        i
        z
        e
        d
        U
        V
        7
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        p
        i
        x
        e
        l
        D
        e
        p
        t
        h
        O
        f
        f
        s
        e
        t
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        p
        i
        x
        e
        l
        D
        e
        p
        t
        h
        O
        f
        f
        s
        e
        t
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        s
        h
        a
        d
        i
        n
        g
        M
        o
        d
        e
        l
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        s
        h
        a
        d
        i
        n
        g
        M
        o
        d
        e
        l
        )
        

         
         
         
         
         
         
         
         
        r
        e
        s
        u
        l
        t
        .
        d
        i
        s
        p
        l
        a
        c
        e
        m
        e
        n
        t
        .
        c
        o
        m
        e
        s
        F
        r
        o
        m
        (
        m
        a
        t
        e
        r
        i
        a
        l
        A
        t
        t
        r
        i
        b
        u
        t
        e
        s
        .
        d
        i
        s
        p
        l
        a
        c
        e
        m
        e
        n
        t
        )
        

         
         
         
         
         
         
         
         
        r
        e
        t
        u
        r
        n
         
        r
        e
        s
        u
        l
        t
        


class MapARPassthroughCameraUV(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialAttributeLayers(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.default_layers = Property(self, 'default_layers', 'MaterialLayersFunctions')
        self.desc = Property(self, 'desc', 'str')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.input = InSocket(self, 'Input', 'StructProperty')
        self.defaultLayers = InSocket(self, 'DefaultLayers', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialFunctionCall(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.material_function = Property(self, 'material_function', 'MaterialFunctionInterface')

        self.functionParameterInfo = InSocket(self, 'FunctionParameterInfo', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialLayerOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.description = Property(self, 'description', 'str')
        self.output_name = Property(self, 'output_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.ID = InSocket(self, 'ID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialProxyReplace(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.realtime = InSocket(self, 'Realtime', 'StructProperty')
        self.materialProxy = InSocket(self, 'MaterialProxy', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXAppend3Vector(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXAppend4Vector(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXBurn(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXDifference(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXDisjointOver(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXDodge(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXFractal3D(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_amplitude = Property(self, 'const_amplitude', 'float')
        self.const_diminish = Property(self, 'const_diminish', 'float')
        self.const_lacunarity = Property(self, 'const_lacunarity', 'float')
        self.const_octaves = Property(self, 'const_octaves', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.levels = Property(self, 'levels', 'int32')
        self.output_max = Property(self, 'output_max', 'float')
        self.output_min = Property(self, 'output_min', 'float')
        self.scale = Property(self, 'scale', 'float')
        self.turbulence = Property(self, 'turbulence', 'bool')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXIn(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXLuminance(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.luminance_factors = Property(self, 'luminance_factors', 'LinearColor')
        self.luminance_mode = Property(self, 'luminance_mode', 'MaterialXLuminanceMode')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXMask(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXMatte(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXMinus(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXOut(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXOver(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXOverlay(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXPlace2D(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_rotation_angle = Property(self, 'const_rotation_angle', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXPlus(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXPremult(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXRamp4(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXRampLeftRight(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXRampTopBottom(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXRemap(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.input_high_default = Property(self, 'input_high_default', 'float')
        self.input_low_default = Property(self, 'input_low_default', 'float')
        self.target_high_default = Property(self, 'target_high_default', 'float')
        self.target_low_default = Property(self, 'target_low_default', 'float')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXRotate2D(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_rotation_angle = Property(self, 'const_rotation_angle', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXScreen(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXSplitLeftRight(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_center = Property(self, 'const_center', 'float')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXSplitTopBottom(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_center = Property(self, 'const_center', 'float')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXSwizzle(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.channels = Property(self, 'channels', 'str')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXTextureSampleParameterBlur(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.filter = Property(self, 'filter', 'MaterialXTextureSampleBlurFilter')
        self.filter_offset = Property(self, 'filter_offset', 'float')
        self.filter_size = Property(self, 'filter_size', 'float')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.kernel_size = Property(self, 'kernel_size', 'MAterialXTextureSampleBlurKernel')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class MaterialXUnpremult(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Max(MaterialExpression):
    def __init__(self, a, b) -> None:
        super().__init__()

        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
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

class Min(MaterialExpression):
    def __init__(self, a, b) -> None:
        super().__init__()

        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
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

class Multiply(MaterialExpression):
    def __init__(self, a, b) -> None:
        super().__init__()

        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
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

class NamedRerouteBase(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class NamedRerouteDeclaration(MaterialExpression):
    def __init__(self, name, input, nodeColor) -> None:
        super().__init__()

        self.name = Property(self, 'name', 'Name')
        self.desc = Property(self, 'desc', 'str')
        self.nodeNolor = Property(self, 'nodeNolor', 'LinearColor')
        self.variableGuid = Property(self, 'variableGuid', 'Guid')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if name is not None:
            self.name.set(name)
        if input is not None:
            self.input.comesFrom(input)
        if nodeColor is not None:
            self.nodeColor.set(nodeColor)

class NamedRerouteUsage(MaterialExpression):
    def __init__(self, declarationGuid) -> None:
        super().__init__()

        self.declarationGuid = Property(self, 'declarationGuid', 'Guid')

        self.output = OutSocket(self, '', 'StructProperty')
        if declarationGuid is not None:
            self.declarationGuid.set(declarationGuid)

class NaniteReplace(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Noise(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.level_scale = Property(self, 'level_scale', 'float')
        self.levels = Property(self, 'levels', 'int32')
        self.noise_function = Property(self, 'noise_function', 'NoiseFunction')
        self.output_max = Property(self, 'output_max', 'float')
        self.output_min = Property(self, 'output_min', 'float')
        self.quality = Property(self, 'quality', 'int32')
        self.repeat_size = Property(self, 'repeat_size', 'uint32')
        self.scale = Property(self, 'scale', 'float')
        self.tiling = Property(self, 'tiling', 'bool')
        self.turbulence = Property(self, 'turbulence', 'bool')

        self.position = InSocket(self, 'Position', 'StructProperty')
        self.filterWidth = InSocket(self, 'FilterWidth', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Normalize(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.vectorInput = InSocket(self, 'VectorInput', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ObjectBounds(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ObjectLocalBounds(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ObjectOrientation(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ObjectPositionWS(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.origin_type = Property(self, 'origin_type', 'PositionOrigin')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ObjectRadius(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class OneMinus(MaterialExpression):
    def __init__(self, input) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if input is not None:
            self.input.comesFrom(input)

class Panner(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_coordinate = Property(self, 'const_coordinate', 'uint32')
        self.desc = Property(self, 'desc', 'str')
        self.fractional_part = Property(self, 'fractional_part', 'bool')
        self.speed_x = Property(self, 'speed_x', 'float')
        self.speed_y = Property(self, 'speed_y', 'float')

        self.coordinate = InSocket(self, 'Coordinate', 'StructProperty')
        self.time = InSocket(self, 'Time', 'StructProperty')
        self.speed = InSocket(self, 'Speed', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Parameter(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleColor(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleDirection(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleMacroUV(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleMotionBlurFade(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticlePositionWS(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.origin_type = Property(self, 'origin_type', 'PositionOrigin')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleRadius(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleRandom(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleRelativeTime(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleSize(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleSpeed(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleSpriteRotation(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleSubUV(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.blend = Property(self, 'blend', 'bool')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = Property(self, 'texture', 'Texture')

        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ParticleSubUVProperties(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PathTracingBufferTexture(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.path_tracing_buffer_texture_id = Property(self, 'path_tracing_buffer_texture_id', 'PathTracingBufferTextureId')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PathTracingQualitySwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PathTracingRayTypeSwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PerInstanceCustomData(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_default_value = Property(self, 'const_default_value', 'float')
        self.data_index = Property(self, 'data_index', 'uint32')
        self.desc = Property(self, 'desc', 'str')

        self.defaultValue = InSocket(self, 'DefaultValue', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PerInstanceCustomData3Vector(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_default_value = Property(self, 'const_default_value', 'LinearColor')
        self.data_index = Property(self, 'data_index', 'uint32')
        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PerInstanceFadeAmount(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PerInstanceRandom(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PinBase(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.reroute_pins = Property(self, 'reroute_pins', 'Array[CompositeReroute]')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PixelDepth(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PixelNormalWS(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Power(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_exponent = Property(self, 'const_exponent', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.base = InSocket(self, 'Base', 'StructProperty')
        self.exponent = InSocket(self, 'Exponent', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PreSkinnedLocalBounds(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PreSkinnedNormal(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PreSkinnedPosition(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PrecomputedAOMask(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class PreviousFrameSwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.currentFrame = InSocket(self, 'CurrentFrame', 'StructProperty')
        self.previousFrame = InSocket(self, 'PreviousFrame', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class QualitySwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.default = InSocket(self, 'Default', 'StructProperty')
        self.low = InSocket(self, 'Low', 'StructProperty')
        self.high = InSocket(self, 'High', 'StructProperty')
        self.medium = InSocket(self, 'Medium', 'StructProperty')
        self.epic = InSocket(self, 'Epic', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class RayTracingQualitySwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.normal = InSocket(self, 'Normal', 'StructProperty')
        self.rayTraced = InSocket(self, 'RayTraced', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ReflectionCapturePassSwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.default = InSocket(self, 'Default', 'StructProperty')
        self.reflection = InSocket(self, 'Reflection', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ReflectionVectorWS(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.normalize_custom_world_normal = Property(self, 'normalize_custom_world_normal', 'bool')

        self.customWorldNormal = InSocket(self, 'CustomWorldNormal', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Reroute(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class RerouteBase(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class RgbToHsv(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class RotateAboutAxis(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.period = Property(self, 'period', 'float')

        self.normalizedRotationAxis = InSocket(self, 'NormalizedRotationAxis', 'StructProperty')
        self.rotationAngle = InSocket(self, 'RotationAngle', 'StructProperty')
        self.pivotPoint = InSocket(self, 'PivotPoint', 'StructProperty')
        self.position = InSocket(self, 'Position', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Rotator(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.center_x = Property(self, 'center_x', 'float')
        self.center_y = Property(self, 'center_y', 'float')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint32')
        self.desc = Property(self, 'desc', 'str')
        self.speed = Property(self, 'speed', 'float')

        self.coordinate = InSocket(self, 'Coordinate', 'StructProperty')
        self.time = InSocket(self, 'Time', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Round(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class RuntimeVirtualTextureOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.baseColor = InSocket(self, 'BaseColor', 'StructProperty')
        self.specular = InSocket(self, 'Specular', 'StructProperty')
        self.roughness = InSocket(self, 'Roughness', 'StructProperty')
        self.normal = InSocket(self, 'Normal', 'StructProperty')
        self.worldHeight = InSocket(self, 'WorldHeight', 'StructProperty')
        self.opacity = InSocket(self, 'Opacity', 'StructProperty')
        self.mask = InSocket(self, 'Mask', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class RuntimeVirtualTextureReplace(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.default = InSocket(self, 'Default', 'StructProperty')
        self.virtualTextureOutput = InSocket(self, 'VirtualTextureOutput', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class RuntimeVirtualTextureSample(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.adaptive = Property(self, 'adaptive', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.enable_feedback = Property(self, 'enable_feedback', 'bool')
        self.material_type = Property(self, 'material_type', 'RuntimeVirtualTextureMaterialType')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'RuntimeVirtualTextureMipValueMode')
        self.single_physical_space = Property(self, 'single_physical_space', 'bool')
        self.texture_address_mode = Property(self, 'texture_address_mode', 'RuntimeVirtualTextureTextureAddressMode')
        self.virtual_texture = Property(self, 'virtual_texture', 'RuntimeVirtualTexture')

        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')
        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')
        self.mipValue = InSocket(self, 'MipValue', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class RuntimeVirtualTextureSampleParameter(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.adaptive = Property(self, 'adaptive', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.enable_feedback = Property(self, 'enable_feedback', 'bool')
        self.group = Property(self, 'group', 'Name')
        self.material_type = Property(self, 'material_type', 'RuntimeVirtualTextureMaterialType')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'RuntimeVirtualTextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.single_physical_space = Property(self, 'single_physical_space', 'bool')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture_address_mode = Property(self, 'texture_address_mode', 'RuntimeVirtualTextureTextureAddressMode')
        self.virtual_texture = Property(self, 'virtual_texture', 'RuntimeVirtualTexture')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')
        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')
        self.mipValue = InSocket(self, 'MipValue', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SamplePhysicsIntegerField(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.field_target = Property(self, 'field_target', 'FieldIntegerType')

        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SamplePhysicsScalarField(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.field_target = Property(self, 'field_target', 'FieldScalarType')

        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SamplePhysicsVectorField(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.field_target = Property(self, 'field_target', 'FieldVectorType')

        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Saturate(MaterialExpression):
    def __init__(self, input) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if input is not None:
            self.input.comesFrom(input)

class ScalarParameter(MaterialExpression):
    def __init__(self, parameter_name, default_value) -> None:
        super().__init__()

        self.default_value = Property(self, 'default_value', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.primitive_data_index = Property(self, 'primitive_data_index', 'uint8')
        self.slider_max = Property(self, 'slider_max', 'float')
        self.slider_min = Property(self, 'slider_min', 'float')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = Property(self, 'use_custom_primitive_data', 'bool')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class SceneColor(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_input = Property(self, 'const_input', 'Vector2D')
        self.desc = Property(self, 'desc', 'str')
        self.input_mode = Property(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        self.input = InSocket(self, 'Input', 'StructProperty')
        self.offsetFraction = InSocket(self, 'OffsetFraction', 'StructProperty')
        self.constInput = InSocket(self, 'ConstInput', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SceneDepth(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_input = Property(self, 'const_input', 'Vector2D')
        self.desc = Property(self, 'desc', 'str')
        self.input_mode = Property(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        self.input = InSocket(self, 'Input', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')
        self.constInput = InSocket(self, 'ConstInput', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SceneDepthWithoutWater(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_input = Property(self, 'const_input', 'Vector2D')
        self.desc = Property(self, 'desc', 'str')
        self.fallback_depth = Property(self, 'fallback_depth', 'float')
        self.input_mode = Property(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        self.input = InSocket(self, 'Input', 'StructProperty')
        self.constInput = InSocket(self, 'ConstInput', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SceneTexelSize(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SceneTexture(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.filtered = Property(self, 'filtered', 'bool')
        self.scene_texture_id = Property(self, 'scene_texture_id', 'SceneTextureId')

        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ScreenPosition(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SetLocal(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.local_name = Property(self, 'local_name', 'Name')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SetMaterialAttributes(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.attribute_set_types = Property(self, 'attribute_set_types', 'Array[Guid]')
        self.desc = Property(self, 'desc', 'str')

        self.materialAttributes = InSocket(self, 'MaterialAttributes', 'StructProperty')
        self.baseColor = InSocket(self, 'BaseColor', 'StructProperty')
        self.metallic = InSocket(self, 'Metallic', 'StructProperty')
        self.specular = InSocket(self, 'Specular', 'StructProperty')
        self.roughness = InSocket(self, 'Roughness', 'StructProperty')
        self.anisotropy = InSocket(self, 'Anisotropy', 'StructProperty')
        self.emissiveColor = InSocket(self, 'EmissiveColor', 'StructProperty')
        self.opacity = InSocket(self, 'Opacity', 'StructProperty')
        self.opacityMask = InSocket(self, 'OpacityMask', 'StructProperty')
        self.normal = InSocket(self, 'Normal', 'StructProperty')
        self.tangent = InSocket(self, 'Tangent', 'StructProperty')
        self.worldPositionOffset = InSocket(self, 'WorldPositionOffset', 'StructProperty')
        self.worldDisplacement = InSocket(self, 'WorldDisplacement', 'StructProperty')
        self.tessellationMultiplier = InSocket(self, 'TessellationMultiplier', 'StructProperty')
        self.subsurfaceColor = InSocket(self, 'SubsurfaceColor', 'StructProperty')
        self.clearCoat = InSocket(self, 'ClearCoat', 'StructProperty')
        self.clearCoatRoughness = InSocket(self, 'ClearCoatRoughness', 'StructProperty')
        self.ambientOcclusion = InSocket(self, 'AmbientOcclusion', 'StructProperty')
        self.refraction = InSocket(self, 'Refraction', 'StructProperty')
        self.customizedUVs = InSocket(self, 'CustomizedUVs', 'StructProperty')
        self.pixelDepthOffset = InSocket(self, 'PixelDepthOffset', 'StructProperty')
        self.shadingModel = InSocket(self, 'ShadingModel', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ShaderStageSwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.pixelShader = InSocket(self, 'PixelShader', 'StructProperty')
        self.vertexShader = InSocket(self, 'VertexShader', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ShadingModel(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.shading_model = Property(self, 'shading_model', 'MaterialShadingModel')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ShadingPathSwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.default = InSocket(self, 'Default', 'StructProperty')
        self.inputs = InSocket(self, 'Inputs', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ShadowReplace(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.default = InSocket(self, 'Default', 'StructProperty')
        self.shadow = InSocket(self, 'Shadow', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Sign(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Sine(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.period = Property(self, 'period', 'float')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SingleLayerWaterMaterialOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.scatteringCoefficients = InSocket(self, 'ScatteringCoefficients', 'StructProperty')
        self.absorptionCoefficients = InSocket(self, 'AbsorptionCoefficients', 'StructProperty')
        self.phaseG = InSocket(self, 'PhaseG', 'StructProperty')
        self.colorScaleBehindWater = InSocket(self, 'ColorScaleBehindWater', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SkyAtmosphereAerialPerspective(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SkyAtmosphereDistantLightScatteredLuminance(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SkyAtmosphereLightDirection(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.light_index = Property(self, 'light_index', 'int32')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SkyAtmosphereLightDiskLuminance(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.light_index = Property(self, 'light_index', 'int32')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SkyAtmosphereLightIlluminance(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.light_index = Property(self, 'light_index', 'int32')

        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SkyAtmosphereViewLuminance(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SkyLightEnvMapSample(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SmoothStep(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_max = Property(self, 'const_max', 'float')
        self.const_min = Property(self, 'const_min', 'float')
        self.const_value = Property(self, 'const_value', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.min = InSocket(self, 'Min', 'StructProperty')
        self.max = InSocket(self, 'Max', 'StructProperty')
        self.value = InSocket(self, 'Value', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Sobol(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_index = Property(self, 'const_index', 'uint32')
        self.const_seed = Property(self, 'const_seed', 'Vector2D')
        self.desc = Property(self, 'desc', 'str')

        self.cell = InSocket(self, 'Cell', 'StructProperty')
        self.index = InSocket(self, 'Index', 'StructProperty')
        self.seed = InSocket(self, 'Seed', 'StructProperty')
        self.constSeed = InSocket(self, 'ConstSeed', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SparseVolumeTextureBase(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.sparse_volume_texture = Property(self, 'sparse_volume_texture', 'SparseVolumeTexture')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SparseVolumeTextureObject(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.sparse_volume_texture = Property(self, 'sparse_volume_texture', 'SparseVolumeTexture')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SparseVolumeTextureObjectParameter(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.sparse_volume_texture = Property(self, 'sparse_volume_texture', 'SparseVolumeTexture')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SparseVolumeTextureSample(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sparse_volume_texture = Property(self, 'sparse_volume_texture', 'SparseVolumeTexture')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SparseVolumeTextureSampleParameter(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.sparse_volume_texture = Property(self, 'sparse_volume_texture', 'SparseVolumeTexture')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SpeedTree(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.accurate_wind_velocities = Property(self, 'accurate_wind_velocities', 'bool')
        self.billboard_threshold = Property(self, 'billboard_threshold', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.geometry_type = Property(self, 'geometry_type', 'SpeedTreeGeometryType')
        self.lod_type = Property(self, 'lod_type', 'SpeedTreeLODType')
        self.wind_type = Property(self, 'wind_type', 'SpeedTreeWindType')

        self.geometryInput = InSocket(self, 'GeometryInput', 'StructProperty')
        self.windInput = InSocket(self, 'WindInput', 'StructProperty')
        self.lODInput = InSocket(self, 'LODInput', 'StructProperty')
        self.extraBendWS = InSocket(self, 'ExtraBendWS', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SphereMask(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.attenuation_radius = Property(self, 'attenuation_radius', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.hardness_percent = Property(self, 'hardness_percent', 'float')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.radius = InSocket(self, 'Radius', 'StructProperty')
        self.hardness = InSocket(self, 'Hardness', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SphericalParticleOpacity(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.constant_density = Property(self, 'constant_density', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.density = InSocket(self, 'Density', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SpriteTextureSampler(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.additional_slot_index = Property(self, 'additional_slot_index', 'int32')
        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sample_additional_textures = Property(self, 'sample_additional_textures', 'bool')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.slot_display_name = Property(self, 'slot_display_name', 'Text')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SquareRoot(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StaticBool(MaterialExpression):
    def __init__(self, value) -> None:
        super().__init__()

        self.value = Property(self, 'Value', 'bool')

        self.output = OutSocket(self, '', 'StructProperty')
        if value is not None:
            self.value.set(value)

class StaticBoolParameter(MaterialExpression):
    def __init__(self, parameter_name, default_value) -> None:
        super().__init__()

        self.default_value = Property(self, 'default_value', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.dynamic_branch = Property(self, 'dynamic_branch', 'bool')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class StaticComponentMaskParameter(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.default_a = Property(self, 'default_a', 'bool')
        self.default_b = Property(self, 'default_b', 'bool')
        self.default_g = Property(self, 'default_g', 'bool')
        self.default_r = Property(self, 'default_r', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StaticSwitch(MaterialExpression):
    def __init__(self, true, false, value) -> None:
        super().__init__()

        self.default_value = Property(self, 'default_value', 'bool')
        self.desc = Property(self, 'desc', 'str')

        self.true = InSocket(self, 'True', 'StructProperty')
        self.false = InSocket(self, 'False', 'StructProperty')
        self.value = InSocket(self, 'Value', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if true is not None:
            self.true.comesFrom(true)
        if false is not None:
            self.false.comesFrom(false)
        if value is not None:
            self.value.comesFrom(value)

class StaticSwitchParameter(MaterialExpression):
    def __init__(self, parameter_name, default_value) -> None:
        super().__init__()

        self.default_value = Property(self, 'default_value', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.dynamic_branch = Property(self, 'dynamic_branch', 'bool')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class Step(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_x = Property(self, 'const_x', 'float')
        self.const_y = Property(self, 'const_y', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.y = InSocket(self, 'Y', 'StructProperty')
        self.x = InSocket(self, 'X', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataAdd(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.use_parameter_blending = Property(self, 'use_parameter_blending', 'bool')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataBSDF(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataConvertToDecal(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataEyeBSDF(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.subsurface_profile = Property(self, 'subsurface_profile', 'SubsurfaceProfile')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataHairBSDF(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataHazinessToSecondaryRoughness(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataHorizontalMixing(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.use_parameter_blending = Property(self, 'use_parameter_blending', 'bool')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataLegacyConversion(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.subsurface_profile = Property(self, 'subsurface_profile', 'SubsurfaceProfile')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataLightFunction(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataMetalnessToDiffuseAlbedoF0(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataPostProcess(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataSimpleClearCoatBSDF(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataSingleLayerWaterBSDF(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataSlabBSDF(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.specular_profile = Property(self, 'specular_profile', 'SpecularProfile')
        self.subsurface_profile = Property(self, 'subsurface_profile', 'SubsurfaceProfile')
        self.use_sss_diffusion = Property(self, 'use_sss_diffusion', 'bool')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataThinFilm(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataTransmittanceToMFP(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataUI(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataUnlitBSDF(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataUtilityBase(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataVerticalLayering(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.use_parameter_blending = Property(self, 'use_parameter_blending', 'bool')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataVolumetricFogCloudBSDF(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class StrataWeight(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class SubsurfaceMediumMaterialOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Subtract(MaterialExpression):
    def __init__(self, a, b) -> None:
        super().__init__()

        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
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

class Switch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_default = Property(self, 'const_default', 'float')
        self.const_switch_value = Property(self, 'const_switch_value', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.description = Property(self, 'description', 'str')
        self.inputs = Property(self, 'inputs', 'Array[SwitchCustomInput]')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Tangent(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.period = Property(self, 'period', 'float')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TangentOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TemporalSobol(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.const_index = Property(self, 'const_index', 'uint32')
        self.const_seed = Property(self, 'const_seed', 'Vector2D')
        self.desc = Property(self, 'desc', 'str')

        self.index = InSocket(self, 'Index', 'StructProperty')
        self.seed = InSocket(self, 'Seed', 'StructProperty')
        self.constSeed = InSocket(self, 'ConstSeed', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TextureBase(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = Property(self, 'texture', 'Texture')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TextureCoordinate(MaterialExpression):
    def __init__(self, u_tiling, v_tiling) -> None:
        super().__init__()

        self.coordinate_index = Property(self, 'coordinate_index', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.u_tiling = Property(self, 'u_tiling', 'float')
        self.un_mirror_u = Property(self, 'un_mirror_u', 'bool')
        self.un_mirror_v = Property(self, 'un_mirror_v', 'bool')
        self.v_tiling = Property(self, 'v_tiling', 'float')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        if u_tiling is not None:
            self.u_tiling.set(u_tiling)
        if v_tiling is not None:
            self.v_tiling.set(v_tiling)

class TextureObject(MaterialExpression):
    def __init__(self, sampler_type, texture) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = Property(self, 'texture', 'Texture')

        self.output = OutSocket(self, '', 'StructProperty')
        if sampler_type is not None:
            self.sampler_type.set(sampler_type)
        if texture is not None:
            self.texture.set(texture)

class TextureObjectParameter(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TextureProperty(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.property_ = Property(self, 'property_', 'MaterialExposedTextureProperty')

        self.textureObject = InSocket(self, 'TextureObject', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TextureSample(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = Property(self, 'texture', 'Texture')

        self.UVs = InSocket(self, 'UVs', 'StructProperty')
        self.tex = InSocket(self, 'Tex', 'StructProperty')
        self.applyViewMipBias = InSocket(self, 'ApplyViewMipBias', 'StructProperty')

        self.RGB = OutSocket(self, 'RGB', 'StructProperty')
        self.r = OutSocket(self, 'R', 'StructProperty')
        self.g = OutSocket(self, 'G', 'StructProperty')
        self.b = OutSocket(self, 'B', 'StructProperty')
        self.a = OutSocket(self, 'A', 'StructProperty')
        self.RGBA = OutSocket(self, 'RGBA', 'StructProperty')

class TextureSampleParameter(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TextureSampleParameter2D(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TextureSampleParameter2DArray(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TextureSampleParameterCube(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TextureSampleParameterCubeArray(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TextureSampleParameterSubUV(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.blend = Property(self, 'blend', 'bool')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TextureSampleParameterVolume(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.texture = Property(self, 'texture', 'Texture')

        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ThinTranslucentMaterialOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.transmittanceColor = InSocket(self, 'TransmittanceColor', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Time(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.ignore_pause = Property(self, 'ignore_pause', 'bool')
        self.override_period = Property(self, 'override_period', 'bool')
        self.period = Property(self, 'period', 'float')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Transform(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.transform_source_type = Property(self, 'transform_source_type', 'MaterialVectorCoordTransformSource')
        self.transform_type = Property(self, 'transform_type', 'MaterialVectorCoordTransform')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TransformPosition(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.transform_source_type = Property(self, 'transform_source_type', 'MaterialPositionTransformSource')
        self.transform_type = Property(self, 'transform_type', 'MaterialPositionTransformSource')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class Truncate(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TruncateLWC(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class TwoSidedSign(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class VectorNoise(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.noise_function = Property(self, 'noise_function', 'VectorNoiseFunction')
        self.quality = Property(self, 'quality', 'int32')
        self.tile_size = Property(self, 'tile_size', 'uint32')
        self.tiling = Property(self, 'tiling', 'bool')

        self.position = InSocket(self, 'Position', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class VectorParameter(MaterialExpression):
    def __init__(self, parameter_name, default_value) -> None:
        super().__init__()

        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.default_value = Property(self, 'default_value', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.primitive_data_index = Property(self, 'primitive_data_index', 'uint8')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = Property(self, 'use_custom_primitive_data', 'bool')

        self.defaultValue = InSocket(self, 'DefaultValue', 'StructProperty')
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')
        self.r = OutSocket(self, 'r', 'StructProperty')
        self.g = OutSocket(self, 'g', 'StructProperty')
        self.b = OutSocket(self, 'b', 'StructProperty')
        self.a = OutSocket(self, 'a', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)

class VertexColor(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class VertexInterpolator(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, 'Input', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class VertexNormalWS(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class VertexTangentWS(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ViewProperty(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.property_ = Property(self, 'property_', 'MaterialExposedViewProperty')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class ViewSize(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class VirtualTextureFeatureSwitch(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.no = InSocket(self, 'No', 'StructProperty')
        self.yes = InSocket(self, 'Yes', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class VolumetricAdvancedMaterialInput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class VolumetricAdvancedMaterialOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.clamp_multi_scattering_contribution = Property(self, 'clamp_multi_scattering_contribution', 'bool')
        self.const_multi_scattering_contribution = Property(self, 'const_multi_scattering_contribution', 'float')
        self.const_multi_scattering_eccentricity = Property(self, 'const_multi_scattering_eccentricity', 'float')
        self.const_multi_scattering_occlusion = Property(self, 'const_multi_scattering_occlusion', 'float')
        self.const_phase_blend = Property(self, 'const_phase_blend', 'float')
        self.const_phase_g = Property(self, 'const_phase_g', 'float')
        self.const_phase_g2 = Property(self, 'const_phase_g2', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.gray_scale_material = Property(self, 'gray_scale_material', 'bool')
        self.ground_contribution = Property(self, 'ground_contribution', 'bool')
        self.multi_scattering_approximation_octave_count = Property(self, 'multi_scattering_approximation_octave_count', 'uint32')
        self.per_sample_phase_evaluation = Property(self, 'per_sample_phase_evaluation', 'bool')
        self.ray_march_volume_shadow = Property(self, 'ray_march_volume_shadow', 'bool')

        self.phaseG = InSocket(self, 'PhaseG', 'StructProperty')
        self.phaseG2 = InSocket(self, 'PhaseG2', 'StructProperty')
        self.phaseBlend = InSocket(self, 'PhaseBlend', 'StructProperty')
        self.multiScatteringContribution = InSocket(self, 'MultiScatteringContribution', 'StructProperty')
        self.multiScatteringOcclusion = InSocket(self, 'MultiScatteringOcclusion', 'StructProperty')
        self.multiScatteringEccentricity = InSocket(self, 'MultiScatteringEccentricity', 'StructProperty')
        self.conservativeDensity = InSocket(self, 'ConservativeDensity', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class VolumetricCloudEmptySpaceSkippingInput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class VolumetricCloudEmptySpaceSkippingOutput(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class WhileLoop(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')

class WorldPosition(MaterialExpression):
    def __init__(self) -> None:
        super().__init__()

        self.desc = Property(self, 'desc', 'str')
        self.world_position_shader_offset = Property(self, 'world_position_shader_offset', 'WorldPositionIncludedOffsets')

        self.input = InSocket(self, '', 'StructProperty')

        self.output = OutSocket(self, '', 'StructProperty')