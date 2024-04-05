import unreal

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_expression.material_expression_container_builder_base import MaterialExpressionContainerBuilderBase

class LayerBuild:
    @staticmethod
    def call_and_connect_LandscapeBaseMaterial(builder: MaterialExpressionContainerBuilderBase, connectOpacity: bool):
        appendVector = AppendVector(builder.inputs.uvParams, builder.inputs.uvParams.a)
        appendVector.add_rt()

        call = builder.MF_LandscapeBaseMaterial.call()

        builder.inputs.albedo.connectTo(call.inputs.albedo)
        builder.inputs.colorOverlay.connectTo(call.inputs.colorOverlay)
        builder.inputs.colorOverlayIntensity.connectTo(call.inputs.colorOverlayIntensity)
        builder.inputs.contrast.connectTo(call.inputs.contrast)
        builder.inputs.contrastVariation.connectTo(call.inputs.contrastVariation)
        builder.inputs.roughness.connectTo(call.inputs.roughness)
        builder.inputs.roughnessIntensity.connectTo(call.inputs.roughnessIntensity)
        builder.inputs.normalIntensity.connectTo(call.inputs.normalIntensity)
        builder.inputs.normal.connectTo(call.inputs.normal)
        builder.inputs.displacement.connectTo(call.inputs.displacement)
        builder.inputs.uvParams.connectTo(appendVector.output.rt)
        builder.inputs.rotation.connectTo(call.inputs.rotation)
        builder.inputs.doTextureBomb.connectTo(call.inputs.doTextureBomb)
        builder.inputs.doRotationVariation.connectTo(call.inputs.doRotationVariation)
        builder.inputs.bombCellScale.connectTo(call.inputs.bombCellScale)
        builder.inputs.bombPatternScale.connectTo(call.inputs.bombPatternScale)
        builder.inputs.bombRandomOffset.connectTo(call.inputs.bombRandomOffset)
        builder.inputs.bombRotationVariation.connectTo(call.inputs.bombRotationVariation)

        if connectOpacity:
            builder.inputs.opacityStrength.connectTo(call.inputs.opacityStrength)
            builder.inputs.opacityAdd.connectTo(call.inputs.opacityAdd)
            builder.inputs.opacityContrast.connectTo(call.inputs.opacityContrast)

        call.outputs.result.connectTo(builder.outputs.result)
        call.outputs.height.connectTo(builder.outputs.height)

        return call