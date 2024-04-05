import unreal
MEL = unreal.MaterialEditingLibrary

from pathlib import Path
import sys
from importlib import * 

sys.path.append(str(Path(__file__).parent.parent.parent.parent.resolve()))

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.builders.material_builder import MaterialBuilder
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase

from pamux_unreal_tools.examples.M_Landscape_Master.params import *
from pamux_unreal_tools.examples.M_Landscape_Master.globals import *

from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_LandscapeBaseMaterial import MF_LandscapeBaseMaterial
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_Wetness import MF_Wetness
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_Puddles import MF_Puddles
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_BlendTwoMaterialsViaHighOpacityMap import MF_BlendTwoMaterialsViaHighOpacityMap
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_GlancingAngleSpecCorrection import MF_GlancingAngleSpecCorrection
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_TextureCellBombing_Landscape import MF_TextureCellBombing_Landscape
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MF_FoliageMask import MF_FoliageMask

from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MLF_LayerX import MLF_LayerX
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MLF_ForestGround import MLF_ForestGround

# https://github.com/SomeRanDev/Haxe-UnrealEngine5/blob/d17e0b1f9d8973ed0641484148c55d552ba69dff/Externs/generated_5_0_3/MaterialExpressionLinearInterpolate.hx#L4
class M_Landscape_Master:

    class Inputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            pass

    class Outputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            pass
             
    class Dependencies:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            # self.SCurve = builder.load_MF("/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment/SCurve", [ "In", "Power" ], [ "Result" ])

            self.MF_TextureCellBombing_Landscape = MF_TextureCellBombing_Landscape.Builder().get()

            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial.Builder().get()

            self.MF_Wetness = MF_Wetness.Builder().get()
            self.MF_Puddles = MF_Puddles.Builder().get()
            self.MF_BlendTwoMaterialsViaHighOpacityMap = MF_BlendTwoMaterialsViaHighOpacityMap.Builder().get()
            self.MF_GlancingAngleSpecCorrection = MF_GlancingAngleSpecCorrection.Builder().get()

            self.MF_FoliageMask = MF_FoliageMask.Builder().get()

            self.MLF_ForestGround = MLF_ForestGround.Builder(self.MF_LandscapeBaseMaterial).get()

            self.MLF_Layers = {}
            for layer_name in Globals.layer_names:
                if layer_name != "ForestGround":
                    self.MLF_Layers[layer_name] = MLF_LayerX.Builder(layer_name, self.MF_LandscapeBaseMaterial).get()

            
    class Builder(MaterialBuilder):
        def __init__(self, asset_path: str):
            super().__init__(
                asset_path,
                M_Landscape_Master.Dependencies,
                M_Landscape_Master.Inputs,
                M_Landscape_Master.Outputs)

        # def __buildMainPath(self, MF_BlendTwoMaterialsViaHighOpacityMap_Output):
        #     makeMaterialAttributes = MakeMaterialAttributes(self.material)
        #     makeMaterialAttributes.input.comesFrom(self.params.LandscapeRVT)

        #     virtualTextureFeatureSwitch = VirtualTextureFeatureSwitch(self.material)
        #     virtualTextureFeatureSwitch.in1.comesFrom(MF_BlendTwoMaterialsViaHighOpacityMap_Output)
        #     virtualTextureFeatureSwitch.in2.comesFrom(makeMaterialAttributes)

        #     self.MF_GlancingAngleSpecCorrection.call()
        #     self.MF_GlancingAngleSpecCorrection.call_result.in1.comesFrom(virtualTextureFeatureSwitch.output)

        #     qualitySwitch = QualitySwitch(self.material)
        #     qualitySwitch.in1.comesFrom(call_MF_GlancingAngleSpecCorrection.output)
        #     qualitySwitch.in2.comesFrom(virtualTextureFeatureSwitch.output)

        #     makeMaterialAttributes = MakeMaterialAttributes(self.material)
        #     makeMaterialAttributes.in1.comesFrom(qualitySwitch.output)
        #     makeMaterialAttributes.in2.comesFrom(self.params.LandscapeVisibilityMask)

        # def __rvtSpecular(self, baseColor):
        #     sCurve = MaterialFunctionFactory().load("SCurve", "/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment", True)
        #     call_SCurve = sCurve.call()
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
                call_MLF_LayerX = self.MLF_Layers[layer_name].call()

                MEL.connect_material_expressions(call_MLF_LayerX.unrealAsset, "Result", landscapeLayerBlend.unrealAsset, f"Layer {layer_name}")
                MEL.connect_material_expressions(call_MLF_LayerX.unrealAsset, "Height", landscapeLayerBlend.unrealAsset, f"Height {layer_name}")

            return landscapeLayerBlend.output

        def build(self):
            return
            # blendedLandscapeLayers = self.__blendLandscapeLayers()

            # call_MF_Wetness = self.MF_Wetness.call()
            # call_MF_Wetness.input.comesFrom(blendedLandscapeLayers)

            # return call_MF_Wetness.output

            # call_MF_Puddles = self.MF_Puddles.call()
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

#
#call_SCurve = sCurve.call()
#call_SCurve.In.comesFrom(baseColor)
#call_SCurve.Power.comesFrom(Params.specularContrast)

if __name__=="__main__":
    M_Landscape_Master.Builder("/Game/Materials/Pamux/M_Landscape_Master").get(purge=True)
