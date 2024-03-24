from unreal_materials.nodes.utils.node_base import PortsBase
from unreal_materials.nodes.material_functions.commons.material_function_call import MaterialFunctionCallBase

class MaterialLayerFunctionCall(MaterialFunctionCallBase):
    class OutputPorts(PortsBase):
        def __init__(self):
            super().__init__([ "Result", "Height" ])

    def __init__(self, name_suffix):
        super().__init__(type = "MLF_{name_suffix}", outputPorts = MaterialLayerFunctionCall.OutputPorts())
