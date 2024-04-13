from pamux_unreal_tools.tools.code_generators.base.method_params import *
from pamux_unreal_tools.tools.code_generators.base.code_generator_base import *
from pamux_unreal_tools.tools.code_generators.base.method_params import *

class PyCodeGenerator(CodeGeneratorBase):
    def __init__(self) -> None:
        super().__init__()
        self.block_opener = ":"
        self.block_closer = ""
        self.condition_opener = ""
        self.condition_closer = ""
        self.inline_comment_marker = "# "
        self.required_initial_parameters = [ "self" ]
        self.selfref = "self."

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
    
    def begin_method(self, method_name, method_args = [], return_type = None) -> None:
        if return_type is None:
            return_type = "None"
        self.append_line(f"def {method_name}({', '.join(method_args)}) -> {return_type}:")
        self.indent()

    def begin_static_method(self, method_name, method_args = [], return_type = None) -> None:
        self.append_line("@staticmethod")
        self.begin_method(method_name, method_args, return_type)

    def begin_ctor(self, class_name, ctor_args = []) -> None:
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

    def append_pass(self):
        self.append_line("pass")

    def get_parameter_code(self, mp: MethodParam) -> str:
        result = mp.name

        if mp.type is not None:
            result += f": {mp.type}"

        if mp.default_value is None:
            return result

        result += " = "

        if mp.default_value == "NULL":
            result += "None";
        else:
            result += mp.default_value

        return result


    def append_base_ctor_call(self, codeGen, base_class_name, params):
        codeGen.append_line(f"super().__init__({params})")