# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/tools/generate_material_expressions_wrappers.py"
# https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-expressions-reference
import unreal
import sys
import json
import inspect
import types
from pathlib import Path
from importlib import * 

sys.path.append(str(Path(__file__).parent.parent.parent.parent.parent.resolve()))

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools") and "generated" not in k:
        reloads.append(v)

for module in reloads: 
    reload(module)

from pamux_unreal_tools.tools.code_generators.cpp_code_generator import *

from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.ctor_params import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.globals import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.values import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.unreal_dump import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.inputs import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.outputs import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.properties import *
from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator import custom_base_classes

codeGen = CppCodeGenerator()
codeGen.declaration_filepath = generated_h_out_filepath
codeGen.definition_filepath = generated_cpp_out_filepath

headers = { 
    "Less": "Materials/MaterialExpressionBinaryOp.h",
    "HeightfieldMinMaxTexture": "HeightfieldMinMaxTextureMaterialExpression.h",
    "ConstantDouble": "Materials/MaterialExpressionGenericConstant.h",
    "CloudSampleAttribute": "Materials/MaterialExpressionCloudLayer.h",
    "NamedRerouteBase": "Materials/MaterialExpressionNamedReroute.h",
    "NamedRerouteDeclaration": "Materials/MaterialExpressionNamedReroute.h",
    "NamedRerouteUsage": "Materials/MaterialExpressionNamedReroute.h"
}

def get_required_includes(pamux_wrapper_class_name: str) -> str:
    if pamux_wrapper_class_name in headers.keys():        
        result = f'#include "{headers[pamux_wrapper_class_name]}"'
    else:
        result = f'#include "Materials/MaterialExpression{pamux_wrapper_class_name}.h"'
    return result

def get_expression_properties(pamux_wrapper_class_name: str, values) -> str:

    result = ""
    # values = [ 'EditorProperty threshold;' ]
    for item in values.items:
        result += ' ' * 8 + item.cpp_type + " " + item.field_name(pamux_wrapper_class_name) + ";\n"
    return result

def get_properties_initializers(pamux_wrapper_class_name: str, values) -> str:
    result = ""
    values = [ '\n    : threshold("threshold", "float")' ]
    for v in values:
        result += v
    return result

def get_expression_inputs(pamux_wrapper_class_name: str, values) -> str:
    result = ""
    values = [ 'InputSocket input;' ]
    for v in values:
        result += v
    return result

def get_inputs_initializers(pamux_wrapper_class_name: str, values) -> str:
    result = ""
    values = [ '\n    : input("UVs", "StructProperty")' ]
    for v in values:
        result += v
    return result

def get_expression_outputs(pamux_wrapper_class_name: str, values) -> str:
    result = ""
    values = [ 'OutputSocket output;' ]
    for v in values:
        result += v
    return result

def get_outputs_initializers(pamux_wrapper_class_name: str, values) -> str:
    result = ""
    values = [ '\n    : output("UVs", "StructProperty")' ]
    for v in values:
        result += v
    return result

def get_base_class_ctor_parameter_values(pamux_wrapper_class_name: str, values) -> str:
    result = ""
    return result

def get_main_initializers(pamux_wrapper_class_name: str, values) -> str:
    result = ""
    return result

def get_ctor_parameters(pamux_wrapper_class_name: str, values) -> str:
    result = ""
    return result

class UnrealClass:
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc

def generate_pamux_wrapper_class(codeGen: CodeGeneratorBase, c: unreal.MaterialExpression):
    pamux_wrapper_class_name = c.__name__[len("MaterialExpression"):]

    base_class_candidate_name = f"{pamux_wrapper_class_name}Base"
    if hasattr(custom_base_classes, base_class_candidate_name):
        base_class_name = base_class_candidate_name
    else:
        base_class_name = "MaterialExpressionParametrizedBase"

    #codeGen.append_blank_line()
    #codeGen.begin_class(pamux_wrapper_class_name, base_class_name)
    
    # codeGen.append_blank_line()
    
    #codeGen.begin_ctor(pamux_wrapper_class_name, ctor_params)
    #codeGen.append_base_ctor_call(base_class_name, f"unreal.MaterialExpression{pamux_wrapper_class_name}, node_pos")

    #properties.to_py("MaterialExpressionEditorPropertyImpl", codeGen)
    #inputs.to_py("InSocketImpl", codeGen)
    #outputs.to_py("OutSocketImpl", codeGen)

    # codeGen.append_line(f"self.properties = {pamux_wrapper_class_name}.Properties()")
    # codeGen.append_line(f"self.inputs = {pamux_wrapper_class_name}.Inputs()")
    # codeGen.append_line(f"self.outputs = {pamux_wrapper_class_name}.Outputs()")
    
    #ctor_params.append_assignment_lines(codeGen)
    #codeGen.end_ctor()

    #codeGen.end_class()

def generate_pamux_wrapper_classes():
    read_dump_data()

    
    # codeGen.append_import("unreal")

    # codeGen.append_import_from("pamux_unreal_tools.impl.material_expression_impl", "MaterialExpressionImpl")
    # codeGen.append_import_from("pamux_unreal_tools.impl.material_expression_editor_property_impl", "MaterialExpressionEditorPropertyImpl")
    # codeGen.append_import_from("pamux_unreal_tools.impl.in_socket_impl", "InSocketImpl")
    # codeGen.append_import_from("pamux_unreal_tools.impl.out_socket_impl", "OutSocketImpl")
    # codeGen.append_import_from("pamux_unreal_tools.utils.node_pos", "NodePos")

    # codeGen.append_include("Materials/MaterialExpressionBreakMaterialAttributes.h")
    
    # codeGen.append_include("MaterialExpressionImpl.h")
    # codeGen.append_include("MaterialExpressionEditorPropertyImpl.h")
    # codeGen.append_include("InSocketImpl.h")
    # codeGen.append_include("OutSocketImpl.h")
    # codeGen.append_include("NodePos.h")

    

    h_template = ""
    cpp_template = ""
    with open(h_template_filepath, "rt") as f:
        h_template = f.readlines()

    with open(cpp_template_filepath, "rt") as f:
        cpp_template = f.readlines()

    unreal_classes = []

    for class_name in dir(unreal):
        unreal_class = getattr(unreal, class_name)
        if not inspect.isclass(unreal_class):
            continue

        c = {
            "name": unreal_class.__name__, 
            "doc": unreal_class.__doc__
        }

        unreal_classes.append(c)

        if not issubclass(unreal_class, unreal.MaterialExpression):
            continue
        if unreal_class == unreal.MaterialExpression:
            continue


        if unreal_class.__name__ in skip_these_classes:
            continue

        

        # if unreal_class.__name__.startswith("MaterialExpressionSamplePhysics"):
        #     print(unreal_class.__name__)

        # if not os.path.isfile(f"C:/Program Files/Epic Games/UE_5.3/Engine/Source/Runtime/Engine/Classes/Materials/{unreal_class.__name__}.h"):
        #     print(unreal_class.__name__)
            
        pamux_wrapper_class_name = unreal_class.__name__[len("MaterialExpression"):]

        inputs = setup_input_sockets(pamux_wrapper_class_name)
        outputs = setup_output_sockets(pamux_wrapper_class_name)
        ctor_params = setup_ctor_params(pamux_wrapper_class_name)
        properties = setup_properties(pamux_wrapper_class_name, unreal_class.__doc__)

        h_code = ""
        for l in h_template:
            
            l = l.replace("__REQUIRED_INCLUDES__", get_required_includes(pamux_wrapper_class_name))
            l = l.replace("__DECLARE_EXPRESSION_PROPERTIES__", get_expression_properties(pamux_wrapper_class_name, properties))
            l = l.replace("__DECLARE_EXPRESSION_INPUTS__", get_expression_inputs(pamux_wrapper_class_name, inputs))
            l = l.replace("__DECLARE_EXPRESSION_OUTPUTS__", get_expression_outputs(pamux_wrapper_class_name, outputs))
            l = l.replace("__CTOR_PARAMETERS__", get_ctor_parameters(pamux_wrapper_class_name, ctor_params))
            l = l.replace("__CLASS_NAME__", pamux_wrapper_class_name)
            h_code += l

        cpp_code = ""
        for l in cpp_template:
            l = l.replace("__BASE_CLASS_CTOR_PARAMETERS_VALUES__", get_base_class_ctor_parameter_values(pamux_wrapper_class_name, ctor_params))
            l = l.replace("__MAIN_INITIALIZERS__", get_main_initializers(pamux_wrapper_class_name, ctor_params))
            l = l.replace("__PROPERTIES_INITIALIZERS__", get_properties_initializers(pamux_wrapper_class_name, properties))
            l = l.replace("__INPUTS_INITIALIZERS__", get_inputs_initializers(pamux_wrapper_class_name, inputs))
            l = l.replace("__OUTPUTS_INITIALIZERS__", get_outputs_initializers(pamux_wrapper_class_name, outputs))
            l = l.replace("__CTOR_PARAMETERS__", get_ctor_parameters(pamux_wrapper_class_name, ctor_params))
            l = l.replace("__CLASS_NAME__", pamux_wrapper_class_name)
            cpp_code += l

        with open(f"{generated_files_root}/{pamux_wrapper_class_name}.h", "wt") as f:
            f.writelines(h_code)

        with open(f"{generated_files_root}/{pamux_wrapper_class_name}.cpp", "wt") as f:
            f.writelines(cpp_code)
    with open(unreal_classes_list, "wt") as f:
            f.writelines(json.dumps(unreal_classes, indent=4, sort_keys=True))
generate_pamux_wrapper_classes()
