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

    elif pamux_wrapper_class_name == "QualitySwitch":
        result.append(InputSocketInfo('Default', 'StructProperty'))
        result.append(InputSocketInfo('Low', 'StructProperty'))
        result.append(InputSocketInfo('High', 'StructProperty'))
        result.append(InputSocketInfo('Medium', 'StructProperty'))
        result.append(InputSocketInfo('Epic', 'StructProperty'))

    elif pamux_wrapper_class_name == "SetMaterialAttributes":

        func = lambda item: result.append(InputSocketInfo(item, 'StructProperty'))
        MaterialAttributeFields.for_each(func, False,  ['MaterialAttributes', 'WorldDisplacement', 'TessellationMultiplier', 'CustomizedUVs'], "")

    elif pamux_wrapper_class_name == "MakeMaterialAttributes":

        func = lambda item: result.append(InputSocketInfo(item, 'StructProperty'))
        MaterialAttributeFields.for_each(func, False,  ['Displacement'], "_")

    elif pamux_wrapper_class_name == "Desaturation":
        result.append(InputSocketInfo('Fraction', 'StructProperty'))
    
    elif pamux_wrapper_class_name in material_expressions_dump_data:
         result = material_expressions_dump_data[pamux_wrapper_class_name].inputs

    return result