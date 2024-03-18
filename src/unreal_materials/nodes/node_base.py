from unreal_materials.nodes.ports_base import DefaultInputPorts, DefaultOutputPorts

class NodeBase:
    class DetailsBase:
        def __init__(self):
            pass

    def __init__(
            self,

            type: str,
            name: str = None,

            desc: str = None,

            details: DetailsBase = DetailsBase(),

            inPorts: DefaultInputPorts = DefaultInputPorts(),
            outPorts: DefaultOutputPorts = DefaultOutputPorts()):

        if name is None:
            name = type

        self.type = type
        self.name = name

        self.desc = desc

        self.details = details

        self.inPorts = inPorts
        self.outPorts = outPorts


class ParameterBase(NodeBase):
    def __init__(
            self,

            type: str,
            name: str = None,

            desc: str = None,

            details: NodeBase.DetailsBase = NodeBase.DetailsBase(),

            inPorts: DefaultInputPorts = DefaultInputPorts(),
            outPorts: DefaultOutputPorts = DefaultOutputPorts()):

        super().__init__(type, name, desc, details, inPorts, outPorts)



class MaterialExpressionBase(NodeBase):
    def __init__(
            self,

            type: str,
            name: str = None,

            desc: str = None,

            details: NodeBase.DetailsBase = NodeBase.DetailsBase(),

            inPorts: DefaultInputPorts = DefaultInputPorts(),
            outPorts: DefaultOutputPorts = DefaultOutputPorts()):

        super().__init__(type, name, desc, details, inPorts, outPorts)

