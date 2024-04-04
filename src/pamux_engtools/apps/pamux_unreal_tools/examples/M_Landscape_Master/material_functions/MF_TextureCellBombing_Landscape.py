from pathlib import Path
import sys

# sys.path.append(str(Path(__file__).parent.parent.parent.parent.parent.resolve()))

# from importlib import * 

# reloads = []
# for  k, v in sys.modules.items():
#     if k.startswith("pamux_unreal_tools"):
#         reloads.append(v)

# for module in reloads:
#     reload(module)

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.builders.material_function_builder import MaterialFunctionBuilder
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase

from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.interfaces.IRotateAboutWorldAxis_cheap import IRotateAboutWorldAxis_cheap

from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.ITextureCellBombing_Landscape import ITextureCellBombing_Landscape
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory


class MF_TextureCellBombing_Landscape:
    class Dependencies:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            self.rotateAboutWorldAxis_cheap = builder.load_MF(
                "/Engine/Functions/Engine_MaterialFunctions02/WorldPositionOffset/RotateAboutWorldAxis_cheap",
                [ "Rotation Amount", "PivotPoint", "WorldPosition" ], [ "X-Axis", "Y-Axis", "Z-Axis" ])


    class Inputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            self.texture                    = builder.build_FunctionInput("Texture",                    0, TextureObject(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR, None), False)
            self.UVs                        = builder.build_FunctionInput("UVs",                        1, TextureCoordinate(1.0, 1.0))

            self.cellScale                  = builder.build_FunctionInput("CellScale",                  3, 2.0)
            self.patternScale               = builder.build_FunctionInput("PatternScale",               4, 10.0)
            self.doRotationVariation        = builder.build_FunctionInput("DoRotationVariation",        5, False)
            self.randomOffsetVariation      = builder.build_FunctionInput("RandomOffsetVariation",      6, 1.0)
            self.randomRotationVariation    = builder.build_FunctionInput("RandomRotationVariation",    7, 1.0)
            self.isNormalMap                = builder.build_FunctionInput("IsNormalMap",                8, False)

    # [ "Texture", "UVs", "CellScale", "PatternScale", "DoRotationVariation", "RandomOffsetVariation", "RandomRotationVariation", "IsNormalMap" ], [ "Result" ]
    class Builder(MaterialFunctionBuilder):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_TextureCellBombing_Landscape",
                MF_TextureCellBombing_Landscape.Dependencies,
                MF_TextureCellBombing_Landscape.Inputs,
                MaterialFunctionOutputs.Result)

        def build(self):
            UVs3Vector = AppendVector(self.inputs.UVs, Constant(0.0))
            UVs3Vector.add_rt()

            patternScaledUVs3Vector = Multiply(UVs3Vector, self.inputs.patternScale)
            patternScaledUVs3Vector.add_rt()

            patternScaledUVs3VectorRG = ComponentMask(patternScaledUVs3Vector, "RG")
            patternScaledUVs3VectorRG.add_rt()

            cellScaledUVs3Vector = Multiply(UVs3Vector, self.inputs.cellScale)
            cellScaledUVs3Vector.add_rt()

            cellScaledUVs3VectorRG = ComponentMask(cellScaledUVs3Vector, "RG")
            cellScaledUVs3VectorRG.add_rt()

            patternScaledInputTexture = TextureSample()
            patternScaledInputTexture.RGB.add_rt()
            patternScaledInputTexture.UVs.comesFrom(patternScaledUVs3VectorRG)
            patternScaledInputTexture.tex.comesFrom(self.inputs.texture)
            patternScaledInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            patternScaledInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)

            cellScaledInputTexture = TextureSample()
            cellScaledInputTexture.RGB.add_rt()
            cellScaledInputTexture.r.add_rt()
            cellScaledInputTexture.a.add_rt()
            cellScaledInputTexture.UVs.comesFrom(cellScaledUVs3VectorRG)
            cellScaledInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            cellScaledInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
            cellScaledInputTexture.texture.set(unreal.load_asset("/Script/Engine.Texture2D'/Game/Materials/Functions/TextureCellBombing/T_Voronoi_Perturbed_4k.T_Voronoi_Perturbed_4k'"))

            offsetVariation = Multiply(self.inputs.randomOffsetVariation, cellScaledInputTexture.RGB)
            rotationVariation = Multiply(cellScaledInputTexture.r, self.inputs.randomRotationVariation)
            negativeRotationVariation = Multiply(rotationVariation, -1.0)

            pivotPoint1 = Constant3Vector(None)
            pivotPoint1.add_rt()

            worldPosition = Add(patternScaledUVs3Vector, offsetVariation)

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

            lerp = LinearInterpolate(patternScaledInputTexture.RGB, switch2, cellScaledInputTexture.a)
            lerp.connectTo(self.outputs.result)

# MF_TextureCellBombing_Landscape.Builder().get()
