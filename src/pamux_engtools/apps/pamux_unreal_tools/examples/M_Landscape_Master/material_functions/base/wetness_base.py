from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.base.material_function_builder_base import MaterialFunctionBuilderBase
from pamux_unreal_tools.material import Material
from pamux_unreal_tools.material_function import MaterialFunction

from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *

LandscapeMaterialFunctionPackage = "/Game/Materials/Pamux/Landscape/Functions"

class WetnessBuilderBase(MaterialFunctionBuilderBase):
    def __init__(self, container_name: str, package_name: str = LandscapeMaterialFunctionPackage):
        super().__init__(container_name, package_name)

    def getMaterialAttributesOutput(self):
        textureSampleSet = MaterialFunctionBuilderBase.TextureSampleSet(
            "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_A", 
            "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_R", 
            "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_D", 
            "/Game/Materials/Landscape/Textures/GrassyLayer/T_GrassyLayer_N")

        makeMaterialAttributes = MakeMaterialAttributes()
        makeMaterialAttributes.baseColor.comesFrom(textureSampleSet.baseColor.RGB)
        makeMaterialAttributes.roughness.comesFrom(textureSampleSet.roughness.RGB)
        makeMaterialAttributes.opacity.comesFrom(textureSampleSet.opacity.RGB)
        makeMaterialAttributes.normal.comesFrom(textureSampleSet.normal.RGB)

        materialAttributes = FunctionInput()
        materialAttributes.input_name.set("MaterialAttributes")
        materialAttributes.input_type.set(unreal.FunctionInputType.FUNCTION_INPUT_MATERIAL_ATTRIBUTES)
        materialAttributes.preview.comesFrom(makeMaterialAttributes.output)

        return materialAttributes.output