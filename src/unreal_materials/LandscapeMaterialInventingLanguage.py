import unreal

class Utils:
    def readParamConfig(filePath: str):
        return None

    def M_Landscape_Master(out):
        pass

    def rvtOutput(baseColor, rvtSpecularResult,roughness, normal, worldHeight):
        pass

class Node:
    pass

class Nodes:
    def UMaterialExpressionWorldPosition():
        result = Node()
        return result

    def desaturate(value, fraction: float = None):
        result = Node()
        return result


    def lerp(a, b, alpha):
        result = Node()
        return result

    
    def subtract(a: float, b: float):
        result = Node()
        return result


    def divide(a: float, b: float):
        result = Node()
        return result

    def multiply(a: float, b: float):
        result = Node()
        return result

    def saturate(value: float):
        result = Node()
        return result
    
    def getMaterialAttributes(value):
        result = Node()
        return result

    def setMaterialAttributes(value):
        result = Node()
        return result

    def virtualTextureFeatureSwitch(no, yes):
        result = Node()
        return result


    def qualitySwitch(default, low):
        result = Node()
        return result
    
    def sCurve(baseColor, specularContrast):
        result = Node()
        return result
    
    def mask(value, rgbaMask):
        result = Node()
        return result



# Begins here
# https://docs.unrealengine.com/5.0/en-US/landscape-material-expressions-in-unreal-engine/
# https://docs.unrealengine.com/4.27/en-US/ProductionPipelines/ScriptingAndAutomation/Python/
# https://www.tacolor.xyz/Howto/Manipulate_Material_Expression_Nodes_Of_Material_With_Python_In_UE.html
    
class Unreal:
    BPFactory = unreal.BlueprintFactory()
    AT = unreal.AssetToolsHelpers.get_asset_tools()
    EAL = unreal.EditorAssetLibrary
    MEL = unreal.MaterialEditingLibrary

    @staticmethod
    def create_material_asset(material_name):
        result = Unreal.AT.create_asset(f"M_{material_name}", f"{Unreal.material_asset_folder(material_name)}", unreal.Material, unreal.MaterialFactoryNew())
        Unreal.EAL.save_asset(result.get_path_name())
        return result

    @staticmethod
    def create_material_function_asset(material_name, name):
        result = Unreal.AT.create_asset(f"MF_{material_name}", f"{Unreal.material_function_asset_folder(material_name)}", unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew())
        Unreal.EAL.save_asset(result.get_path_name())
        return result
    
    @staticmethod
    def material_asset_folder(material_name):
        return f"/Game/Materials/M_{material_name}"
    
    @staticmethod
    def material_function_asset_folder(material_name):
        return f"{Unreal.material_asset_folder(material_name)}/functions"
    
    @staticmethod
    def material_function_asset_path(material_name, material_function_name):
        return f"{Unreal.material_function_asset_folder(material_name)}/MF_{material_function_name}"


    # unreal.MaterialExpressionAdd
    # unreal.MaterialExpressionTextureSampleParameter2D
    # unreal.MaterialExpressionMaterialFunctionCall

    # https://dev.epicgames.com/documentation/en-us/unreal-engine/PythonAPI/class/MaterialEditingLibrary?application_version=5.3
    # https://github.com/Tangerie/Json2DA/blob/21234174d5ebafb69782dee39a3b044638e25a6a/MaterialExpressions.py#L83

    @staticmethod
    # create_material_expression(material, unreal.MaterialExpressionAdd)
    def create_material_expression(material, node_type):    
        result = unreal.MaterialEditingLibrary.create_material_expression(material, node_type, node_pos_x=-200, node_pos_y=0)
        return result
    
    
    @staticmethod
    # create_material_expression_in_function(material_function, unreal.MaterialExpressionAdd)    
    def create_material_expression_in_function(material_function, node_type):    
        result = unreal.MaterialEditingLibrary.create_material_expression_in_function(material_function, node_type)
        return result
    

    @staticmethod
    # Unreal.create_material_expression_function_call(material, material_function_asset_path)    
    def create_material_expression_function_call(material, material_function_asset_path):    
        result = Unreal.create_material_expression(material, unreal.MaterialExpressionMaterialFunctionCall)
        result.set_editor_property("material_function", unreal.load_asset(material_function_asset_path))
        return result    
    


    # @staticmethod
    # # Unreal.create_material_expression_set_material_attributes(material, ["MP_Specular", "MP_Normal", "MP_WorldPositionOffset", "MP_CustomData0", "MP_CustomizedUVs0"])
    # def create_material_expression_set_material_attributes(material, attribute_names):    
    #     result = Unreal.create_material_expression(material, unreal.MaterialExpressionSetMaterialAttributes)
    #     for name in attribute_names:
    #         Unreal.MEL.add_input_at_expression_set_material_attributes(result, name)

    #     return result
    
    # @staticmethod
    # # Unreal.create_material_expression_set_material_attributes(material, ["MP_Specular", "MP_Normal", "MP_WorldPositionOffset", "MP_CustomData0", "MP_CustomizedUVs0"])
    # def create_material_expression_get_material_attributes(material, attribute_names):    
    #     result = Unreal.create_material_expression(material, unreal.MaterialExpressionGetMaterialAttributes)
    #     for name in attribute_names:
    #         Unreal.MEL.add_output_at_expression_get_material_attributes(result, name)
    #     return result
    

    # get_inputs_for_material_expression

    
    @staticmethod
    def create_material_expression_LandscapeLayerBlend(material, attribute_names):    
        landscapeLayerBlend = Unreal.create_material_expression(material, unreal.MaterialExpressionLandscapeLayerBlend)
        
        layers = []

        for name in attribute_names:
            layer = unreal.LayerBlendInput()
            
            layer.layer_name = name

            layers.append(name)

        landscapeLayerBlend.set_editor_property('layers', layers)


        for name in attribute_names:
            call = Unreal.create_material_expression_function_call(material, f"/Game/Materials/Landscape/MLF_{name}")

            Unreal.MEL.connect_material_expressions(call , "Result" , landscapeLayerBlend, f"Layer{name}")
            Unreal.MEL.connect_material_expressions(call , "Height" , landscapeLayerBlend, f"Height{name}")
    

Params = Utils.readParamConfig("./LandscapeMaterialInventingLanguage.Params.json")

class Globals:
    Layers = ["Dirt", "Grass", "Mud", "StonyGround", "Fields", "PlowedGround", "ForestGround", "HeavyMud"]
    LayersForGrass = ["Dirt", "Grass", "StonyGround", "Fields", "PlowedGround", "HeavyMud"]
    AbsoluteWorldPosition = Nodes.UMaterialExpressionWorldPosition()


material = Unreal.create_material_asset("tesds")
# material = Unreal.create_material_function_asset("test", "test_dirt")

landscapeLayerBlendNode = Unreal.create_material_expression_LandscapeLayerBlend(material, Globals.layer_names)


class MaterialFunctions:
    def blendTwoMaterialsViaHighOpacityMap(blendedLandscapeLayersWithWetness, blendedLandscapeLayersWithWetnessAndPuddles):
        result = Node()
        return result
    
    def applyWetness(blendedLandscapeLayers, wetness):
        result = Node()
        return result

    def applyPuddles(blendedLandscapeLayersWithWetness):
        result = Node()
        return result
    
    def correctGlancingAngleSpec(value):
        result = Node()
        return result

    def blendLandscapeLayers(layers: list):
        result = Node()
        
        for layer in layers:
            layerOut = MaterialLayerFunctions.call(layer)

        return result
    
    def landscapeBaseMaterial(commonParams, opacityParams):
        result = Node()
        height = Node()


        # commonParams.DoTextureBomb = True
        # commonParams.Albedo = Texture Object
        # commonParams.Bomb.DoRotationVariation = false
        # commonParams.Bomb.DoCellScale = 1.0
        # commonParams.Bomb.PatternScale = 1.0
        # commonParams.Bomb.RandomOffset = 0.0
        # commonParams.Bomb.RotationVariation = 0
        # commonParams.UVParams (1,1,.5,.5)
        # commonParams.Rotation = 0.0
        # commonParams.ColorOverlay = (1,1,1)
        # commonParams.Contrast = 0.0
        # commonParams.Contrast.Variation = 1.0

        uvParamsComponents = Nodes.BreakOutFloat4Components(commonParams.UVParams)
        uvParamsRG = Nodes.Append(uvParamsComponents.r, uvParamsComponents.g)
        uvParamsBA = Nodes.Append(uvParamsComponents.b, uvParamsComponents.a)

        uvs = Nodes.multiply(Nodes.landscapeLayerCoords(), uvParamsRG)

        rotatedUVs = Nodes.customRotator(uvs, uvParamsBA, commonParams.Rotation)


        ####
        

        qualitySwitched = Nodes.qualitySwitch(commonParams.DoTextureBomb, False)

        heightTexture = Blocks.heightTexture(qualitySwitched, commonParams, rotatedUVs)

        baseColor = Blocks.baseColorPath(qualitySwitched, commonParams, rotatedUVs, heightTexture)
        roughness = Blocks.roughnessPath(qualitySwitched, commonParams, rotatedUVs)        
        opacity = Blocks.opacityPath(heightTexture, commonParams)
        normal = Blocks.normalPath(qualitySwitched, commonParams, rotatedUVs)

        sma = Nodes.setMaterialAttributes(baseColor, roughness, normal, opacity)
        gma, gmaOpacity = Nodes.getMaterialAttributes(sma)

        gmaOpacityR = Nodes.mask(gmaOpacity, "R")

        return gma, gmaOpacityR

        # MaterialFunctions.landscapeBaseMaterial(
        #     commonParams.Albedo,
        #     commonParams.ColorOverlay,
        #     commonParams.ColorOverlay.Intensity,

        #     commonParams.Contrast,
        #     commonParams.Contrast.Variation,

        #     commonParams.Roughness,
        #     commonParams.Roughness.Intensity,

        #     commonParams.Normal.Intensity,
        #     commonParams.Normal,

        #     commonParams.Displacement,

        #     commonParams.UVParams, # Append(Result, RotCenterY -A-)

        #     commonParams.Rotation,

        #     commonParams.DoTextureBomb,
        #     commonParams.Bomb.DoRotationVariation,
        #     commonParams.Bomb.DoCellScale,
        #     commonParams.Bomb.PatternScale,
        #     commonParams.Bomb.RandomOffset,
        #     commonParams.Bomb.RotationVariation,

        #     opacityParams.Strength,
        #     opacityParams.Add,
        #     opacityParams.Contrast
        # )

        
        return result, height


class MaterialLayerFunctions:
    def call(layer):
        result = Node()
        return result

class Blocks:
    def rvtSpecular(baseColor, params):
        result = Nodes.sCurve(baseColor, Params.specularContrast)
        result = Nodes.desaturate(result)
        result = Nodes.multiply(result, Params.specular)
        result = Nodes.lerp(0.0, Params.specularMax, result)
        return result
    
    def landscapeGrassOutputAndMasking(foliageMask, layers):
        result = Node()
        return result

    def baseColorPath(qualitySwitched, commonParams, rotatedUVs, heightTexture):
        switched = Blocks.doStuffWithTexture(commonParams.Albedo, False, qualitySwitched, commonParams, rotatedUVs)        

        switchedAndMultipliedColorOverlay = Nodes.multiply(switched, commonParams.ColorOverlay)

        blendOverlay = Nodes.blend_overlay(switched, commonParams.ColorOverlay)


        qualitySwitched2 = Nodes.qualitySwitch(blendOverlay, switchedAndMultipliedColorOverlay)

        lerpedColorOverlay = Nodes.lerp(switched, qualitySwitched2, commonParams.ColorOverlay.Intensity)

        cheapContrastOverlay = Nodes.cheapContrast_RGB(lerpedColorOverlay, commonParams.Contrast)

        heightLerp = Nodes.height_lerp(lerpedColorOverlay, cheapContrastOverlay, commonParams.Contrast.Variation, heightTexture)

        return Nodes.qualitySwitch(heightLerp, lerpedColorOverlay)


    def roughnessPath(qualitySwitched, commonParams, rotatedUVs):
        switched = Blocks.doStuffWithTexture(commonParams.Roughness, False, qualitySwitched, commonParams, rotatedUVs)        

        return Nodes.multiply(switched, commonParams.Roughness.Intensity)

    @staticmethod
    def normalPath(qualitySwitched, commonParams, rotatedUVs):
        switched = Blocks.doStuffWithTexture(commonParams.Normal, True, qualitySwitched, commonParams, rotatedUVs)

        computedIntensity = Nodes.append(commonParams.Normal.Intensity, commonParams.Normal.Intensity)
        constZero = 0
        computedIntensity = Nodes.append(computedIntensity, constZero)

        return Nodes.multiplyAdd(switched, computedIntensity)
    
    @staticmethod
    def heightTexture(qualitySwitched, commonParams, rotatedUVs):
        return Blocks.doStuffWithTexture(commonParams.Displacement, False, qualitySwitched, commonParams, rotatedUVs)
        
    @staticmethod
    def doStuffWithTexture(texture, isNormalMap, qualitySwitched, commonParams, rotatedUVs):
        textureCellBombing_LandscapeResult = MaterialFunctions.textureCellBombing_Landscape(
            texture,
            rotatedUVs,
            commonParams.Bomb.DoCellScale,
            commonParams.Bomb.PatternScale,
            commonParams.Bomb.DoRotationVariation,
            commonParams.Bomb.RandomOffset, # Variation??
            commonParams.Bomb.RotationVariation,
            isNormalMap)
        
        textureSample = Nodes.TextureSample(uvs = rotatedUVs, tex = texture)

        return Nodes.switch(textureCellBombing_LandscapeResult, textureSample, qualitySwitched)



    def opacityPath(heightTexture, commonParams):
        # # commonParams.D.Intensity = 1
        
        # isNormalMap = True

        # textureCellBombing_LandscapeResult = MaterialFunctions.textureCellBombing_Landscape(
        #     commonParams.Displacement,
        #     rotatedUVs,
        #     commonParams.Bomb.DoCellScale,
        #     commonParams.Bomb.PatternScale,
        #     commonParams.Bomb.DoRotationVariation,
        #     commonParams.Bomb.RandomOffset, # Variation??
        #     commonParams.Bomb.RotationVariation,
        #     isNormalMap)
        
        # textureSample = Nodes.TextureSample(uvs = rotatedUVs, tex = commonParams.Normal)

        # switched = Nodes.switch(textureCellBombing_LandscapeResult, textureSample, qualitySwitched)

        computedIntensity = Nodes.power(heightTexture, commonParams.Opacity.Contrast)
        computedIntensity = Nodes.multiply(computedIntensity, commonParams.Opacity.Strength)
        computedIntensity = Nodes.add(computedIntensity, commonParams.Opacity.Add)

        return Nodes.multiplyAdd(heightTexture, computedIntensity)


def M_Landscape_Master():
    blendedLandscapeLayers = MaterialFunctions.blendLandscapeLayers(Globals.layer_names)

    blendedLandscapeLayersWithWetness = MaterialFunctions.applyWetness(blendedLandscapeLayers, Params.wetness)
    blendedLandscapeLayersWithWetnessAndPuddles = MaterialFunctions.applyPuddles(blendedLandscapeLayersWithWetness)

    saturatedWetness = Nodes.saturate(Nodes.divide(Nodes.subtract(Params.wetness, 0.5), 0.5))

    materialsBlendedViaHighOpacityMap = MaterialFunctions.blendTwoMaterialsViaHighOpacityMap(blendedLandscapeLayersWithWetness, blendedLandscapeLayersWithWetnessAndPuddles, saturatedWetness)

    return (
        M_Landscape_Master_Main(materialsBlendedViaHighOpacityMap),
        M_Landscape_Master_RVTOutput(materialsBlendedViaHighOpacityMap),
        M_Landscape_Master_LandscapeGrassOutputAndMasking(materialsBlendedViaHighOpacityMap)
    )

def M_Landscape_Master_Main(materialsBlendedViaHighOpacityMap):
    landscapeRVTWithMaterialAttributes = Nodes.setMaterialAttributes(Params.landscapeRVT)

    virtualTextureFeatureSwitchResult = Nodes.virtualTextureFeatureSwitch(materialsBlendedViaHighOpacityMap, landscapeRVTWithMaterialAttributes)

    correctedGlancingAngleSpec = MaterialFunctions.correctGlancingAngleSpec(virtualTextureFeatureSwitchResult)

    qualitySwitchResult = Nodes.qualitySwitch(correctedGlancingAngleSpec, virtualTextureFeatureSwitchResult)

    return Nodes.setMaterialAttributes(qualitySwitchResult, Params.landscapeVisibilityMask)


def M_Landscape_Master_RVTOutput(materialsBlendedViaHighOpacityMap):
    materialsBlendedViaHighOpacityMapMaterialAttributes = Nodes.getMaterialAttributes(materialsBlendedViaHighOpacityMap)

    rvtSpecularResult = Blocks.rvtSpecular(materialsBlendedViaHighOpacityMapMaterialAttributes.baseColor)

    return Blocks.rvtOutput(materialsBlendedViaHighOpacityMapMaterialAttributes.baseColor, rvtSpecularResult, materialsBlendedViaHighOpacityMapMaterialAttributes.roughness, materialsBlendedViaHighOpacityMapMaterialAttributes.normal, Globals.AbsoluteWorldPosition.z)

def M_Landscape_Master_LandscapeGrassOutputAndMasking():
    landscapeGrassOutput = Blocks.landscapeGrassOutputAndMasking(Params.foliageMask, Globals.grass_layer_names)

def MLF_Dirt():
    return MaterialFunctions.landscapeBaseMaterial(Params.Dirt)

def MLF_Grass():
    return MaterialFunctions.landscapeBaseMaterial(Params.Grass)

def MLF_Mud():
    return MaterialFunctions.landscapeBaseMaterial(Params.Mud)

def MLF_StonyGround():
    return MaterialFunctions.landscapeBaseMaterial(Params.StonyGround)

def MLF_Fields():
    return MaterialFunctions.landscapeBaseMaterial(Params.Fields)

def MLF_PlowedGround():
    return MaterialFunctions.landscapeBaseMaterial(Params.PlowedGround)

def MLF_HeavyMud():
    return MaterialFunctions.landscapeBaseMaterial(Params.HeavyMud)

def MLF_ForestGround():
    result, height = MaterialFunctions.landscapeBaseMaterial(Params.ForestGround, Params.ForestGround.Opacity)

    materialAttributes = Nodes.getMaterialAttributes(result)

    fuzzyShading = Nodes.fuzzyShading(
        materialAttributes.baseColor,
        materialAttributes.normal,
        Params.ForestGround.FuzzCoreDarkness,
        Params.ForestGround.FuzzPower,
        Params.ForestGround.FuzzBrightness
    )

    rouhgnessB = Nodes.mask(materialAttributes.rouhgness, "B")

    lerped = Nodes.lerp(materialAttributes.baseColor, fuzzyShading, rouhgnessB)

    return Nodes.setMaterialAttributes(
        lerped,
        materialAttributes.normal,
        materialAttributes.specular,
        materialAttributes.roughness
    ), height



#BlueprintEditorLibrary
# BlueprintEditorToolMenuContext
# BlueprintFactory
# BlueprintGeneratedClass

# # Registries and Libraries
# asset_registry_helper = unreal.AssetRegistryHelpers()
# asset_registry        = asset_registry_helper.get_asset_registry()
# EditorAssetLibrary    = unreal.EditorAssetLibrary()
# ToolMenus             = unreal.ToolMenus.get()
# AssetTools            = unreal.AssetToolsHelpers.get_asset_tools()

# # Subsystems
# AssetEditorSubsystem   = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)
# EditorActorSubsystem   = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
# EditorUtilitySubsystem = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem)
# LevelEditorSubsystem   = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)


# @unreal.ufunction(params=[int], static=True, meta=dict(Category="Editor Utils lib"))
# def create_blueprint(count):
#     for i in range(count):
#         # if we try to create an asset at a certain folder that doesn't exists
#         # unreal will automatically catch that and create the folder structure
#         bp_name = "MyPlayerController{}".format(i) 
#         bp_path = "/Game/PlayerController"
#         # assets are created through factories 
#         factory = unreal.BlueprintFactory()
#         # we need to set the parent in the factory 
#         # note that also factory derives from object
#         factory.set_editor_property("ParentClass", unreal.PlayerController)
#         asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
#         asset = asset_tools.create_asset(bp_name, bp_path, None, factory)
#         # much faster to change than in c++ no need to recompile anything :)
#         unreal.EditorAssetLibrary.save_loaded_asset(asset)



#             self.MEL.get_material_property_input_node(self.material, p)
#             for i in self.MEL.get_inputs_for_material_expression(self.material, n):
# unreal.MaterialEditingLibrary.recompile_material(material)
# unreal.EditorAssetLibrary.list_assets
                #  const = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant, -300, 0)

            # unreal.MaterialEditingLibrary.connect_material_property(const, "", unreal.MaterialProperty.MP_OPACITY_MASK)

    # @staticmethod
    # def connect_material_property(from_expression):
    #     unreal.MaterialEditingLibrary.connect_material_property(from_expression=from_expression, from_output_name="", property_ = unreal.MaterialProperty.MP_BASE_COLOR)

        # Unreal.MEL.connect_material_property(from_expression=from_expression, from_output_name="", material_property_str="MP_WorldPositionOffset")

    # @staticmethod
    # def create_output(self, material: unreal.Material, custom_node: unreal.MaterialExpressionCustom) -> None:
    #     mat_att = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionBreakMaterialAttributes, -300, 0)
    #     # Connect custom node to the new break
    #     unreal.MaterialEditingLibrary.connect_material_expressions(custom_node, '', mat_att, 'Attr')
    #     # Connect all outputs
    #     unreal.MaterialEditingLibrary.connect_material_property(mat_att, "BaseColor", unreal.MaterialProperty.MP_BASE_COLOR)
    #     unreal.MaterialEditingLibrary.connect_material_property(mat_att, "Metallic", unreal.MaterialProperty.MP_METALLIC)
    #     unreal.MaterialEditingLibrary.connect_material_property(mat_att, "Roughness", unreal.MaterialProperty.MP_ROUGHNESS)
    #     unreal.MaterialEditingLibrary.connect_material_property(mat_att, "EmissiveColor", unreal.MaterialProperty.MP_EMISSIVE_COLOR)
    #     unreal.MaterialEditingLibrary.connect_material_property(mat_att, "OpacityMask", unreal.MaterialProperty.MP_OPACITY_MASK)
    #     unreal.MaterialEditingLibrary.connect_material_property(mat_att, "Normal", unreal.MaterialProperty.MP_NORMAL)
    #     unreal.MaterialEditingLibrary.connect_material_property(mat_att, "AmbientOcclusion", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)


    # texture_asset = unreal.load_asset("/Game/StarterContent/Textures/T_Brick_Clay_Beveled_D")
    # node_tex.set_editor_property("texture", texture_asset)
    # 



ut_asset = "/Game/Materials/Landscape/M_Landscape_Master"
a = unreal.EditorAssetLibrary.load_asset(ut_asset)
a2 = unreal.EditorAssetLibrary.duplicate_asset(
            source_asset_path=ut_asset,
            destination_asset_path=f"{ut_asset}2"
        )

blueprint_generated = unreal.EditorAssetLibrary.load_blueprint_class(ut_asset)


import unreal

asset_name = "M_Landscape_Master"
package_path = "/Game/Materials/Landscape"
unreal.EditorAssetLibrary.load_asset(asset_name)


factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Actor)

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# unreal.EditorAssetLibrary.save_loaded_asset(my_new_asset)



 'acquire_editor_element_handle', 'call_method', 'cast', 'checkout_asset', 'checkout_directory', 'checkout_loaded_asset', 'checkout_loaded_assets', 'consolidate_assets', 'delete_asset', 'delete_directory', 'delete_loaded_asset', 'delete_loaded_assets
', 'do_assets_exist', 'does_asset_exist', 'does_directory_exist', 'does_directory_have_assets', 'duplicate_asset', 'duplicate_directory', 'duplicate_loaded_asset', 'find_asset_data', 'find_package_referencers_for_asset', 'get_class', 'get_default_object',
'get_editor_property', 'get_fname', 'get_full_name', 'get_metadata_tag', 'get_metadata_tag_values', 'get_name', 'get_outer', 'get_outermost', 'get_package', 'get_path_name', 'get_path_name_for_loaded_asset', 'get_tag_values', 'get_typed_outer', 
'get_world', 'is_package_external', 'list_asset_by_tag_value', 'list_assets', 'load_asset', 'load_blueprint_class', 'make_directory', 'modify', 'remove_metadata_tag', 'rename', 'rename_asset', 'rename_directory', 'rename_loaded_asset', 
'save_asset', 'save_directory', 'save_loaded_asset', 'save_loaded_assets', 'set_editor_properties', 'set_editor_property', 'set_metadata_tag', 'static_class', 'sync_browser_to_objects']


 'acquire_editor_element_handle'
 'always_evaluate_world_position_offset'
 'automatically_set_usage_in_editor'
 'blend_mode'
 'blendable_location'
 'blendable_output_alpha'
 'blendable_priority'
 'call_method'
 'cast'
 'decal_blend_mode'
 'displacement_scaling'
 'float_precision_mode'
 'forward_blends_sky_light_cubemaps'
 'forward_render_use_preintegrated_gf_for_simple_ibl'
 'fully_rough'
 'get_base_material'
 'get_blend_mode'
 'get_class'
 'get_default_object'
 'get_editor_property'
 'get_fname'
 'get_full_name'
 'get_name'
 'get_nanite_overide_material'
 'get_outer'
 'get_outermost'
 'get_package'
 'get_parameter_info'
 'get_path_name'
 'get_physical_material'
 'get_physical_material_from_map'
 'get_physical_material_mask'
 'get_typed_outer'
 'get_world'
 'is_blendable'
 'is_package_external'
 'material_decal_response'
 'material_domain'
 'max_world_position_offset_displacement'
 'max_world_position_offset_distance'
 'mobile_enable_high_quality_brdf'
 'modify'
 'normal_curvature_to_roughness'
 'parameter_group_data'
 'rename'
 'set_editor_properties'
 'set_editor_property'
 'set_force_mip_levels_to_be_resident'
 'static_class'
 'subsurface_profile'
 'use_alpha_to_coverage'
 'use_emissive_for_dynamic_area_lighting'
 'use_hq_forward_reflections'
 'use_lightmap_directionality'
 'use_planar_forward_reflections'
 'used_with_beam_trails'
 'used_with_clothing'
 'used_with_editor_compositing'
 'used_with_geometry_cache'
 'used_with_geometry_collections'
 'used_with_hair_strands'
 'used_with_heterogeneous_volumes'
 'used_with_instanced_static_meshes'
 'used_with_lidar_point_cloud'
 'used_with_mesh_particles'
 'used_with_morph_targets'
 'used_with_nanite'
 'used_with_niagara_mesh_particles'
 'used_with_niagara_ribbons'
 'used_with_niagara_sprites'
 'used_with_particle_sprites'
 'used_with_skeletal_mesh'
 'used_with_spline_meshes'
 'used_with_static_lighting'
 'used_with_virtual_heightfield_mesh'
 'used_with_volumetric_cloud'
 'used_with_water'