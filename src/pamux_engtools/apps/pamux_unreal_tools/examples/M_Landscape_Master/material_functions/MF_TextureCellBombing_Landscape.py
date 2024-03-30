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


    class Outputs:
        def __init__(self, builder):
            CurrentNodePos.y = 0
            self.Result = builder.makeFunctionOutput_Result()
        
    class Builder(MaterialFunctionBuilderBase):
        def __init__(self):
            super().__init__("MF_TextureCellBombing_Landscape")

        def build_dependencies(self):
            factory = MaterialFunctionFactory()
            self.rotateAboutWorldAxis_cheap = factory.load("RotateAboutWorldAxis_cheap", "/Engine/Functions/Engine_MaterialFunctions02/WorldPositionOffset", True)

            # self.blend_Overlay = factory.load("Blend_Overlay", "/Engine/Functions/Engine_MaterialFunctions03/Blends", True)
            # self.cheapContrast_RGB = factory.load("CheapContrast_RGB", "/Engine/Functions/Engine_MaterialFunctions01/ImageAdjustment", True)
            # self.heightLerp = factory.load("HeightLerp", "/Engine/Functions/Engine_MaterialFunctions02/Texturing", True)
            # self.multiplyAdd = factory.load("MultiplyAdd", "/Engine/Functions/Engine_MaterialFunctions02/Math", True)
            # self.breakOutFloat4Components = factory.load("BreakOutFloat4Components", "/Engine/Functions/Engine_MaterialFunctions02/Utility", True)
            # self.multiplyAdd = factory.load("MultiplyAdd", "/Engine/Functions/Engine_MaterialFunctions02/Math", True)
            # self.customRotator = factory.load("CustomRotator", "/Engine/Functions/Engine_MaterialFunctions02/Texturing", True)
    
        def build_input_nodes(self):
            self.inputs = MF_TextureCellBombing_Landscape.Inputs(self)

            self.sampledInputTexture = self.texture

            self.patternScaledInputTexture = TextureSample()
            self.patternScaledInputTexture.UVs.comesFrom(self.patternScaledUVs3VectorRG)
            self.patternScaledInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.patternScaledInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
            self.patternScaledInputTexture.texture.set(self.inputs.texture)

            self.rotatedInputTexture = TextureSample()
            self.rotatedInputTexture.UVs.comesFrom(self.randomRotateRG)
            self.rotatedInputTexture.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.rotatedInputTexture.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_COLOR)
            self.rotatedInputTexture.texture.set(self.inputs.texture)

        def __build_RandomRotate(self):
            pivotPoint = Constant3Vector()

            self.worldPosition = Add(self.patternScaledUVs3Vector, self.offsetVariation)

            rotated = self.callMaterialFunction(self.rotateAboutWorldAxis_cheap, [ "RotationAmount", "PivotPoint", "WorldPosition" ], [ "XAxis", "YAxis", "ZAxis" ])
            rotated.rotationAmount.comesFrom(self.rotationVariation)
            rotated.pivotPoint.comesFrom(pivotPoint)
            rotated.rotationAmount.comesFrom(self.worldPosition)

            self.add = Add(rotated.zAxis, self.worldPosition)

            switch = Switch() ## GENERATE BETTER
            switch.true.comesFrom(self.add)
            switch.false.comesFrom(self.worldPosition)
            switch.value.comesFrom(self.inputs.doRotationVariation)

            self.randomRotateRG = ComponentMask(switch)
            self.randomRotateRG.r.set(True)
            self.randomRotateRG.g.set(True)
            self.randomRotateRG.b.set(False)
            self.randomRotateRG.a.set(False)

            return self.randomRotateRG.output, self.patternScaledUVs3VectorRG.output



        
        def __build_NormalRotation(self):
            pivotPoint = Constant3Vector()

            rotated = self.callMaterialFunction(self.rotateAboutWorldAxis_cheap, [ "RotationAmount", "PivotPoint", "WorldPosition" ], [ "XAxis", "YAxis", "ZAxis" ])
            rotated.rotationAmount.comesFrom(self.negativeRotationVariation)
            rotated.pivotPoint.comesFrom(pivotPoint)
            rotated.worldPosition.comesFrom(self.rotatedInputTexture.RGB)

            self.normalRotation = Add(rotated.zAxis, self.rotatedInputTexture.RGB)

            return self.normalRotation

        def __build_PreOutput(self):
            switch1 = Switch()
            switch1.true.comesFrom(self.normalRotation)
            switch1.false.comesFrom(self.rotatedInputTexture)
            switch1.value.comesFrom(self.inputs.isNormalMap)

            switch2 = Switch()
            switch2.true.comesFrom(switch1)
            switch2.false.comesFrom(self.rotatedInputTexture)
            switch2.value.comesFrom(self.inputs.doRotationVariation)


            self.lerp = LinearInterpolate(self.patternScaledInputTexture, switch2, self.textureSample.a)

        def __build_PostInput(self):
            self.UVs3Vector = AppendVector() ## GENERATE BETTER
            self.UVs3Vector.a.comesFrom(self.inputs.UVs)
            self.UVs3Vector.b.comesFrom(Constant(0.0))

            self.patternScaledUVs3Vector = Multiply(self.UVs3Vector, self.inputs.patternScale)
            self.cellScaledUVs3Vector = Multiply(self.UVs3Vector, self.inputs.cellScale)

            self.cellScaledUVs3VectorRG = ComponentMask(self.cellScaledUVs3Vector)
            self.cellScaledUVs3VectorRG.r.set(True)
            self.cellScaledUVs3VectorRG.g.set(True)
            self.cellScaledUVs3VectorRG.b.set(False)
            self.cellScaledUVs3VectorRG.a.set(False)

            self.patternScaledUVs3VectorRG = ComponentMask(self.patternScaledUVs3Vector)
            self.patternScaledUVs3VectorRG.r.set(True)
            self.patternScaledUVs3VectorRG.g.set(True)
            self.patternScaledUVs3VectorRG.b.set(False)
            self.patternScaledUVs3VectorRG.a.set(False)

            self.textureSample = TextureSample()
            self.textureSample.UVs.comesFrom(self.cellScaledUVs3VectorRG)
            self.textureSample.sampler_source.set(unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
            self.textureSample.sampler_type.set(unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
            self.textureSample.texture.set(unreal.load_asset("/Script/Engine.Texture2D'/Game/Materials/Functions/TextureCellBombing/T_Voronoi_Perturbed_4k.T_Voronoi_Perturbed_4k'"))

            self.offsetVariation = Multiply(self.inputs.randomOffsetVariation, self.textureSample.RGB)
            self.rotationVariation = Multiply(self.textureSample.r, self.inputs.randomRotationVariation)
            self.negativeRotationVariation = Multiply(self.rotationVariation, -1)

            return self.patternScaledUVs3Vector.output, self.textureSample.a, self.offsetVariation.output, self.rotationVariation.output

        def build_process_nodes(self):
            self.__build_RandomRotate()
            self.__build_NormalRotation()
            self.__build_PostInput()
            self.__build_PreOutput()
        
        def build_output_nodes(self):
            self.outputs = MF_TextureCellBombing_Landscape.Outputs(self)


        def finalize_node_connections(self):
            self.lerp.connectTo(self.outputs.Result)


folder = "C:/src/Unreal Projects/PamuxSurvival/Content/Materials/Pamux"
if os.path.isdir(folder):
    shutil.rmtree(folder)

material = MF_TextureCellBombing_Landscape.Builder().get()
