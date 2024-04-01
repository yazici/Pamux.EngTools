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
from pamux_unreal_tools.base.material_function_builder_base import MaterialFunctionBuilderBase

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.material_function import MaterialFunctionFactory

class MF_TextureCellBombing_Landscape:
    class Inputs:
        def __init__(self, builder):
            self.patternScale = builder.build_FunctionInput("PatternScale", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(10.0))
            self.UVs = builder.build_FunctionInput("UVs", unreal.FunctionInputType.FUNCTION_INPUT_VECTOR2, TextureCoordinate(1.0, 1.0))
            self.randomOffsetVariation = builder.build_FunctionInput("RandomOffsetVariation", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(1.0))
            self.randomRotationVariation = builder.build_FunctionInput("RandomRotationVariation", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(1.0))
            self.cellScale = builder.build_FunctionInput("CellScale", unreal.FunctionInputType.FUNCTION_INPUT_SCALAR, Constant(2.0))
            self.doRotationVariation = builder.build_FunctionInput("DoRotationVariation", unreal.FunctionInputType.FUNCTION_INPUT_STATIC_BOOL, StaticBool(False))
            self.isNormalMap = builder.build_FunctionInput("IsNormalMap", unreal.FunctionInputType.FUNCTION_INPUT_STATIC_BOOL, StaticBool(False))
            self.texture = builder.build_FunctionInput("Texture", unreal.FunctionInputType.FUNCTION_INPUT_TEXTURE2D, TextureObject())
            self.texture.use_preview_value_as_default.set(False)

    class Outputs:
        def __init__(self, builder):
            CurrentNodePos.y = 0
            self.Result = builder.makeFunctionOutput_Result()
        
    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__("MF_TextureCellBombing_Landscape")

        def build_dependencies(self):
            factory = MaterialFunctionFactory()
            self.rotateAboutWorldAxis_cheap = factory.load("RotateAboutWorldAxis_cheap", "/Engine/Functions/Engine_MaterialFunctions02/WorldPositionOffset")

        def build_input_nodes(self):
            self.inputs = MF_TextureCellBombing_Landscape.Inputs(self)

            self.UVs3Vector = AppendVector(self.inputs.UVs.rt, Constant(0.0))

            self.patternScaledUVs3Vector = Multiply(self.UVs3Vector, self.inputs.patternScale.rt)
            self.patternScaledUVs3VectorRG = ComponentMask(self.patternScaledUVs3Vector, "RG")

            self.cellScaledUVs3Vector = Multiply(self.UVs3Vector, self.inputs.cellScale.rt)
            self.cellScaledUVs3VectorRG = ComponentMask(self.cellScaledUVs3Vector, "RG")

            self.patternScaledInputTexture = TextureSample()
            self.patternScaledInputTexture.UVs.comesFrom(self.patternScaledUVs3VectorRG)
            self.patternScaledInputTexture.tex.comesFrom(self.inputs.texture.rt)
            self.patternScaledInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.patternScaledInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
            self.patternScaledInputTexture.rt = NamedRerouteDeclaration(f"rtPatternScaledInputTexture", self.patternScaledInputTexture.RGB)


        def __build_RandomRotate(self):
            pivotPoint = Constant3Vector()

            self.worldPosition = Add(self.patternScaledUVs3Vector, self.offsetVariation)

            rotated = self.callMaterialFunction(self.rotateAboutWorldAxis_cheap, [ "Rotation Amount", "PivotPoint", "WorldPosition" ], [ "X-Axis", "Y-Axis", "Z-Axis" ])
            rotated.rotationAmount.comesFrom(self.rotationVariation)
            rotated.pivotPoint.comesFrom(pivotPoint)
            rotated.worldPosition.comesFrom(self.worldPosition)

            usage = NamedRerouteUsage()
            usage.asset.set_editor_property("Declaration", self.inputs.doRotationVariation.rt)

            switch = StaticSwitch(Add(rotated.zAxis, self.worldPosition), self.worldPosition, usage ) # self.inputs.doRotationVariation.rt

            self.randomRotateRG = ComponentMask(switch, "RG")

            return self.randomRotateRG.output, self.patternScaledUVs3VectorRG.output
        
        def __build_NormalRotation(self):
            pivotPoint = Constant3Vector()

            self.rotatedInputTexture = TextureSample()
            self.rotatedInputTexture.UVs.comesFrom(self.randomRotateRG)
            self.rotatedInputTexture.tex.comesFrom(self.inputs.texture.rt)
            self.rotatedInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.rotatedInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
            self.rotatedInputTexture.rt = NamedRerouteDeclaration(f"rtRotatedInputTexture", self.rotatedInputTexture.RGB)

            rotated = self.callMaterialFunction(self.rotateAboutWorldAxis_cheap, [ "Rotation Amount", "PivotPoint", "WorldPosition" ], [ "X-Axis", "Y-Axis", "Z-Axis" ])
            rotated.rotationAmount.comesFrom(self.negativeRotationVariation)
            rotated.pivotPoint.comesFrom(pivotPoint)
            rotated.worldPosition.comesFrom(self.rotatedInputTexture.rt)

            self.normalRotation = Add(rotated.zAxis, self.rotatedInputTexture.rt)

            return self.normalRotation

        def __build_PreOutput(self):
            switch1 = StaticSwitch(self.normalRotation, self.rotatedInputTexture.rt, self.inputs.isNormalMap.rt)
            switch2 = StaticSwitch(switch1, self.rotatedInputTexture.rt, self.inputs.doRotationVariation.rt)

            self.lerp = LinearInterpolate(self.patternScaledInputTexture.rt, switch2, self.textureSample.a)

        def __build_PostInput(self):
            self.textureSample = TextureSample()
            self.textureSample.UVs.comesFrom(self.cellScaledUVs3VectorRG)
            self.textureSample.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.textureSample.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
            self.textureSample.texture.set(unreal.load_asset("/Script/Engine.Texture2D'/Game/Materials/Functions/TextureCellBombing/T_Voronoi_Perturbed_4k.T_Voronoi_Perturbed_4k'"))

            self.offsetVariation = Multiply(self.inputs.randomOffsetVariation.rt, self.textureSample.RGB)
            self.rotationVariation = Multiply(self.textureSample.r, self.inputs.randomRotationVariation.rt)
            self.negativeRotationVariation = Multiply(self.rotationVariation, -1.0)

            return self.patternScaledUVs3Vector.output, self.textureSample.a, self.offsetVariation.output, self.rotationVariation.output

        def build_process_nodes(self):
            self.__build_PostInput()
            self.__build_RandomRotate()
            self.__build_NormalRotation()
            self.__build_PreOutput()
        
        def build_output_nodes(self):
            self.outputs = MF_TextureCellBombing_Landscape.Outputs(self)


        def finalize_node_connections(self):
            return self.lerp.output.connectToFunctionOutput(self.outputs.Result)

folder = "C:/src/Unreal Projects/PamuxSurvival/Content/Materials/Pamux"
if os.path.isdir(folder):
    shutil.rmtree(folder)

material = MF_TextureCellBombing_Landscape.Builder().get()
