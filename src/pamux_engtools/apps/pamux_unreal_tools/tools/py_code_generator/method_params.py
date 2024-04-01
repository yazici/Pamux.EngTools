class MethodParam:
    def __init__(self, name, type = None, default_value = None) -> None:
        self.name = name
        self.type = type
        self.default_value = default_value

    @property
    def code(self) -> str:
        result = self.name

        if self.type is not None:
            result += f": {self.type}"

        if self.default_value is not None:
            result += f" = {self.default_value}"

        return result
