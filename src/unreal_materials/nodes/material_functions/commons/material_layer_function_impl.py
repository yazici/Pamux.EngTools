from unreal_materials.nodes.utils.node_base import PortsBase, NodeBase
from unreal_materials.nodes.utils.rgba import RGBA

from unreal_materials.nodes.material_functions.commons.material_function_call import MaterialFunctionCallBase
from unreal_materials.nodes.material_functions.commons.binary_function_call import BinaryFunctionCall
from unreal_materials.nodes.material_functions.commons.binary_function_call import AppendVector

from unreal_materials.nodes.material_expressions.parameters.TextureParameter import TextureParameter
from unreal_materials.nodes.material_expressions.parameters.ScalarParameter import ScalarParameter
from unreal_materials.nodes.material_expressions.parameters.VectorParameter import VectorParameter
from unreal_materials.nodes.material_expressions.parameters.StaticBoolParameter import StaticBoolParameter

from unreal_materials.nodes.output.MaterialFunctionOutput import MaterialFunctionOutput
from unreal_materials.nodes.output.MaterialFunctionOutput import MaterialFunctionHeightOutput

class ColorOverlayParameter(TextureParameter):
    class OutputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "DefaultValue" ])

    def __init__(self, name: str):
        super().__init__(type =f"{name}ColorOverlay", outputPorts = ColorOverlayParameter.OutputPorts())

class MaterialLayerFunctionImpl(NodeBase):
    def __init__(self, name):
        # Albedo Texture
        albedoTextureParam = TextureParameter(f"{name}Albedo") 
        albedoTextureParam.details.materialExpression.group = name
        albedoTextureParam.details.textureName = "T_DrySoil_A"
        
        colorOverlayParam = ColorOverlayParameter(name) 
        colorOverlayParam.details.materialExpression.group = name
        colorOverlayParam.defaultValue = RGBA(0.5,0.5,0.5,1.0)

        colorOverlayIntensityParam = ScalarParameter(f"{name}ColorOverlayIntensity") 
        colorOverlayIntensityParam.details.materialExpression.group = name
        colorOverlayIntensityParam.details.scalarParameter.sliderMax = 1.5

        contrastParam = ScalarParameter(f"{name}Contrast") 
        contrastParam.details.materialExpression.group = name
        contrastParam.details.scalarParameter.defaultValue = 1.0

        contrastVariationParam = ScalarParameter(f"{name}ContrastVariation") 
        contrastVariationParam.details.materialExpression.group = name
        contrastVariationParam.details.scalarParameter.defaultValue = 0.0

        # Roughness Texture
        roughnessTextureParam = TextureParameter(f"{name}Roughness") 
        roughnessTextureParam.details.materialExpression.group = name
        roughnessTextureParam.details.textureName = "T_DrySoil_R"

        roughnessIntensityParam = ScalarParameter(f"{name}RoughnessIntensity") 
        roughnessIntensityParam.details.materialExpression.group = name
        roughnessIntensityParam.details.scalarParameter.sliderMax = 1.0


        # Normal Texture
        normalTextureParam = TextureParameter(f"{name}Normal") 
        normalTextureParam.details.materialExpression.group = name
        normalTextureParam.details.textureName = "T_DrySoil_N"        
        normalTextureParam.details.samplerType = "Normal"

        normalIntensityParam = ScalarParameter(f"{name}NormalIntensity") 
        normalIntensityParam.details.materialExpression.group = name
        normalIntensityParam.details.scalarParameter.sliderMax = 0.0

         # Displacement Texture
        displacementTextureParam = TextureParameter(f"{name}Displacement") 
        displacementTextureParam.details.materialExpression.group = name
        displacementTextureParam.details.textureName = "T_DrySoil_D"        
        displacementTextureParam.details.samplerType = "Color"

        uvParams = VectorParameter(f"{name}UVParams") 
        uvParams.details.materialExpression.group = name
        uvParams.details.defaultValue = RGBA(1.0, 1.0, 0.5, 0.5)

        appendResult = AppendVector(uvParams.result, uvParams.a)

        # Textue Bombing
        rotationParam = ScalarParameter(f"{name}Rotation") 
        rotationParam.details.materialExpression.group = name
        rotationParam.details.scalarParameter.sliderMax = 0.0

        doTheTextureBombParam = StaticBoolParameter(f"{name}DoTheTextureBomb") 
        doTheTextureBombParam.details.materialExpression.group = name
        doTheTextureBombParam.details.boolParameter.defaultValue = True
        
        bombDoRotationVariationParam = StaticBoolParameter(f"{name}BombDoRotationVariation") 
        bombDoRotationVariationParam.details.materialExpression.group = name
        bombDoRotationVariationParam.details.boolParameter.defaultValue = True

        bombCellScaleParam = ScalarParameter(f"{name}BombCellScale") 
        bombCellScaleParam.details.materialExpression.group = name
        bombCellScaleParam.details.scalarParameter.defaultValue = 0.01

        bombPatternScaleParam = ScalarParameter(f"{name}BombPatternScale") 
        bombPatternScaleParam.details.materialExpression.group = name
        bombPatternScaleParam.details.scalarParameter.defaultValue = 0.1

        bombRandomOffsetParam = ScalarParameter(f"{name}BombRandomOffset") 
        bombRandomOffsetParam.details.materialExpression.group = name
        bombRandomOffsetParam.details.scalarParameter.defaultValue = 1.0

        bombRotationVariationParam = ScalarParameter(f"{name}BombRotationVariation") 
        bombRotationVariationParam.details.materialExpression.group = name
        bombRotationVariationParam.details.scalarParameter.defaultValue = 1.0


        MaterialFunctionOutput()
        MaterialFunctionHeightOutput()