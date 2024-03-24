#region Ports (I/O sockets)

class PortsBase:
    def __init__(self, names: list = []):
        self.names = names

class DefaultInputPorts(PortsBase):
    def __init__(self, names: list = []):
        super().__init__(names)

class DefaultOutputPorts(PortsBase):
    def __init__(self, names: list = [ "Result" ]):
        super().__init__(names)

#endregion
        
#region Base classes

class NodeBase:
    class DetailsBase:
        def __init__(self):
            pass

    def __init__(
            self,

            type: str,
            name: str = None,

            details: DetailsBase = DetailsBase(),

            inputPorts: DefaultInputPorts = DefaultInputPorts(),
            outputPorts: DefaultOutputPorts = DefaultOutputPorts()):

        if name is None:
            name = type

        self.type = type
        self.name = name

        self.desc = None

        self.details = details

        self.inputPorts = inputPorts
        self.outputPorts = outputPorts


class ParameterBase(NodeBase):
    def __init__(
            self,

            type: str,
            name: str = None,

            details: NodeBase.DetailsBase = NodeBase.DetailsBase(),

            inputPorts: DefaultInputPorts = DefaultInputPorts(),
            outputPorts: DefaultOutputPorts = DefaultOutputPorts()):

        super().__init__(type, name, details, inputPorts, outputPorts)


class GroupedParameterBase(ParameterBase):
    class DetailsBase(ParameterBase.DetailsBase):
        class MaterialExpression:
            def __init__(self):
                self.group = "Globals"
                self.sortPriority = 32

        def __init__(self):
            self.materialExpression = GroupedParameterBase.DetailsBase.MaterialExpression()

    def __init__(
            self,

            type: str,
            name: str = None,

            details: DetailsBase = DetailsBase(),

            inputPorts: DefaultInputPorts = DefaultInputPorts(),
            outputPorts: DefaultOutputPorts = DefaultOutputPorts()):
        super().__init__(type, name, details, inputPorts, outputPorts)


class MaterialExpressionBase(NodeBase):
    def __init__(
            self,

            type: str,
            name: str = None,

            details: NodeBase.DetailsBase = NodeBase.DetailsBase(),

            inputPorts: DefaultInputPorts = DefaultInputPorts(),
            outputPorts: DefaultOutputPorts = DefaultOutputPorts()):

        super().__init__(type, name, details, inputPorts, outputPorts)


#endregion