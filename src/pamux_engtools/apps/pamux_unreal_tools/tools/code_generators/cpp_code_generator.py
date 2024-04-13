from pamux_unreal_tools.tools.code_generators.base.method_params import *
from pamux_unreal_tools.tools.code_generators.base.code_generator_base import *

class CppCodeGenerator(CodeGeneratorBase):
    def __init__(self) -> None:
        super().__init__()
        self.block_opener = " {"
        self.block_closer = "}"
        self.condition_opener = "("
        self.condition_closer = "("

    def begin_class(self, class_name, base_class_name = None) -> None:
        if base_class_name is None:
            self.append_line(f"class {class_name}{self.block_opener}")
        else:
            self.append_line(f"class {class_name}: public {base_class_name}{self.block_opener}")
        self.indent()
    
    def begin_method(self, method_name, method_args = [], return_type = None) -> None:
        if return_type is None:
            return_type = "void"

        self.append_line(f"{return_type} {method_name}({', '.join(method_args)}){self.block_opener}")
        self.indent()

    def begin_static_method(self, method_name, method_args = [], return_type = None) -> None:
        self.append_line(f"static {return_type} {method_name}({', '.join(method_args)}){self.block_opener}")
        self.indent()

    def begin_ctor(self, class_name, ctor_args = []) -> None:
        self.begin_method(class_name, ctor_args)

    def begin_if(self, condition) -> None:
        self.append_line(f"if {self.condition_opener}{condition}{self.condition_closer}{self.block_opener}")
        self.indent()

    def begin_elif(self, condition) -> None:
        self.unindent()
        self.append_line(f"else if {self.condition_opener}{condition}{self.condition_closer}{self.block_opener}")
        self.indent()

    def begin_else(self) -> None:
        self.unindent()
        self.append_line(f"else{self.block_opener}")
        self.indent()

    def end_if(self) -> None:
        self.unindent()

    def end_class(self) -> None:
        self.unindent()

    def end_method(self) -> None:
        self.unindent()

    def end_static_method(self) -> None:
        self.end_method()

    def end_ctor(self) -> None:
        self.end_method()

    def append_pass(self):
        pass
