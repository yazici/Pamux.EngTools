# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/examples/M_SimpleMaterial.py"

import unreal

from pathlib import Path
import sys
import os
import shutil

sys.path.append(str(Path(__file__).parent.parent.parent.parent.resolve()))

from importlib import * 

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)
 
from pamux_unreal_tools.material import MaterialFactory
from pamux_unreal_tools.generated.material_expression_wrappers import *
from pamux_unreal_tools.base.material_expression_container import *
from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_builder_base import MaterialBuilderBase
class M_SimpleMaterial:
    class Builder(MaterialBuilderBase):
        def __init__(self, material_name: str, package_name: str):
            super().__init__(None, material_name, package_name)

    def build_dependencies(self):
        pass

    def build_input_nodes(self):
        pass

    def build_process_nodes(self):
        self.colorParameter = VectorParameter("Color", unreal.LinearColor(0.259027, 0.320382, 0.383775, 1.0))
        self.constHalf = Constant(0.5)
        self.roughness = ScalarParameter("Roughness", 0.5)
        self.textureCoord = TextureCoordinate(0.5, 0.5)
        self.textureSample = TextureSample()

    def build_output_nodes(self):
        pass

    def finalize_node_connections(self):
        self.colorParameter.output.connectTo(unreal.MaterialProperty.MP_BASE_COLOR)
        self.constHalf.output.connectTo(unreal.MaterialProperty.MP_METALLIC)
        self.roughness.output.connectTo(unreal.MaterialProperty.MP_ROUGHNESS)

        self.textureSample.UVs.comesFrom(self.textureCoord.output)


material = M_SimpleMaterial.Builder("M_SimpleMaterial", "/Game/Materials/Pamux").get()
