# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/tools/generate_material_expressions_wrappers.py"
# https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-expressions-reference
import unreal
import sys
import inspect
import types
from pathlib import Path
from importlib import * 

print(str(Path(__file__).parent.parent.parent.resolve()))
sys.path.append(str(Path(__file__).parent.parent.parent.resolve()))

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools") and "generated" not in k:
        reloads.append(v)

for module in reloads:
    reload(module)

from pamux_unreal_tools.tools.py_code_generator.main import *

from pamux_unreal_tools.tools.material_expression_wrapper_generator.ctor_params import *
from pamux_unreal_tools.tools.material_expression_wrapper_generator.globals import *
from pamux_unreal_tools.tools.material_expression_wrapper_generator.values import *
from pamux_unreal_tools.tools.material_expression_wrapper_generator.unreal_dump import *
from pamux_unreal_tools.tools.material_expression_wrapper_generator.inputs import *
from pamux_unreal_tools.tools.material_expression_wrapper_generator.outputs import *
from pamux_unreal_tools.tools.material_expression_wrapper_generator.properties import *
from pamux_unreal_tools.tools.material_expression_wrapper_generator.custom_code import *

def generate_pamux_wrapper_class(pyGen: PyCodeGenerator, c: unreal.MaterialExpression):
    pamux_wrapper_class_name = c.__name__[len("MaterialExpression"):]

    inputs = setup_input_sockets(pamux_wrapper_class_name)
    outputs = setup_output_sockets(pamux_wrapper_class_name)
    properties = setup_properties(pamux_wrapper_class_name, c.__doc__)
    ctor_params = setup_ctor_params(pamux_wrapper_class_name)
    


    pyGen.append_blank_line()
    pyGen.begin_class(pamux_wrapper_class_name, "MaterialExpression")
    
    # pyGen.begin_class("Properties")
    # pyGen.begin_ctor(["self"])
    # pyGen.end_ctor()
    # pyGen.end_class()

    # pyGen.begin_class("Inputs")
    # pyGen.begin_ctor(["self"])
    # inputs.to_py("InSocket", pyGen)
    # pyGen.end_ctor()
    # pyGen.end_class()

    # pyGen.begin_class("Outputs")
    # pyGen.begin_ctor(["self"])
    # outputs.to_py("OutSocket", pyGen)
    # pyGen.end_ctor()
    # pyGen.end_class()

    # pyGen.append_blank_line()
    pyGen.begin_ctor(ctor_params.declaration_code)
    pyGen.append_line(f"super().__init__(unreal.MaterialExpression{pamux_wrapper_class_name}, node_pos)")

    properties.to_py("Property", pyGen)
    inputs.to_py("InSocket", pyGen)
    outputs.to_py("OutSocket", pyGen)

    # pyGen.append_line(f"self.properties = {pamux_wrapper_class_name}.Properties()")
    # pyGen.append_line(f"self.inputs = {pamux_wrapper_class_name}.Inputs()")
    # pyGen.append_line(f"self.outputs = {pamux_wrapper_class_name}.Outputs()")
    
    ctor_params.append_assignment_lines(pyGen)
    pyGen.end_ctor()

    pyGen.end_class()

def generate_pamux_wrapper_classes():
    read_dump_data()

    pyGen = PyCodeGenerator()
    pyGen.append_import("unreal")
    pyGen.append_import_from("pamux_unreal_tools.material_expression", "MaterialExpression")
    pyGen.append_import_from("pamux_unreal_tools.base.material_expression_container", "*")
    pyGen.append_import_from("pamux_unreal_tools.utils.build_stack", "NodePos")

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
        generate_pamux_wrapper_class(pyGen, c)

    pyGen.write(generated_py_out_filepath)

# print(material_expressions_dump_data)
generate_pamux_wrapper_classes()


        # type(unreal.MaterialExpressionAdd()).mro()
        # type(unreal.MaterialExpressionAntialiasedTextureMask()).mro()
        # unreal.MaterialExpressionAntialiasedTextureMask.mro()

        # if "MaterialExpression" in class_name:
        #unrealClass = UnrealClass.from_class_name(class_name)
        # unrealClass.dump()
        # material_expressions.append(unrealClass)

        #UnrealClass.from_unreal_module_class(class_name)



# c = getattr(unreal, "MaterialExpressionAdd")
# print (c)
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
    # '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', 
            # '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_post_init',
            #  '_wrapper_meta_data', 'acquire_editor_element_handle', 'call_method', 'cast', 
            # 'get_class', 'get_default_object', 'get_editor_property', 'get_fname', 
            # 'get_full_name', 'get_interpolated_pcg_landscape_layer_weights', 'get_name',
            #  'get_outer', 'get_outermost', 'get_package', 
# 'get_path_name', 'get_typed_outer', 'get_world', 'is_package_external', 'material_expression_editor_x', 'material_expression_editor_y', 'modify', 'rename', 'set_editor_properties', 'set_editor_property', 'static_class']
# o = c()
# print (o)
# <Object '/Engine/Transient.MaterialExpressionAdd_0' (0x000006F8FA505B40) Class 'MaterialExpressionAdd'>



 # inspect.getmro(cls)
    # addClass = unreal.MaterialExpressionAdd
    # addObject = unreal.MaterialExpressionAdd()
    # print(dir(addClass))
    # print(dir(addObject))
    # inspect.getmembers(addObject)
    # inspect.getmembers(addObject, predicate=inspect.ismethod)
    # members = inspect.getmembers(addObject, predicate=lambda x: not (inspect.ismethod(x) or inspect.isclass(x)))

def pred(x):
    if inspect.ismethod(x):
        return False
    # if inspect.ismethodwrapper(x):
    #     return False
    if inspect.isbuiltin(x):
        return False
    if inspect.isclass(x):
        return False
    if isinstance(x,  types.MethodWrapperType):
        return False   

    
    print(x)
    return True
    # inspect.getmembers(unreal.MaterialExpressionAntialiasedTextureMask(), predicate=pred)


    # 


#MaterialEditLibrary.connect_material_expressions
#MaterialEditLibrary.connect_material_property
#MEL.get_inputs_for_material_expression(self.material, n)
#MEL.get_input_node_output_name_for_material_expression

# from_expression (MaterialExpression) – Expression to make connection from
# from_output_name (str) – Name of output of FromExpression to make connection from. Leave empty to use first output.
# to_expression (MaterialExpression) – Expression to make connection to
# to_input_name (str) – Name of input of ToExpression to make connection to. Leave empty to use first input.
