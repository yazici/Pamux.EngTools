import logging
logger = logging.getLogger(__name__)

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.utils.types import *

from pamux_unreal_tools.builders.material_function_builder import MaterialFunctionBuilder
from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase

from pamux_unreal_tools.base.material_function.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.interfaces.IRotateAboutWorldAxis_cheap import IRotateAboutWorldAxis_cheap

from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.ITextureCellBombing_Landscape import ITextureCellBombing_Landscape
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.utils.asset_cache import AssetCache

class MF_TextureCellBombing_Landscape:
    AssetPath = "/Game/Materials/Pamux/Landscape/Functions/MF_TextureCellBombing_Landscape"

    @staticmethod
    def load_MF(builder):
        return builder.load_MF(MF_TextureCellBombing_Landscape.AssetPath,
            ["Texture", "UVs", "CellScale", "PatternScale", "DoRotationVariation", "RandomOffsetVariation", "RandomRotationVariation", "IsNormalMap"],
            ["Result"])

    class Dependencies:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase) -> None:
            self.rotateAboutWorldAxis_cheap = builder.load_RotateAboutWorldAxis_cheap()


    class Inputs:
        def __init__(self, builder: MaterialExpressionContainerBuilderBase):
            self.texture                    = builder.build_FunctionInput("Texture",                    0, TTextureObject_Color(),          True, False)
            self.UVs                        = builder.build_FunctionInput("UVs",                        1, TTextureCoordinate(1.0, 1.0),    True, True)

            self.cellScale                  = builder.build_FunctionInput("CellScale",                  3, 2.0,                             True, True)
            self.patternScale               = builder.build_FunctionInput("PatternScale",               4, 10.0,                            True, True)
            self.doRotationVariation        = builder.build_FunctionInput("DoRotationVariation",        5, False,                           True, True)
            self.randomOffsetVariation      = builder.build_FunctionInput("RandomOffsetVariation",      6, 1.0,                             True, True)
            self.randomRotationVariation    = builder.build_FunctionInput("RandomRotationVariation",    7, 1.0,                             True, True)
            self.isNormalMap                = builder.build_FunctionInput("IsNormalMap",                8, False,                           True, True)

    class Builder(MaterialFunctionBuilder):
        def __init__(self):
            super().__init__(
                MF_TextureCellBombing_Landscape.AssetPath,
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
            cellScaledInputTexture.texture.set(AssetCache.get("BombingTexture"))
            cellScaledInputTexture.RGB.add_rt()
            cellScaledInputTexture.r.add_rt()
            cellScaledInputTexture.a.add_rt()
            cellScaledInputTexture.UVs.comesFrom(cellScaledUVs3VectorRG)
            cellScaledInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            cellScaledInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
            cellScaledInputTexture.automatic_view_mip_bias.set(True)
            cellScaledInputTexture.const_mip_value.set(-1)
            

            offsetVariation = Multiply(self.inputs.randomOffsetVariation, cellScaledInputTexture.RGB)
            rotationVariation = Multiply(cellScaledInputTexture.r, self.inputs.randomRotationVariation)
            negativeRotationVariation = Multiply(rotationVariation, -1.0)

            pivotPoint1 = Constant3Vector(None)
            pivotPoint1.add_rt()

            worldPosition = Add(patternScaledUVs3Vector, offsetVariation)

            call_result = self.dependencies.rotateAboutWorldAxis_cheap.call()
            call_result.inputs.rotationAmount.comesFrom(rotationVariation)
            call_result.inputs.pivotPoint.comesFrom(pivotPoint1)
            call_result.inputs.worldPosition.comesFrom(worldPosition)

            switch = StaticSwitch(Add(call_result.outputs.zAxis, worldPosition), worldPosition, self.inputs.doRotationVariation)

            randomRotateRG = ComponentMask(switch, "RG")

            pivotPoint2 = Constant3Vector(None)
            pivotPoint2.add_rt()

            rotatedInputTexture = TextureSample()
            rotatedInputTexture.RGB.add_rt()
            rotatedInputTexture.UVs.comesFrom(randomRotateRG)
            rotatedInputTexture.tex.comesFrom(self.inputs.texture)
            rotatedInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            rotatedInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)

            call_result = self.dependencies.rotateAboutWorldAxis_cheap.call()
            call_result.inputs.rotationAmount.comesFrom(negativeRotationVariation)
            call_result.inputs.pivotPoint.comesFrom(pivotPoint2)
            call_result.inputs.worldPosition.comesFrom(rotatedInputTexture)

            normalRotation = Add(call_result.outputs.zAxis, rotatedInputTexture)

            switch1 = StaticSwitch(normalRotation, rotatedInputTexture, self.inputs.isNormalMap)
            switch2 = StaticSwitch(switch1, rotatedInputTexture, self.inputs.doRotationVariation)

            lerp = LinearInterpolate(patternScaledInputTexture.RGB, switch2, cellScaledInputTexture.a)
            lerp.connectTo(self.outputs.result)
