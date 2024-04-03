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
## 
from pamux_unreal_tools.base.material_function_builder_base import *

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.factories.material_function_factory import MaterialFunctionFactory
from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase
class MF_TextureCellBombing_Landscape:
    class Dependencies:
        def __init__(self, builder: ContainerBuilderBase) -> None:
             pass

    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            self.patternScale = builder.build_FunctionInput("PatternScale", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(10.0))
            self.UVs = builder.build_FunctionInput("UVs", unreal.FunctionInputType.FUNCTION_INPUT_VECTOR2, TextureCoordinate(1.0, 1.0))
            self.randomOffsetVariation = builder.build_FunctionInput("RandomOffsetVariation", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(1.0))
            self.randomRotationVariation = builder.build_FunctionInput("RandomRotationVariation", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(1.0))
            self.cellScale = builder.build_FunctionInput("CellScale", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(2.0))
            self.doRotationVariation = builder.build_FunctionInput("DoRotationVariation", unreal.FunctionInputType.FUNCTION_INPUT_STATIC_BOOL, StaticBool(False))
            self.isNormalMap = builder.build_FunctionInput("IsNormalMap", unreal.FunctionInputType.FUNCTION_INPUT_STATIC_BOOL, StaticBool(False))

            self.texture = builder.build_FunctionInput("Texture", unreal.FunctionInputType.FUNCTION_INPUT_TEXTURE2D, TextureObject(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR, None))
            self.texture.use_preview_value_as_default.set(False)

            self.UVs3Vector = AppendVector(self.UVs.rt, Constant(0.0))

            self.patternScaledUVs3Vector = Multiply(self.UVs3Vector, self.patternScale.rt)
            self.patternScaledUVs3VectorRG = ComponentMask(self.patternScaledUVs3Vector, "RG")

            self.cellScaledUVs3Vector = Multiply(self.UVs3Vector, self.cellScale.rt)
            self.cellScaledUVs3VectorRG = ComponentMask(self.cellScaledUVs3Vector, "RG")

            self.patternScaledInputTexture = TextureSample()
            self.patternScaledInputTexture.UVs.comesFrom(self.patternScaledUVs3VectorRG)
            self.patternScaledInputTexture.tex.comesFrom(self.texture.rt)
            self.patternScaledInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.patternScaledInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)

            NamedRerouteDeclaration("rtPatternScaledInputTexture.RGB", self.patternScaledInputTexture.RGB)


    # [ "Texture", "UVs", "CellScale", "PatternScale", "DoRotationVariation", "RandomOffsetVariation", "RandomRotationVariation", "IsNormalMap" ], [ "Result" ]
    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__(
                "/Game/Materials/Pamux/Landscape/Functions/MF_TextureCellBombing_Landscape",
                MaterialFunctionDependenciesBase,
                MF_TextureCellBombing_Landscape.Inputs,
                MaterialFunctionOutputs.Result)

        def build_dependencies(self):
            self.rotateAboutWorldAxis_cheap = self.load_MF(
                "/Engine/Functions/Engine_MaterialFunctions02/WorldPositionOffset/RotateAboutWorldAxis_cheap",
                [ "Rotation Amount", "PivotPoint", "WorldPosition" ], [ "X-Axis", "Y-Axis", "Z-Axis" ])


        def __build_RandomRotate(self):
            pivotPoint = Constant3Vector(None)

            self.worldPosition = Add(self.inputs.patternScaledUVs3Vector, self.offsetVariation)

            self.rotateAboutWorldAxis_cheap.call()
            self.rotateAboutWorldAxis_cheap.call_result.rotationAmount.comesFrom(self.rotationVariation)
            self.rotateAboutWorldAxis_cheap.call_result.pivotPoint.comesFrom(pivotPoint)
            self.rotateAboutWorldAxis_cheap.call_result.worldPosition.comesFrom(self.worldPosition)

            usage = NamedRerouteUsage(None)
            #usage.unrealAsset.set_editor_property("Declaration", self.inputs.doRotationVariation.rt)

            # self.inputs.doRotationVariation.rt
            switch = StaticSwitch(Add(self.rotateAboutWorldAxis_cheap.call_result.zAxis, self.worldPosition), self.worldPosition, usage)

            self.randomRotateRG = ComponentMask(switch, "RG")

            #return self.randomRotateRG.output, self.inputs.patternScaledUVs3VectorRG.output
        
        def __build_NormalRotation(self):
            pivotPoint = Constant3Vector(None)

            self.rotatedInputTexture = TextureSample()
            self.rotatedInputTexture.UVs.comesFrom(self.randomRotateRG)
            self.rotatedInputTexture.tex.comesFrom(self.inputs.texture.rt)
            self.rotatedInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.rotatedInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
            self.rotatedInputTexture.rt = NamedRerouteDeclaration(f"rtRotatedInputTexture", self.rotatedInputTexture.RGB)
            #self.rotatedInputTexture.rt.material_expression_editor_x.set(self.rotatedInputTexture.material_expression_editor_x.get() + 50)

            self.rotateAboutWorldAxis_cheap.call()
            self.rotateAboutWorldAxis_cheap.call_result.rotationAmount.comesFrom(self.negativeRotationVariation)
            self.rotateAboutWorldAxis_cheap.call_result.pivotPoint.comesFrom(pivotPoint)
            self.rotateAboutWorldAxis_cheap.call_result.worldPosition.comesFrom(self.rotatedInputTexture.rt)

            self.normalRotation = Add(self.rotateAboutWorldAxis_cheap.call_result.zAxis, self.rotatedInputTexture.rt)

            return self.normalRotation

        def __build_PreOutput(self):
            switch1 = StaticSwitch(self.normalRotation, self.rotatedInputTexture.rt, self.inputs.isNormalMap.rt)
            switch2 = StaticSwitch(switch1, self.rotatedInputTexture.rt, self.inputs.doRotationVariation.rt)

            self.lerp = LinearInterpolate(self.inputs.patternScaledInputTexture.RGB.rt, switch2, self.textureSample.a.rt)

        def __build_PostInput(self):
            self.textureSample = TextureSample()
            self.textureSample.UVs.comesFrom(self.inputs.cellScaledUVs3VectorRG)
            self.textureSample.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.textureSample.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
            self.textureSample.texture.set(unreal.load_asset("/Script/Engine.Texture2D'/Game/Materials/Functions/TextureCellBombing/T_Voronoi_Perturbed_4k.T_Voronoi_Perturbed_4k'"))
            
            self.textureSample.RGB.rt = NamedRerouteDeclaration(f"rtTextureSample.RGB", self.textureSample.RGB)
            self.textureSample.r.rt = NamedRerouteDeclaration(f"rtTextureSample.R", self.textureSample.r)
            self.textureSample.a.rt = NamedRerouteDeclaration(f"rtTextureSample.A", self.textureSample.a)


            self.offsetVariation = Multiply(self.inputs.randomOffsetVariation.rt, self.textureSample.RGB.rt)
            self.rotationVariation = Multiply(self.textureSample.r.rt, self.inputs.randomRotationVariation.rt)
            self.negativeRotationVariation = Multiply(self.rotationVariation, -1.0)

            # return self.inputs.patternScaledUVs3Vector.output, self.textureSample.a.rt, self.offsetVariation.output, self.rotationVariation.output

        def build(self):
            self.__build_PostInput()
            self.__build_RandomRotate()
            self.__build_NormalRotation()
            self.__build_PreOutput()

            self.lerp.output.connectToFunctionOutput(self.outputs.Result)

MF_TextureCellBombing_Landscape.Builder().get()
