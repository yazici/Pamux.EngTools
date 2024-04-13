class CodeGeneratorBase:
    def __init__(self) -> None:
        self.lines = []
        self.indentation = 0
        self.indentation_amount = 4

        self.block_opener = None
        self.block_closer = None
        self.condition_opener = None
        self.condition_closer = None

    def write(self, file_path) -> None:
        with open(file_path, "w+t") as py_file:
            py_file.write("# This file is generated. Please do NOT modify.")

            for line in self.lines:
                py_file.write(f"\n{line}")

    def print_code(self) -> None:
        for line in self.lines:
            print(line)

    def indent(self) -> None:
        self.indentation += self.indentation_amount

    def unindent(self) -> None:
        self.indentation -= self.indentation_amount

    def append_line(self, line: str) -> None:
        self.lines.append(f"{' ' * self.indentation}{line}")

    def append_lines(self, lines: list) -> None:
        for line in lines:
            self.append_line(line)

    def append_blank_line(self) -> None:
        self.lines.append("")

    def append_import(self, package_name) -> None:
        pass
    
    def append_import_from(self, package_name, imports) -> None:
        pass

    def end_block(self) -> None:
        self.unindent()
        if self.block_closer != "":
            self.append_line(self.block_closer)