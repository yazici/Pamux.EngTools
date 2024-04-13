# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/tools/generate_material_expressions_wrappers.py"
# https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-expressions-reference
import unreal
import sys
import inspect
import types
from pathlib import Path
from importlib import * 
# from abc import ABC, abstractmethod
# print(str(Path(__file__).parent.parent.parent.parent.resolve()))
sys.path.append(str(Path(__file__).parent.parent.parent.parent.resolve()))

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools") and "generated" not in k:
        reloads.append(v)

for module in reloads: 
    reload(module)

from pamux_engtools.apps.pamux_unreal_tools.tools.code_generators.py_code_generator import *

from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.ctor_params import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.globals import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.values import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.unreal_dump import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.inputs import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.outputs import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.properties import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator import custom_base_classes

def generate_pamux_wrapper_class(codeGen: PyCodeGenerator, c: unreal.MaterialExpression):
    pamux_wrapper_class_name = c.__name__[len("MaterialExpression"):]

    inputs = setup_input_sockets(pamux_wrapper_class_name)
    outputs = setup_output_sockets(pamux_wrapper_class_name)
    properties = setup_properties(pamux_wrapper_class_name, c.__doc__)
    ctor_params = setup_ctor_params(pamux_wrapper_class_name)

    
    base_class_candidate_name = f"{pamux_wrapper_class_name}Base"
    if hasattr(custom_base_classes, base_class_candidate_name):
        base_class_name = base_class_candidate_name
    else:
        base_class_name = "MaterialExpressionImpl"

    codeGen.append_blank_line()
    codeGen.begin_class(pamux_wrapper_class_name, base_class_name)
    
    # codeGen.append_blank_line()
    codeGen.begin_ctor(ctor_params.declaration_code)
    codeGen.append_line(f"super().__init__(unreal.MaterialExpression{pamux_wrapper_class_name}, node_pos)")

    properties.to_py("MaterialExpressionEditorPropertyImpl", codeGen)
    inputs.to_py("InSocketImpl", codeGen)
    outputs.to_py("OutSocketImpl", codeGen)

    # codeGen.append_line(f"self.properties = {pamux_wrapper_class_name}.Properties()")
    # codeGen.append_line(f"self.inputs = {pamux_wrapper_class_name}.Inputs()")
    # codeGen.append_line(f"self.outputs = {pamux_wrapper_class_name}.Outputs()")
    
    ctor_params.append_assignment_lines(codeGen)
    codeGen.end_ctor()

    codeGen.end_class()

def generate_pamux_wrapper_classes():
    read_dump_data()

    codeGen = PyCodeGenerator()
    codeGen.append_import("unreal")

    codeGen.append_import_from("pamux_unreal_tools.impl.material_expression_impl", "MaterialExpressionImpl")
    codeGen.append_import_from("pamux_unreal_tools.impl.material_expression_editor_property_impl", "MaterialExpressionEditorPropertyImpl")
    codeGen.append_import_from("pamux_unreal_tools.impl.in_socket_impl", "InSocketImpl")
    codeGen.append_import_from("pamux_unreal_tools.impl.out_socket_impl", "OutSocketImpl")
    codeGen.append_import_from("pamux_unreal_tools.utils.node_pos", "NodePos")

    for class_name in dir(unreal):
        c = getattr(unreal, class_name)
        if not inspect.isclass(c):
            continue
        if not issubclass(c, unreal.MaterialExpression):
            continue
        if c == unreal.MaterialExpression:
            continue
        if c.__name__ in skip_these_classes:
            continue
        generate_pamux_wrapper_class(codeGen, c)

    codeGen.write(generated_py_out_filepath)

generate_pamux_wrapper_classes()
