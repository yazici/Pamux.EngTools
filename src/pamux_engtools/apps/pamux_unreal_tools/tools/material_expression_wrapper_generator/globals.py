dump_folder = "C:/src/UNrealEngineClassDump/Class/Script"
generated_py_out_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/generated/material_expression_wrappers.py"

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
    "Floor",
    "BreakMaterialAttributes"
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

# skip_these_classes = []