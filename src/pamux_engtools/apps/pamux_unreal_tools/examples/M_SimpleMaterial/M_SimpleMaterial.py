import unreal

from importlib import * 
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent.parent.resolve()))

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)

from pamux_unreal_tools.generated.material_expression_wrappers import *

from pamux_unreal_tools.base.material_function_dependencies_base import MaterialFunctionDependenciesBase
from pamux_unreal_tools.base.material_builder_base import MaterialBuilderBase
from pamux_unreal_tools.base.material_function_outputs_base import MaterialFunctionOutputs
from pamux_unreal_tools.base.container_builder_base import ContainerBuilderBase

class M_SimpleMaterial:
    class Inputs:
        def __init__(self, builder: ContainerBuilderBase):
            self.colorParameter = VectorParameter("Color", unreal.LinearColor(0.259027, 0.320382, 0.383775, 1.0))
            self.constHalf = Constant(0.5)
            self.roughness = ScalarParameter("Roughness", 0.5)
            self.textureCoord = TextureCoordinate(0.5, 0.5)
            self.textureSample = TextureSample()

    class Builder(MaterialBuilderBase):
        def __init__(self, container_path: str):
            super().__init__(
                container_path,
                MaterialFunctionDependenciesBase,
                M_SimpleMaterial.Inputs,
                MaterialFunctionOutputs.Result)

    def build(self):
        self.colorParameter.connectTo(unreal.MaterialProperty.MP_BASE_COLOR)
        self.constHalf.connectTo(unreal.MaterialProperty.MP_METALLIC)
        self.roughness.connectTo(unreal.MaterialProperty.MP_ROUGHNESS)

        self.textureSample.UVs.comesFrom(self.textureCoord)

M_SimpleMaterial.Builder("/Game/Materials/Pamux/M_SimpleMaterial").get()
