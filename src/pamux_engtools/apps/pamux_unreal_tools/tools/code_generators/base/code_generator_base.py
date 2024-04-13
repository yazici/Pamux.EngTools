from pamux_unreal_tools.tools.code_generators.base.method_params import *


class CodeGeneratorBase:
    def __init__(self) -> None:
        self.lines = []
        self.indentation = 0
        self.indentation_amount = 4

        self.block_opener = None
        self.block_closer = None
        self.condition_opener = None
        self.condition_closer = None

        self.inline_comment_marker = "// "

        self.required_initial_parameters = [ ]
        self.null_name = None
        self.selfref = None
        self.ctor_method_name = None

    def write(self, file_path) -> None:
        with open(file_path, "w+t") as py_file:
            py_file.write(self.inline_comment_marker + " This file is generated. Please do NOT modify.")

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

    def append_include(self, header_name) -> None:
        pass
    
    def append_import_from(self, package_name, imports) -> None:
        pass

    def end_block(self) -> None:
        self.unindent()
        if self.block_closer != "":
            self.append_line(self.block_closer)

    def end_if(self) -> None:
        self.end_block()

    def end_class(self) -> None:
        self.end_block()

    def end_method(self) -> None:
        self.end_block()

    def end_static_method(self) -> None:
        self.end_block()

    def end_ctor(self) -> None:
        self.end_block()

    def append_pass(self):
        pass

    def append_base_ctor_call(self, base_class_name, params):
        pass

    def get_declaration_code(self, mp: MethodParam) -> str:
        return ""

    def get_initializer_code(self, class_name, parameters: MethodParams = NO_PARAMS) -> str:
        return ""
    
    def get_method_signature(self, before_method_name, method_name, parameters: MethodParams, after_param_list) -> str: 
        return f"{before_method_name}{method_name}({parameters.get_list_for_method_declaration(self)}){after_param_list}"
    
    def begin_method(self, method_name: str, parameters: MethodParams = NO_PARAMS, return_type: str = None) -> None:
        self.begin_method_impl(False, method_name, parameters, return_type)

    def begin_static_method(self, method_name: str, parameters: MethodParams = NO_PARAMS, return_type: str = None) -> None:
        self.begin_method_impl(True, method_name, parameters, return_type)

    def begin_ctor(self, class_name, parameters: MethodParams = NO_PARAMS) -> None:
        if self.ctor_method_name == "CLASS_NAME":
            method_name = class_name
        else:
            method_name = self.ctor_method_name

        self.begin_method(method_name, parameters, "CTOR")

    def begin_method_impl(self, isStatic: bool, method_name: str, parameters: MethodParams, return_type: str) -> None:
        pass