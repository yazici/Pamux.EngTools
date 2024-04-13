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
        self.ctor_method_name = "__init__"

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

    def get_for_method_declaration(self, mp: MethodParam) -> str:
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

    def get_initializer_code(self, mp: MethodParam) -> str:
        return mp.name
    
    def append_base_ctor_call(self, base_class_name, params):
        self.append_line(f"super().__init__({params})")

#Below implementation

    def begin_method_impl(self, isStatic: bool, method_name: str, parameters: MethodParams, return_type: str) -> None:
        if return_type == "void":
            return_type = "None"
        elif return_type == "CTOR":
            return_type = "None"
        elif return_type == None:
            return_type = ""
        else:
            return_type = return_type.strip()
        
        if return_type != "":
            return_type = f" -> {return_type}"

        if isStatic:
            self.append_line("@staticmethod")

        self.append_line(self.get_method_signature("def ", method_name, parameters, f"{return_type}{self.block_opener}"))
        self.indent()
