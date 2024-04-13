//  This file is generated. Please do NOT modify.
#include <MaterialExpressionImpl.h>
#include <MaterialExpressionEditorPropertyImpl.h>
#include <InSocketImpl.h>
#include <OutSocketImpl.h>
#include <NodePos.h>

class Abs: public MaterialExpressionImpl {
    Abs(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class AbsorptionMediumMaterialOutput: public MaterialExpressionImpl {
    AbsorptionMediumMaterialOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ActorPositionWS: public MaterialExpressionImpl {
    ActorPositionWS(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.origin_type = MaterialExpressionEditorPropertyImpl(self, 'origin_type', 'PositionOrigin')
    }
}

class Add: public MaterialExpressionImpl {
    Add(None a = None, None b = None, NodePos node_pos = nullptr): base(None a = None, None b = None, NodePos node_pos = nullptr) {

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if (a is not None( {
            if (isinstance(a, float)( {
                self.const_a.set(a)
            else {
                self.a.comesFrom(a)
            }
        }
        if (b is not None( {
            if (isinstance(b, float)( {
                self.const_b.set(b)
            else {
                self.b.comesFrom(b)
            }
        }
    }
}

class AntialiasedTextureMask: public MaterialExpressionImpl {
    AntialiasedTextureMask(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class AppendVector: public MaterialExpressionImpl {
    AppendVector(None a = None, None b = None, NodePos node_pos = nullptr): base(None a = None, None b = None, NodePos node_pos = nullptr) {

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if (a is not None( {
            self.a.comesFrom(a)
        }
        if (b is not None( {
            self.b.comesFrom(b)
        }
    }
}

class Arccosine: public MaterialExpressionImpl {
    Arccosine(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ArccosineFast: public MaterialExpressionImpl {
    ArccosineFast(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Arcsine: public MaterialExpressionImpl {
    Arcsine(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ArcsineFast: public MaterialExpressionImpl {
    ArcsineFast(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Arctangent: public MaterialExpressionImpl {
    Arctangent(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Arctangent2: public MaterialExpressionImpl {
    Arctangent2(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.y = InSocketImpl(self, 'Y', 'StructProperty')
        self.x = InSocketImpl(self, 'X', 'StructProperty')
    }
}

class Arctangent2Fast: public MaterialExpressionImpl {
    Arctangent2Fast(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.y = InSocketImpl(self, 'Y', 'StructProperty')
        self.x = InSocketImpl(self, 'X', 'StructProperty')
    }
}

class ArctangentFast: public MaterialExpressionImpl {
    ArctangentFast(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class AtmosphericFogColor: public MaterialExpressionImpl {
    AtmosphericFogColor(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')
    }
}

class AtmosphericLightColor: public MaterialExpressionImpl {
    AtmosphericLightColor(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class AtmosphericLightVector: public MaterialExpressionImpl {
    AtmosphericLightVector(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class BentNormalCustomOutput: public MaterialExpressionImpl {
    BentNormalCustomOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class BinaryOp: public MaterialExpressionImpl {
    BinaryOp(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')
    }
}

class BlackBody: public MaterialExpressionImpl {
    BlackBody(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.temp = InSocketImpl(self, 'Temp', 'StructProperty')
    }
}

class BlendMaterialAttributes: public MaterialExpressionImpl {
    BlendMaterialAttributes(None a = None, None b = None, None alpha = None, NodePos node_pos = nullptr): base(None a = None, None b = None, None alpha = None, NodePos node_pos = nullptr) {

        self.pixel_attribute_blend_type = MaterialExpressionEditorPropertyImpl(self, 'pixel_attribute_blend_type', 'MaterialAttributeBlend')
        self.vertex_attribute_blend_type = MaterialExpressionEditorPropertyImpl(self, 'vertex_attribute_blend_type', 'MaterialAttributeBlend')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        self.alpha = InSocketImpl(self, 'Alpha', 'StructProperty')
        if (a is not None( {
            if (isinstance(a, float)( {
                self.const_a.set(a)
            else {
                self.a.comesFrom(a)
            }
        }
        if (b is not None( {
            if (isinstance(b, float)( {
                self.const_b.set(b)
            else {
                self.b.comesFrom(b)
            }
        }
        if (alpha is not None( {
            if (isinstance(alpha, float)( {
                self.const_alpha.set(alpha)
            else {
                self.alpha.comesFrom(alpha)
            }
        }
    }
}

class BreakMaterialAttributes: public MaterialExpressionImpl {
    BreakMaterialAttributes(None input = None, bool shouldAddRTParams = False, NodePos node_pos = nullptr): base(None input = None, bool shouldAddRTParams = False, NodePos node_pos = nullptr) {

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
        if (input is not None( {
            self.input.comesFrom(input)
        }
        if (shouldAddRTParams( {
            self.baseColor.add_rt()
            self.metallic.add_rt()
            self.specular.add_rt()
            self.roughness.add_rt()
            self.anisotropy.add_rt()
            self.emissiveColor.add_rt()
            self.opacity.add_rt()
            self.opacityMask.add_rt()
            self.normal.add_rt()
            self.tangent.add_rt()
            self.worldPositionOffset.add_rt()
            self.subsurfaceColor.add_rt()
            self.clearCoat.add_rt()
            self.clearCoatRoughness.add_rt()
            self.ambientOcclusion.add_rt()
            self.refraction.add_rt()
            self.customizedUV0.add_rt()
            self.customizedUV1.add_rt()
            self.customizedUV2.add_rt()
            self.customizedUV3.add_rt()
            self.customizedUV4.add_rt()
            self.customizedUV5.add_rt()
            self.customizedUV6.add_rt()
            self.customizedUV7.add_rt()
            self.pixelDepthOffset.add_rt()
            self.shadingModel.add_rt()
            self.displacement.add_rt()
        }
    }
}

class BumpOffset: public MaterialExpressionImpl {
    BumpOffset(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint32')
        self.height_ratio = MaterialExpressionEditorPropertyImpl(self, 'height_ratio', 'float')
        self.reference_plane = MaterialExpressionEditorPropertyImpl(self, 'reference_plane', 'float')

        self.coordinate = InSocketImpl(self, 'Coordinate', 'StructProperty')
        self.height = InSocketImpl(self, 'Height', 'StructProperty')
        self.heightRatioInput = InSocketImpl(self, 'HeightRatioInput', 'StructProperty')
    }
}

class CameraPositionWS: public MaterialExpressionImpl {
    CameraPositionWS(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class CameraVectorWS: public MaterialExpressionImpl {
    CameraVectorWS(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Ceil: public MaterialExpressionImpl {
    Ceil(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ChannelMaskParameter: public MaterialExpressionImpl {
    ChannelMaskParameter(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr): base(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr) {

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
    }
}

class Clamp: public MaterialExpressionImpl {
    Clamp(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.clamp_mode = MaterialExpressionEditorPropertyImpl(self, 'clamp_mode', 'ClampMode')
        self.max_default = MaterialExpressionEditorPropertyImpl(self, 'max_default', 'float')
        self.min_default = MaterialExpressionEditorPropertyImpl(self, 'min_default', 'float')

        self.min = InSocketImpl(self, 'Min', 'StructProperty')
        self.max = InSocketImpl(self, 'Max', 'StructProperty')
    }
}

class ClearCoatNormalCustomOutput: public MaterialExpressionImpl {
    ClearCoatNormalCustomOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class CloudSampleAttribute: public MaterialExpressionImpl {
    CloudSampleAttribute(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class CollectionParameter: public MaterialExpressionImpl {
    CollectionParameter(None parameter_name = None, NodePos node_pos = nullptr): base(None parameter_name = None, NodePos node_pos = nullptr) {

        self.collection = MaterialExpressionEditorPropertyImpl(self, 'collection', 'MaterialParameterCollection')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')

        self.parameterId = InSocketImpl(self, 'ParameterId', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
    }
}

class Comment: public MaterialExpressionImpl {
    Comment(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.color_comment_bubble = MaterialExpressionEditorPropertyImpl(self, 'color_comment_bubble', 'bool')
        self.comment_bubble_visible_in_details_panel = MaterialExpressionEditorPropertyImpl(self, 'comment_bubble_visible_in_details_panel', 'bool')
        self.comment_color = MaterialExpressionEditorPropertyImpl(self, 'comment_color', 'LinearColor')
        self.font_size = MaterialExpressionEditorPropertyImpl(self, 'font_size', 'int32')
        self.group_mode = MaterialExpressionEditorPropertyImpl(self, 'group_mode', 'bool')
        self.text = MaterialExpressionEditorPropertyImpl(self, 'text', 'str')

        self.commentColor = InSocketImpl(self, 'CommentColor', 'StructProperty')
    }
}

class ComponentMask: public MaterialExpressionImpl {
    ComponentMask(None input = None, str rgbaMask = None, NodePos node_pos = nullptr): base(None input = None, str rgbaMask = None, NodePos node_pos = nullptr) {

        self.a = MaterialExpressionEditorPropertyImpl(self, 'a', 'bool')
        self.b = MaterialExpressionEditorPropertyImpl(self, 'b', 'bool')
        self.g = MaterialExpressionEditorPropertyImpl(self, 'g', 'bool')
        self.r = MaterialExpressionEditorPropertyImpl(self, 'r', 'bool')
        if (input is not None( {
            self.input.comesFrom(input)
        }
        if (rgbaMask is not None( {
            __mask = rgbaMask.lower()
            self.r.set('r' in __mask)
            self.g.set('g' in __mask)
            self.b.set('b' in __mask)
            self.a.set('a' in __mask)
        else {
            self.r.set(True)
            self.g.set(True)
            self.b.set(False)
            self.a.set(False)
        }
    }
}

class Composite: public MaterialExpressionImpl {
    Composite(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.subgraph_name = MaterialExpressionEditorPropertyImpl(self, 'subgraph_name', 'str')
    }
}

class Constant: public MaterialExpressionImpl {
    Constant(None r = None, NodePos node_pos = nullptr): base(None r = None, NodePos node_pos = nullptr) {

        self.r = MaterialExpressionEditorPropertyImpl(self, 'r', 'float')
        if r is not None:
            self.r.set(r)
    }
}

class Constant2Vector: public MaterialExpressionImpl {
    Constant2Vector(None constant = None, NodePos node_pos = nullptr): base(None constant = None, NodePos node_pos = nullptr) {

        self.g = MaterialExpressionEditorPropertyImpl(self, 'g', 'float')
        self.r = MaterialExpressionEditorPropertyImpl(self, 'r', 'float')

        self.r = OutSocketImpl(self, 'r', 'StructProperty')
        self.g = OutSocketImpl(self, 'g', 'StructProperty')
        if constant is not None:
            self.constant.set(constant)
    }
}

class Constant3Vector: public MaterialExpressionImpl {
    Constant3Vector(None constant = None, NodePos node_pos = nullptr): base(None constant = None, NodePos node_pos = nullptr) {

        self.constant = MaterialExpressionEditorPropertyImpl(self, 'constant', 'LinearColor')

        self.r = OutSocketImpl(self, 'r', 'StructProperty')
        self.g = OutSocketImpl(self, 'g', 'StructProperty')
        self.b = OutSocketImpl(self, 'b', 'StructProperty')
        if constant is not None:
            self.constant.set(constant)
    }
}

class Constant4Vector: public MaterialExpressionImpl {
    Constant4Vector(None constant = None, NodePos node_pos = nullptr): base(None constant = None, NodePos node_pos = nullptr) {

        self.constant = MaterialExpressionEditorPropertyImpl(self, 'constant', 'LinearColor')

        self.r = OutSocketImpl(self, 'r', 'StructProperty')
        self.g = OutSocketImpl(self, 'g', 'StructProperty')
        self.b = OutSocketImpl(self, 'b', 'StructProperty')
        self.a = OutSocketImpl(self, 'a', 'StructProperty')
        if constant is not None:
            self.constant.set(constant)
    }
}

class ConstantBiasScale: public MaterialExpressionImpl {
    ConstantBiasScale(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.bias = MaterialExpressionEditorPropertyImpl(self, 'bias', 'float')
        self.scale = MaterialExpressionEditorPropertyImpl(self, 'scale', 'float')
    }
}

class ConstantDouble: public MaterialExpressionImpl {
    ConstantDouble(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.value = MaterialExpressionEditorPropertyImpl(self, 'value', 'double')
    }
}

class Cosine: public MaterialExpressionImpl {
    Cosine(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.period = MaterialExpressionEditorPropertyImpl(self, 'period', 'float')
    }
}

class CrossProduct: public MaterialExpressionImpl {
    CrossProduct(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
    }
}

class CurveAtlasRowParameter: public MaterialExpressionImpl {
    CurveAtlasRowParameter(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr): base(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr) {

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
    }
}

class Custom: public MaterialExpressionImpl {
    Custom(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.additional_defines = MaterialExpressionEditorPropertyImpl(self, 'additional_defines', 'Array[CustomDefine]')
        self.additional_outputs = MaterialExpressionEditorPropertyImpl(self, 'additional_outputs', 'Array[CustomOutput]')
        self.code = MaterialExpressionEditorPropertyImpl(self, 'code', 'str')
        self.description = MaterialExpressionEditorPropertyImpl(self, 'description', 'str')
        self.include_file_paths = MaterialExpressionEditorPropertyImpl(self, 'include_file_paths', 'Array[str]')
        self.inputs = MaterialExpressionEditorPropertyImpl(self, 'inputs', 'Array[CustomInput]')
        self.output_type = MaterialExpressionEditorPropertyImpl(self, 'output_type', 'CustomMaterialOutputType')
    }
}

class CustomOutput: public MaterialExpressionImpl {
    CustomOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class DBufferTexture: public MaterialExpressionImpl {
    DBufferTexture(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.d_buffer_texture_id = MaterialExpressionEditorPropertyImpl(self, 'd_buffer_texture_id', 'DBufferTextureId')
    }
}

class DDX: public MaterialExpressionImpl {
    DDX(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.value = InSocketImpl(self, 'Value', 'StructProperty')
    }
}

class DDY: public MaterialExpressionImpl {
    DDY(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.value = InSocketImpl(self, 'Value', 'StructProperty')
    }
}

class DataDrivenShaderPlatformInfoSwitch: public MaterialExpressionImpl {
    DataDrivenShaderPlatformInfoSwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.ddspi_property_names = MaterialExpressionEditorPropertyImpl(self, 'ddspi_property_names', 'Array[DataDrivenShaderPlatformInfoInput]')
    }
}

class DecalColor: public MaterialExpressionImpl {
    DecalColor(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class DecalDerivative: public MaterialExpressionImpl {
    DecalDerivative(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class DecalLifetimeOpacity: public MaterialExpressionImpl {
    DecalLifetimeOpacity(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class DecalMipmapLevel: public MaterialExpressionImpl {
    DecalMipmapLevel(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_height = MaterialExpressionEditorPropertyImpl(self, 'const_height', 'float')
        self.const_width = MaterialExpressionEditorPropertyImpl(self, 'const_width', 'float')

        self.textureSize = InSocketImpl(self, 'TextureSize', 'StructProperty')
    }
}

class DeltaTime: public MaterialExpressionImpl {
    DeltaTime(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class DepthFade: public MaterialExpressionImpl {
    DepthFade(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.fade_distance_default = MaterialExpressionEditorPropertyImpl(self, 'fade_distance_default', 'float')
        self.opacity_default = MaterialExpressionEditorPropertyImpl(self, 'opacity_default', 'float')

        self.inOpacity = InSocketImpl(self, 'InOpacity', 'StructProperty')
        self.fadeDistance = InSocketImpl(self, 'FadeDistance', 'StructProperty')
    }
}

class DepthOfFieldFunction: public MaterialExpressionImpl {
    DepthOfFieldFunction(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.function_value = MaterialExpressionEditorPropertyImpl(self, 'function_value', 'DepthOfFieldFunctionValue')

        self.depth = InSocketImpl(self, 'Depth', 'StructProperty')
    }
}

class DeriveNormalZ: public MaterialExpressionImpl {
    DeriveNormalZ(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.inXY = InSocketImpl(self, 'InXY', 'StructProperty')
    }
}

class Desaturation: public MaterialExpressionImpl {
    Desaturation(None input = None, None fraction = None, NodePos node_pos = nullptr): base(None input = None, None fraction = None, NodePos node_pos = nullptr) {

        self.luminance_factors = MaterialExpressionEditorPropertyImpl(self, 'luminance_factors', 'LinearColor')

        self.fraction = InSocketImpl(self, 'Fraction', 'StructProperty')
        if (input is not None( {
            self.input.comesFrom(input)
        }
        if (fraction is not None( {
            self.fraction.comesFrom(fraction)
        }
    }
}

class Distance: public MaterialExpressionImpl {
    Distance(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
    }
}

class DistanceCullFade: public MaterialExpressionImpl {
    DistanceCullFade(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class DistanceFieldApproxAO: public MaterialExpressionImpl {
    DistanceFieldApproxAO(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.base_distance_default = MaterialExpressionEditorPropertyImpl(self, 'base_distance_default', 'float')
        self.num_steps = MaterialExpressionEditorPropertyImpl(self, 'num_steps', 'uint32')
        self.radius_default = MaterialExpressionEditorPropertyImpl(self, 'radius_default', 'float')
        self.step_scale_default = MaterialExpressionEditorPropertyImpl(self, 'step_scale_default', 'float')
    }
}

class DistanceFieldGradient: public MaterialExpressionImpl {
    DistanceFieldGradient(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.position = InSocketImpl(self, 'Position', 'StructProperty')
    }
}

class DistanceFieldsRenderingSwitch: public MaterialExpressionImpl {
    DistanceFieldsRenderingSwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.no = InSocketImpl(self, 'No', 'StructProperty')
        self.yes = InSocketImpl(self, 'Yes', 'StructProperty')
    }
}

class DistanceToNearestSurface: public MaterialExpressionImpl {
    DistanceToNearestSurface(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.position = InSocketImpl(self, 'Position', 'StructProperty')
    }
}

class Divide: public MaterialExpressionImpl {
    Divide(None a = None, None b = None, NodePos node_pos = nullptr): base(None a = None, None b = None, NodePos node_pos = nullptr) {

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if (a is not None( {
            if (isinstance(a, float)( {
                self.const_a.set(a)
            else {
                self.a.comesFrom(a)
            }
        }
        if (b is not None( {
            if (isinstance(b, float)( {
                self.const_b.set(b)
            else {
                self.b.comesFrom(b)
            }
        }
    }
}

class DotProduct: public MaterialExpressionImpl {
    DotProduct(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
    }
}

class DoubleVectorParameter: public MaterialExpressionImpl {
    DoubleVectorParameter(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr): base(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr) {

        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'Vector4d')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if default_value is not None:
            self.default_value.set(default_value)
    }
}

class DynamicParameter: public MaterialExpressionImpl {
    DynamicParameter(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'LinearColor')
        self.param_names = MaterialExpressionEditorPropertyImpl(self, 'param_names', 'Array[str]')
        self.parameter_index = MaterialExpressionEditorPropertyImpl(self, 'parameter_index', 'uint32')

        self.defaultValue = InSocketImpl(self, 'DefaultValue', 'StructProperty')
    }
}

class ExecBegin: public MaterialExpressionImpl {
    ExecBegin(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ExecEnd: public MaterialExpressionImpl {
    ExecEnd(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Exponential: public MaterialExpressionImpl {
    Exponential(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Exponential2: public MaterialExpressionImpl {
    Exponential2(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class EyeAdaptation: public MaterialExpressionImpl {
    EyeAdaptation(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class EyeAdaptationInverse: public MaterialExpressionImpl {
    EyeAdaptationInverse(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class FeatureLevelSwitch: public MaterialExpressionImpl {
    FeatureLevelSwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
    }
}

class Floor: public MaterialExpressionImpl {
    Floor(None input = None, NodePos node_pos = nullptr): base(None input = None, NodePos node_pos = nullptr) {
        if (input is not None( {
            self.input.comesFrom(input)
        }
    }
}

class Fmod: public MaterialExpressionImpl {
    Fmod(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
    }
}

class FontSample: public MaterialExpressionImpl {
    FontSample(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.font = MaterialExpressionEditorPropertyImpl(self, 'font', 'Font')
        self.font_texture_page = MaterialExpressionEditorPropertyImpl(self, 'font_texture_page', 'int32')
    }
}

class FontSampleParameter: public MaterialExpressionImpl {
    FontSampleParameter(None parameter_name = None, NodePos node_pos = nullptr): base(None parameter_name = None, NodePos node_pos = nullptr) {

        self.font = MaterialExpressionEditorPropertyImpl(self, 'font', 'Font')
        self.font_texture_page = MaterialExpressionEditorPropertyImpl(self, 'font_texture_page', 'int32')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
    }
}

class ForLoop: public MaterialExpressionImpl {
    ForLoop(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Frac: public MaterialExpressionImpl {
    Frac(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Fresnel: public MaterialExpressionImpl {
    Fresnel(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.base_reflect_fraction = MaterialExpressionEditorPropertyImpl(self, 'base_reflect_fraction', 'float')
        self.exponent = MaterialExpressionEditorPropertyImpl(self, 'exponent', 'float')

        self.exponentIn = InSocketImpl(self, 'ExponentIn', 'StructProperty')
        self.baseReflectFractionIn = InSocketImpl(self, 'BaseReflectFractionIn', 'StructProperty')
        self.normal = InSocketImpl(self, 'Normal', 'StructProperty')
    }
}

class FunctionInput: public MaterialExpressionImpl {
    FunctionInput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.description = MaterialExpressionEditorPropertyImpl(self, 'description', 'str')
        self.input_name = MaterialExpressionEditorPropertyImpl(self, 'input_name', 'Name')
        self.input_type = MaterialExpressionEditorPropertyImpl(self, 'input_type', 'FunctionInputType')
        self.preview_value = MaterialExpressionEditorPropertyImpl(self, 'preview_value', 'Vector4f')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.use_preview_value_as_default = MaterialExpressionEditorPropertyImpl(self, 'use_preview_value_as_default', 'bool')

        self.preview = InSocketImpl(self, 'Preview', 'StructProperty')
        self.ID = InSocketImpl(self, 'ID', 'StructProperty')
        self.previewValue = InSocketImpl(self, 'PreviewValue', 'StructProperty')
    }
}

class FunctionOutput: public MaterialExpressionImpl {
    FunctionOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.description = MaterialExpressionEditorPropertyImpl(self, 'description', 'str')
        self.output_name = MaterialExpressionEditorPropertyImpl(self, 'output_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.ID = InSocketImpl(self, 'ID', 'StructProperty')
    }
}

class GIReplace: public MaterialExpressionImpl {
    GIReplace(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.staticIndirect = InSocketImpl(self, 'StaticIndirect', 'StructProperty')
        self.dynamicIndirect = InSocketImpl(self, 'DynamicIndirect', 'StructProperty')
    }
}

class GenericConstant: public MaterialExpressionImpl {
    GenericConstant(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class GetLocal: public MaterialExpressionImpl {
    GetLocal(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.local_name = MaterialExpressionEditorPropertyImpl(self, 'local_name', 'Name')
    }
}

class GetMaterialAttributes: public MaterialExpressionImpl {
    GetMaterialAttributes(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class HairAttributes: public MaterialExpressionImpl {
    HairAttributes(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.use_tangent_space = MaterialExpressionEditorPropertyImpl(self, 'use_tangent_space', 'bool')
    }
}

class HairColor: public MaterialExpressionImpl {
    HairColor(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.melanin = InSocketImpl(self, 'Melanin', 'StructProperty')
        self.redness = InSocketImpl(self, 'Redness', 'StructProperty')
        self.dyeColor = InSocketImpl(self, 'DyeColor', 'StructProperty')
    }
}

class HeightfieldMinMaxTexture: public MaterialExpressionImpl {
    HeightfieldMinMaxTexture(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.min_max_texture = MaterialExpressionEditorPropertyImpl(self, 'min_max_texture', 'HeightfieldMinMaxTexture')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
    }
}

class HsvToRgb: public MaterialExpressionImpl {
    HsvToRgb(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class If: public MaterialExpressionImpl {
    If(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')
        self.equals_threshold = MaterialExpressionEditorPropertyImpl(self, 'equals_threshold', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        self.aGreaterThanB = InSocketImpl(self, 'AGreaterThanB', 'StructProperty')
        self.aEqualsB = InSocketImpl(self, 'AEqualsB', 'StructProperty')
        self.aLessThanB = InSocketImpl(self, 'ALessThanB', 'StructProperty')
    }
}

class IfThenElse: public MaterialExpressionImpl {
    IfThenElse(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class InverseLinearInterpolate: public MaterialExpressionImpl {
    InverseLinearInterpolate(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.clamp_result = MaterialExpressionEditorPropertyImpl(self, 'clamp_result', 'bool')
        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')
        self.const_value = MaterialExpressionEditorPropertyImpl(self, 'const_value', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        self.value = InSocketImpl(self, 'Value', 'StructProperty')
    }
}

class IsOrthographic: public MaterialExpressionImpl {
    IsOrthographic(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class LandscapeGrassOutput: public MaterialExpressionImpl {
    LandscapeGrassOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.grass_types = MaterialExpressionEditorPropertyImpl(self, 'grass_types', 'Array[GrassInput]')
    }
}

class LandscapeLayerBlend: public MaterialExpressionImpl {
    LandscapeLayerBlend(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.layers = MaterialExpressionEditorPropertyImpl(self, 'layers', 'Array[LayerBlendInput]')
    }
}

class LandscapeLayerCoords: public MaterialExpressionImpl {
    LandscapeLayerCoords(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.custom_uv_type = MaterialExpressionEditorPropertyImpl(self, 'custom_uv_type', 'LandscapeCustomizedCoordType')
        self.mapping_pan_u = MaterialExpressionEditorPropertyImpl(self, 'mapping_pan_u', 'float')
        self.mapping_pan_v = MaterialExpressionEditorPropertyImpl(self, 'mapping_pan_v', 'float')
        self.mapping_rotation = MaterialExpressionEditorPropertyImpl(self, 'mapping_rotation', 'float')
        self.mapping_scale = MaterialExpressionEditorPropertyImpl(self, 'mapping_scale', 'float')
        self.mapping_type = MaterialExpressionEditorPropertyImpl(self, 'mapping_type', 'TerrainCoordMappingType')
    }
}

class LandscapeLayerSample: public MaterialExpressionImpl {
    LandscapeLayerSample(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.preview_weight = MaterialExpressionEditorPropertyImpl(self, 'preview_weight', 'float')
    }
}

class LandscapeLayerSwitch: public MaterialExpressionImpl {
    LandscapeLayerSwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.preview_used = MaterialExpressionEditorPropertyImpl(self, 'preview_used', 'bool')
    }
}

class LandscapeLayerWeight: public MaterialExpressionImpl {
    LandscapeLayerWeight(None parameter_name = None, float preview_weight = None, NodePos node_pos = nullptr): base(None parameter_name = None, float preview_weight = None, NodePos node_pos = nullptr) {

        self.const_base = MaterialExpressionEditorPropertyImpl(self, 'const_base', 'Vector')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.preview_weight = MaterialExpressionEditorPropertyImpl(self, 'preview_weight', 'float')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
        if preview_weight is not None:
            self.preview_weight.set(preview_weight)
    }
}

class LandscapePhysicalMaterialOutput: public MaterialExpressionImpl {
    LandscapePhysicalMaterialOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.inputs = MaterialExpressionEditorPropertyImpl(self, 'inputs', 'Array[PhysicalMaterialInput]')
    }
}

class LandscapeVisibilityMask: public MaterialExpressionImpl {
    LandscapeVisibilityMask(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Length: public MaterialExpressionImpl {
    Length(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Less: public MaterialExpressionImpl {
    Less(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')
    }
}

class LightVector: public MaterialExpressionImpl {
    LightVector(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class LightmapUVs: public MaterialExpressionImpl {
    LightmapUVs(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class LightmassReplace: public MaterialExpressionImpl {
    LightmassReplace(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.realtime = InSocketImpl(self, 'Realtime', 'StructProperty')
        self.lightmass = InSocketImpl(self, 'Lightmass', 'StructProperty')
    }
}

class LinearInterpolate: public MaterialExpressionImpl {
    LinearInterpolate(None a = None, None b = None, None alpha = None, NodePos node_pos = nullptr): base(None a = None, None b = None, None alpha = None, NodePos node_pos = nullptr) {

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        self.alpha = InSocketImpl(self, 'Alpha', 'StructProperty')
        if (a is not None( {
            if (isinstance(a, float)( {
                self.const_a.set(a)
            else {
                self.a.comesFrom(a)
            }
        }
        if (b is not None( {
            if (isinstance(b, float)( {
                self.const_b.set(b)
            else {
                self.b.comesFrom(b)
            }
        }
        if (alpha is not None( {
            if (isinstance(alpha, float)( {
                self.const_alpha.set(alpha)
            else {
                self.alpha.comesFrom(alpha)
            }
        }
    }
}

class Logarithm: public MaterialExpressionImpl {
    Logarithm(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Logarithm10: public MaterialExpressionImpl {
    Logarithm10(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.x = InSocketImpl(self, 'X', 'StructProperty')
    }
}

class Logarithm2: public MaterialExpressionImpl {
    Logarithm2(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.x = InSocketImpl(self, 'X', 'StructProperty')
    }
}

class MakeMaterialAttributes: public MaterialExpressionImpl {
    MakeMaterialAttributes(BreakMaterialAttributes materialAttributes = None, NodePos node_pos = nullptr): base(BreakMaterialAttributes materialAttributes = None, NodePos node_pos = nullptr) {

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

        if materialAttributes is not None:
            self.baseColor.comesFrom(materialAttributes.baseColor)
            self.metallic.comesFrom(materialAttributes.metallic)
            self.specular.comesFrom(materialAttributes.specular)
            self.roughness.comesFrom(materialAttributes.roughness)
            self.anisotropy.comesFrom(materialAttributes.anisotropy)
            self.emissiveColor.comesFrom(materialAttributes.emissiveColor)
            self.opacity.comesFrom(materialAttributes.opacity)
            self.opacityMask.comesFrom(materialAttributes.opacityMask)
            self.normal.comesFrom(materialAttributes.normal)
            self.tangent.comesFrom(materialAttributes.tangent)
            self.worldPositionOffset.comesFrom(materialAttributes.worldPositionOffset)
            self.subsurfaceColor.comesFrom(materialAttributes.subsurfaceColor)
            self.clearCoat.comesFrom(materialAttributes.clearCoat)
            self.clearCoatRoughness.comesFrom(materialAttributes.clearCoatRoughness)
            self.ambientOcclusion.comesFrom(materialAttributes.ambientOcclusion)
            self.refraction.comesFrom(materialAttributes.refraction)
            self.pixelDepthOffset.comesFrom(materialAttributes.pixelDepthOffset)
            self.shadingModel.comesFrom(materialAttributes.shadingModel)
            self.displacement.comesFrom(materialAttributes.displacement)
    }
}

class MapARPassthroughCameraUV: public MaterialExpressionImpl {
    MapARPassthroughCameraUV(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')
    }
}

class MaterialAttributeLayers: public MaterialExpressionImpl {
    MaterialAttributeLayers(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.default_layers = MaterialExpressionEditorPropertyImpl(self, 'default_layers', 'MaterialLayersFunctions')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        self.defaultLayers = InSocketImpl(self, 'DefaultLayers', 'StructProperty')
    }
}

class MaterialFunctionCall: public MaterialExpressionImpl {
    MaterialFunctionCall(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.material_function = MaterialExpressionEditorPropertyImpl(self, 'material_function', 'MaterialFunctionInterface')

        self.functionParameterInfo = InSocketImpl(self, 'FunctionParameterInfo', 'StructProperty')
    }
}

class MaterialLayerOutput: public MaterialExpressionImpl {
    MaterialLayerOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.description = MaterialExpressionEditorPropertyImpl(self, 'description', 'str')
        self.output_name = MaterialExpressionEditorPropertyImpl(self, 'output_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.ID = InSocketImpl(self, 'ID', 'StructProperty')
    }
}

class MaterialProxyReplace: public MaterialExpressionImpl {
    MaterialProxyReplace(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.realtime = InSocketImpl(self, 'Realtime', 'StructProperty')
        self.materialProxy = InSocketImpl(self, 'MaterialProxy', 'StructProperty')
    }
}

class MaterialXAppend3Vector: public MaterialExpressionImpl {
    MaterialXAppend3Vector(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class MaterialXAppend4Vector: public MaterialExpressionImpl {
    MaterialXAppend4Vector(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class MaterialXBurn: public MaterialExpressionImpl {
    MaterialXBurn(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXDifference: public MaterialExpressionImpl {
    MaterialXDifference(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXDisjointOver: public MaterialExpressionImpl {
    MaterialXDisjointOver(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXDodge: public MaterialExpressionImpl {
    MaterialXDodge(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXFractal3D: public MaterialExpressionImpl {
    MaterialXFractal3D(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_amplitude = MaterialExpressionEditorPropertyImpl(self, 'const_amplitude', 'float')
        self.const_diminish = MaterialExpressionEditorPropertyImpl(self, 'const_diminish', 'float')
        self.const_lacunarity = MaterialExpressionEditorPropertyImpl(self, 'const_lacunarity', 'float')
        self.const_octaves = MaterialExpressionEditorPropertyImpl(self, 'const_octaves', 'int32')
        self.levels = MaterialExpressionEditorPropertyImpl(self, 'levels', 'int32')
        self.output_max = MaterialExpressionEditorPropertyImpl(self, 'output_max', 'float')
        self.output_min = MaterialExpressionEditorPropertyImpl(self, 'output_min', 'float')
        self.scale = MaterialExpressionEditorPropertyImpl(self, 'scale', 'float')
        self.turbulence = MaterialExpressionEditorPropertyImpl(self, 'turbulence', 'bool')
    }
}

class MaterialXIn: public MaterialExpressionImpl {
    MaterialXIn(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXLuminance: public MaterialExpressionImpl {
    MaterialXLuminance(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.luminance_factors = MaterialExpressionEditorPropertyImpl(self, 'luminance_factors', 'LinearColor')
        self.luminance_mode = MaterialExpressionEditorPropertyImpl(self, 'luminance_mode', 'MaterialXLuminanceMode')
    }
}

class MaterialXMask: public MaterialExpressionImpl {
    MaterialXMask(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXMatte: public MaterialExpressionImpl {
    MaterialXMatte(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXMinus: public MaterialExpressionImpl {
    MaterialXMinus(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXOut: public MaterialExpressionImpl {
    MaterialXOut(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXOver: public MaterialExpressionImpl {
    MaterialXOver(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXOverlay: public MaterialExpressionImpl {
    MaterialXOverlay(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXPlace2D: public MaterialExpressionImpl {
    MaterialXPlace2D(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
        self.const_rotation_angle = MaterialExpressionEditorPropertyImpl(self, 'const_rotation_angle', 'float')
    }
}

class MaterialXPlus: public MaterialExpressionImpl {
    MaterialXPlus(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXPremult: public MaterialExpressionImpl {
    MaterialXPremult(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class MaterialXRamp4: public MaterialExpressionImpl {
    MaterialXRamp4(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
    }
}

class MaterialXRampLeftRight: public MaterialExpressionImpl {
    MaterialXRampLeftRight(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
    }
}

class MaterialXRampTopBottom: public MaterialExpressionImpl {
    MaterialXRampTopBottom(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
    }
}

class MaterialXRemap: public MaterialExpressionImpl {
    MaterialXRemap(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.input_high_default = MaterialExpressionEditorPropertyImpl(self, 'input_high_default', 'float')
        self.input_low_default = MaterialExpressionEditorPropertyImpl(self, 'input_low_default', 'float')
        self.target_high_default = MaterialExpressionEditorPropertyImpl(self, 'target_high_default', 'float')
        self.target_low_default = MaterialExpressionEditorPropertyImpl(self, 'target_low_default', 'float')
    }
}

class MaterialXRotate2D: public MaterialExpressionImpl {
    MaterialXRotate2D(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_rotation_angle = MaterialExpressionEditorPropertyImpl(self, 'const_rotation_angle', 'float')
    }
}

class MaterialXScreen: public MaterialExpressionImpl {
    MaterialXScreen(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_alpha = MaterialExpressionEditorPropertyImpl(self, 'const_alpha', 'float')
    }
}

class MaterialXSplitLeftRight: public MaterialExpressionImpl {
    MaterialXSplitLeftRight(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_center = MaterialExpressionEditorPropertyImpl(self, 'const_center', 'float')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
    }
}

class MaterialXSplitTopBottom: public MaterialExpressionImpl {
    MaterialXSplitTopBottom(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_center = MaterialExpressionEditorPropertyImpl(self, 'const_center', 'float')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint8')
    }
}

class MaterialXSwizzle: public MaterialExpressionImpl {
    MaterialXSwizzle(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.channels = MaterialExpressionEditorPropertyImpl(self, 'channels', 'str')
    }
}

class MaterialXTextureSampleParameterBlur: public MaterialExpressionImpl {
    MaterialXTextureSampleParameterBlur(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class MaterialXUnpremult: public MaterialExpressionImpl {
    MaterialXUnpremult(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Max: public MaterialExpressionImpl {
    Max(None a = None, None b = None, NodePos node_pos = nullptr): base(None a = None, None b = None, NodePos node_pos = nullptr) {

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if (a is not None( {
            if (isinstance(a, float)( {
                self.const_a.set(a)
            else {
                self.a.comesFrom(a)
            }
        }
        if (b is not None( {
            if (isinstance(b, float)( {
                self.const_b.set(b)
            else {
                self.b.comesFrom(b)
            }
        }
    }
}

class Min: public MaterialExpressionImpl {
    Min(None a = None, None b = None, NodePos node_pos = nullptr): base(None a = None, None b = None, NodePos node_pos = nullptr) {

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if (a is not None( {
            if (isinstance(a, float)( {
                self.const_a.set(a)
            else {
                self.a.comesFrom(a)
            }
        }
        if (b is not None( {
            if (isinstance(b, float)( {
                self.const_b.set(b)
            else {
                self.b.comesFrom(b)
            }
        }
    }
}

class Multiply: public MaterialExpressionImpl {
    Multiply(None a = None, None b = None, NodePos node_pos = nullptr): base(None a = None, None b = None, NodePos node_pos = nullptr) {

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if (a is not None( {
            if (isinstance(a, float)( {
                self.const_a.set(a)
            else {
                self.a.comesFrom(a)
            }
        }
        if (b is not None( {
            if (isinstance(b, float)( {
                self.const_b.set(b)
            else {
                self.b.comesFrom(b)
            }
        }
    }
}

class NamedRerouteBase: public MaterialExpressionImpl {
    NamedRerouteBase(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class NamedRerouteDeclaration: public MaterialExpressionImpl {
    NamedRerouteDeclaration(None name = None, None input = None, None nodeColor = None, NodePos node_pos = nullptr): base(None name = None, None input = None, None nodeColor = None, NodePos node_pos = nullptr) {

        self.name = MaterialExpressionEditorPropertyImpl(self, 'name', 'Name')
        self.nodeNolor = MaterialExpressionEditorPropertyImpl(self, 'nodeNolor', 'LinearColor')
        self.variableGuid = MaterialExpressionEditorPropertyImpl(self, 'variableGuid', 'Guid')

        self.variableGuid = InSocketImpl(self, 'VariableGuid', 'StructProperty')
        if name is not None:
            self.name.set(name)
        if (input is not None( {
            self.input.comesFrom(input)
            input.rt = self
        }
        if nodeColor is not None:
            self.nodeColor.set(nodeColor)
    }
}

class NamedRerouteUsage: public MaterialExpressionImpl {
    NamedRerouteUsage(None declarationGuid = None, NodePos node_pos = nullptr): base(None declarationGuid = None, NodePos node_pos = nullptr) {

        self.declarationGuid = MaterialExpressionEditorPropertyImpl(self, 'declarationGuid', 'Guid')
        if declarationGuid is not None:
            self.declarationGuid.set(declarationGuid)
    }
}

class NaniteReplace: public MaterialExpressionImpl {
    NaniteReplace(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Noise: public MaterialExpressionImpl {
    Noise(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class Normalize: public MaterialExpressionImpl {
    Normalize(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.vectorInput = InSocketImpl(self, 'VectorInput', 'StructProperty')
    }
}

class ObjectBounds: public MaterialExpressionImpl {
    ObjectBounds(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ObjectLocalBounds: public MaterialExpressionImpl {
    ObjectLocalBounds(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ObjectOrientation: public MaterialExpressionImpl {
    ObjectOrientation(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ObjectPositionWS: public MaterialExpressionImpl {
    ObjectPositionWS(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.origin_type = MaterialExpressionEditorPropertyImpl(self, 'origin_type', 'PositionOrigin')
    }
}

class ObjectRadius: public MaterialExpressionImpl {
    ObjectRadius(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class OneMinus: public MaterialExpressionImpl {
    OneMinus(None input = None, NodePos node_pos = nullptr): base(None input = None, NodePos node_pos = nullptr) {
        if (input is not None( {
            self.input.comesFrom(input)
        }
    }
}

class Panner: public MaterialExpressionImpl {
    Panner(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint32')
        self.fractional_part = MaterialExpressionEditorPropertyImpl(self, 'fractional_part', 'bool')
        self.speed_x = MaterialExpressionEditorPropertyImpl(self, 'speed_x', 'float')
        self.speed_y = MaterialExpressionEditorPropertyImpl(self, 'speed_y', 'float')

        self.coordinate = InSocketImpl(self, 'Coordinate', 'StructProperty')
        self.time = InSocketImpl(self, 'Time', 'StructProperty')
        self.speed = InSocketImpl(self, 'Speed', 'StructProperty')
    }
}

class Parameter: public MaterialExpressionImpl {
    Parameter(None parameter_name = None, NodePos node_pos = nullptr): base(None parameter_name = None, NodePos node_pos = nullptr) {

        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
    }
}

class ParticleColor: public MaterialExpressionImpl {
    ParticleColor(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ParticleDirection: public MaterialExpressionImpl {
    ParticleDirection(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ParticleMacroUV: public MaterialExpressionImpl {
    ParticleMacroUV(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ParticleMotionBlurFade: public MaterialExpressionImpl {
    ParticleMotionBlurFade(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ParticlePositionWS: public MaterialExpressionImpl {
    ParticlePositionWS(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.origin_type = MaterialExpressionEditorPropertyImpl(self, 'origin_type', 'PositionOrigin')
    }
}

class ParticleRadius: public MaterialExpressionImpl {
    ParticleRadius(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ParticleRandom: public MaterialExpressionImpl {
    ParticleRandom(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ParticleRelativeTime: public MaterialExpressionImpl {
    ParticleRelativeTime(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ParticleSize: public MaterialExpressionImpl {
    ParticleSize(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ParticleSpeed: public MaterialExpressionImpl {
    ParticleSpeed(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ParticleSpriteRotation: public MaterialExpressionImpl {
    ParticleSpriteRotation(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ParticleSubUV: public MaterialExpressionImpl {
    ParticleSubUV(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class ParticleSubUVProperties: public MaterialExpressionImpl {
    ParticleSubUVProperties(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class PathTracingBufferTexture: public MaterialExpressionImpl {
    PathTracingBufferTexture(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.path_tracing_buffer_texture_id = MaterialExpressionEditorPropertyImpl(self, 'path_tracing_buffer_texture_id', 'PathTracingBufferTextureId')
    }
}

class PathTracingQualitySwitch: public MaterialExpressionImpl {
    PathTracingQualitySwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class PathTracingRayTypeSwitch: public MaterialExpressionImpl {
    PathTracingRayTypeSwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class PerInstanceCustomData: public MaterialExpressionImpl {
    PerInstanceCustomData(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_default_value = MaterialExpressionEditorPropertyImpl(self, 'const_default_value', 'float')
        self.data_index = MaterialExpressionEditorPropertyImpl(self, 'data_index', 'uint32')

        self.defaultValue = InSocketImpl(self, 'DefaultValue', 'StructProperty')
    }
}

class PerInstanceCustomData3Vector: public MaterialExpressionImpl {
    PerInstanceCustomData3Vector(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_default_value = MaterialExpressionEditorPropertyImpl(self, 'const_default_value', 'LinearColor')
        self.data_index = MaterialExpressionEditorPropertyImpl(self, 'data_index', 'uint32')
    }
}

class PerInstanceFadeAmount: public MaterialExpressionImpl {
    PerInstanceFadeAmount(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class PerInstanceRandom: public MaterialExpressionImpl {
    PerInstanceRandom(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class PinBase: public MaterialExpressionImpl {
    PinBase(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.reroute_pins = MaterialExpressionEditorPropertyImpl(self, 'reroute_pins', 'Array[CompositeReroute]')
    }
}

class PixelDepth: public MaterialExpressionImpl {
    PixelDepth(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class PixelNormalWS: public MaterialExpressionImpl {
    PixelNormalWS(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Power: public MaterialExpressionImpl {
    Power(None base = None, None exponent = None, NodePos node_pos = nullptr): base(None base = None, None exponent = None, NodePos node_pos = nullptr) {

        self.const_exponent = MaterialExpressionEditorPropertyImpl(self, 'const_exponent', 'float')

        self.base = InSocketImpl(self, 'Base', 'StructProperty')
        self.exponent = InSocketImpl(self, 'Exponent', 'StructProperty')
        if (base is not None( {
            self.base.comesFrom(base)
        }
        if (exponent is not None( {
            self.exponent.comesFrom(exponent)
        }
    }
}

class PreSkinnedLocalBounds: public MaterialExpressionImpl {
    PreSkinnedLocalBounds(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class PreSkinnedNormal: public MaterialExpressionImpl {
    PreSkinnedNormal(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class PreSkinnedPosition: public MaterialExpressionImpl {
    PreSkinnedPosition(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class PrecomputedAOMask: public MaterialExpressionImpl {
    PrecomputedAOMask(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class PreviousFrameSwitch: public MaterialExpressionImpl {
    PreviousFrameSwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.currentFrame = InSocketImpl(self, 'CurrentFrame', 'StructProperty')
        self.previousFrame = InSocketImpl(self, 'PreviousFrame', 'StructProperty')
    }
}

class QualitySwitch: public MaterialExpressionImpl {
    QualitySwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.low = InSocketImpl(self, 'Low', 'StructProperty')
        self.high = InSocketImpl(self, 'High', 'StructProperty')
        self.medium = InSocketImpl(self, 'Medium', 'StructProperty')
        self.epic = InSocketImpl(self, 'Epic', 'StructProperty')
    }
}

class RayTracingQualitySwitch: public MaterialExpressionImpl {
    RayTracingQualitySwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.normal = InSocketImpl(self, 'Normal', 'StructProperty')
        self.rayTraced = InSocketImpl(self, 'RayTraced', 'StructProperty')
    }
}

class ReflectionCapturePassSwitch: public MaterialExpressionImpl {
    ReflectionCapturePassSwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.reflection = InSocketImpl(self, 'Reflection', 'StructProperty')
    }
}

class ReflectionVectorWS: public MaterialExpressionImpl {
    ReflectionVectorWS(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.normalize_custom_world_normal = MaterialExpressionEditorPropertyImpl(self, 'normalize_custom_world_normal', 'bool')

        self.customWorldNormal = InSocketImpl(self, 'CustomWorldNormal', 'StructProperty')
    }
}

class Reroute: public MaterialExpressionImpl {
    Reroute(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class RerouteBase: public MaterialExpressionImpl {
    RerouteBase(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class RgbToHsv: public MaterialExpressionImpl {
    RgbToHsv(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class RotateAboutAxis: public MaterialExpressionImpl {
    RotateAboutAxis(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.period = MaterialExpressionEditorPropertyImpl(self, 'period', 'float')

        self.normalizedRotationAxis = InSocketImpl(self, 'NormalizedRotationAxis', 'StructProperty')
        self.rotationAngle = InSocketImpl(self, 'RotationAngle', 'StructProperty')
        self.pivotPoint = InSocketImpl(self, 'PivotPoint', 'StructProperty')
        self.position = InSocketImpl(self, 'Position', 'StructProperty')
    }
}

class Rotator: public MaterialExpressionImpl {
    Rotator(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.center_x = MaterialExpressionEditorPropertyImpl(self, 'center_x', 'float')
        self.center_y = MaterialExpressionEditorPropertyImpl(self, 'center_y', 'float')
        self.const_coordinate = MaterialExpressionEditorPropertyImpl(self, 'const_coordinate', 'uint32')
        self.speed = MaterialExpressionEditorPropertyImpl(self, 'speed', 'float')

        self.coordinate = InSocketImpl(self, 'Coordinate', 'StructProperty')
        self.time = InSocketImpl(self, 'Time', 'StructProperty')
    }
}

class Round: public MaterialExpressionImpl {
    Round(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class RuntimeVirtualTextureOutput: public MaterialExpressionImpl {
    RuntimeVirtualTextureOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.baseColor = InSocketImpl(self, 'BaseColor', 'StructProperty')
        self.specular = InSocketImpl(self, 'Specular', 'StructProperty')
        self.roughness = InSocketImpl(self, 'Roughness', 'StructProperty')
        self.normal = InSocketImpl(self, 'Normal', 'StructProperty')
        self.worldHeight = InSocketImpl(self, 'WorldHeight', 'StructProperty')
        self.opacity = InSocketImpl(self, 'Opacity', 'StructProperty')
        self.mask = InSocketImpl(self, 'Mask', 'StructProperty')
    }
}

class RuntimeVirtualTextureReplace: public MaterialExpressionImpl {
    RuntimeVirtualTextureReplace(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.virtualTextureOutput = InSocketImpl(self, 'VirtualTextureOutput', 'StructProperty')
    }
}

class RuntimeVirtualTextureSample: public MaterialExpressionImpl {
    RuntimeVirtualTextureSample(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class RuntimeVirtualTextureSampleParameter: public MaterialExpressionImpl {
    RuntimeVirtualTextureSampleParameter(None parameter_name = None, NodePos node_pos = nullptr): base(None parameter_name = None, NodePos node_pos = nullptr) {

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
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
    }
}

class SamplePhysicsIntegerField: public MaterialExpressionImpl {
    SamplePhysicsIntegerField(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.field_target = MaterialExpressionEditorPropertyImpl(self, 'field_target', 'FieldIntegerType')

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')
    }
}

class SamplePhysicsScalarField: public MaterialExpressionImpl {
    SamplePhysicsScalarField(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.field_target = MaterialExpressionEditorPropertyImpl(self, 'field_target', 'FieldScalarType')

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')
    }
}

class SamplePhysicsVectorField: public MaterialExpressionImpl {
    SamplePhysicsVectorField(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.field_target = MaterialExpressionEditorPropertyImpl(self, 'field_target', 'FieldVectorType')

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')
    }
}

class Saturate: public MaterialExpressionImpl {
    Saturate(None input = None, NodePos node_pos = nullptr): base(None input = None, NodePos node_pos = nullptr) {
        if (input is not None( {
            self.input.comesFrom(input)
        }
    }
}

class ScalarParameter: public MaterialExpressionImpl {
    ScalarParameter(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr): base(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr) {

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
    }
}

class SceneColor: public MaterialExpressionImpl {
    SceneColor(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_input = MaterialExpressionEditorPropertyImpl(self, 'const_input', 'Vector2D')
        self.input_mode = MaterialExpressionEditorPropertyImpl(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        self.offsetFraction = InSocketImpl(self, 'OffsetFraction', 'StructProperty')
        self.constInput = InSocketImpl(self, 'ConstInput', 'StructProperty')
    }
}

class SceneDepth: public MaterialExpressionImpl {
    SceneDepth(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_input = MaterialExpressionEditorPropertyImpl(self, 'const_input', 'Vector2D')
        self.input_mode = MaterialExpressionEditorPropertyImpl(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')
        self.constInput = InSocketImpl(self, 'ConstInput', 'StructProperty')
    }
}

class SceneDepthWithoutWater: public MaterialExpressionImpl {
    SceneDepthWithoutWater(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_input = MaterialExpressionEditorPropertyImpl(self, 'const_input', 'Vector2D')
        self.fallback_depth = MaterialExpressionEditorPropertyImpl(self, 'fallback_depth', 'float')
        self.input_mode = MaterialExpressionEditorPropertyImpl(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        self.constInput = InSocketImpl(self, 'ConstInput', 'StructProperty')
    }
}

class SceneTexelSize: public MaterialExpressionImpl {
    SceneTexelSize(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class SceneTexture: public MaterialExpressionImpl {
    SceneTexture(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.filtered = MaterialExpressionEditorPropertyImpl(self, 'filtered', 'bool')
        self.scene_texture_id = MaterialExpressionEditorPropertyImpl(self, 'scene_texture_id', 'SceneTextureId')

        self.coordinates = InSocketImpl(self, 'Coordinates', 'StructProperty')
    }
}

class ScreenPosition: public MaterialExpressionImpl {
    ScreenPosition(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class SetLocal: public MaterialExpressionImpl {
    SetLocal(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.local_name = MaterialExpressionEditorPropertyImpl(self, 'local_name', 'Name')
    }
}

class SetMaterialAttributes: public MaterialExpressionImpl {
    SetMaterialAttributes(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
        self.customizedUV0 = InSocketImpl(self, 'CustomizedUV0', 'StructProperty')
        self.customizedUV1 = InSocketImpl(self, 'CustomizedUV1', 'StructProperty')
        self.customizedUV2 = InSocketImpl(self, 'CustomizedUV2', 'StructProperty')
        self.customizedUV3 = InSocketImpl(self, 'CustomizedUV3', 'StructProperty')
        self.customizedUV4 = InSocketImpl(self, 'CustomizedUV4', 'StructProperty')
        self.customizedUV5 = InSocketImpl(self, 'CustomizedUV5', 'StructProperty')
        self.customizedUV6 = InSocketImpl(self, 'CustomizedUV6', 'StructProperty')
        self.customizedUV7 = InSocketImpl(self, 'CustomizedUV7', 'StructProperty')
        self.pixelDepthOffset = InSocketImpl(self, 'PixelDepthOffset', 'StructProperty')
        self.shadingModel = InSocketImpl(self, 'ShadingModel', 'StructProperty')
    }
}

class ShaderStageSwitch: public MaterialExpressionImpl {
    ShaderStageSwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.pixelShader = InSocketImpl(self, 'PixelShader', 'StructProperty')
        self.vertexShader = InSocketImpl(self, 'VertexShader', 'StructProperty')
    }
}

class ShadingModel: public MaterialExpressionImpl {
    ShadingModel(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.shading_model = MaterialExpressionEditorPropertyImpl(self, 'shading_model', 'MaterialShadingModel')
    }
}

class ShadingPathSwitch: public MaterialExpressionImpl {
    ShadingPathSwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.inputs = InSocketImpl(self, 'Inputs', 'StructProperty')
    }
}

class ShadowReplace: public MaterialExpressionImpl {
    ShadowReplace(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.default = InSocketImpl(self, 'Default', 'StructProperty')
        self.shadow = InSocketImpl(self, 'Shadow', 'StructProperty')
    }
}

class Sign: public MaterialExpressionImpl {
    Sign(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Sine: public MaterialExpressionImpl {
    Sine(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.period = MaterialExpressionEditorPropertyImpl(self, 'period', 'float')
    }
}

class SingleLayerWaterMaterialOutput: public MaterialExpressionImpl {
    SingleLayerWaterMaterialOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.scatteringCoefficients = InSocketImpl(self, 'ScatteringCoefficients', 'StructProperty')
        self.absorptionCoefficients = InSocketImpl(self, 'AbsorptionCoefficients', 'StructProperty')
        self.phaseG = InSocketImpl(self, 'PhaseG', 'StructProperty')
        self.colorScaleBehindWater = InSocketImpl(self, 'ColorScaleBehindWater', 'StructProperty')
    }
}

class SkyAtmosphereAerialPerspective: public MaterialExpressionImpl {
    SkyAtmosphereAerialPerspective(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')
    }
}

class SkyAtmosphereDistantLightScatteredLuminance: public MaterialExpressionImpl {
    SkyAtmosphereDistantLightScatteredLuminance(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class SkyAtmosphereLightDirection: public MaterialExpressionImpl {
    SkyAtmosphereLightDirection(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.light_index = MaterialExpressionEditorPropertyImpl(self, 'light_index', 'int32')
    }
}

class SkyAtmosphereLightDiskLuminance: public MaterialExpressionImpl {
    SkyAtmosphereLightDiskLuminance(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.light_index = MaterialExpressionEditorPropertyImpl(self, 'light_index', 'int32')
    }
}

class SkyAtmosphereLightIlluminance: public MaterialExpressionImpl {
    SkyAtmosphereLightIlluminance(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.light_index = MaterialExpressionEditorPropertyImpl(self, 'light_index', 'int32')

        self.worldPosition = InSocketImpl(self, 'WorldPosition', 'StructProperty')
    }
}

class SkyAtmosphereViewLuminance: public MaterialExpressionImpl {
    SkyAtmosphereViewLuminance(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class SkyLightEnvMapSample: public MaterialExpressionImpl {
    SkyLightEnvMapSample(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class SmoothStep: public MaterialExpressionImpl {
    SmoothStep(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_max = MaterialExpressionEditorPropertyImpl(self, 'const_max', 'float')
        self.const_min = MaterialExpressionEditorPropertyImpl(self, 'const_min', 'float')
        self.const_value = MaterialExpressionEditorPropertyImpl(self, 'const_value', 'float')

        self.min = InSocketImpl(self, 'Min', 'StructProperty')
        self.max = InSocketImpl(self, 'Max', 'StructProperty')
        self.value = InSocketImpl(self, 'Value', 'StructProperty')
    }
}

class Sobol: public MaterialExpressionImpl {
    Sobol(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_index = MaterialExpressionEditorPropertyImpl(self, 'const_index', 'uint32')
        self.const_seed = MaterialExpressionEditorPropertyImpl(self, 'const_seed', 'Vector2D')

        self.cell = InSocketImpl(self, 'Cell', 'StructProperty')
        self.index = InSocketImpl(self, 'Index', 'StructProperty')
        self.seed = InSocketImpl(self, 'Seed', 'StructProperty')
        self.constSeed = InSocketImpl(self, 'ConstSeed', 'StructProperty')
    }
}

class SparseVolumeTextureBase: public MaterialExpressionImpl {
    SparseVolumeTextureBase(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.sparse_volume_texture = MaterialExpressionEditorPropertyImpl(self, 'sparse_volume_texture', 'SparseVolumeTexture')
    }
}

class SparseVolumeTextureObject: public MaterialExpressionImpl {
    SparseVolumeTextureObject(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.sparse_volume_texture = MaterialExpressionEditorPropertyImpl(self, 'sparse_volume_texture', 'SparseVolumeTexture')
    }
}

class SparseVolumeTextureObjectParameter: public MaterialExpressionImpl {
    SparseVolumeTextureObjectParameter(None parameter_name = None, NodePos node_pos = nullptr): base(None parameter_name = None, NodePos node_pos = nullptr) {

        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.sparse_volume_texture = MaterialExpressionEditorPropertyImpl(self, 'sparse_volume_texture', 'SparseVolumeTexture')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
    }
}

class SparseVolumeTextureSample: public MaterialExpressionImpl {
    SparseVolumeTextureSample(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sparse_volume_texture = MaterialExpressionEditorPropertyImpl(self, 'sparse_volume_texture', 'SparseVolumeTexture')
    }
}

class SparseVolumeTextureSampleParameter: public MaterialExpressionImpl {
    SparseVolumeTextureSampleParameter(None parameter_name = None, NodePos node_pos = nullptr): base(None parameter_name = None, NodePos node_pos = nullptr) {

        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sampler_source = MaterialExpressionEditorPropertyImpl(self, 'sampler_source', 'SamplerSourceMode')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')
        self.sparse_volume_texture = MaterialExpressionEditorPropertyImpl(self, 'sparse_volume_texture', 'SparseVolumeTexture')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
    }
}

class SpeedTree: public MaterialExpressionImpl {
    SpeedTree(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.accurate_wind_velocities = MaterialExpressionEditorPropertyImpl(self, 'accurate_wind_velocities', 'bool')
        self.billboard_threshold = MaterialExpressionEditorPropertyImpl(self, 'billboard_threshold', 'float')
        self.geometry_type = MaterialExpressionEditorPropertyImpl(self, 'geometry_type', 'SpeedTreeGeometryType')
        self.lod_type = MaterialExpressionEditorPropertyImpl(self, 'lod_type', 'SpeedTreeLODType')
        self.wind_type = MaterialExpressionEditorPropertyImpl(self, 'wind_type', 'SpeedTreeWindType')

        self.geometryInput = InSocketImpl(self, 'GeometryInput', 'StructProperty')
        self.windInput = InSocketImpl(self, 'WindInput', 'StructProperty')
        self.lODInput = InSocketImpl(self, 'LODInput', 'StructProperty')
        self.extraBendWS = InSocketImpl(self, 'ExtraBendWS', 'StructProperty')
    }
}

class SphereMask: public MaterialExpressionImpl {
    SphereMask(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.attenuation_radius = MaterialExpressionEditorPropertyImpl(self, 'attenuation_radius', 'float')
        self.hardness_percent = MaterialExpressionEditorPropertyImpl(self, 'hardness_percent', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        self.radius = InSocketImpl(self, 'Radius', 'StructProperty')
        self.hardness = InSocketImpl(self, 'Hardness', 'StructProperty')
    }
}

class SphericalParticleOpacity: public MaterialExpressionImpl {
    SphericalParticleOpacity(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.constant_density = MaterialExpressionEditorPropertyImpl(self, 'constant_density', 'float')

        self.density = InSocketImpl(self, 'Density', 'StructProperty')
    }
}

class SpriteTextureSampler: public MaterialExpressionImpl {
    SpriteTextureSampler(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class SquareRoot: public MaterialExpressionImpl {
    SquareRoot(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StaticBool: public MaterialExpressionImpl {
    StaticBool(None value = None, NodePos node_pos = nullptr): base(None value = None, NodePos node_pos = nullptr) {

        self.value = MaterialExpressionEditorPropertyImpl(self, 'Value', 'bool')
        if value is not None:
            self.value.set(value)
    }
}

class StaticBoolParameter: public MaterialExpressionImpl {
    StaticBoolParameter(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr): base(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr) {

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
    }
}

class StaticComponentMaskParameter: public MaterialExpressionImpl {
    StaticComponentMaskParameter(None parameter_name = None, NodePos node_pos = nullptr): base(None parameter_name = None, NodePos node_pos = nullptr) {

        self.default_a = MaterialExpressionEditorPropertyImpl(self, 'default_a', 'bool')
        self.default_b = MaterialExpressionEditorPropertyImpl(self, 'default_b', 'bool')
        self.default_g = MaterialExpressionEditorPropertyImpl(self, 'default_g', 'bool')
        self.default_r = MaterialExpressionEditorPropertyImpl(self, 'default_r', 'bool')
        self.group = MaterialExpressionEditorPropertyImpl(self, 'group', 'Name')
        self.parameter_name = MaterialExpressionEditorPropertyImpl(self, 'parameter_name', 'Name')
        self.sort_priority = MaterialExpressionEditorPropertyImpl(self, 'sort_priority', 'int32')

        self.expressionGUID = InSocketImpl(self, 'ExpressionGUID', 'StructProperty')
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
    }
}

class StaticSwitch: public MaterialExpressionImpl {
    StaticSwitch(None true = None, None false = None, None value = None, NodePos node_pos = nullptr): base(None true = None, None false = None, None value = None, NodePos node_pos = nullptr) {

        self.default_value = MaterialExpressionEditorPropertyImpl(self, 'default_value', 'bool')

        self.true = InSocketImpl(self, 'True', 'StructProperty')
        self.false = InSocketImpl(self, 'False', 'StructProperty')
        self.value = InSocketImpl(self, 'Value', 'StructProperty')
        if (true is not None( {
            self.true.comesFrom(true)
        }
        if (false is not None( {
            self.false.comesFrom(false)
        }
        if (value is not None( {
            self.value.comesFrom(value)
        }
    }
}

class StaticSwitchParameter: public MaterialExpressionImpl {
    StaticSwitchParameter(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr): base(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr) {

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
    }
}

class Step: public MaterialExpressionImpl {
    Step(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_x = MaterialExpressionEditorPropertyImpl(self, 'const_x', 'float')
        self.const_y = MaterialExpressionEditorPropertyImpl(self, 'const_y', 'float')

        self.y = InSocketImpl(self, 'Y', 'StructProperty')
        self.x = InSocketImpl(self, 'X', 'StructProperty')
    }
}

class StrataAdd: public MaterialExpressionImpl {
    StrataAdd(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.use_parameter_blending = MaterialExpressionEditorPropertyImpl(self, 'use_parameter_blending', 'bool')
    }
}

class StrataBSDF: public MaterialExpressionImpl {
    StrataBSDF(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataConvertToDecal: public MaterialExpressionImpl {
    StrataConvertToDecal(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataEyeBSDF: public MaterialExpressionImpl {
    StrataEyeBSDF(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.subsurface_profile = MaterialExpressionEditorPropertyImpl(self, 'subsurface_profile', 'SubsurfaceProfile')
    }
}

class StrataHairBSDF: public MaterialExpressionImpl {
    StrataHairBSDF(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataHazinessToSecondaryRoughness: public MaterialExpressionImpl {
    StrataHazinessToSecondaryRoughness(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataHorizontalMixing: public MaterialExpressionImpl {
    StrataHorizontalMixing(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.use_parameter_blending = MaterialExpressionEditorPropertyImpl(self, 'use_parameter_blending', 'bool')
    }
}

class StrataLegacyConversion: public MaterialExpressionImpl {
    StrataLegacyConversion(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.subsurface_profile = MaterialExpressionEditorPropertyImpl(self, 'subsurface_profile', 'SubsurfaceProfile')
    }
}

class StrataLightFunction: public MaterialExpressionImpl {
    StrataLightFunction(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataMetalnessToDiffuseAlbedoF0: public MaterialExpressionImpl {
    StrataMetalnessToDiffuseAlbedoF0(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataPostProcess: public MaterialExpressionImpl {
    StrataPostProcess(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataSimpleClearCoatBSDF: public MaterialExpressionImpl {
    StrataSimpleClearCoatBSDF(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataSingleLayerWaterBSDF: public MaterialExpressionImpl {
    StrataSingleLayerWaterBSDF(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataSlabBSDF: public MaterialExpressionImpl {
    StrataSlabBSDF(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.specular_profile = MaterialExpressionEditorPropertyImpl(self, 'specular_profile', 'SpecularProfile')
        self.subsurface_profile = MaterialExpressionEditorPropertyImpl(self, 'subsurface_profile', 'SubsurfaceProfile')
        self.use_sss_diffusion = MaterialExpressionEditorPropertyImpl(self, 'use_sss_diffusion', 'bool')
    }
}

class StrataThinFilm: public MaterialExpressionImpl {
    StrataThinFilm(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataTransmittanceToMFP: public MaterialExpressionImpl {
    StrataTransmittanceToMFP(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataUI: public MaterialExpressionImpl {
    StrataUI(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataUnlitBSDF: public MaterialExpressionImpl {
    StrataUnlitBSDF(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataUtilityBase: public MaterialExpressionImpl {
    StrataUtilityBase(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataVerticalLayering: public MaterialExpressionImpl {
    StrataVerticalLayering(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.use_parameter_blending = MaterialExpressionEditorPropertyImpl(self, 'use_parameter_blending', 'bool')
    }
}

class StrataVolumetricFogCloudBSDF: public MaterialExpressionImpl {
    StrataVolumetricFogCloudBSDF(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class StrataWeight: public MaterialExpressionImpl {
    StrataWeight(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class SubsurfaceMediumMaterialOutput: public MaterialExpressionImpl {
    SubsurfaceMediumMaterialOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class Subtract: public MaterialExpressionImpl {
    Subtract(None a = None, None b = None, NodePos node_pos = nullptr): base(None a = None, None b = None, NodePos node_pos = nullptr) {

        self.const_a = MaterialExpressionEditorPropertyImpl(self, 'const_a', 'float')
        self.const_b = MaterialExpressionEditorPropertyImpl(self, 'const_b', 'float')

        self.a = InSocketImpl(self, 'A', 'StructProperty')
        self.b = InSocketImpl(self, 'B', 'StructProperty')
        if (a is not None( {
            if (isinstance(a, float)( {
                self.const_a.set(a)
            else {
                self.a.comesFrom(a)
            }
        }
        if (b is not None( {
            if (isinstance(b, float)( {
                self.const_b.set(b)
            else {
                self.b.comesFrom(b)
            }
        }
    }
}

class Switch: public MaterialExpressionImpl {
    Switch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_default = MaterialExpressionEditorPropertyImpl(self, 'const_default', 'float')
        self.const_switch_value = MaterialExpressionEditorPropertyImpl(self, 'const_switch_value', 'float')
        self.description = MaterialExpressionEditorPropertyImpl(self, 'description', 'str')
        self.inputs = MaterialExpressionEditorPropertyImpl(self, 'inputs', 'Array[SwitchCustomInput]')
    }
}

class Tangent: public MaterialExpressionImpl {
    Tangent(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.period = MaterialExpressionEditorPropertyImpl(self, 'period', 'float')
    }
}

class TangentOutput: public MaterialExpressionImpl {
    TangentOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class TemporalSobol: public MaterialExpressionImpl {
    TemporalSobol(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.const_index = MaterialExpressionEditorPropertyImpl(self, 'const_index', 'uint32')
        self.const_seed = MaterialExpressionEditorPropertyImpl(self, 'const_seed', 'Vector2D')

        self.index = InSocketImpl(self, 'Index', 'StructProperty')
        self.seed = InSocketImpl(self, 'Seed', 'StructProperty')
        self.constSeed = InSocketImpl(self, 'ConstSeed', 'StructProperty')
    }
}

class TextureBase: public MaterialExpressionImpl {
    TextureBase(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')
    }
}

class TextureCoordinate: public MaterialExpressionImpl {
    TextureCoordinate(None u_tiling = None, None v_tiling = None, NodePos node_pos = nullptr): base(None u_tiling = None, None v_tiling = None, NodePos node_pos = nullptr) {

        self.coordinate_index = MaterialExpressionEditorPropertyImpl(self, 'coordinate_index', 'int32')
        self.u_tiling = MaterialExpressionEditorPropertyImpl(self, 'u_tiling', 'float')
        self.un_mirror_u = MaterialExpressionEditorPropertyImpl(self, 'un_mirror_u', 'bool')
        self.un_mirror_v = MaterialExpressionEditorPropertyImpl(self, 'un_mirror_v', 'bool')
        self.v_tiling = MaterialExpressionEditorPropertyImpl(self, 'v_tiling', 'float')
        if u_tiling is not None:
            self.u_tiling.set(u_tiling)
        if v_tiling is not None:
            self.v_tiling.set(v_tiling)
    }
}

class TextureObject: public MaterialExpressionImpl {
    TextureObject(None sampler_type = None, None texture = None, NodePos node_pos = nullptr): base(None sampler_type = None, None texture = None, NodePos node_pos = nullptr) {

        self.is_default_meshpaint_texture = MaterialExpressionEditorPropertyImpl(self, 'is_default_meshpaint_texture', 'bool')
        self.sampler_type = MaterialExpressionEditorPropertyImpl(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = MaterialExpressionEditorPropertyImpl(self, 'texture', 'Texture')
        if sampler_type is not None:
            self.sampler_type.set(sampler_type)
        if texture is not None:
            self.texture.set(texture)
    }
}

class TextureObjectParameter: public MaterialExpressionImpl {
    TextureObjectParameter(None parameter_name = None, NodePos node_pos = nullptr): base(None parameter_name = None, NodePos node_pos = nullptr) {

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
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
    }
}

class TextureProperty: public MaterialExpressionImpl {
    TextureProperty(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.property_ = MaterialExpressionEditorPropertyImpl(self, 'property_', 'MaterialExposedTextureProperty')

        self.textureObject = InSocketImpl(self, 'TextureObject', 'StructProperty')
    }
}

class TextureSample: public MaterialExpressionImpl {
    TextureSample(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class TextureSampleParameter: public MaterialExpressionImpl {
    TextureSampleParameter(None parameter_name = None, NodePos node_pos = nullptr): base(None parameter_name = None, NodePos node_pos = nullptr) {

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
        if parameter_name is not None:
            self.parameter_name.set(parameter_name)
    }
}

class TextureSampleParameter2D: public MaterialExpressionImpl {
    TextureSampleParameter2D(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class TextureSampleParameter2DArray: public MaterialExpressionImpl {
    TextureSampleParameter2DArray(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class TextureSampleParameterCube: public MaterialExpressionImpl {
    TextureSampleParameterCube(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class TextureSampleParameterCubeArray: public MaterialExpressionImpl {
    TextureSampleParameterCubeArray(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class TextureSampleParameterSubUV: public MaterialExpressionImpl {
    TextureSampleParameterSubUV(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class TextureSampleParameterVolume: public MaterialExpressionImpl {
    TextureSampleParameterVolume(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class ThinTranslucentMaterialOutput: public MaterialExpressionImpl {
    ThinTranslucentMaterialOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.transmittanceColor = InSocketImpl(self, 'TransmittanceColor', 'StructProperty')
    }
}

class Time: public MaterialExpressionImpl {
    Time(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.ignore_pause = MaterialExpressionEditorPropertyImpl(self, 'ignore_pause', 'bool')
        self.override_period = MaterialExpressionEditorPropertyImpl(self, 'override_period', 'bool')
        self.period = MaterialExpressionEditorPropertyImpl(self, 'period', 'float')
    }
}

class Transform: public MaterialExpressionImpl {
    Transform(None input = None, NodePos node_pos = nullptr): base(None input = None, NodePos node_pos = nullptr) {

        self.transform_source_type = MaterialExpressionEditorPropertyImpl(self, 'transform_source_type', 'MaterialVectorCoordTransformSource')
        self.transform_type = MaterialExpressionEditorPropertyImpl(self, 'transform_type', 'MaterialVectorCoordTransform')
        if (input is not None( {
            self.input.comesFrom(input)
        }
    }
}

class TransformPosition: public MaterialExpressionImpl {
    TransformPosition(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.transform_source_type = MaterialExpressionEditorPropertyImpl(self, 'transform_source_type', 'MaterialPositionTransformSource')
        self.transform_type = MaterialExpressionEditorPropertyImpl(self, 'transform_type', 'MaterialPositionTransformSource')
    }
}

class Truncate: public MaterialExpressionImpl {
    Truncate(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class TruncateLWC: public MaterialExpressionImpl {
    TruncateLWC(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class TwoSidedSign: public MaterialExpressionImpl {
    TwoSidedSign(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class VectorNoise: public MaterialExpressionImpl {
    VectorNoise(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.noise_function = MaterialExpressionEditorPropertyImpl(self, 'noise_function', 'VectorNoiseFunction')
        self.quality = MaterialExpressionEditorPropertyImpl(self, 'quality', 'int32')
        self.tile_size = MaterialExpressionEditorPropertyImpl(self, 'tile_size', 'uint32')
        self.tiling = MaterialExpressionEditorPropertyImpl(self, 'tiling', 'bool')

        self.position = InSocketImpl(self, 'Position', 'StructProperty')
    }
}

class VectorParameter: public MaterialExpressionImpl {
    VectorParameter(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr): base(None parameter_name = None, None default_value = None, NodePos node_pos = nullptr) {

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
    }
}

class VertexColor: public MaterialExpressionImpl {
    VertexColor(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class VertexInterpolator: public MaterialExpressionImpl {
    VertexInterpolator(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class VertexNormalWS: public MaterialExpressionImpl {
    VertexNormalWS(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class VertexTangentWS: public MaterialExpressionImpl {
    VertexTangentWS(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class ViewProperty: public MaterialExpressionImpl {
    ViewProperty(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.property_ = MaterialExpressionEditorPropertyImpl(self, 'property_', 'MaterialExposedViewProperty')
    }
}

class ViewSize: public MaterialExpressionImpl {
    ViewSize(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class VirtualTextureFeatureSwitch: public MaterialExpressionImpl {
    VirtualTextureFeatureSwitch(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.no = InSocketImpl(self, 'No', 'StructProperty')
        self.yes = InSocketImpl(self, 'Yes', 'StructProperty')
    }
}

class VolumetricAdvancedMaterialInput: public MaterialExpressionImpl {
    VolumetricAdvancedMaterialInput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class VolumetricAdvancedMaterialOutput: public MaterialExpressionImpl {
    VolumetricAdvancedMaterialOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

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
    }
}

class VolumetricCloudEmptySpaceSkippingInput: public MaterialExpressionImpl {
    VolumetricCloudEmptySpaceSkippingInput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class VolumetricCloudEmptySpaceSkippingOutput: public MaterialExpressionImpl {
    VolumetricCloudEmptySpaceSkippingOutput(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class WhileLoop: public MaterialExpressionImpl {
    WhileLoop(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {
    }
}

class WorldPosition: public MaterialExpressionImpl {
    WorldPosition(NodePos node_pos = nullptr): base(NodePos node_pos = nullptr) {

        self.world_position_shader_offset = MaterialExpressionEditorPropertyImpl(self, 'world_position_shader_offset', 'WorldPositionIncludedOffsets')
    }
}