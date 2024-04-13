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

    def append_include(self, header_name) -> None:
        self.append_line(f"#include <{header_name}>")

    def begin_class(self, class_name, base_class_name = None) -> None:
        if base_class_name is None:
            self.append_line(f"class {class_name}{self.block_opener}")
        else:
            self.append_line(f"class {class_name}: public {base_class_name}{self.block_opener}")
        self.indent()
    
    def begin_method(self, method_name, parameters: MethodParams = NO_PARAMS, return_type = None) -> None:
        if return_type is None:
            return_type = "void "

        self.append_line(f"{return_type}{method_name}({self.get_declaration_code(parameters)}){self.block_opener}")
        self.indent()

    def begin_static_method(self, method_name, parameters: MethodParams = NO_PARAMS, return_type = None) -> None:
        self.append_line(f"static {return_type} {method_name}({', '.join(parameters)}){self.block_opener}")
        self.indent()

    def begin_ctor(self, class_name, parameters: MethodParams = NO_PARAMS) -> None:
        self.append_line(f"{class_name}({parameters.get_declaration_code(self)}){parameters.get_initializer_code(self, class_name)}{self.block_opener}")
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

    def get_declaration_code(self, mp: MethodParam) -> str:
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
    
    # def append_base_ctor_call(self, base_class_name, params):
    #     codeGen.append_line(f"{base_class_name}({params})")