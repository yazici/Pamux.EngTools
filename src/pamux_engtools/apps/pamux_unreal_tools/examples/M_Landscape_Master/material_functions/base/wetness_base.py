
from pamux_unreal_tools.base.material_function_builder_base import *

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.material_expression_factories import *
from pamux_unreal_tools.base.texture_sample_set import TextureSampleSet

class WetnessBuilderBase(MaterialFunctionBuilderBase):
    def __init__(self, container_path: str):
        super().__init__(container_path)

    def getMaterialAttributes(self) -> FunctionInput:
        textureSampleSet = TextureSampleSet(
            "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_A", 
            "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_R", 
            "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_D", 
            "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_N")

        makeMaterialAttributes = MakeMaterialAttributes()
        makeMaterialAttributes.baseColor.comesFrom(textureSampleSet.baseColor.RGB)
        makeMaterialAttributes.roughness.comesFrom(textureSampleSet.roughness.RGB)
        makeMaterialAttributes.opacity.comesFrom(textureSampleSet.opacity.RGB)
        makeMaterialAttributes.normal.comesFrom(textureSampleSet.normal.RGB)

        return FunctionInputFactory.create("MaterialAttributes", unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES, makeMaterialAttributes)