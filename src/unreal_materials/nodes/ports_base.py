class PortsBase:
    def __init__(self, names: list = []):
        self.names = names

class DefaultInputPorts(PortsBase):
    def __init__(self, names: list = []):
        super().__init__(names)

class DefaultOutputPorts(PortsBase):
    def __init__(self, names: list = [ "Result" ]):
        super().__init__(names)
