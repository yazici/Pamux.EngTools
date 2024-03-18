# Attempt to write Medieval Game Environment Landscape Materials in some kind of code and use it to generate Shader Graph

# winget install --id GitHub.cli	
# gh auth login

# ~/.gitconfig
# ~/.config/git/config 
# /etc/gitconfig
# git config --system
# git config --list --show-origin
# git config --global user.name "yazici"
# git config --global user.email "yazici.b@gmail.com"


from unreal_materials.nodes.material_expressions.LandscapeLayerWeightParameter import LandscapeLayerWeightParameter

from src.unreal_materials.nodes.material_expressions.StaticBoolParameter import MaterialExpressionStaticBoolParameter
from src.unreal_materials.nodes.material_expressions.ScalarParameter import MaterialExpressionScalarParameter
from unreal_materials.nodes.material_expressions.LandscapeLayerWeightParameter import MaterialExpressionLandscapeLayerWeightParameter



from unreal_materials.nodes.material_expressions.RuntimeVirtualTextureSampleParameter import RuntimeVirtualTextureSampleParameter
from unreal_materials.nodes.material_expressions.RuntimeVirtualTextureSampleParameter import Details

from unreal_materials.nodes.landscape_material_layers import LandscapeMaterialLayers

from unreal_materials.nodes.material_functions.built_ins.LandscapeLayerBlend import LandscapeLayerBlend
from unreal_materials.nodes.material_functions.user_functions.MF_Wetness import MF_Wetness

from unreal_materials.nodes.output.LandscapeGrassOutput import LandscapeGrassOutput
from unreal_materials.nodes.material_expressions.MaterialExpressionParameterBase import MaterialExpressionParameterBase

class LayerParameterGroup:
    def __init__(self, name: str, foliageEnabledDefaultValue: bool = True):
        self.name = name
        self.weight = MaterialExpressionLandscapeLayerWeightParameter(f"{name}")
        self.foliageThreshold = MaterialExpressionScalarParameter(f"{name}FoliageThreshold")
        self.foliageEnabled = MaterialExpressionStaticBoolParameter(f"{name}FoliageEnabled", foliageEnabledDefaultValue)
        
class Parameters:
    

    def __init__(self):
        self.wetness = MaterialExpressionLandscapeLayerWeightParameter("Wetness")

        self.foliageMask = MaterialExpressionLandscapeLayerWeightParameter("FoliageMask")

        self.dirt = LayerParameterGroup("Dirt")
        self.grass = LayerParameterGroup("Grass")
        self.heavyMud = LayerParameterGroup("HeavyMud")
        self.stonyGround = LayerParameterGroup("StonyGround")
        self.fields = LayerParameterGroup("Fields")
        self.forestGrounds = LayerParameterGroup("ForestGrounds")
        self.plowedSoil = LayerParameterGroup("PlowedSoil")

        self.landscapeRVT = RuntimeVirtualTextureSampleParameter(
            "LandscapeRVT",
            Details(
                materialExpression = MaterialExpressionParameterBase.DetailsBase.MaterialExpression(group = "Globals", sortPriority = 32),
                virtualTexture = RuntimeVirtualTextureSampleParameter.Details.VirtualTexture("RVT_Landscape_01", "BaseColor,Normal,Roughness,Specular"),
                textureSample = RuntimeVirtualTextureSampleParameter.Details.TextureSample(mipValueMode = "Default", addressMode = "Clamp")
            ))

params = Parameters()

landscapeLayerBlendResult = LandscapeLayerBlend(LandscapeMaterialLayers.ALL)

wetnessResult = MF_Wetness(landscapeLayerBlendResult, params.wetness)

landscapeGrassOutput = LandscapeGrassOutput()
landscapeGrassOutput.setFoliageMasks(params.foliageMask, [params.dirt, params.grass, params.heavyMud, params.stonyGround, params.fields, params.plowedSoil])


# def M_Landscape_Master():
#     # https://docs.unrealengine.com/5.0/en-US/landscape-material-layer-blending-in-unreal-engine/

#     # The LandscapeLayerBlend node enables you to blend together multiple Textures or Material networks so that they can be used as Landscape layers. 
#     # The LandscapeLayerBlend uses an array to store information about the Landscape layers.


#     # Layer Dirt, Height Dirt, etc.
#     blendedLandscapeLayers = LandscapeLayerBlend([ 
#         MLF_LandscapeLayer("Dirt"),
#         MLF_LandscapeLayer("Grass"),
#         MLF_LandscapeLayer("Mud"),
#         MLF_LandscapeLayer("StonyGround"),
#         MLF_LandscapeLayer("Fields"),
#         MLF_LandscapeLayer("PlowedGround"),
#         MLF_LandscapeLayer("ForestGrounds"),
#         MLF_LandscapeLayer("HeavyMud")]
#         )

    
#     mfWetnessResult = MF_Wetness(blendedLandscapeLayers, params.wetness)

#     mfPuddlesResult = MF_Puddles(mfWetnessResult)

#     wetnessSub = Subtract(wetnessParam, 0.5) 
#     wetnessDiv = Divide(wetnessParam, 0.5) 

#     saturateResult = Saturate(wetnessDiv)


#     mfBlendTwoMaterialsViaHeightOpacityMapResult = MF_BlendTwoMaterialsViaHeightOpacityMap(mfWetnessResult, mfPuddlesResult, saturateResult)

#     getMaterialAttributesResult = GetMaterialAttributes(mfBlendTwoMaterialsViaHeightOpacityMapResult)
#     virtualTextureFeatureSwitchResult = VirtualTextureFeatureSwitch(mfBlendTwoMaterialsViaHeightOpacityMapResult)




