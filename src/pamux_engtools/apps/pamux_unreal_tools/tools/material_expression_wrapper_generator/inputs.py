from pamux_unreal_tools.tools.material_expression_wrapper_generator.values import *
from pamux_unreal_tools.tools.material_expression_wrapper_generator.globals import *

def setup_input_sockets(pamux_wrapper_class_name):
    result = Values()
    if pamux_wrapper_class_name in output_only_classes:
        return result
    
    if pamux_wrapper_class_name == "StaticSwitch":
        result.append(InputSocketInfo('True', 'StructProperty'))
        result.append(InputSocketInfo('False', 'StructProperty'))
        result.append(InputSocketInfo('Value', 'StructProperty'))

    elif pamux_wrapper_class_name == "TextureSample":
        result.append(InputSocketInfo('UVs', 'StructProperty'))
        result.append(InputSocketInfo('Tex', 'StructProperty'))
        result.append(InputSocketInfo('ApplyViewMipBias', 'StructProperty'))

    elif pamux_wrapper_class_name == "AntialiasedTextureMask":
        result.append(InputSocketInfo('UVs', 'StructProperty'))
        result.append(InputSocketInfo('ApplyViewMipBias', 'StructProperty'))

    elif pamux_wrapper_class_name == "Saturate":
        result.append(InputSocketInfo('', 'StructProperty'))

    elif pamux_wrapper_class_name == "ComponentMask":
        result.append(InputSocketInfo('', 'StructProperty'))
        
    elif pamux_wrapper_class_name == "NamedRerouteDeclaration":
        result.append(InputSocketInfo('', 'StructProperty'))

    elif pamux_wrapper_class_name == "QualitySwitch":
        result.append(InputSocketInfo('Default', 'StructProperty'))
        result.append(InputSocketInfo('Low', 'StructProperty'))
        result.append(InputSocketInfo('High', 'StructProperty'))
        result.append(InputSocketInfo('Medium', 'StructProperty'))
        result.append(InputSocketInfo('Epic', 'StructProperty'))

    elif pamux_wrapper_class_name == "SetMaterialAttributes":
        result.append(InputSocketInfo('MaterialAttributes', 'StructProperty'))

        result.append(InputSocketInfo('BaseColor', 'StructProperty'))
        result.append(InputSocketInfo('Metallic', 'StructProperty'))
        result.append(InputSocketInfo('Specular', 'StructProperty'))
        result.append(InputSocketInfo('Roughness', 'StructProperty'))
        result.append(InputSocketInfo('Anisotropy', 'StructProperty'))
        result.append(InputSocketInfo('EmissiveColor', 'StructProperty'))
        result.append(InputSocketInfo('Opacity', 'StructProperty'))
        result.append(InputSocketInfo('OpacityMask', 'StructProperty'))
        result.append(InputSocketInfo('Normal', 'StructProperty'))
        result.append(InputSocketInfo('Tangent', 'StructProperty'))
        result.append(InputSocketInfo('WorldPositionOffset', 'StructProperty'))
        result.append(InputSocketInfo('WorldDisplacement', 'StructProperty'))
        result.append(InputSocketInfo('TessellationMultiplier', 'StructProperty'))
        result.append(InputSocketInfo('SubsurfaceColor', 'StructProperty'))
        result.append(InputSocketInfo('ClearCoat', 'StructProperty'))
        result.append(InputSocketInfo('ClearCoatRoughness', 'StructProperty'))
        result.append(InputSocketInfo('AmbientOcclusion', 'StructProperty'))
        result.append(InputSocketInfo('Refraction', 'StructProperty'))
        result.append(InputSocketInfo('CustomizedUVs', 'StructProperty'))
        result.append(InputSocketInfo('PixelDepthOffset', 'StructProperty'))
        result.append(InputSocketInfo('ShadingModel', 'StructProperty'))

    elif pamux_wrapper_class_name == "MakeMaterialAttributes":
        result.append(InputSocketInfo('BaseColor', 'StructProperty'))
        result.append(InputSocketInfo('Metallic', 'StructProperty'))
        result.append(InputSocketInfo('Specular', 'StructProperty'))
        result.append(InputSocketInfo('Roughness', 'StructProperty'))
        result.append(InputSocketInfo('Anisotropy', 'StructProperty'))
        result.append(InputSocketInfo('EmissiveColor', 'StructProperty'))
        result.append(InputSocketInfo('Opacity', 'StructProperty'))
        result.append(InputSocketInfo('OpacityMask', 'StructProperty'))
        result.append(InputSocketInfo('Normal', 'StructProperty'))
        result.append(InputSocketInfo('Tangent', 'StructProperty'))
        result.append(InputSocketInfo('WorldPositionOffset', 'StructProperty'))
        # result.append(InputSocketInfo('WorldDisplacement', 'StructProperty'))
        #result.append(InputSocketInfo('TessellationMultiplier', 'StructProperty'))
        result.append(InputSocketInfo('SubsurfaceColor', 'StructProperty'))
        result.append(InputSocketInfo('ClearCoat', 'StructProperty'))
        result.append(InputSocketInfo('ClearCoatRoughness', 'StructProperty'))
        result.append(InputSocketInfo('AmbientOcclusion', 'StructProperty'))
        result.append(InputSocketInfo('Refraction', 'StructProperty'))
        result.append(InputSocketInfo('CustomizedUV_0', 'StructProperty'))
        result.append(InputSocketInfo('CustomizedUV_1', 'StructProperty'))
        result.append(InputSocketInfo('CustomizedUV_2', 'StructProperty'))
        result.append(InputSocketInfo('CustomizedUV_3', 'StructProperty'))
        result.append(InputSocketInfo('CustomizedUV_4', 'StructProperty'))
        result.append(InputSocketInfo('CustomizedUV_5', 'StructProperty'))
        result.append(InputSocketInfo('CustomizedUV_6', 'StructProperty'))
        result.append(InputSocketInfo('CustomizedUV_7', 'StructProperty'))
        result.append(InputSocketInfo('PixelDepthOffset', 'StructProperty'))
        result.append(InputSocketInfo('ShadingModel', 'StructProperty'))
        result.append(InputSocketInfo('Displacement', 'StructProperty'))

    elif pamux_wrapper_class_name == "BreakMaterialAttributes":
        result.append(InputSocketInfo('', 'StructProperty'))

    elif pamux_wrapper_class_name == "GetMaterialAttributes":
        result.append(InputSocketInfo('', 'StructProperty'))

    elif pamux_wrapper_class_name == "OneMinus":
        result.append(InputSocketInfo('', 'StructProperty'))

    elif pamux_wrapper_class_name == "Desaturation":
        result.append(InputSocketInfo('', 'StructProperty'))
        result.append(InputSocketInfo('Fraction', 'StructProperty'))
    
    elif pamux_wrapper_class_name in material_expressions_dump_data:
         result = material_expressions_dump_data[pamux_wrapper_class_name].inputs

    if result.is_empty:
        result.append(InputSocketInfo("", "StructProperty"))
        
    return result