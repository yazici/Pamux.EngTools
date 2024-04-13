from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.values import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.globals import *

def setup_output_sockets(pamux_wrapper_class_name):
    result = Values()

    if pamux_wrapper_class_name in input_only_classes:
        return result

    if pamux_wrapper_class_name == "TextureSample":
        result.append(OutputSocketInfo('RGB', 'StructProperty'))
        result.append(OutputSocketInfo('R', 'StructProperty'))
        result.append(OutputSocketInfo('G', 'StructProperty'))
        result.append(OutputSocketInfo('B', 'StructProperty'))
        result.append(OutputSocketInfo('A', 'StructProperty'))
        result.append(OutputSocketInfo('RGBA', 'StructProperty'))

    elif pamux_wrapper_class_name == "GetMaterialAttributes":
        func = lambda item: result.append(OutputSocketInfo(item, 'StructProperty'))

        MaterialAttributeFields.for_each(func, False,  ['MaterialAttributes', 'WorldDisplacement', 'TessellationMultiplier', 'CustomizedUVs'], None)

    elif pamux_wrapper_class_name == "BreakMaterialAttributes":
        func = lambda item: result.append(OutputSocketInfo(item, 'StructProperty'))

        MaterialAttributeFields.for_each(func, False,  ["Displacement"], "")

        # result.append(OutputSocketInfo('BaseColor', 'StructProperty'))
        # result.append(OutputSocketInfo('Metallic', 'StructProperty'))
        # result.append(OutputSocketInfo('Specular', 'StructProperty'))
        # result.append(OutputSocketInfo('Roughness', 'StructProperty'))
        # result.append(OutputSocketInfo('Anisotropy', 'StructProperty'))
        # result.append(OutputSocketInfo('EmissiveColor', 'StructProperty'))
        # result.append(OutputSocketInfo('Opacity', 'StructProperty'))
        # result.append(OutputSocketInfo('OpacityMask', 'StructProperty'))
        # result.append(OutputSocketInfo('Normal', 'StructProperty'))
        # result.append(OutputSocketInfo('Tangent', 'StructProperty'))
        # result.append(OutputSocketInfo('WorldPositionOffset', 'StructProperty'))
        # # result.append(OutputSocketInfo('WorldDisplacement', 'StructProperty'))
        # #result.append(OutputSocketInfo('TessellationMultiplier', 'StructProperty'))
        # result.append(OutputSocketInfo('SubsurfaceColor', 'StructProperty'))
        # result.append(OutputSocketInfo('ClearCoat', 'StructProperty'))
        # result.append(OutputSocketInfo('ClearCoatRoughness', 'StructProperty'))
        # result.append(OutputSocketInfo('AmbientOcclusion', 'StructProperty'))
        # result.append(OutputSocketInfo('Refraction', 'StructProperty'))
        # result.append(OutputSocketInfo('CustomizedUV0', 'StructProperty'))
        # result.append(OutputSocketInfo('CustomizedUV1', 'StructProperty'))
        # result.append(OutputSocketInfo('CustomizedUV2', 'StructProperty'))
        # result.append(OutputSocketInfo('CustomizedUV3', 'StructProperty'))
        # result.append(OutputSocketInfo('CustomizedUV4', 'StructProperty'))
        # result.append(OutputSocketInfo('CustomizedUV5', 'StructProperty'))
        # result.append(OutputSocketInfo('CustomizedUV6', 'StructProperty'))
        # result.append(OutputSocketInfo('CustomizedUV7', 'StructProperty'))
        # result.append(OutputSocketInfo('PixelDepthOffset', 'StructProperty'))
        # result.append(OutputSocketInfo('ShadingModel', 'StructProperty'))
        # result.append(OutputSocketInfo('Displacement', 'StructProperty'))

    # elif pamux_wrapper_class_name == "MakeMaterialAttributes":
    #     result.append(OutputSocketInfo('', 'StructProperty'))

    elif pamux_wrapper_class_name == "VectorParameter":
        # result.append(OutputSocketInfo('', 'StructProperty'))
        result.append(OutputSocketInfo('r', 'StructProperty'))
        result.append(OutputSocketInfo('g', 'StructProperty'))
        result.append(OutputSocketInfo('b', 'StructProperty'))
        result.append(OutputSocketInfo('a', 'StructProperty'))

    # elif pamux_wrapper_class_name == "Constant":
    #     result.append(OutputSocketInfo('', 'StructProperty'))
        #result.append(OutputSocketInfo('r', 'StructProperty'))

    elif pamux_wrapper_class_name == "Constant2Vector":
        # result.append(OutputSocketInfo('', 'StructProperty'))
        result.append(OutputSocketInfo('r', 'StructProperty'))
        result.append(OutputSocketInfo('g', 'StructProperty'))

    elif pamux_wrapper_class_name == "Constant3Vector":
        # result.append(OutputSocketInfo('', 'StructProperty'))
        result.append(OutputSocketInfo('r', 'StructProperty'))
        result.append(OutputSocketInfo('g', 'StructProperty'))
        result.append(OutputSocketInfo('b', 'StructProperty'))

    elif pamux_wrapper_class_name == "Constant4Vector":
        # result.append(OutputSocketInfo('', 'StructProperty'))
        result.append(OutputSocketInfo('r', 'StructProperty'))
        result.append(OutputSocketInfo('g', 'StructProperty'))
        result.append(OutputSocketInfo('b', 'StructProperty'))
        result.append(OutputSocketInfo('a', 'StructProperty'))


    elif pamux_wrapper_class_name in material_expressions_dump_data:
        result = material_expressions_dump_data[pamux_wrapper_class_name].outputs

    # if result.is_empty:
    #     result.append(OutputSocketInfo("", "StructProperty"))

    return result