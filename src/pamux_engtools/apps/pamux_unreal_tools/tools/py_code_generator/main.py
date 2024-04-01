from pamux_unreal_tools.tools.py_code_generator.method_params import *

class PyCodeGenerator:
    def __init__(self) -> None:
        self.lines = []
        self.indentation = 0
        self.indentation_amount = 4

    def write(self, file_path) -> None:
        with open(file_path, "w+t") as py_file:
            py_file.write("# This file is generated. Please do NOT modify.")

            for line in self.lines:
                py_file.write(f"\n{line}")

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
        self.append_line(f"import {package_name}")
    
    def append_import_from(self, package_name, imports) -> None:
        self.append_line(f"from {package_name} import {imports}")
    
    def begin_class(self, class_name, base_class_name = None) -> None:
        if base_class_name is None:
            self.append_line(f"class {class_name}:")
        else:
            self.append_line(f"class {class_name}({base_class_name}):")
        self.indent()
    
    def begin_method(self, method_name, method_args = [], return_type = "None") -> None:
        self.append_line(f"def {method_name}({', '.join(method_args)}) -> {return_type}:")
        self.indent()

    def begin_ctor(self, ctor_args = []) -> None:
        self.begin_method("__init__", ctor_args)

    def begin_if(self, condition) -> None:
        self.append_line(f"if {condition}:")
        self.indent()

    def begin_elif(self, condition) -> None:
        self.unindent()
        self.append_line(f"elif {condition}:")
        self.indent()

    def begin_else(self) -> None:
        self.unindent()
        self.append_line(f"else:")
        self.indent()

    def end_if(self) -> None:
        self.unindent()

    def end_class(self) -> None:
        self.unindent()

    def end_method(self) -> None:
        self.unindent()

    def end_ctor(self) -> None:
        self.end_method()

    def append_pass(self):
        self.append_line("pass")
