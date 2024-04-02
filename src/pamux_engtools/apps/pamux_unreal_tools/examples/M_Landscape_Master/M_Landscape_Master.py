# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/examples/M_Landscape_Master/M_Landscape_Master.py"
from pathlib import Path
import sys
import os
import shutil

sys.path.append(str(Path(__file__).parent.parent.parent.parent.resolve()))

from importlib import * 

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_builder_base import MaterialBuilderBase

from pamux_unreal_tools.examples.M_Landscape_Master.params import *
from pamux_unreal_tools.examples.M_Landscape_Master.globals import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_LandscapeBaseMaterial import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_Wetness import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_Puddles import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MLF_LayerX import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_BlendTwoMaterialsViaHighOpacityMap import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_GlancingAngleSpecCorrection import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_TextureCellBombing_Landscape import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MLF_ForestGround import *
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_FoliageMask import *

# https://github.com/SomeRanDev/Haxe-UnrealEngine5/blob/d17e0b1f9d8973ed0641484148c55d552ba69dff/Externs/generated_5_0_3/MaterialExpressionLinearInterpolate.hx#L4
class M_Landscape_Master:
    class Builder(MaterialBuilderBase):
        def __init__(self, asset_path: str):
            super().__init__(Params, asset_path)

        # def __buildMainPath(self, MF_BlendTwoMaterialsViaHighOpacityMap_Output):
        #     makeMaterialAttributes = MakeMaterialAttributes(self.material)
        #     makeMaterialAttributes.input.comesFrom(self.params.LandscapeRVT)

        #     virtualTextureFeatureSwitch = VirtualTextureFeatureSwitch(self.material)
        #     virtualTextureFeatureSwitch.in1.comesFrom(MF_BlendTwoMaterialsViaHighOpacityMap_Output)
        #     virtualTextureFeatureSwitch.in2.comesFrom(makeMaterialAttributes)

        #     call_MF_GlancingAngleSpecCorrection = self.MF_GlancingAngleSpecCorrection.call(self)
        #     call_MF_GlancingAngleSpecCorrection.in1.comesFrom(virtualTextureFeatureSwitch.output)

        #     qualitySwitch = QualitySwitch(self.material)
        #     qualitySwitch.in1.comesFrom(call_MF_GlancingAngleSpecCorrection.output)
        #     qualitySwitch.in2.comesFrom(virtualTextureFeatureSwitch.output)

        #     makeMaterialAttributes = MakeMaterialAttributes(self.material)
        #     makeMaterialAttributes.in1.comesFrom(qualitySwitch.output)
        #     makeMaterialAttributes.in2.comesFrom(self.params.LandscapeVisibilityMask)

        # def __rvtSpecular(self, baseColor):
        #     sCurve = MaterialFunctionFactory().load("SCurve", "/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment", True)
        #     call_SCurve = sCurve.call(self)
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
        #     breakMaterialAttributes = BreakMaterialAttributes(self.material)
        #     breakMaterialAttributes.input.comesFrom(MF_BlendTwoMaterialsViaHighOpacityMap_Output)

        #     rvtSpecular = self.__rvtSpecular(breakMaterialAttributes.baseColor)

        #     return self.__rvtOutput(
        #          breakMaterialAttributes.baseColor, 
        #          rvtSpecular,
        #          breakMaterialAttributes.roughness, 
        #          breakMaterialAttributes.normal, 
        #          WorldPosition(self.material).z) # AbsoluteWorldPosition?

        # def __buildLandscapeGrassOutputAndMaskingPath(self, MF_BlendTwoMaterialsViaHighOpacityMap_Output):
        #         #landscapeGrassOutput = Blocks.landscapeGrassOutputAndMasking(Params.foliageMask, Globals.LayersForGrass)
        #         pass
            
        def build_dependencies(self):
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial.Builder().get()

            self.MLF_Layers = {}
            for layer_name in Globals.layer_names:
                if layer_name == "ForestGround":
                    self.MLF_ForestGround = MLF_ForestGround.Builder(self.MF_LandscapeBaseMaterial).get()
                else:
                    self.MLF_Layers[layer_name] = MLF_LayerX.Builder(layer_name, self.MF_LandscapeBaseMaterial).get()

            self.MF_Wetness = MF_Wetness.Builder().get()
            self.MF_Puddles = MF_Puddles.Builder().get()
            self.MF_BlendTwoMaterialsViaHighOpacityMap = MF_BlendTwoMaterialsViaHighOpacityMap.Builder().get()
            self.MF_GlancingAngleSpecCorrection = MF_GlancingAngleSpecCorrection.Builder().get()

            self.MF_FoliageMask = MF_FoliageMask.Builder().get()
            self.MF_TextureCellBombing_Landscape = MF_TextureCellBombing_Landscape.Builder().get()
            

        def __blendLandscapeLayers(self):
            landscapeLayerBlend = LandscapeLayerBlend(self.material)

            layers = unreal.Array(unreal.LayerBlendInput)
            

            for layer_name in Globals.layer_names:
                layer = unreal.LayerBlendInput()
                
                layer.set_editor_property("blend_type", unreal.LandscapeLayerBlendType.LB_HEIGHT_BLEND)
                layer.set_editor_property("layer_name", layer_name)
                layer.set_editor_property("preview_weight", 0.0)
                layers.append(layer)

            landscapeLayerBlend.layers.set(layers)

            for layer_name in Globals.layer_names:
                call_MLF_LayerX = self.MLF_Layers[layer_name].call(self)

                MEL.connect_material_expressions(call_MLF_LayerX.asset, "Result", landscapeLayerBlend.asset, f"Layer {layer_name}")
                MEL.connect_material_expressions(call_MLF_LayerX.asset, "Height", landscapeLayerBlend.asset, f"Height {layer_name}")

            return landscapeLayerBlend.output

        def build_process_nodes(self):
            pass
            # blendedLandscapeLayers = self.__blendLandscapeLayers()

            # call_MF_Wetness = self.MF_Wetness.call(self)
            # call_MF_Wetness.input.comesFrom(blendedLandscapeLayers)

            # return call_MF_Wetness.output

            # call_MF_Puddles = self.MF_Puddles.call(self)
            # call_MF_Puddles.input.comesFrom(call_MF_Wetness.output)

            # subtractHalf = Subtract(self.material)
            # subtractHalf.a.comesFrom(self.params.Wetness.output)
            # subtractHalf.constB = 0.5

            # divideHalf = Divide(self.material)
            # divideHalf.a.comesFrom(subtractHalf.output)
            # divideHalf.constB = 0.5

            # saturatedWetmess = Saturate(self.material)
            # saturatedWetmess.input.comesFrom(divideHalf.output)

            # # saturatedWetmess = Chain(self.material, Saturate(Divide(Subtract(self.params.Wetness.output, 0.5), 0.5))

            # call_MF_BlendTwoMaterialsViaHighOpacityMap = self.MF_BlendTwoMaterialsViaHighOpacityMap(self)
            # call_MF_BlendTwoMaterialsViaHighOpacityMap.in1.comesFrom(call_MF_Wetness.output)
            # call_MF_BlendTwoMaterialsViaHighOpacityMap.in2.comesFrom(call_MF_Puddles.output)
            # call_MF_BlendTwoMaterialsViaHighOpacityMap.in3.comesFrom(saturatedWetmess.output)

            # self.__buildMainPath(call_MF_BlendTwoMaterialsViaHighOpacityMap.output)
            # self.__buildRVTOutputPath(call_MF_BlendTwoMaterialsViaHighOpacityMap.output)
            # self.__buildLandscapeGrassOutputAndMaskingPath(call_MF_BlendTwoMaterialsViaHighOpacityMap.output)

            
            return




#sCurve = MaterialFunctionFactory().load("SCurve", "/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment", True)
#call_SCurve = sCurve.call()
#call_SCurve.In.comesFrom(baseColor)
#call_SCurve.Power.comesFrom(Params.specularContrast)

folder = "C:/src/Unreal Projects/PamuxSurvival/Content/Materials/Pamux"
if os.path.isdir(folder):
    shutil.rmtree(folder)

material = M_Landscape_Master.Builder("M_Landscape_Master", "/Game/Materials/Pamux").get()
