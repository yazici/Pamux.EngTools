import unreal
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.utils.node_pos import NodePos, CurrentNodePos

class FunctionInputFactory:
    @staticmethod
    def create(input_name, input_type, preview = None) -> FunctionInput:
        if isinstance(preview, float):
            preview = Constant(preview)
        elif isinstance(preview, unreal.LinearColor):
            preview = Constant4Vector(preview)

        result = FunctionInput()
        result.input_name.set(input_name)
        result.input_type.set(input_type)
        if preview is not None:
            result.preview.comesFrom(preview)
        return result


class MakeMaterialAttributesFactory:
    @staticmethod
    def create(materialAttributes) -> MakeMaterialAttributes:
        result = MakeMaterialAttributes()
        result.baseColor.comesFrom(materialAttributes.baseColor)
        result.metallic.comesFrom(materialAttributes.metallic)
        result.specular.comesFrom(materialAttributes.specular)
        result.roughness.comesFrom(materialAttributes.roughness)
        result.anisotropy.comesFrom(materialAttributes.anisotropy)
        result.emissiveColor.comesFrom(materialAttributes.emissiveColor)
        result.opacity.comesFrom(materialAttributes.opacity)
        result.opacityMask.comesFrom(materialAttributes.opacityMask)
        result.normal.comesFrom(materialAttributes.normal)
        result.tangent.comesFrom(materialAttributes.tangent)
        result.worldPositionOffset.comesFrom(materialAttributes.worldPositionOffset)
        result.subsurfaceColor.comesFrom(materialAttributes.subsurfaceColor)
        result.clearCoat.comesFrom(materialAttributes.clearCoat)
        result.clearCoatRoughness.comesFrom(materialAttributes.clearCoatRoughness)
        result.ambientOcclusion.comesFrom(materialAttributes.ambientOcclusion)
        result.refraction.comesFrom(materialAttributes.refraction)
        result.customizedUV_0.comesFrom(materialAttributes.customizedUV0)
        result.customizedUV_1.comesFrom(materialAttributes.customizedUV1)
        result.customizedUV_2.comesFrom(materialAttributes.customizedUV2)
        result.customizedUV_3.comesFrom(materialAttributes.customizedUV3)
        result.customizedUV_4.comesFrom(materialAttributes.customizedUV4)
        result.customizedUV_5.comesFrom(materialAttributes.customizedUV5)
        result.customizedUV_6.comesFrom(materialAttributes.customizedUV6)
        result.customizedUV_7.comesFrom(materialAttributes.customizedUV7)
        result.pixelDepthOffset.comesFrom(materialAttributes.pixelDepthOffset)
        result.shadingModel.comesFrom(materialAttributes.shadingModel)
        result.displacement.comesFrom(materialAttributes.displacement)
        return result