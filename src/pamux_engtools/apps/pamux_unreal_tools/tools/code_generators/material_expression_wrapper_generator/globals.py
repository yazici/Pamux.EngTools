dump_folder = "C:/src/UNrealEngineClassDump/Class/Script"
generated_files_root = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/generated"
generated_py_out_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/generated/material_expression_wrappers.py"
generated_h_out_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/generated/material_expression_wrappers.h"

generated_cpp_out_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/generated/material_expression_wrappers.cpp"

h_template_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/templates/class_template.h"
cpp_template_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/templates/class_template.cpp"
py_template_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/templates/class_template.py"

generated_files_root = "C:/src/PamuxUnrealTools/Plugins/PamuxMaterialPlugin/Source/PamuxMaterialPlugin/Private/generated"
generated_h_out_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/generated/material_expression_wrappers.h"
h_template_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/templates/class_template2.h"
cpp_template_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/templates/class_template2.cpp"

unreal_classes_list = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/unreal_classes.json"
unreal_material_expression_classes = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/unreal_material_expression_classes.json"

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
    "MaterialExpressionPerInstanceCustomData3Vector",
    "MaterialExpressionSamplePhysicsIntegerField",
    "MaterialExpressionSamplePhysicsScalarField",
    "MaterialExpressionSamplePhysicsVectorField",

    "MaterialExpressionSkyAtmosphereAerialPerspective",
    "MaterialExpressionSkyAtmosphereDistantLightScatteredLuminance",
    "MaterialExpressionCloudSampleAttribute",
    "MaterialExpressionConstantDouble",
    "MaterialExpressionLandscapeGrassOutput",
    "MaterialExpressionLandscapeLayerBlend",
    "MaterialExpressionLandscapeLayerCoords",
    "MaterialExpressionLandscapeLayerSample",
    "MaterialExpressionLandscapeLayerSwitch",
    "MaterialExpressionLandscapeLayerWeight",
    "MaterialExpressionLandscapePhysicalMaterialOutput",
    "MaterialExpressionLandscapeVisibilityMask",
    "MaterialExpressionLess",
    "MaterialExpressionNamedRerouteBase",
    "MaterialExpressionNamedRerouteDeclaration",
    "MaterialExpressionNamedRerouteUsage",
    "MaterialExpressionSkyAtmosphereLightDiskLuminance",
    "MaterialExpressionSparseVolumeTextureObjectParameter",
    "MaterialExpressionSparseVolumeTextureSampleParameter",
    "MaterialExpressionSpriteTextureSampler",
    "MaterialExpressionStrataAdd",
    "MaterialExpressionStrataBSDF",
    "MaterialExpressionStrataConvertToDecal",
    "MaterialExpressionStrataEyeBSDF",
    "MaterialExpressionStrataHairBSDF",
    "MaterialExpressionStrataHazinessToSecondaryRoughness",
    "MaterialExpressionStrataHorizontalMixing",
    "MaterialExpressionStrataLegacyConversion",
    "MaterialExpressionStrataLightFunction",
    "MaterialExpressionStrataMetalnessToDiffuseAlbedoF0",
    "MaterialExpressionStrataPostProcess",
    "MaterialExpressionStrataSimpleClearCoatBSDF",
    "MaterialExpressionStrataSingleLayerWaterBSDF",
    "MaterialExpressionStrataSlabBSDF",
    "MaterialExpressionStrataThinFilm",
    "MaterialExpressionStrataTransmittanceToMFP",
    "MaterialExpressionStrataUI",
    "MaterialExpressionStrataUnlitBSDF",
    "MaterialExpressionStrataUtilityBase",
    "MaterialExpressionStrataVerticalLayering",
    "MaterialExpressionStrataVolumetricFogCloudBSDF",
    "MaterialExpressionStrataWeight",
    "MaterialExpressionVolumetricCloudEmptySpaceSkippingInput",
    "MaterialExpressionVolumetricCloudEmptySpaceSkippingOutput",

    "MaterialExpressionMaterialXAppend3Vector",
    "MaterialExpressionMaterialXAppend4Vector",
    "MaterialExpressionMaterialXBurn",
    "MaterialExpressionMaterialXDifference",
    "MaterialExpressionMaterialXDisjointOver",
    "MaterialExpressionMaterialXDodge",
    "MaterialExpressionMaterialXFractal3D",
    "MaterialExpressionMaterialXIn",
    "MaterialExpressionMaterialXLuminance",
    "MaterialExpressionMaterialXMask",
    "MaterialExpressionMaterialXMatte",
    "MaterialExpressionMaterialXMinus",
    "MaterialExpressionMaterialXOut",
    "MaterialExpressionMaterialXOver",
    "MaterialExpressionMaterialXOverlay",
    "MaterialExpressionMaterialXPlace2D",
    "MaterialExpressionMaterialXPlus",
    "MaterialExpressionMaterialXPremult",
    "MaterialExpressionMaterialXRamp4",
    "MaterialExpressionMaterialXRampLeftRight",
    "MaterialExpressionMaterialXRampTopBottom",
    "MaterialExpressionMaterialXRemap",
    "MaterialExpressionMaterialXRotate2D",
    "MaterialExpressionMaterialXScreen",
    "MaterialExpressionMaterialXSplitLeftRight",
    "MaterialExpressionMaterialXSplitTopBottom",
    "MaterialExpressionMaterialXSwizzle",
    "MaterialExpressionMaterialXTextureSampleParameterBlur",
    "MaterialExpressionMaterialXUnpremult",

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
    "MaterialExpressionRamp4",
    "MaterialExpressionHeightfieldMinMaxTexture"
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
