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

from unreal_materials.nodes.material_expressions.parameters.LLWeightParameter import LLWeightParameter
from unreal_materials.nodes.material_expressions.parameters.RVTSampleParameter import RVTSampleParameter
from unreal_materials.nodes.material_expressions.parameters.ScalarParameter import ScalarParameter
from unreal_materials.nodes.material_expressions.parameters.StaticBoolParameter import StaticBoolParameter

from unreal_materials.nodes.material_expressions.LandscapeVisibilityMask import LandscapeVisibilityMask
from unreal_materials.nodes.material_expressions.Desaturation import Desaturation

from unreal_materials.nodes.material_functions.built_ins.LandscapeLayerBlend import LandscapeLayerBlend
from unreal_materials.nodes.material_functions.commons.ternary_function_call import Lerp
from unreal_materials.nodes.material_functions.commons.binary_function_call import Subtract
from unreal_materials.nodes.material_functions.commons.binary_function_call import Divide
from unreal_materials.nodes.material_functions.commons.binary_function_call import Multiply
from unreal_materials.nodes.material_functions.commons.unary_function_call import Saturate

from unreal_materials.nodes.material_functions.user_functions.MF_Wetness import MF_Wetness
from unreal_materials.nodes.material_functions.user_functions.MF_Puddles import MF_Puddles
from unreal_materials.nodes.material_functions.user_functions.MF_BlendTwoMaterialsViaHeightOpacityMap import MF_BlendTwoMaterialsViaHeightOpacityMap
from unreal_materials.nodes.material_functions.user_functions.MF_GlancingAngleSpecCorrection import MF_GlancingAngleSpecCorrection
from unreal_materials.nodes.material_functions.user_functions.MF_LandscapeBaseMaterial import MF_LandscapeBaseMaterial

from unreal_materials.nodes.material_functions.built_ins.SCurve import SCurve
from unreal_materials.nodes.material_functions.built_ins.QualitySwitch import QualitySwitch
from unreal_materials.nodes.material_functions.built_ins.GetMaterialAttributes import GetMaterialAttributes
from unreal_materials.nodes.material_functions.built_ins.SetMaterialAttributes import SetMaterialAttributes
from unreal_materials.nodes.material_functions.built_ins.VirtualTextureFeatureSwitch import VirtualTextureFeatureSwitch

from unreal_materials.nodes.output.LandscapeGrassOutput import LandscapeGrassOutput
from unreal_materials.nodes.output.M_Landscape_Master import M_Landscape_Master
from unreal_materials.nodes.output.RVTOutput import RVTOutput
from unreal_materials.nodes.material_expressions.AbsoluteWorldPosition import AbsoluteWorldPosition

from src.unreal_materials.nodes.utils.landscape_material_layers import LandscapeMaterialLayers
from src.unreal_materials.nodes.utils.node_organizer import NodeOrganizer

class LayerSpecificParameters:
    def __init__(self, name: str, foliageEnabledDefaultValue: bool = True):
        self.name = name

        self.weight = LLWeightParameter(f"{name}")
        self.foliageThreshold = ScalarParameter(f"{name}FoliageThreshold")
        self.foliageEnabled = StaticBoolParameter(f"{name}FoliageEnabled", foliageEnabledDefaultValue)
        
class Parameters:
    def __init__(self):
        self.wetness = LLWeightParameter("Wetness")
        self.foliageMask = LLWeightParameter("FoliageMask")

        self.specular = ScalarParameter("Specular")
        self.specular.defaultValue = 0.9

        self.specularContrast = ScalarParameter("SpecularContrast")
        self.specularContrast.defaultValue = 0.15

        self.specularMax = ScalarParameter("SpecularMax")
        self.specularMax.defaultValue = 0.5

        self.dirt = LayerSpecificParameters("Dirt")
        self.grass = LayerSpecificParameters("Grass")
        self.mud = LayerSpecificParameters("Mud")
        self.stonyGround = LayerSpecificParameters("StonyGround")
        self.fields = LayerSpecificParameters("Fields")
        self.plowedGround = LayerSpecificParameters("PlowedGround")
        self.forestGround = LayerSpecificParameters("ForestGround")
        self.heavyMud = LayerSpecificParameters("HeavyMud")

        self.landscapeRVT = RVTSampleParameter("LandscapeRVT")
        self.landscapeRVT.details.virtualTexture.name = "RVT_Landscape_01"
        self.landscapeRVT.details.virtualTexture.content = "BaseColor,Normal,Roughness,Specular"

params = Parameters()

landscapeLayerBlendResult = LandscapeLayerBlend(LandscapeMaterialLayers.ALL)

mfWetnessResult = MF_Wetness(landscapeLayerBlendResult, params.wetness)
mfPuddlesResult = MF_Puddles(mfWetnessResult)


wetnessMinusHalf = Subtract(params.wetness, 0.5) 
wetnessMinusHalfDivHalf = Divide(wetnessMinusHalf, 0.5) 
saturateResult = Saturate(wetnessMinusHalfDivHalf)

mfBlendTwoMaterialsViaHeightOpacityMapResult = MF_BlendTwoMaterialsViaHeightOpacityMap(mfWetnessResult, mfPuddlesResult, saturateResult)

getMaterialAttributesResult = GetMaterialAttributes(mfBlendTwoMaterialsViaHeightOpacityMapResult)
setMaterialAttributesResult = SetMaterialAttributes(params.landscapeRVT)

virtualTextureFeatureSwitchResult = VirtualTextureFeatureSwitch(mfBlendTwoMaterialsViaHeightOpacityMapResult, setMaterialAttributesResult)

glancingAngleSpecCorrectionResult = MF_GlancingAngleSpecCorrection(virtualTextureFeatureSwitchResult)

qualitySwitchResult = QualitySwitch(glancingAngleSpecCorrectionResult, virtualTextureFeatureSwitchResult)

opacityMask = LandscapeVisibilityMask()

setMaterialAttributesResult = SetMaterialAttributes(qualitySwitchResult, opacityMask)

masterMaterialOutput = M_Landscape_Master(setMaterialAttributesResult)

def RVTSpecular(nodeOrganizer: NodeOrganizer):
    sCurveResult = SCurve(getMaterialAttributesResult.baseColor, params.specularContrast)
    desaturationResult = Desaturation(sCurveResult)

    multiplyResult = Multiply(desaturationResult, params.specular)

    return Lerp(0.0, params.specularMax, multiplyResult)

rvtSpecular = RVTSpecular(NodeOrganizer("RVT Specular"))

absoluteWorldPosition = AbsoluteWorldPosition()

masterMaterialOutput = RVTOutput(
    baseColor = getMaterialAttributesResult.baseColor,
    specular = rvtSpecular.result,
    roughness = getMaterialAttributesResult.roughness,
    normal = getMaterialAttributesResult.normal,
    worldHeight = absoluteWorldPosition.z)



landscapeGrassOutput = LandscapeGrassOutput()
landscapeGrassOutput.setFoliageMasks(params.foliageMask, [params.dirt, params.grass, params.heavyMud, params.stonyGround, params.fields, params.plowedSoil])

landscapeGrassOutputAndMasking = NodeOrganizer("LandscapeGrassOutput and Masking")




