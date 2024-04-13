class CodeGeneratorBase:
    def __init__(self) -> None:
        self.lines = []
        self.indentation = 0
        self.indentation_amount = 4
