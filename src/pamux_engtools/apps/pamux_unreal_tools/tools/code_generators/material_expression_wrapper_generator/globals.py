dump_folder = "C:/src/UNrealEngineClassDump/Class/Script"
generated_py_out_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/generated/material_expression_wrappers.py"
generated_h_out_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/generated/material_expression_wrappers.h"
generated_cpp_out_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/generated/material_expression_wrappers.cpp"

material_expressions_dump_data = {}

input_only_classes = []
output_only_classes = [ 
    "Constant",
    "Constant2Vector",
    "Constant3Vector",
    "Constant4Vector",
    "NamedRerouteUsage",
    "StaticBool",
    "TextureObject"
]

parameter_without_default_value_classes = [
    "Parameter",
    "TextureObjectParameter",
    "TextureSampleParameter",
    "SparseVolumeTextureObjectParameter",
    "CollectionParameter",
    "FontSampleParameter",
    "RuntimeVirtualTextureSampleParameter",
    "SparseVolumeTextureSampleParameter",
    "StaticComponentMaskParameter"
]

parameter_with_default_value_classes = [
    "StaticBoolParameter",
    "ScalarParameter",
    "StaticSwitchParameter",
    "VectorParameter",
    "ChannelMaskParameter",
    "CurveAtlasRowParameter",
    "DoubleVectorParameter"]

binary_op_classes = [ "AppendVector" ]

binary_op_classes_with_const = [
    "Add",
    "Multiply",
    "Subtract",
    "Divide",
    "Max",
    "Min"
]

unary_op_classes = [
    "Saturate",
    "OneMinus",
    "Floor"
]




# See unreal.py
# many are deprecated: 'MaterialExpressionDisjointOver' was renamed to 'MaterialExpressionMaterialXDisjointOver'.
skip_these_classes= [    
    "MaterialExpressionAppend3Vector",
    "MaterialExpressionAppend4Vector",
    "MaterialExpressionBurn",
    "MaterialExpressionDifference",
    "MaterialExpressionDisjointOver",
    "MaterialExpressionDodge",
    "MaterialExpressionFractal3D",
    "MaterialExpressionIn",
    "MaterialExpressionLuminance",
    "MaterialExpressionMask",
    "MaterialExpressionMatte",
    "MaterialExpressionMinus",
    "MaterialExpressionOut",
    "MaterialExpressionOver",
    "MaterialExpressionOverlay",
    "MaterialExpressionPlace2D",
    "MaterialExpressionPlus",
    "MaterialExpressionPremult",
    "MaterialExpressionRampLeftRight",
    "MaterialExpressionRampTopBottom",
    "MaterialExpressionRemap",
    "MaterialExpressionRotate2D",
    "MaterialExpressionScreen",
    "MaterialExpressionSplitLeftRight",
    "MaterialExpressionSplitTopBottom",
    "MaterialExpressionTextureSampleParameterBlur",
    "MaterialExpressionUnpremult",
    "MaterialExpressionTerrainLayerCoords",
    "MaterialExpressionTerrainLayerSwitch",
    "MaterialExpressionTerrainLayerWeight",
    "MaterialExpressionMaterialXExponential",
    "MaterialExpressionMaterialXHsvToRgb",
    "MaterialExpressionMaterialXLength",
    "MaterialExpressionMaterialXLogarithm",
    "MaterialExpressionMaterialXRgbToHsv",
    "MaterialExpressionRamp4"
]

class MaterialAttributeFields:
    __items = [
        '#   MaterialAttributes',
        'BaseColor',
        'Metallic',
        'Specular',
        'Roughness',
        'Anisotropy',
        'EmissiveColor',
        'Opacity',
        'OpacityMask',
        'Normal',
        'Tangent',
        'WorldPositionOffset',
        '#   WorldDisplacement',
        '#   TessellationMultiplier',
        'SubsurfaceColor',
        'ClearCoat',
        'ClearCoatRoughness',
        'AmbientOcclusion',
        'Refraction',
        '#   CustomizedUVs',
        'PixelDepthOffset',
        'ShadingModel',
        '#   Displacement'
    ]
    
    @staticmethod
    def for_each(func, lowerCaseStart = False, enable = [], customUVSeparator = None):
        for item in MaterialAttributeFields.__items:
            item = item.strip()
            is_sharp = item.startswith("#")
            if is_sharp:
                item = item.strip("#").strip()

            if lowerCaseStart:
                final_item  = item[0].lower() + item[1:]
            else:
                final_item = item

            if not is_sharp:
                func(final_item)
                continue

            if item == 'CustomizedUVs':
                if customUVSeparator is not None:
                    final_item = final_item[0:-1]
                    for i in range(0, 8):
                        func(f"{final_item}{customUVSeparator}{i}")
                    continue


            if item in enable:
                func(final_item)
