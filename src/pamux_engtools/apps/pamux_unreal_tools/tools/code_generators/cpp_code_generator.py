from pamux_unreal_tools.tools.code_generators.base.method_params import *
from pamux_unreal_tools.tools.code_generators.base.code_generator_base import *
from pamux_unreal_tools.tools.code_generators.base.method_params import *

class CppCodeGenerator(CodeGeneratorBase):
    def __init__(self) -> None:
        super().__init__()
        
        self.block_opener = " {"
        self.block_closer = "}"
        self.condition_opener = "("
        self.condition_closer = "("

        self.inline_comment_marker = "// "

        self.null_name = "nullptr"
        self.selfref = "this->"
        self.ctor_method_name = "CLASS_NAME"

    def append_include(self, header_name) -> None:
        self.append_line(f"#include <{header_name}>")

    def begin_class(self, class_name, base_class_name = None) -> None:
        if base_class_name is None:
            self.append_line(f"class {class_name}{self.block_opener}")
        else:
            self.append_line(f"class {class_name}: public {base_class_name}{self.block_opener}")
        self.indent()

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

    def get_for_method_declaration(self, mp: MethodParam) -> str:
        result = f"{mp.type} {mp.name}"

        if mp.default_value is None:
            return result

        result += " = "

        if mp.default_value == "NULL":
            result += "nullptr";
        else:
            result += mp.default_value

        return result
    
    def get_initializer_code(self, mp: MethodParam) -> str:
        return mp.name

#Below implementation

    def begin_method_impl(self, isStatic: bool, method_name: str, parameters: MethodParams, return_type: str) -> None:
        if return_type == "void":
            return_type = "void"
        elif return_type == "CTOR":
            return_type = ""
        elif return_type == None:
            return_type = ""
        else:
            return_type = return_type.strip()

        if isStatic:
            return_type = f"static {return_type}"

        return_type += " "

        self.append_line(self.get_method_signature(return_type, method_name, parameters, self.block_opener))
        self.indent()
    
    # def append_base_ctor_call(self, base_class_name, params):
    #     codeGen.append_line(f"{base_class_name}({params})")