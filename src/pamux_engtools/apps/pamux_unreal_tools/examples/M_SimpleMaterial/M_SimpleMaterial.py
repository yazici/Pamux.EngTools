# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/examples/M_SimpleMaterial.py"

import unreal

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent.resolve()))
 
from pamux_unreal_tools.material import MaterialFactory
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *

class MaterialBuilder:
    def __init__(self, material):
        self.material = material

    def build(self):
        colorParameter = VectorParameter(self.material)
        colorParameter.parameter_name = "Color"
        colorParameter.default_value = unreal.LinearColor(0.259027, 0.320382, 0.383775, 1.0)
        colorParameter.output.connectTo(unreal.MaterialProperty.MP_BASE_COLOR)

        constHalf = Constant(self.material)
        constHalf.r = 0.5
        constHalf.output.connectTo(unreal.MaterialProperty.MP_METALLIC)

        roughness = ScalarParameter(self.material)
        roughness.parameter_name = "Roughness"
        roughness.default_value = 0.5
        roughness.output.connectTo(unreal.MaterialProperty.MP_ROUGHNESS)

        textureCoord = TextureCoordinate(self.material)
        textureCoord.u_tiling = 0.5
        textureCoord.v_tiling = 0.5

        textureSample = TextureSample(self.material)
        textureSample.UVs.comesFrom(textureCoord.output)

material = MaterialFactory().loadOrCreate("M_Test", "/Game/Materials/Pamux", True)

material_builder = MaterialBuilder(material)
material_builder.build()

material.save()