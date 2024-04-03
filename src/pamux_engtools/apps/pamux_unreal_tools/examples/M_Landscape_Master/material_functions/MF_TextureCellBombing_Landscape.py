from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent.parent.parent.resolve()))

from importlib import * 

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)


from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_function_builder_base import MaterialFunctionBuilderBase
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase

from pamux_unreal_tools.base.material_function_outputs_base import MaterialFunctionOutputs

class MF_TextureCellBombing_Landscape:
    class Dependencies:
        def __init__(self, builder: ContainerBuilderBase) -> None:
            self.rotateAboutWorldAxis_cheap = builder.load_MF(
                "/Engine/Functions/Engine_MaterialFunctions02/WorldPositionOffset/RotateAboutWorldAxis_cheap",
                [ "Rotation Amount", "PivotPoint", "WorldPosition" ], [ "X-Axis", "Y-Axis", "Z-Axis" ])


    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            self.patternScale = builder.build_FunctionInput("PatternScale", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(10.0))
            self.patternScale.add_rt()

            self.UVs = builder.build_FunctionInput("UVs", unreal.FunctionInputType.FUNCTION_INPUT_VECTOR2, TextureCoordinate(1.0, 1.0))
            self.UVs.add_rt()

            self.randomOffsetVariation = builder.build_FunctionInput("RandomOffsetVariation", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(1.0))
            self.randomOffsetVariation.add_rt()

            self.randomRotationVariation = builder.build_FunctionInput("RandomRotationVariation", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(1.0))
            self.randomRotationVariation.add_rt()

            self.cellScale = builder.build_FunctionInput("CellScale", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(2.0))
            self.cellScale.add_rt()

            self.doRotationVariation = builder.build_FunctionInput("DoRotationVariation", unreal.FunctionInputType.FUNCTION_INPUT_STATIC_BOOL, StaticBool(False))
            self.doRotationVariation.add_rt()

            self.isNormalMap = builder.build_FunctionInput("IsNormalMap", unreal.FunctionInputType.FUNCTION_INPUT_STATIC_BOOL, StaticBool(False))
            self.isNormalMap.add_rt()

            self.texture = builder.build_FunctionInput("Texture", unreal.FunctionInputType.FUNCTION_INPUT_TEXTURE2D, TextureObject(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR, None))
            self.texture.add_rt()
            self.texture.use_preview_value_as_default.set(False)

            self.UVs3Vector = AppendVector(self.UVs, Constant(0.0))
            self.UVs3Vector.add_rt()

            self.patternScaledUVs3Vector = Multiply(self.UVs3Vector, self.patternScale)
            self.patternScaledUVs3Vector.add_rt()

            self.patternScaledUVs3VectorRG = ComponentMask(self.patternScaledUVs3Vector, "RG")
            self.patternScaledUVs3VectorRG.add_rt()

            self.cellScaledUVs3Vector = Multiply(self.UVs3Vector, self.cellScale)
            self.cellScaledUVs3Vector.add_rt()

            self.cellScaledUVs3VectorRG = ComponentMask(self.cellScaledUVs3Vector, "RG")
            self.cellScaledUVs3VectorRG.add_rt()

            self.patternScaledInputTexture = TextureSample()
            self.patternScaledInputTexture.RGB.add_rt()
            self.patternScaledInputTexture.UVs.comesFrom(self.patternScaledUVs3VectorRG)
            self.patternScaledInputTexture.tex.comesFrom(self.texture)
            self.patternScaledInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.patternScaledInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)

    # [ "Texture", "UVs", "CellScale", "PatternScale", "DoRotationVariation", "RandomOffsetVariation", "RandomRotationVariation", "IsNormalMap" ], [ "Result" ]
    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_TextureCellBombing_Landscape",
                MF_TextureCellBombing_Landscape.Dependencies,
                MF_TextureCellBombing_Landscape.Inputs,
                MaterialFunctionOutputs.Result)

        def build(self):
            textureSample = TextureSample()
            textureSample.RGB.add_rt()
            textureSample.r.add_rt()
            textureSample.a.add_rt()
            textureSample.UVs.comesFrom(self.inputs.cellScaledUVs3VectorRG)
            textureSample.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            textureSample.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
            textureSample.texture.set(unreal.load_asset("/Script/Engine.Texture2D'/Game/Materials/Functions/TextureCellBombing/T_Voronoi_Perturbed_4k.T_Voronoi_Perturbed_4k'"))

            offsetVariation = Multiply(self.inputs.randomOffsetVariation, textureSample.RGB)
            rotationVariation = Multiply(textureSample.r, self.inputs.randomRotationVariation)
            negativeRotationVariation = Multiply(rotationVariation, -1.0)

            pivotPoint1 = Constant3Vector(None)
            pivotPoint1.add_rt()

            worldPosition = Add(self.inputs.patternScaledUVs3Vector, offsetVariation)

            rotateAboutWorldAxis_cheap_result1 = self.dependencies.rotateAboutWorldAxis_cheap.call()
            rotateAboutWorldAxis_cheap_result1.rotationAmount.comesFrom(rotationVariation)
            rotateAboutWorldAxis_cheap_result1.pivotPoint.comesFrom(pivotPoint1)
            rotateAboutWorldAxis_cheap_result1.worldPosition.comesFrom(worldPosition)

            switch = StaticSwitch(Add(rotateAboutWorldAxis_cheap_result1.zAxis, worldPosition), worldPosition, self.inputs.doRotationVariation)

            randomRotateRG = ComponentMask(switch, "RG")

            pivotPoint2 = Constant3Vector(None)
            pivotPoint2.add_rt()

            rotatedInputTexture = TextureSample()
            rotatedInputTexture.RGB.add_rt()
            rotatedInputTexture.UVs.comesFrom(randomRotateRG)
            rotatedInputTexture.tex.comesFrom(self.inputs.texture)
            rotatedInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            rotatedInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)

            rotateAboutWorldAxis_cheap_result2 = self.dependencies.rotateAboutWorldAxis_cheap.call()
            rotateAboutWorldAxis_cheap_result2.rotationAmount.comesFrom(negativeRotationVariation)
            rotateAboutWorldAxis_cheap_result2.pivotPoint.comesFrom(pivotPoint2)
            rotateAboutWorldAxis_cheap_result2.worldPosition.comesFrom(rotatedInputTexture)

            normalRotation = Add(rotateAboutWorldAxis_cheap_result2.zAxis, rotatedInputTexture)

            switch1 = StaticSwitch(normalRotation, rotatedInputTexture, self.inputs.isNormalMap)
            switch2 = StaticSwitch(switch1, rotatedInputTexture, self.inputs.doRotationVariation)

            lerp = LinearInterpolate(self.inputs.patternScaledInputTexture.RGB, switch2, textureSample.a)
            lerp.connectTo(self.outputs.result)

MF_TextureCellBombing_Landscape.Builder().get()
