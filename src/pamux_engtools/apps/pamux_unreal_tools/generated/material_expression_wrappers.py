# This file is generated. Please do NOT modify.

import unreal

from pamux_unreal_tools.material_expression import MaterialExpression
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.utils.build_stack import NodePos


class Abs(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionAbs, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class AbsorptionMediumMaterialOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionAbsorptionMediumMaterialOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ActorPositionWS(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionActorPositionWS, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.origin_type = Property(self, 'origin_type', 'PositionOrigin')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Add(MaterialExpression):
    def __init__(self, a = None, b = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionAdd, node_pos)

        # Properties
        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
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
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionAntialiasedTextureMask, node_pos)

        # Properties
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

        # Input Sockets
        self.UVs = InSocket(self, 'UVs', 'StructProperty')
        self.applyViewMipBias = InSocket(self, 'ApplyViewMipBias', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Append3Vector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionAppend3Vector, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Append4Vector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionAppend4Vector, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class AppendVector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionAppendVector, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Arccosine(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionArccosine, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ArccosineFast(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionArccosineFast, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Arcsine(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionArcsine, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ArcsineFast(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionArcsineFast, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Arctangent(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionArctangent, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Arctangent2(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionArctangent2, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.y = InSocket(self, 'Y', 'StructProperty')
        self.x = InSocket(self, 'X', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Arctangent2Fast(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionArctangent2Fast, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.y = InSocket(self, 'Y', 'StructProperty')
        self.x = InSocket(self, 'X', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ArctangentFast(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionArctangentFast, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class AtmosphericFogColor(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionAtmosphericFogColor, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class AtmosphericLightColor(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionAtmosphericLightColor, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class AtmosphericLightVector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionAtmosphericLightVector, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class BentNormalCustomOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionBentNormalCustomOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class BinaryOp(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionBinaryOp, node_pos)

        # Properties
        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class BlackBody(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionBlackBody, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.temp = InSocket(self, 'Temp', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class BlendMaterialAttributes(MaterialExpression):
    def __init__(self, a = None, b = None, alpha = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionBlendMaterialAttributes, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.pixel_attribute_blend_type = Property(self, 'pixel_attribute_blend_type', 'MaterialAttributeBlend')
        self.vertex_attribute_blend_type = Property(self, 'vertex_attribute_blend_type', 'MaterialAttributeBlend')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.alpha = InSocket(self, 'Alpha', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if a is not None: self.a.comesFrom(a)
        if b is not None: self.b.comesFrom(b)
        if alpha is not None: self.alpha.comesFrom(alpha)

class BreakMaterialAttributes(MaterialExpression):
    def __init__(self, input = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionBreakMaterialAttributes, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
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

        if input is not None: self.input.comesFrom(input)

class BumpOffset(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionBumpOffset, node_pos)

        # Properties
        self.const_coordinate = Property(self, 'const_coordinate', 'uint32')
        self.desc = Property(self, 'desc', 'str')
        self.height_ratio = Property(self, 'height_ratio', 'float')
        self.reference_plane = Property(self, 'reference_plane', 'float')

        # Input Sockets
        self.coordinate = InSocket(self, 'Coordinate', 'StructProperty')
        self.height = InSocket(self, 'Height', 'StructProperty')
        self.heightRatioInput = InSocket(self, 'HeightRatioInput', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Burn(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionBurn, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class CameraPositionWS(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionCameraPositionWS, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class CameraVectorWS(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionCameraVectorWS, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Ceil(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionCeil, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ChannelMaskParameter(MaterialExpression):
    def __init__(self, parameter_name = None, default_value = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionChannelMaskParameter, node_pos)

        # Properties
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.default_value = Property(self, 'default_value', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.mask_channel = Property(self, 'mask_channel', 'ChannelMaskParameterColor')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.primitive_data_index = Property(self, 'primitive_data_index', 'uint8')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = Property(self, 'use_custom_primitive_data', 'bool')

        # Input Sockets
        self.defaultValue = InSocket(self, 'DefaultValue', 'StructProperty')
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if parameter_name is not None: self.parameter_name.set(parameter_name)
        if default_value is not None: self.default_value.set(default_value)

class Clamp(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionClamp, node_pos)

        # Properties
        self.clamp_mode = Property(self, 'clamp_mode', 'ClampMode')
        self.desc = Property(self, 'desc', 'str')
        self.max_default = Property(self, 'max_default', 'float')
        self.min_default = Property(self, 'min_default', 'float')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')
        self.min = InSocket(self, 'Min', 'StructProperty')
        self.max = InSocket(self, 'Max', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ClearCoatNormalCustomOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionClearCoatNormalCustomOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class CloudSampleAttribute(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionCloudSampleAttribute, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class CollectionParameter(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionCollectionParameter, node_pos)

        # Properties
        self.collection = Property(self, 'collection', 'MaterialParameterCollection')
        self.desc = Property(self, 'desc', 'str')
        self.parameter_name = Property(self, 'parameter_name', 'Name')

        # Input Sockets
        self.parameterId = InSocket(self, 'ParameterId', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Comment(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionComment, node_pos)

        # Properties
        self.color_comment_bubble = Property(self, 'color_comment_bubble', 'bool')
        self.comment_bubble_visible_in_details_panel = Property(self, 'comment_bubble_visible_in_details_panel', 'bool')
        self.comment_color = Property(self, 'comment_color', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')
        self.font_size = Property(self, 'font_size', 'int32')
        self.group_mode = Property(self, 'group_mode', 'bool')
        self.text = Property(self, 'text', 'str')

        # Input Sockets
        self.commentColor = InSocket(self, 'CommentColor', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ComponentMask(MaterialExpression):
    def __init__(self, input = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionComponentMask, node_pos)

        # Properties
        self.a = Property(self, 'a', 'bool')
        self.b = Property(self, 'b', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.g = Property(self, 'g', 'bool')
        self.r = Property(self, 'r', 'bool')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if input is not None: self.input.comesFrom(input)

class Composite(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionComposite, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.subgraph_name = Property(self, 'subgraph_name', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Constant(MaterialExpression):
    def __init__(self, r = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionConstant, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.r = Property(self, 'r', 'float')

        # Input Sockets

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if r is not None: self.r.set(r)

class Constant2Vector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionConstant2Vector, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.g = Property(self, 'g', 'float')
        self.r = Property(self, 'r', 'float')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Constant3Vector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionConstant3Vector, node_pos)

        # Properties
        self.constant = Property(self, 'constant', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.constant = InSocket(self, 'Constant', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Constant4Vector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionConstant4Vector, node_pos)

        # Properties
        self.constant = Property(self, 'constant', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.constant = InSocket(self, 'Constant', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ConstantBiasScale(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionConstantBiasScale, node_pos)

        # Properties
        self.bias = Property(self, 'bias', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.scale = Property(self, 'scale', 'float')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ConstantDouble(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionConstantDouble, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.value = Property(self, 'value', 'double')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Cosine(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionCosine, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.period = Property(self, 'period', 'float')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class CrossProduct(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionCrossProduct, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class CurveAtlasRowParameter(MaterialExpression):
    def __init__(self, parameter_name = None, default_value = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionCurveAtlasRowParameter, node_pos)

        # Properties
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

        # Input Sockets
        self.inputTime = InSocket(self, 'InputTime', 'StructProperty')
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if parameter_name is not None: self.parameter_name.set(parameter_name)
        if default_value is not None: self.default_value.set(default_value)

class Custom(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionCustom, node_pos)

        # Properties
        self.additional_defines = Property(self, 'additional_defines', 'Array[CustomDefine]')
        self.additional_outputs = Property(self, 'additional_outputs', 'Array[CustomOutput]')
        self.code = Property(self, 'code', 'str')
        self.desc = Property(self, 'desc', 'str')
        self.description = Property(self, 'description', 'str')
        self.include_file_paths = Property(self, 'include_file_paths', 'Array[str]')
        self.inputs = Property(self, 'inputs', 'Array[CustomInput]')
        self.output_type = Property(self, 'output_type', 'CustomMaterialOutputType')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class CustomOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionCustomOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DBufferTexture(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDBufferTexture, node_pos)

        # Properties
        self.d_buffer_texture_id = Property(self, 'd_buffer_texture_id', 'DBufferTextureId')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DDX(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDDX, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.value = InSocket(self, 'Value', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DDY(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDDY, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.value = InSocket(self, 'Value', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DataDrivenShaderPlatformInfoSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDataDrivenShaderPlatformInfoSwitch, node_pos)

        # Properties
        self.ddspi_property_names = Property(self, 'ddspi_property_names', 'Array[DataDrivenShaderPlatformInfoInput]')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DecalColor(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDecalColor, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DecalDerivative(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDecalDerivative, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DecalLifetimeOpacity(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDecalLifetimeOpacity, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DecalMipmapLevel(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDecalMipmapLevel, node_pos)

        # Properties
        self.const_height = Property(self, 'const_height', 'float')
        self.const_width = Property(self, 'const_width', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.textureSize = InSocket(self, 'TextureSize', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DeltaTime(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDeltaTime, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DepthFade(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDepthFade, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.fade_distance_default = Property(self, 'fade_distance_default', 'float')
        self.opacity_default = Property(self, 'opacity_default', 'float')

        # Input Sockets
        self.inOpacity = InSocket(self, 'InOpacity', 'StructProperty')
        self.fadeDistance = InSocket(self, 'FadeDistance', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DepthOfFieldFunction(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDepthOfFieldFunction, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.function_value = Property(self, 'function_value', 'DepthOfFieldFunctionValue')

        # Input Sockets
        self.depth = InSocket(self, 'Depth', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DeriveNormalZ(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDeriveNormalZ, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.inXY = InSocket(self, 'InXY', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Desaturation(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDesaturation, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.luminance_factors = Property(self, 'luminance_factors', 'LinearColor')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')
        self.fraction = InSocket(self, 'Fraction', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Difference(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDifference, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DisjointOver(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDisjointOver, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Distance(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDistance, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DistanceCullFade(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDistanceCullFade, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DistanceFieldApproxAO(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDistanceFieldApproxAO, node_pos)

        # Properties
        self.base_distance_default = Property(self, 'base_distance_default', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.num_steps = Property(self, 'num_steps', 'uint32')
        self.radius_default = Property(self, 'radius_default', 'float')
        self.step_scale_default = Property(self, 'step_scale_default', 'float')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DistanceFieldGradient(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDistanceFieldGradient, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.position = InSocket(self, 'Position', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DistanceFieldsRenderingSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDistanceFieldsRenderingSwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.no = InSocket(self, 'No', 'StructProperty')
        self.yes = InSocket(self, 'Yes', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DistanceToNearestSurface(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDistanceToNearestSurface, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.position = InSocket(self, 'Position', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Divide(MaterialExpression):
    def __init__(self, a = None, b = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDivide, node_pos)

        # Properties
        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
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

class Dodge(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDodge, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DotProduct(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDotProduct, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class DoubleVectorParameter(MaterialExpression):
    def __init__(self, parameter_name = None, default_value = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDoubleVectorParameter, node_pos)

        # Properties
        self.default_value = Property(self, 'default_value', 'Vector4d')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if parameter_name is not None: self.parameter_name.set(parameter_name)
        if default_value is not None: self.default_value.set(default_value)

class DynamicParameter(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionDynamicParameter, node_pos)

        # Properties
        self.default_value = Property(self, 'default_value', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')
        self.param_names = Property(self, 'param_names', 'Array[str]')
        self.parameter_index = Property(self, 'parameter_index', 'uint32')

        # Input Sockets
        self.defaultValue = InSocket(self, 'DefaultValue', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ExecBegin(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionExecBegin, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ExecEnd(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionExecEnd, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Exponential(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionExponential, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Exponential2(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionExponential2, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class EyeAdaptation(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionEyeAdaptation, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class EyeAdaptationInverse(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionEyeAdaptationInverse, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class FeatureLevelSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionFeatureLevelSwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.default = InSocket(self, 'Default', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Floor(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionFloor, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Fmod(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionFmod, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class FontSample(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionFontSample, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.font = Property(self, 'font', 'Font')
        self.font_texture_page = Property(self, 'font_texture_page', 'int32')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class FontSampleParameter(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionFontSampleParameter, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.font = Property(self, 'font', 'Font')
        self.font_texture_page = Property(self, 'font_texture_page', 'int32')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ForLoop(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionForLoop, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Frac(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionFrac, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Fractal3D(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionFractal3D, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Fresnel(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionFresnel, node_pos)

        # Properties
        self.base_reflect_fraction = Property(self, 'base_reflect_fraction', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.exponent = Property(self, 'exponent', 'float')

        # Input Sockets
        self.exponentIn = InSocket(self, 'ExponentIn', 'StructProperty')
        self.baseReflectFractionIn = InSocket(self, 'BaseReflectFractionIn', 'StructProperty')
        self.normal = InSocket(self, 'Normal', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class FunctionInput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionFunctionInput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.description = Property(self, 'description', 'str')
        self.input_name = Property(self, 'input_name', 'Name')
        self.input_type = Property(self, 'input_type', 'FunctionInputType')
        self.preview_value = Property(self, 'preview_value', 'Vector4f')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.use_preview_value_as_default = Property(self, 'use_preview_value_as_default', 'bool')

        # Input Sockets
        self.preview = InSocket(self, 'Preview', 'StructProperty')
        self.ID = InSocket(self, 'ID', 'StructProperty')
        self.previewValue = InSocket(self, 'PreviewValue', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

    @staticmethod
    def create(input_name, input_type, preview):
        if isinstance(preview, float):
            preview = Constant(preview)

        CurrentNodePos.x += NodePos.DeltaX

        result = FunctionInput()
        result.input_name.set(input_name)
        result.input_type.set(input_type)
        result.preview.comesFrom(preview)
        return result


class FunctionOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionFunctionOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.description = Property(self, 'description', 'str')
        self.output_name = Property(self, 'output_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.ID = InSocket(self, 'ID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class GIReplace(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionGIReplace, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.default = InSocket(self, 'Default', 'StructProperty')
        self.staticIndirect = InSocket(self, 'StaticIndirect', 'StructProperty')
        self.dynamicIndirect = InSocket(self, 'DynamicIndirect', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class GenericConstant(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionGenericConstant, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class GetLocal(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionGetLocal, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.local_name = Property(self, 'local_name', 'Name')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class GetMaterialAttributes(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionGetMaterialAttributes, node_pos)

        # Properties
        self.attribute_get_types = Property(self, 'attribute_get_types', 'Array[Guid]')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
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
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionHairAttributes, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.use_tangent_space = Property(self, 'use_tangent_space', 'bool')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class HairColor(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionHairColor, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.melanin = InSocket(self, 'Melanin', 'StructProperty')
        self.redness = InSocket(self, 'Redness', 'StructProperty')
        self.dyeColor = InSocket(self, 'DyeColor', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class HeightfieldMinMaxTexture(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionHeightfieldMinMaxTexture, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.min_max_texture = Property(self, 'min_max_texture', 'HeightfieldMinMaxTexture')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class HsvToRgb(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionHsvToRgb, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class If(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionIf, node_pos)

        # Properties
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.equals_threshold = Property(self, 'equals_threshold', 'float')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.aGreaterThanB = InSocket(self, 'AGreaterThanB', 'StructProperty')
        self.aEqualsB = InSocket(self, 'AEqualsB', 'StructProperty')
        self.aLessThanB = InSocket(self, 'ALessThanB', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class IfThenElse(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionIfThenElse, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class In(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionIn, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class InverseLinearInterpolate(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionInverseLinearInterpolate, node_pos)

        # Properties
        self.clamp_result = Property(self, 'clamp_result', 'bool')
        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.const_value = Property(self, 'const_value', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.value = InSocket(self, 'Value', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class IsOrthographic(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionIsOrthographic, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LandscapeGrassOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLandscapeGrassOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.grass_types = Property(self, 'grass_types', 'Array[GrassInput]')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LandscapeLayerBlend(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLandscapeLayerBlend, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.layers = Property(self, 'layers', 'Array[LayerBlendInput]')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LandscapeLayerCoords(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLandscapeLayerCoords, node_pos)

        # Properties
        self.custom_uv_type = Property(self, 'custom_uv_type', 'LandscapeCustomizedCoordType')
        self.desc = Property(self, 'desc', 'str')
        self.mapping_pan_u = Property(self, 'mapping_pan_u', 'float')
        self.mapping_pan_v = Property(self, 'mapping_pan_v', 'float')
        self.mapping_rotation = Property(self, 'mapping_rotation', 'float')
        self.mapping_scale = Property(self, 'mapping_scale', 'float')
        self.mapping_type = Property(self, 'mapping_type', 'TerrainCoordMappingType')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LandscapeLayerSample(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLandscapeLayerSample, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.preview_weight = Property(self, 'preview_weight', 'float')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LandscapeLayerSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLandscapeLayerSwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.preview_used = Property(self, 'preview_used', 'bool')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LandscapeLayerWeight(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLandscapeLayerWeight, node_pos)

        # Properties
        self.const_base = Property(self, 'const_base', 'Vector')
        self.desc = Property(self, 'desc', 'str')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.preview_weight = Property(self, 'preview_weight', 'float')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LandscapePhysicalMaterialOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLandscapePhysicalMaterialOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.inputs = Property(self, 'inputs', 'Array[PhysicalMaterialInput]')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LandscapeVisibilityMask(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLandscapeVisibilityMask, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Length(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLength, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Less(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLess, node_pos)

        # Properties
        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LightVector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLightVector, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LightmapUVs(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLightmapUVs, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LightmassReplace(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLightmassReplace, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.realtime = InSocket(self, 'Realtime', 'StructProperty')
        self.lightmass = InSocket(self, 'Lightmass', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class LinearInterpolate(MaterialExpression):
    def __init__(self, a = None, b = None, alpha = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLinearInterpolate, node_pos)

        # Properties
        self.const_a = Property(self, 'const_a', 'float')
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.alpha = InSocket(self, 'Alpha', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if a is not None: self.a.comesFrom(a)
        if b is not None: self.b.comesFrom(b)
        if alpha is not None: self.alpha.comesFrom(alpha)

class Logarithm(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLogarithm, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Logarithm10(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLogarithm10, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.x = InSocket(self, 'X', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Logarithm2(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLogarithm2, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.x = InSocket(self, 'X', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Luminance(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionLuminance, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MakeMaterialAttributes(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMakeMaterialAttributes, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
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

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

    @staticmethod
    def create(materialAttributes):
        result = MakeMaterialAttributes()
        result.baseColor.comesFrom(materialAttributes.baseColor)
        result.metallic.comesFrom(materialAttributes.metallic)
        result.specular.comesFrom(materialAttributes.specular)
        result.roughness.comesFrom(materialAttributes.roughness)
        result.anisotropy.comesFrom(materialAttributes.anisotropy)
        result.emissiveColor.comesFrom(materialAttributes.emissiveColor)
        result.opacity.comesFrom(materialAttributes.opacity)
        result.opacityMask.comesFrom(materialAttributes.opacityMask)
        result.normal.comesFrom(materialAttributes.normal)
        result.tangent.comesFrom(materialAttributes.tangent)
        result.worldPositionOffset.comesFrom(materialAttributes.worldPositionOffset)
        result.subsurfaceColor.comesFrom(materialAttributes.subsurfaceColor)
        result.clearCoat.comesFrom(materialAttributes.clearCoat)
        result.clearCoatRoughness.comesFrom(materialAttributes.clearCoatRoughness)
        result.ambientOcclusion.comesFrom(materialAttributes.ambientOcclusion)
        result.refraction.comesFrom(materialAttributes.refraction)
        result.customizedUV_0.comesFrom(materialAttributes.customizedUV0)
        result.customizedUV_1.comesFrom(materialAttributes.customizedUV1)
        result.customizedUV_2.comesFrom(materialAttributes.customizedUV2)
        result.customizedUV_3.comesFrom(materialAttributes.customizedUV3)
        result.customizedUV_4.comesFrom(materialAttributes.customizedUV4)
        result.customizedUV_5.comesFrom(materialAttributes.customizedUV5)
        result.customizedUV_6.comesFrom(materialAttributes.customizedUV6)
        result.customizedUV_7.comesFrom(materialAttributes.customizedUV7)
        result.pixelDepthOffset.comesFrom(materialAttributes.pixelDepthOffset)
        result.shadingModel.comesFrom(materialAttributes.shadingModel)
        result.displacement.comesFrom(materialAttributes.displacement)
        return result


class MapARPassthroughCameraUV(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMapARPassthroughCameraUV, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Mask(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMask, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialAttributeLayers(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialAttributeLayers, node_pos)

        # Properties
        self.default_layers = Property(self, 'default_layers', 'MaterialLayersFunctions')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.input = InSocket(self, 'Input', 'StructProperty')
        self.defaultLayers = InSocket(self, 'DefaultLayers', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialFunctionCall(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialFunctionCall, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.material_function = Property(self, 'material_function', 'MaterialFunctionInterface')

        # Input Sockets
        self.functionParameterInfo = InSocket(self, 'FunctionParameterInfo', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialLayerOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialLayerOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.description = Property(self, 'description', 'str')
        self.output_name = Property(self, 'output_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.ID = InSocket(self, 'ID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialProxyReplace(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialProxyReplace, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.realtime = InSocket(self, 'Realtime', 'StructProperty')
        self.materialProxy = InSocket(self, 'MaterialProxy', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXAppend3Vector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXAppend3Vector, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXAppend4Vector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXAppend4Vector, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXBurn(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXBurn, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXDifference(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXDifference, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXDisjointOver(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXDisjointOver, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXDodge(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXDodge, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXExponential(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXExponential, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXFractal3D(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXFractal3D, node_pos)

        # Properties
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

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXHsvToRgb(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXHsvToRgb, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXIn(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXIn, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXLength(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXLength, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXLogarithm(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXLogarithm, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXLuminance(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXLuminance, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.luminance_factors = Property(self, 'luminance_factors', 'LinearColor')
        self.luminance_mode = Property(self, 'luminance_mode', 'MaterialXLuminanceMode')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXMask(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXMask, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXMatte(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXMatte, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXMinus(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXMinus, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXOut(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXOut, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXOver(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXOver, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXOverlay(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXOverlay, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXPlace2D(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXPlace2D, node_pos)

        # Properties
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_rotation_angle = Property(self, 'const_rotation_angle', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXPlus(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXPlus, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXPremult(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXPremult, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXRamp4(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXRamp4, node_pos)

        # Properties
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXRampLeftRight(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXRampLeftRight, node_pos)

        # Properties
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXRampTopBottom(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXRampTopBottom, node_pos)

        # Properties
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXRemap(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXRemap, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.input_high_default = Property(self, 'input_high_default', 'float')
        self.input_low_default = Property(self, 'input_low_default', 'float')
        self.target_high_default = Property(self, 'target_high_default', 'float')
        self.target_low_default = Property(self, 'target_low_default', 'float')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXRgbToHsv(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXRgbToHsv, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXRotate2D(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXRotate2D, node_pos)

        # Properties
        self.const_rotation_angle = Property(self, 'const_rotation_angle', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXScreen(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXScreen, node_pos)

        # Properties
        self.const_alpha = Property(self, 'const_alpha', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXSplitLeftRight(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXSplitLeftRight, node_pos)

        # Properties
        self.const_center = Property(self, 'const_center', 'float')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXSplitTopBottom(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXSplitTopBottom, node_pos)

        # Properties
        self.const_center = Property(self, 'const_center', 'float')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXSwizzle(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXSwizzle, node_pos)

        # Properties
        self.channels = Property(self, 'channels', 'str')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXTextureSampleParameterBlur(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXTextureSampleParameterBlur, node_pos)

        # Properties
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

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class MaterialXUnpremult(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMaterialXUnpremult, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Matte(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMatte, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Max(MaterialExpression):
    def __init__(self, a = None, b = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMax, node_pos)

        # Properties
        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
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
    def __init__(self, a = None, b = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMin, node_pos)

        # Properties
        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
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

class Minus(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMinus, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Multiply(MaterialExpression):
    def __init__(self, a = None, b = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionMultiply, node_pos)

        # Properties
        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
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
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionNamedRerouteBase, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class NamedRerouteDeclaration(MaterialExpression):
    def __init__(self, name = None, input = None, nodeColor = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionNamedRerouteDeclaration, node_pos)

        # Properties
        self.name = Property(self, 'name', 'Name')
        self.desc = Property(self, 'desc', 'str')
        self.nodeNolor = Property(self, 'nodeNolor', 'LinearColor')
        self.variableGuid = Property(self, 'variableGuid', 'Guid')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if name is not None: self.name.set(name)
        if input is not None: self.input.comesFrom(input)
        if nodeColor is not None: self.nodeColor.set(nodeColor)

class NamedRerouteUsage(MaterialExpression):
    def __init__(self, declarationGuid = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionNamedRerouteUsage, node_pos)

        # Properties
        self.declarationGuid = Property(self, 'declarationGuid', 'Guid')

        # Input Sockets

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if declarationGuid is not None: self.declarationGuid.set(declarationGuid)

class NaniteReplace(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionNaniteReplace, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Noise(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionNoise, node_pos)

        # Properties
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

        # Input Sockets
        self.position = InSocket(self, 'Position', 'StructProperty')
        self.filterWidth = InSocket(self, 'FilterWidth', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Normalize(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionNormalize, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.vectorInput = InSocket(self, 'VectorInput', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ObjectBounds(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionObjectBounds, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ObjectLocalBounds(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionObjectLocalBounds, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ObjectOrientation(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionObjectOrientation, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ObjectPositionWS(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionObjectPositionWS, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.origin_type = Property(self, 'origin_type', 'PositionOrigin')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ObjectRadius(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionObjectRadius, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class OneMinus(MaterialExpression):
    def __init__(self, input = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionOneMinus, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if input is not None: self.input.comesFrom(input)

class Out(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionOut, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Over(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionOver, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Overlay(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionOverlay, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Panner(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPanner, node_pos)

        # Properties
        self.const_coordinate = Property(self, 'const_coordinate', 'uint32')
        self.desc = Property(self, 'desc', 'str')
        self.fractional_part = Property(self, 'fractional_part', 'bool')
        self.speed_x = Property(self, 'speed_x', 'float')
        self.speed_y = Property(self, 'speed_y', 'float')

        # Input Sockets
        self.coordinate = InSocket(self, 'Coordinate', 'StructProperty')
        self.time = InSocket(self, 'Time', 'StructProperty')
        self.speed = InSocket(self, 'Speed', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Parameter(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParameter, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleColor(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleColor, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleDirection(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleDirection, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleMacroUV(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleMacroUV, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleMotionBlurFade(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleMotionBlurFade, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticlePositionWS(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticlePositionWS, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.origin_type = Property(self, 'origin_type', 'PositionOrigin')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleRadius(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleRadius, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleRandom(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleRandom, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleRelativeTime(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleRelativeTime, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleSize(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleSize, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleSpeed(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleSpeed, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleSpriteRotation(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleSpriteRotation, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleSubUV(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleSubUV, node_pos)

        # Properties
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

        # Input Sockets
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ParticleSubUVProperties(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionParticleSubUVProperties, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PathTracingBufferTexture(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPathTracingBufferTexture, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.path_tracing_buffer_texture_id = Property(self, 'path_tracing_buffer_texture_id', 'PathTracingBufferTextureId')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PathTracingQualitySwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPathTracingQualitySwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PathTracingRayTypeSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPathTracingRayTypeSwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PerInstanceCustomData(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPerInstanceCustomData, node_pos)

        # Properties
        self.const_default_value = Property(self, 'const_default_value', 'float')
        self.data_index = Property(self, 'data_index', 'uint32')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.defaultValue = InSocket(self, 'DefaultValue', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PerInstanceCustomData3Vector(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPerInstanceCustomData3Vector, node_pos)

        # Properties
        self.const_default_value = Property(self, 'const_default_value', 'LinearColor')
        self.data_index = Property(self, 'data_index', 'uint32')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PerInstanceFadeAmount(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPerInstanceFadeAmount, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PerInstanceRandom(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPerInstanceRandom, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PinBase(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPinBase, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.reroute_pins = Property(self, 'reroute_pins', 'Array[CompositeReroute]')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PixelDepth(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPixelDepth, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PixelNormalWS(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPixelNormalWS, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Place2D(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPlace2D, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Plus(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPlus, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Power(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPower, node_pos)

        # Properties
        self.const_exponent = Property(self, 'const_exponent', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.base = InSocket(self, 'Base', 'StructProperty')
        self.exponent = InSocket(self, 'Exponent', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PreSkinnedLocalBounds(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPreSkinnedLocalBounds, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PreSkinnedNormal(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPreSkinnedNormal, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PreSkinnedPosition(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPreSkinnedPosition, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PrecomputedAOMask(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPrecomputedAOMask, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Premult(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPremult, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class PreviousFrameSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionPreviousFrameSwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.currentFrame = InSocket(self, 'CurrentFrame', 'StructProperty')
        self.previousFrame = InSocket(self, 'PreviousFrame', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class QualitySwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionQualitySwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.default = InSocket(self, 'Default', 'StructProperty')
        self.inputs = InSocket(self, 'Inputs', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Ramp4(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRamp4, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class RampLeftRight(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRampLeftRight, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class RampTopBottom(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRampTopBottom, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class RayTracingQualitySwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRayTracingQualitySwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.normal = InSocket(self, 'Normal', 'StructProperty')
        self.rayTraced = InSocket(self, 'RayTraced', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ReflectionCapturePassSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionReflectionCapturePassSwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.default = InSocket(self, 'Default', 'StructProperty')
        self.reflection = InSocket(self, 'Reflection', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ReflectionVectorWS(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionReflectionVectorWS, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.normalize_custom_world_normal = Property(self, 'normalize_custom_world_normal', 'bool')

        # Input Sockets
        self.customWorldNormal = InSocket(self, 'CustomWorldNormal', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Remap(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRemap, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Reroute(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionReroute, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class RerouteBase(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRerouteBase, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class RgbToHsv(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRgbToHsv, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Rotate2D(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRotate2D, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class RotateAboutAxis(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRotateAboutAxis, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.period = Property(self, 'period', 'float')

        # Input Sockets
        self.normalizedRotationAxis = InSocket(self, 'NormalizedRotationAxis', 'StructProperty')
        self.rotationAngle = InSocket(self, 'RotationAngle', 'StructProperty')
        self.pivotPoint = InSocket(self, 'PivotPoint', 'StructProperty')
        self.position = InSocket(self, 'Position', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Rotator(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRotator, node_pos)

        # Properties
        self.center_x = Property(self, 'center_x', 'float')
        self.center_y = Property(self, 'center_y', 'float')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint32')
        self.desc = Property(self, 'desc', 'str')
        self.speed = Property(self, 'speed', 'float')

        # Input Sockets
        self.coordinate = InSocket(self, 'Coordinate', 'StructProperty')
        self.time = InSocket(self, 'Time', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Round(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRound, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class RuntimeVirtualTextureOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRuntimeVirtualTextureOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.baseColor = InSocket(self, 'BaseColor', 'StructProperty')
        self.specular = InSocket(self, 'Specular', 'StructProperty')
        self.roughness = InSocket(self, 'Roughness', 'StructProperty')
        self.normal = InSocket(self, 'Normal', 'StructProperty')
        self.worldHeight = InSocket(self, 'WorldHeight', 'StructProperty')
        self.opacity = InSocket(self, 'Opacity', 'StructProperty')
        self.mask = InSocket(self, 'Mask', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class RuntimeVirtualTextureReplace(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRuntimeVirtualTextureReplace, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.default = InSocket(self, 'Default', 'StructProperty')
        self.virtualTextureOutput = InSocket(self, 'VirtualTextureOutput', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class RuntimeVirtualTextureSample(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRuntimeVirtualTextureSample, node_pos)

        # Properties
        self.adaptive = Property(self, 'adaptive', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.enable_feedback = Property(self, 'enable_feedback', 'bool')
        self.material_type = Property(self, 'material_type', 'RuntimeVirtualTextureMaterialType')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'RuntimeVirtualTextureMipValueMode')
        self.single_physical_space = Property(self, 'single_physical_space', 'bool')
        self.texture_address_mode = Property(self, 'texture_address_mode', 'RuntimeVirtualTextureTextureAddressMode')
        self.virtual_texture = Property(self, 'virtual_texture', 'RuntimeVirtualTexture')

        # Input Sockets
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')
        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')
        self.mipValue = InSocket(self, 'MipValue', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class RuntimeVirtualTextureSampleParameter(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionRuntimeVirtualTextureSampleParameter, node_pos)

        # Properties
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

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')
        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')
        self.mipValue = InSocket(self, 'MipValue', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SamplePhysicsIntegerField(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSamplePhysicsIntegerField, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.field_target = Property(self, 'field_target', 'FieldIntegerType')

        # Input Sockets
        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SamplePhysicsScalarField(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSamplePhysicsScalarField, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.field_target = Property(self, 'field_target', 'FieldScalarType')

        # Input Sockets
        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SamplePhysicsVectorField(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSamplePhysicsVectorField, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.field_target = Property(self, 'field_target', 'FieldVectorType')

        # Input Sockets
        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Saturate(MaterialExpression):
    def __init__(self, input = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSaturate, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if input is not None: self.input.comesFrom(input)

class ScalarParameter(MaterialExpression):
    def __init__(self, parameter_name = None, default_value = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionScalarParameter, node_pos)

        # Properties
        self.default_value = Property(self, 'default_value', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.primitive_data_index = Property(self, 'primitive_data_index', 'uint8')
        self.slider_max = Property(self, 'slider_max', 'float')
        self.slider_min = Property(self, 'slider_min', 'float')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = Property(self, 'use_custom_primitive_data', 'bool')

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if parameter_name is not None: self.parameter_name.set(parameter_name)
        if default_value is not None: self.default_value.set(default_value)

class SceneColor(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSceneColor, node_pos)

        # Properties
        self.const_input = Property(self, 'const_input', 'Vector2D')
        self.desc = Property(self, 'desc', 'str')
        self.input_mode = Property(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')
        self.offsetFraction = InSocket(self, 'OffsetFraction', 'StructProperty')
        self.constInput = InSocket(self, 'ConstInput', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SceneDepth(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSceneDepth, node_pos)

        # Properties
        self.const_input = Property(self, 'const_input', 'Vector2D')
        self.desc = Property(self, 'desc', 'str')
        self.input_mode = Property(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')
        self.constInput = InSocket(self, 'ConstInput', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SceneDepthWithoutWater(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSceneDepthWithoutWater, node_pos)

        # Properties
        self.const_input = Property(self, 'const_input', 'Vector2D')
        self.desc = Property(self, 'desc', 'str')
        self.fallback_depth = Property(self, 'fallback_depth', 'float')
        self.input_mode = Property(self, 'input_mode', 'MaterialSceneAttributeInputMode')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')
        self.constInput = InSocket(self, 'ConstInput', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SceneTexelSize(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSceneTexelSize, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SceneTexture(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSceneTexture, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.filtered = Property(self, 'filtered', 'bool')
        self.scene_texture_id = Property(self, 'scene_texture_id', 'SceneTextureId')

        # Input Sockets
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Screen(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionScreen, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ScreenPosition(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionScreenPosition, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SetLocal(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSetLocal, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.local_name = Property(self, 'local_name', 'Name')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SetMaterialAttributes(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSetMaterialAttributes, node_pos)

        # Properties
        self.attribute_set_types = Property(self, 'attribute_set_types', 'Array[Guid]')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
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

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ShaderStageSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionShaderStageSwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.pixelShader = InSocket(self, 'PixelShader', 'StructProperty')
        self.vertexShader = InSocket(self, 'VertexShader', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ShadingModel(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionShadingModel, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.shading_model = Property(self, 'shading_model', 'MaterialShadingModel')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ShadingPathSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionShadingPathSwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.default = InSocket(self, 'Default', 'StructProperty')
        self.inputs = InSocket(self, 'Inputs', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ShadowReplace(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionShadowReplace, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.default = InSocket(self, 'Default', 'StructProperty')
        self.shadow = InSocket(self, 'Shadow', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Sign(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSign, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Sine(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSine, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.period = Property(self, 'period', 'float')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SingleLayerWaterMaterialOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSingleLayerWaterMaterialOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.scatteringCoefficients = InSocket(self, 'ScatteringCoefficients', 'StructProperty')
        self.absorptionCoefficients = InSocket(self, 'AbsorptionCoefficients', 'StructProperty')
        self.phaseG = InSocket(self, 'PhaseG', 'StructProperty')
        self.colorScaleBehindWater = InSocket(self, 'ColorScaleBehindWater', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SkyAtmosphereAerialPerspective(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSkyAtmosphereAerialPerspective, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SkyAtmosphereDistantLightScatteredLuminance(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSkyAtmosphereDistantLightScatteredLuminance, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SkyAtmosphereLightDirection(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSkyAtmosphereLightDirection, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.light_index = Property(self, 'light_index', 'int32')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SkyAtmosphereLightDiskLuminance(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSkyAtmosphereLightDiskLuminance, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.light_index = Property(self, 'light_index', 'int32')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SkyAtmosphereLightIlluminance(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSkyAtmosphereLightIlluminance, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.light_index = Property(self, 'light_index', 'int32')

        # Input Sockets
        self.worldPosition = InSocket(self, 'WorldPosition', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SkyAtmosphereViewLuminance(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSkyAtmosphereViewLuminance, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SkyLightEnvMapSample(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSkyLightEnvMapSample, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SmoothStep(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSmoothStep, node_pos)

        # Properties
        self.const_max = Property(self, 'const_max', 'float')
        self.const_min = Property(self, 'const_min', 'float')
        self.const_value = Property(self, 'const_value', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.min = InSocket(self, 'Min', 'StructProperty')
        self.max = InSocket(self, 'Max', 'StructProperty')
        self.value = InSocket(self, 'Value', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Sobol(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSobol, node_pos)

        # Properties
        self.const_index = Property(self, 'const_index', 'uint32')
        self.const_seed = Property(self, 'const_seed', 'Vector2D')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.cell = InSocket(self, 'Cell', 'StructProperty')
        self.index = InSocket(self, 'Index', 'StructProperty')
        self.seed = InSocket(self, 'Seed', 'StructProperty')
        self.constSeed = InSocket(self, 'ConstSeed', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SparseVolumeTextureBase(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSparseVolumeTextureBase, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.sparse_volume_texture = Property(self, 'sparse_volume_texture', 'SparseVolumeTexture')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SparseVolumeTextureObject(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSparseVolumeTextureObject, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.sparse_volume_texture = Property(self, 'sparse_volume_texture', 'SparseVolumeTexture')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SparseVolumeTextureObjectParameter(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSparseVolumeTextureObjectParameter, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.sparse_volume_texture = Property(self, 'sparse_volume_texture', 'SparseVolumeTexture')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SparseVolumeTextureSample(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSparseVolumeTextureSample, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sparse_volume_texture = Property(self, 'sparse_volume_texture', 'SparseVolumeTexture')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SparseVolumeTextureSampleParameter(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSparseVolumeTextureSampleParameter, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.sparse_volume_texture = Property(self, 'sparse_volume_texture', 'SparseVolumeTexture')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SpeedTree(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSpeedTree, node_pos)

        # Properties
        self.accurate_wind_velocities = Property(self, 'accurate_wind_velocities', 'bool')
        self.billboard_threshold = Property(self, 'billboard_threshold', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.geometry_type = Property(self, 'geometry_type', 'SpeedTreeGeometryType')
        self.lod_type = Property(self, 'lod_type', 'SpeedTreeLODType')
        self.wind_type = Property(self, 'wind_type', 'SpeedTreeWindType')

        # Input Sockets
        self.geometryInput = InSocket(self, 'GeometryInput', 'StructProperty')
        self.windInput = InSocket(self, 'WindInput', 'StructProperty')
        self.lODInput = InSocket(self, 'LODInput', 'StructProperty')
        self.extraBendWS = InSocket(self, 'ExtraBendWS', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SphereMask(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSphereMask, node_pos)

        # Properties
        self.attenuation_radius = Property(self, 'attenuation_radius', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.hardness_percent = Property(self, 'hardness_percent', 'float')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.radius = InSocket(self, 'Radius', 'StructProperty')
        self.hardness = InSocket(self, 'Hardness', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SphericalParticleOpacity(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSphericalParticleOpacity, node_pos)

        # Properties
        self.constant_density = Property(self, 'constant_density', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.density = InSocket(self, 'Density', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SplitLeftRight(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSplitLeftRight, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SplitTopBottom(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSplitTopBottom, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SpriteTextureSampler(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSpriteTextureSampler, node_pos)

        # Properties
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

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SquareRoot(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSquareRoot, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StaticBool(MaterialExpression):
    def __init__(self, value = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStaticBool, node_pos)

        # Properties
        self.value = Property(self, 'Value', 'bool')

        # Input Sockets

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if value is not None: self.value.set(value)

class StaticBoolParameter(MaterialExpression):
    def __init__(self, parameter_name = None, default_value = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStaticBoolParameter, node_pos)

        # Properties
        self.default_value = Property(self, 'default_value', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.dynamic_branch = Property(self, 'dynamic_branch', 'bool')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if parameter_name is not None: self.parameter_name.set(parameter_name)
        if default_value is not None: self.default_value.set(default_value)

class StaticComponentMaskParameter(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStaticComponentMaskParameter, node_pos)

        # Properties
        self.default_a = Property(self, 'default_a', 'bool')
        self.default_b = Property(self, 'default_b', 'bool')
        self.default_g = Property(self, 'default_g', 'bool')
        self.default_r = Property(self, 'default_r', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StaticSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStaticSwitch, node_pos)

        # Properties
        self.default_value = Property(self, 'default_value', 'bool')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')
        self.value = InSocket(self, 'Value', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StaticSwitchParameter(MaterialExpression):
    def __init__(self, parameter_name = None, default_value = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStaticSwitchParameter, node_pos)

        # Properties
        self.default_value = Property(self, 'default_value', 'bool')
        self.desc = Property(self, 'desc', 'str')
        self.dynamic_branch = Property(self, 'dynamic_branch', 'bool')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.sort_priority = Property(self, 'sort_priority', 'int32')

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')

        if parameter_name is not None: self.parameter_name.set(parameter_name)
        if default_value is not None: self.default_value.set(default_value)

class Step(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStep, node_pos)

        # Properties
        self.const_x = Property(self, 'const_x', 'float')
        self.const_y = Property(self, 'const_y', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.y = InSocket(self, 'Y', 'StructProperty')
        self.x = InSocket(self, 'X', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataAdd(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataAdd, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.use_parameter_blending = Property(self, 'use_parameter_blending', 'bool')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataBSDF(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataBSDF, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataConvertToDecal(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataConvertToDecal, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataEyeBSDF(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataEyeBSDF, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.subsurface_profile = Property(self, 'subsurface_profile', 'SubsurfaceProfile')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataHairBSDF(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataHairBSDF, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataHazinessToSecondaryRoughness(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataHazinessToSecondaryRoughness, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataHorizontalMixing(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataHorizontalMixing, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.use_parameter_blending = Property(self, 'use_parameter_blending', 'bool')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataLegacyConversion(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataLegacyConversion, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.subsurface_profile = Property(self, 'subsurface_profile', 'SubsurfaceProfile')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataLightFunction(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataLightFunction, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataMetalnessToDiffuseAlbedoF0(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataMetalnessToDiffuseAlbedoF0, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataPostProcess(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataPostProcess, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataSimpleClearCoatBSDF(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataSimpleClearCoatBSDF, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataSingleLayerWaterBSDF(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataSingleLayerWaterBSDF, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataSlabBSDF(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataSlabBSDF, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.specular_profile = Property(self, 'specular_profile', 'SpecularProfile')
        self.subsurface_profile = Property(self, 'subsurface_profile', 'SubsurfaceProfile')
        self.use_sss_diffusion = Property(self, 'use_sss_diffusion', 'bool')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataThinFilm(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataThinFilm, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataTransmittanceToMFP(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataTransmittanceToMFP, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataUI(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataUI, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataUnlitBSDF(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataUnlitBSDF, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataUtilityBase(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataUtilityBase, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataVerticalLayering(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataVerticalLayering, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.use_parameter_blending = Property(self, 'use_parameter_blending', 'bool')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataVolumetricFogCloudBSDF(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataVolumetricFogCloudBSDF, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class StrataWeight(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionStrataWeight, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class SubsurfaceMediumMaterialOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSubsurfaceMediumMaterialOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Subtract(MaterialExpression):
    def __init__(self, a = None, b = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSubtract, node_pos)

        # Properties
        self.const_a = Property(self, 'const_a', 'float')
        self.const_b = Property(self, 'const_b', 'float')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.a = InSocket(self, 'A', 'StructProperty')
        self.b = InSocket(self, 'B', 'StructProperty')

        # Output Sockets
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
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionSwitch, node_pos)

        # Properties
        self.const_default = Property(self, 'const_default', 'float')
        self.const_switch_value = Property(self, 'const_switch_value', 'float')
        self.desc = Property(self, 'desc', 'str')
        self.description = Property(self, 'description', 'str')
        self.inputs = Property(self, 'inputs', 'Array[SwitchCustomInput]')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Tangent(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTangent, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.period = Property(self, 'period', 'float')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TangentOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTangentOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TemporalSobol(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTemporalSobol, node_pos)

        # Properties
        self.const_index = Property(self, 'const_index', 'uint32')
        self.const_seed = Property(self, 'const_seed', 'Vector2D')
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.index = InSocket(self, 'Index', 'StructProperty')
        self.seed = InSocket(self, 'Seed', 'StructProperty')
        self.constSeed = InSocket(self, 'ConstSeed', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TerrainLayerCoords(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTerrainLayerCoords, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TerrainLayerSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTerrainLayerSwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TerrainLayerWeight(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTerrainLayerWeight, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureBase(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureBase, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = Property(self, 'texture', 'Texture')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureCoordinate(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureCoordinate, node_pos)

        # Properties
        self.coordinate_index = Property(self, 'coordinate_index', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.u_tiling = Property(self, 'u_tiling', 'float')
        self.un_mirror_u = Property(self, 'un_mirror_u', 'bool')
        self.un_mirror_v = Property(self, 'un_mirror_v', 'bool')
        self.v_tiling = Property(self, 'v_tiling', 'float')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureObject(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureObject, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = Property(self, 'texture', 'Texture')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureObjectParameter(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureObjectParameter, node_pos)

        # Properties
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

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureProperty(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureProperty, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.property_ = Property(self, 'property_', 'MaterialExposedTextureProperty')

        # Input Sockets
        self.textureObject = InSocket(self, 'TextureObject', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureSample(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureSample, node_pos)

        # Properties
        self.automatic_view_mip_bias = Property(self, 'automatic_view_mip_bias', 'bool')
        self.const_coordinate = Property(self, 'const_coordinate', 'uint8')
        self.const_mip_value = Property(self, 'const_mip_value', 'int32')
        self.desc = Property(self, 'desc', 'str')
        self.is_default_meshpaint_texture = Property(self, 'is_default_meshpaint_texture', 'bool')
        self.mip_value_mode = Property(self, 'mip_value_mode', 'TextureMipValueMode')
        self.sampler_source = Property(self, 'sampler_source', 'SamplerSourceMode')
        self.sampler_type = Property(self, 'sampler_type', 'MaterialSamplerType')
        self.texture = Property(self, 'texture', 'Texture')

        # Input Sockets
        self.UVs = InSocket(self, 'UVs', 'StructProperty')
        self.tex = InSocket(self, 'Tex', 'StructProperty')
        self.applyViewMipBias = InSocket(self, 'ApplyViewMipBias', 'StructProperty')

        # Output Sockets
        self.RGB = OutSocket(self, 'RGB', 'StructProperty')
        self.r = OutSocket(self, 'R', 'StructProperty')
        self.g = OutSocket(self, 'G', 'StructProperty')
        self.b = OutSocket(self, 'B', 'StructProperty')
        self.a = OutSocket(self, 'A', 'StructProperty')
        self.RGBA = OutSocket(self, 'RGBA', 'StructProperty')


class TextureSampleParameter(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureSampleParameter, node_pos)

        # Properties
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

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureSampleParameter2D(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureSampleParameter2D, node_pos)

        # Properties
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

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureSampleParameter2DArray(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureSampleParameter2DArray, node_pos)

        # Properties
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

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureSampleParameterBlur(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureSampleParameterBlur, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureSampleParameterCube(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureSampleParameterCube, node_pos)

        # Properties
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

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureSampleParameterCubeArray(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureSampleParameterCubeArray, node_pos)

        # Properties
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

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureSampleParameterSubUV(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureSampleParameterSubUV, node_pos)

        # Properties
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

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TextureSampleParameterVolume(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTextureSampleParameterVolume, node_pos)

        # Properties
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

        # Input Sockets
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')
        self.coordinates = InSocket(self, 'Coordinates', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ThinTranslucentMaterialOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionThinTranslucentMaterialOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.transmittanceColor = InSocket(self, 'TransmittanceColor', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Time(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTime, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.ignore_pause = Property(self, 'ignore_pause', 'bool')
        self.override_period = Property(self, 'override_period', 'bool')
        self.period = Property(self, 'period', 'float')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Transform(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTransform, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.transform_source_type = Property(self, 'transform_source_type', 'MaterialVectorCoordTransformSource')
        self.transform_type = Property(self, 'transform_type', 'MaterialVectorCoordTransform')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TransformPosition(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTransformPosition, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.transform_source_type = Property(self, 'transform_source_type', 'MaterialPositionTransformSource')
        self.transform_type = Property(self, 'transform_type', 'MaterialPositionTransformSource')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Truncate(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTruncate, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TruncateLWC(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTruncateLWC, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class TwoSidedSign(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionTwoSidedSign, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class Unpremult(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionUnpremult, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class VectorNoise(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVectorNoise, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.noise_function = Property(self, 'noise_function', 'VectorNoiseFunction')
        self.quality = Property(self, 'quality', 'int32')
        self.tile_size = Property(self, 'tile_size', 'uint32')
        self.tiling = Property(self, 'tiling', 'bool')

        # Input Sockets
        self.position = InSocket(self, 'Position', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class VectorParameter(MaterialExpression):
    def __init__(self, parameter_name = None, default_value = None, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVectorParameter, node_pos)

        # Properties
        self.channel_names = Property(self, 'channel_names', 'ParameterChannelNames')
        self.default_value = Property(self, 'default_value', 'LinearColor')
        self.desc = Property(self, 'desc', 'str')
        self.group = Property(self, 'group', 'Name')
        self.parameter_name = Property(self, 'parameter_name', 'Name')
        self.primitive_data_index = Property(self, 'primitive_data_index', 'uint8')
        self.sort_priority = Property(self, 'sort_priority', 'int32')
        self.use_custom_primitive_data = Property(self, 'use_custom_primitive_data', 'bool')

        # Input Sockets
        self.defaultValue = InSocket(self, 'DefaultValue', 'StructProperty')
        self.expressionGUID = InSocket(self, 'ExpressionGUID', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')
        self.r = OutSocket(self, 'r', 'StructProperty')
        self.g = OutSocket(self, 'g', 'StructProperty')
        self.b = OutSocket(self, 'b', 'StructProperty')
        self.a = OutSocket(self, 'a', 'StructProperty')

        if parameter_name is not None: self.parameter_name.set(parameter_name)
        if default_value is not None: self.default_value.set(default_value)

class VertexColor(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVertexColor, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class VertexInterpolator(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVertexInterpolator, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, 'Input', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class VertexNormalWS(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVertexNormalWS, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class VertexTangentWS(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVertexTangentWS, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ViewProperty(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionViewProperty, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.property_ = Property(self, 'property_', 'MaterialExposedViewProperty')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class ViewSize(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionViewSize, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class VirtualTextureFeatureSwitch(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVirtualTextureFeatureSwitch, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.no = InSocket(self, 'No', 'StructProperty')
        self.yes = InSocket(self, 'Yes', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class VolumetricAdvancedMaterialInput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVolumetricAdvancedMaterialInput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class VolumetricAdvancedMaterialOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVolumetricAdvancedMaterialOutput, node_pos)

        # Properties
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

        # Input Sockets
        self.phaseG = InSocket(self, 'PhaseG', 'StructProperty')
        self.phaseG2 = InSocket(self, 'PhaseG2', 'StructProperty')
        self.phaseBlend = InSocket(self, 'PhaseBlend', 'StructProperty')
        self.multiScatteringContribution = InSocket(self, 'MultiScatteringContribution', 'StructProperty')
        self.multiScatteringOcclusion = InSocket(self, 'MultiScatteringOcclusion', 'StructProperty')
        self.multiScatteringEccentricity = InSocket(self, 'MultiScatteringEccentricity', 'StructProperty')
        self.conservativeDensity = InSocket(self, 'ConservativeDensity', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class VolumetricCloudEmptySpaceSkippingInput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVolumetricCloudEmptySpaceSkippingInput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class VolumetricCloudEmptySpaceSkippingOutput(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionVolumetricCloudEmptySpaceSkippingOutput, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class WhileLoop(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionWhileLoop, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')


class WorldPosition(MaterialExpression):
    def __init__(self, node_pos: NodePos = None):
        super().__init__(unreal.MaterialExpressionWorldPosition, node_pos)

        # Properties
        self.desc = Property(self, 'desc', 'str')
        self.world_position_shader_offset = Property(self, 'world_position_shader_offset', 'WorldPositionIncludedOffsets')

        # Input Sockets
        self.input = InSocket(self, '', 'StructProperty')

        # Output Sockets
        self.output = OutSocket(self, '', 'StructProperty')
