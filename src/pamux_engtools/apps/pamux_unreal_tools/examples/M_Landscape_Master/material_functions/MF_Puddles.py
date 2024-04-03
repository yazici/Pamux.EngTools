import unreal
from pathlib import Path
import sys
import os
import shutil

sys.path.append(str(Path(__file__).parent.parent.parent.parent.parent.resolve()))

from importlib import * 

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)

from pamux_unreal_tools.base.material_function_builder_base import *

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase

from pamux_unreal_tools.examples.M_Landscape_Master.material_functions.base.wetness_base import WetnessBuilderBase
from pamux_unreal_tools.factories.material_expression_factories import *
from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos
class MF_Puddles:
    class Dependencies:
        def __init__(self, builder: ContainerBuilderBase) -> None:
             pass

    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            self.materialAttributes = builder.getMaterialAttributes()
            self.materialAttributes.add_rt()

            self.breakMaterialAttributes = BreakMaterialAttributes(self.materialAttributes)
            self.breakMaterialAttributes.baseColor.add_rt()
            self.breakMaterialAttributes.metallic.add_rt()
            self.breakMaterialAttributes.specular.add_rt()
            self.breakMaterialAttributes.roughness.add_rt()
            self.breakMaterialAttributes.anisotropy.add_rt()
            self.breakMaterialAttributes.emissiveColor.add_rt()
            self.breakMaterialAttributes.opacity.add_rt()
            self.breakMaterialAttributes.opacityMask.add_rt()
            self.breakMaterialAttributes.normal.add_rt()
            self.breakMaterialAttributes.tangent.add_rt()
            self.breakMaterialAttributes.worldPositionOffset.add_rt()
            self.breakMaterialAttributes.subsurfaceColor.add_rt()
            self.breakMaterialAttributes.clearCoat.add_rt()
            self.breakMaterialAttributes.clearCoatRoughness.add_rt()
            self.breakMaterialAttributes.ambientOcclusion.add_rt()
            self.breakMaterialAttributes.refraction.add_rt()
            self.breakMaterialAttributes.customizedUV0.add_rt()
            self.breakMaterialAttributes.customizedUV1.add_rt()
            self.breakMaterialAttributes.customizedUV2.add_rt()
            self.breakMaterialAttributes.customizedUV3.add_rt()
            self.breakMaterialAttributes.customizedUV4.add_rt()
            self.breakMaterialAttributes.customizedUV5.add_rt()
            self.breakMaterialAttributes.customizedUV6.add_rt()
            self.breakMaterialAttributes.customizedUV7.add_rt()
            self.breakMaterialAttributes.pixelDepthOffset.add_rt()
            self.breakMaterialAttributes.shadingModel.add_rt()
            self.breakMaterialAttributes.displacement.add_rt()

            self.puddleColor = VectorParameter("Puddle Color", unreal.LinearColor(0.057292, 0.051375, 0.034017, 1.0))
            self.puddleColor.add_rt()
            self.puddleColor.a.add_rt()
            
            self.puddleHeight = ScalarParameter("Puddle Height", 1.0)
            self.puddleHeight.add_rt()
            
            self.puddleSlope = ScalarParameter("Puddle Slope", 0.25)
            self.puddleSlope.add_rt()
            
            self.puddleDepth = ScalarParameter("Puddle Depth", 0.75)
            self.puddleDepth.add_rt()
            
            self.puddleRoughness = ScalarParameter("Puddle Roughness", 0.15)
            self.puddleRoughness.add_rt()

            self.puddleSpecular = OneMinus(self.puddleRoughness)
            self.puddleSpecular.add_rt()

            self.puddleNormal = Constant3Vector()
            self.puddleNormal.add_rt()
            self.puddleNormal.constant = MaterialExpressionEditorPropertyImpl(self.puddleNormal, 'constant', 'LinearColor') # TODO No Input
            self.puddleNormal.constant.set(unreal.LinearColor(0.0, 0.0, 1.0))

            self.puddleOpacity = Constant(1.0)
            self.puddleOpacity.add_rt()

            self.puddleColorMultiply = Multiply(self.puddleColor.output, self.puddleColor.a)
            self.puddleColorMultiply.add_rt()

    class Outputs(MaterialFunctionOutputs.Result):
        def __init__(self, builder: ContainerBuilderBase):
            super().__init__(builder)
            CurrentNodePos.y += NodePos.DeltaY
            self.puddleMask = builder.makeFunctionOutput("PuddleMask", 1)

    class Builder(WetnessBuilderBase):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_Puddles",
                MaterialFunctionDependenciesBase,
                MF_Puddles.Inputs,
                MF_Puddles.Outputs)

        def build(self):
            lerp = LinearInterpolate(self.inputs.breakMaterialAttributes.baseColor, self.inputs.puddleColorMultiply, self.inputs.puddleDepth)
            lerp.add_rt()

            makeMaterialAttributes = MakeMaterialAttributesFactory.create(self.inputs.breakMaterialAttributes)
            makeMaterialAttributes.add_rt()
            makeMaterialAttributes.baseColor.comesFrom(lerp)
            makeMaterialAttributes.specular.comesFrom(self.inputs.puddleSpecular)
            makeMaterialAttributes.roughness.comesFrom(self.inputs.puddleRoughness)
            makeMaterialAttributes.opacity.comesFrom(self.inputs.puddleOpacity)
            makeMaterialAttributes.normal.comesFrom(self.inputs.puddleNormal)

            componentMask = ComponentMask(self.inputs.breakMaterialAttributes.opacity, "r")

            saturate = Saturate(OneMinus(Saturate(Divide(Subtract(componentMask, self.inputs.puddleHeight), self.inputs.puddleSlope))))

            blendMaterialAttributes = BlendMaterialAttributes(self.inputs.materialAttributes, makeMaterialAttributes, saturate)

            blendMaterialAttributes.connectTo(self.outputs.result)
            saturate.connectTo(self.outputs.puddleMask)

# MF_Puddles.Builder().get()
