
# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/examples/M_Landscape_Master/M_Landscape_Master.py"

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent.parent.resolve()))

from pamux_unreal_tools.material import Material

from pamux_unreal_tools.material_script_helpers import *
from pamux_unreal_tools.examples.M_Landscape_Master.params import *
from pamux_unreal_tools.examples.M_Landscape_Master.globals import *
from pamux_unreal_tools.material_expressions.material_expression_wrappers import *

# from pamux_unreal_tools.material_expression_container import *


from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_LandscapeBaseMaterial import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_Wetness import *
# from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_Puddles import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MLF_LayerX import *
# from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_BlendTwoMaterialsViaHighOpacityMap import *
# from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_GlancingAngleSpecCorrection import *


# https://github.com/SomeRanDev/Haxe-UnrealEngine5/blob/d17e0b1f9d8973ed0641484148c55d552ba69dff/Externs/generated_5_0_3/MaterialExpressionLinearInterpolate.hx#L4
class M_Landscape_Master:
    class Builder:
        def __init__(self, material):
            self.material = material
            self.params = Params(self.material)

        # def __buildMainPath(self, MF_BlendTwoMaterialsViaHighOpacityMap_Output):
        #     setMaterialAttributes = SetMaterialAttributes(self.material)
        #     setMaterialAttributes.input.comesFrom(self.params.LandscapeRVT)

        #     virtualTextureFeatureSwitch = VirtualTextureFeatureSwitch(self.material)
        #     virtualTextureFeatureSwitch.in1.comesFrom(MF_BlendTwoMaterialsViaHighOpacityMap_Output)
        #     virtualTextureFeatureSwitch.in2.comesFrom(setMaterialAttributes)

        #     call_MF_GlancingAngleSpecCorrection = callMaterialFunction(self.material, MF_GlancingAngleSpecCorrection.Builder().get())
        #     call_MF_GlancingAngleSpecCorrection.in1.comesFrom(virtualTextureFeatureSwitch.output)

        #     qualitySwitch = QualitySwitch(self.material)
        #     qualitySwitch.in1.comesFrom(call_MF_GlancingAngleSpecCorrection.output)
        #     qualitySwitch.in2.comesFrom(virtualTextureFeatureSwitch.output)

        #     setMaterialAttributes = SetMaterialAttributes(self.material)
        #     setMaterialAttributes.in1.comesFrom(qualitySwitch.output)
        #     setMaterialAttributes.in2.comesFrom(self.params.LandscapeVisibilityMask)

        # def __rvtSpecular(self, baseColor):
        #     sCurve = MaterialFunction.load("SCurve", "/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment", True)
        #     call_SCurve = callMaterialFunction(self.material, sCurve)
        #     call_SCurve.In.comesFrom(baseColor)
        #     call_SCurve.Power.comesFrom(Params.specularContrast)

        #     # SCurve(In: Vector3, Power:Scalar)


        #     desaturation = Desaturation(self.material)
        #     desaturation.input.comesFrom(sCurve.Result)

        #     multiply = Multiply(self.material)
        #     multiply.a.comesFrom(desaturation.output)
        #     multiply.b.comesFrom(Params.specular)

        #     lerp = LinearInterpolate(self.material)
        #     lerp.const_a.set(0.0)
        #     lerp.b.comesFrom(Params.specularMax)
        #     lerp.alpha.comesFrom(multiply.output)

        #     return lerp.output

        # def __rvtOutput(self, baseColor, rvtSpecular, roughness, normal, worldHeight):
        #      return
        
        # def __buildRVTOutputPath(self, MF_BlendTwoMaterialsViaHighOpacityMap_Output):
        #     getMaterialAttributes = GetMaterialAttributes(self.material)
        #     getMaterialAttributes.in1.comesFrom(MF_BlendTwoMaterialsViaHighOpacityMap_Output)

        #     rvtSpecular = self.__rvtSpecular(getMaterialAttributes.baseColor)

        #     return self.__rvtOutput(
        #          getMaterialAttributes.baseColor, 
        #          rvtSpecular,
        #          getMaterialAttributes.roughness, 
        #          getMaterialAttributes.normal, 
        #          WorldPosition(self.material).z) # AbsoluteWorldPosition?

        # def __buildLandscapeGrassOutputAndMaskingPath(self, MF_BlendTwoMaterialsViaHighOpacityMap_Output):
        #         #landscapeGrassOutput = Blocks.landscapeGrassOutputAndMasking(Params.foliageMask, Globals.LayersForGrass)
        #         pass

        def __blendLandscapeLayers(self, layer_names):
            landscapeLayerBlend = LandscapeLayerBlend(self.material)

            layers = unreal.Array(unreal.LayerBlendInput)
            mfLandscapeBaseMaterial = MF_LandscapeBaseMaterial.Builder().get()

            for layer_name in layer_names:
                layer = unreal.LayerBlendInput()
                
                layer.set_editor_property("blend_type", unreal.LandscapeLayerBlendType.LB_HEIGHT_BLEND)
                layer.set_editor_property("layer_name", layer_name)
                layer.set_editor_property("preview_weight", 0.0)
                layers.append(layer)

            landscapeLayerBlend.layers.set(layers)

            for layer_name in layer_names:
                mlfLayerX = MLF_LayerX.Builder(layer_name, mfLandscapeBaseMaterial).get()
                
                call_MLF_LayerX = callMaterialFunction(self.material, mlfLayerX)

                MEL.connect_material_expressions(call_MLF_LayerX.asset, "Result", landscapeLayerBlend.asset, f"Layer {layer_name}")
                MEL.connect_material_expressions(call_MLF_LayerX.asset, "Height", landscapeLayerBlend.asset, f"Height {layer_name}")

            return landscapeLayerBlend.output
        
        def build(self):
            blendedLandscapeLayers = self.__blendLandscapeLayers(Globals.Layers)

            call_MF_Wetness = callMaterialFunction(self.material, MF_Wetness.Builder().get())
            call_MF_Wetness.input.comesFrom(blendedLandscapeLayers)

            return call_MF_Wetness.output

            call_MF_Puddles = callMaterialFunction(self.material, MF_Puddles.Builder().get())
            call_MF_Puddles.input.comesFrom(call_MF_Wetness.output)

            subtractHalf = Subtract(self.material)
            subtractHalf.a.comesFrom(self.params.Wetness.output)
            subtractHalf.constB = 0.5

            divideHalf = Divide(self.material)
            divideHalf.a.comesFrom(subtractHalf.output)
            divideHalf.constB = 0.5

            saturatedWetmess = Saturate(self.material)
            saturatedWetmess.input.comesFrom(divideHalf.output)

            # saturatedWetmess = Chain(self.material, Saturate(Divide(Subtract(self.params.Wetness.output, 0.5), 0.5))

            call_MF_BlendTwoMaterialsViaHighOpacityMap = callMaterialFunction(self.material, MF_BlendTwoMaterialsViaHighOpacityMap.Builder.get())
            call_MF_BlendTwoMaterialsViaHighOpacityMap.in1.comesFrom(call_MF_Wetness.output)
            call_MF_BlendTwoMaterialsViaHighOpacityMap.in2.comesFrom(call_MF_Puddles.output)
            call_MF_BlendTwoMaterialsViaHighOpacityMap.in3.comesFrom(saturatedWetmess.output)

            self.__buildMainPath(call_MF_BlendTwoMaterialsViaHighOpacityMap.output)
            self.__buildRVTOutputPath(call_MF_BlendTwoMaterialsViaHighOpacityMap.output)
            self.__buildLandscapeGrassOutputAndMaskingPath(call_MF_BlendTwoMaterialsViaHighOpacityMap.output)


material = Material.loadOrCreate("M_Landscape_Master", "/Game/Materials/Pamux", True)

#sCurve = MaterialFunction.load("SCurve", "/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment", True)
#call_SCurve = callMaterialFunction(material, sCurve)
#call_SCurve.In.comesFrom(baseColor)
#call_SCurve.Power.comesFrom(Params.specularContrast)

material_builder = M_Landscape_Master.Builder(material).build()

material.save()