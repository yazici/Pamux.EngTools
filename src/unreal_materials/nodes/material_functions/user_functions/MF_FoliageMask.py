from unreal_materials.nodes.utils.node_base import PortsBase
from unreal_materials.nodes.material_functions.commons.material_function_call import MaterialFunctionCallBase

class MF_FoliageMask(MaterialFunctionCallBase):
    class InputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "LayerSample", "FoliageMask", "Threshold", "Enabled" ])

    def __init__(self):
        super().__init__("MF_FoliageMask", MF_FoliageMask.InputPorts())
