from unreal_materials.nodes.ports_base import DefaultInputPorts, DefaultOutputPorts
from unreal_materials.nodes.node_base import NodeBase, ParameterBase

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/MaterialExpressionLandscapeLayerWeight.html
class MaterialExpressionParameterBase(ParameterBase):    
    class DetailsBase(NodeBase.DetailsBase):
        class MaterialExpression:
            def __init__(self, group: str = "Globals", sortPriority: int = 32):
                self.group = group
                self.sortPriority = sortPriority

        def __init__(
                self,
                group: str = "Globals",
                sortPriority: int = 32):
            
            self.materialExpression = MaterialExpressionParameterBase.DetailsBase.MaterialExpression(group, sortPriority)

    def __init__(
            
            self,

            type: str,
            name: str = None,

            desc: str = None,

            details: NodeBase.DetailsBase = NodeBase.DetailsBase(),

            inPorts: DefaultInputPorts = DefaultInputPorts(),
            outPorts: DefaultOutputPorts = DefaultOutputPorts()):
        super().__init__(type, name, desc, details, inPorts, outPorts)
