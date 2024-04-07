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
from pamux_unreal_tools.factories.material_expression_factories import MakeMaterialAttributesFactory

from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MLF_LayerX import MLF_LayerX
from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.MLF_ForestGround import MLF_ForestGround
from pamux_unreal_tools.base.material_function.material_function_base import MaterialFunctionBase

        
# https://github.com/SomeRanDev/Haxe-UnrealEngine5/blob/d17e0b1f9d8973ed0641484148c55d552ba69dff/Externs/generated_5_0_3/MaterialExpressionLinearInterpolate.hx#L4
class M_Landscape_Master:

    class Inputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            self.wetness = LandscapeLayerWeight("Wetness", 0.0)
            self.wetness.add_rt()

            self.landscapeRVT = RuntimeVirtualTextureSampleParameter("LandscapeRVT")
            self.landscapeRVT.virtual_texture.set(unreal.load_asset("/Script/Engine.RuntimeVirtualTexture'/Game/Materials/Landscape/RVT/RVT_Landscape_01.RVT_Landscape_01'"))

    class Outputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            pass
             
    class Dependencies:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            self.SCurve = builder.load_SCurve()

            self.MF_TextureCellBombing_Landscape = MF_TextureCellBombing_Landscape.load_MF(builder)

            #self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial.load_MF(builder)
            self.MF_LandscapeBaseMaterial = MF_LandscapeBaseMaterial.Builder().get() # load_MF(builder)

            self.MF_Wetness = MF_Wetness.load_MF(builder)
            self.MF_Puddles = MF_Puddles.load_MF(builder)
            self.MF_BlendTwoMaterialsViaHighOpacityMap = MF_BlendTwoMaterialsViaHighOpacityMap.load_MF(builder)
            self.MF_GlancingAngleSpecCorrection = MF_GlancingAngleSpecCorrection.load_MF(builder)

            self.MF_FoliageMask = MF_FoliageMask.Builder().get() # load_MF(builder)

            self.MLF_Layers = {}
            for layer_name in Globals.layer_names:
                if layer_name == "ForestGround":
                    self.MLF_Layers[layer_name] = MLF_ForestGround.Builder().get()
                else:
                    self.MLF_Layers[layer_name] = MLF_LayerX.Builder(layer_name).get()

            
    class Builder(MaterialBuilder):
        def __init__(self, asset_path: str):
            super().__init__(
                asset_path,
                M_Landscape_Master.Dependencies,
                M_Landscape_Master.Inputs,
                M_Landscape_Master.Outputs)

        def __buildMainPath(self, blendCall):
            makeMaterialAttributes = MakeMaterialAttributes()
            makeMaterialAttributes.input.comesFrom(self.inputs.landscapeRVT)

            virtualTextureFeatureSwitch = VirtualTextureFeatureSwitch()
            virtualTextureFeatureSwitch.no.comesFrom(blendCall)
            virtualTextureFeatureSwitch.yes.comesFrom(makeMaterialAttributes)

            glancingAngleSpecCorrectionCall = self.dependencies.MF_GlancingAngleSpecCorrection.call()
            glancingAngleSpecCorrectionCall.inputs.materialAttributes.comesFrom(virtualTextureFeatureSwitch.output)

            qualitySwitch = QualitySwitch()
            qualitySwitch.default.comesFrom(glancingAngleSpecCorrectionCall.outputs.result)
            qualitySwitch.low.comesFrom(virtualTextureFeatureSwitch)

            breakMaterialAttributes = BreakMaterialAttributes()
            breakMaterialAttributes.materialAttributes.comesFrom(qualitySwitch)

            result = MakeMaterialAttributesFactory.create(breakMaterialAttributes)
            #result.opacityMask.comesFrom(self.params.LandscapeVisibilityMask)

            return result

        def __rvtSpecular(self, baseColor):
            sCurveCall = self.dependencies.SCurve.call()
            # sCurveCall._in.comesFrom(baseColor)
            # sCurveCall.power.comesFrom(Params.specularContrast)

            desaturation = Desaturation()
            desaturation.input.comesFrom(sCurveCall.outputs.result)

            multiply = Multiply()
            multiply.a.comesFrom(desaturation.output)
            # multiply.b.comesFrom(Params.specular)

            lerp = LinearInterpolate()
            lerp.const_a.set(0.0)
            # lerp.b.comesFrom(Params.specularMax)
            lerp.alpha.comesFrom(multiply.output)

            return lerp.output

        def __rvtOutput(self, baseColor, rvtSpecular, roughness, normal, worldHeight):
             return
        
        def __buildRVTOutputPath(self, blendCall):
            breakMaterialAttributes = BreakMaterialAttributes()
            breakMaterialAttributes.input.comesFrom(blendCall)

            rvtSpecular = self.__rvtSpecular(breakMaterialAttributes.baseColor)

            return self.__rvtOutput(
                 breakMaterialAttributes.baseColor, 
                 rvtSpecular,
                 breakMaterialAttributes.roughness, 
                 breakMaterialAttributes.normal, None)
                 ##WorldPosition().z) # AbsoluteWorldPosition?

        def __buildLandscapeGrassOutputAndMaskingPath(self, blendCall):
                #landscapeGrassOutput = Blocks.landscapeGrassOutputAndMasking(Params.foliageMask, Globals.LayersForGrass)
                pass

        def __blendLandscapeLayers(self):
            landscapeLayerBlend = LandscapeLayerBlend()

            layers = unreal.Array(unreal.LayerBlendInput)

            landscapeLayerBlend.inputs = MaterialFunctionBase.Inputs()
            landscapeLayerBlend.inputs.layers = {}

            for layer_name in Globals.layer_names:
                layer = unreal.LayerBlendInput()

                layer.set_editor_property("blend_type", unreal.LandscapeLayerBlendType.LB_HEIGHT_BLEND)
                layer.set_editor_property("layer_name", layer_name)
                layer.set_editor_property("preview_weight", 0.0)
                layers.append(layer)

            landscapeLayerBlend.layers.set(layers)

            for layer_name in Globals.layer_names:
                call = self.dependencies.MLF_Layers[layer_name].call()

                call.outputs.result.connectTo(InSocketImpl(landscapeLayerBlend, f"Layer {layer_name}", 'StructProperty'))
                call.outputs.height.connectTo(InSocketImpl(landscapeLayerBlend, f"Height {layer_name}", 'StructProperty'))

            landscapeLayerBlend.add_rt()
            return landscapeLayerBlend

        def build(self):
            landscapeLayerBlend = self.__blendLandscapeLayers()

            wetnessCall = self.dependencies.MF_Wetness.call()
            wetnessCall.outputs.result.add_rt()
            wetnessCall.inputs.materialAttributes.comesFrom(landscapeLayerBlend)
            wetnessCall.inputs.wetness.comesFrom(self.inputs.wetness)

            puddlesCall = self.dependencies.MF_Puddles.call()
            puddlesCall.outputs.result.add_rt()
            puddlesCall.inputs.materialAttributes.comesFrom(wetnessCall.outputs.result)

            saturatedWetmess = Saturate(Divide(Subtract(self.inputs.wetness, 0.5), 0.5))

            blendCall = self.dependencies.MF_BlendTwoMaterialsViaHighOpacityMap.call()

            blendCall.inputs.materialA.comesFrom(wetnessCall.outputs.result)
            blendCall.inputs.materialB.comesFrom(puddlesCall.outputs.result)
            blendCall.inputs.alpha.comesFrom(saturatedWetmess)

            self.__buildMainPath(blendCall)
            self.__buildRVTOutputPath(blendCall)
            self.__buildLandscapeGrassOutputAndMaskingPath(blendCall)

if __name__=="__main__":
    M_Landscape_Master.Builder("/Game/Materials/Pamux/M_Landscape_Master").get()
