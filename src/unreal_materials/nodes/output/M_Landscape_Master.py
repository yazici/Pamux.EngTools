from unreal_materials.nodes.output import MasterMaterialOutput

class M_Landscape_Master(MasterMaterialOutput):
    def __init__(self):
        super().__init__("M_Landscape_Master", MasterMaterialOutput.Details(), MasterMaterialOutput.InputPorts())
