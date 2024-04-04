import unreal
from pathlib import Path
import sys
import os
import shutil
import ast

#print(Path(__file__).parent.parent.parent.resolve())
sys.path.append(str(Path(__file__).parent.parent.parent.resolve()))

from importlib import * 

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)

import inspect
from pamux_unreal_tools.interfaces.IHeightLerpWithTwoHeightMaps import IHeightLerpWithTwoHeightMaps
from pamux_unreal_tools.tools.py_code_generator.main import *
from pamux_unreal_tools.tools.py_code_generator.method_params import *
def flatten(decorator_list):
    for d in decorator_list:
        try:
            yield d.id
        except AttributeError:
            yield d.func.id


def get_decorators(function):
  # If we have no func_closure, it means we are not wrapping any other functions.
  if not function.func_closure:
    return [function]
  decorators = []
  # Otherwise, we want to collect all of the recursive results for every closure we have.
  for closure in function.func_closure:
    decorators.extend(get_decorators(closure.cell_contents))
  return [function] + decorators

class InterfaceImplementer:
    def __init__(self, interface):
        self.interface = interface
        self.parse_interface()

    def implement(self):
        self.implement_dependencies_object()
        self.implement_inputs_object()
        self.implement_outputs_object()

    def parse_interface(self):
        signature = inspect.signature(self.interface)

        self.function_name = self.interface.__name__
        self.function_parameters = signature.parameters
        self.function_return = signature.return_annotation

        if hasattr(self.interface, "_asset_path"):
            print(self.interface._asset_path)
        if hasattr(self.interface, "_parameter_name_prefix"):
            print(self.interface._parameter_name_prefix)

        print(self.function_name)
        print(self.function_parameters)
        print(self.function_return)

    def implement_dependencies_object(self):
        pyGen = PyCodeGenerator()
        pyGen.append_import("unreal")
        pyGen.append_import_from("pamux_unreal_tools.base.container_builder_base", "ContainerBuilderBase")

        pyGen.begin_class("Dependencies", None)
        pyGen.begin_ctor(["builder: ContainerBuilderBase"])

        

        


        pyGen.end_ctor()
        pyGen.end_class()

        #pyGen.print_code()

    def implement_inputs_object(self):
        print(self.interface)
        
    def implement_outputs_object(self):
        print(self.interface)



ii = InterfaceImplementer(IHeightLerpWithTwoHeightMaps)
ii.implement_dependencies_object()

# class Dependencies:
#         def __init__(self, builder: ContainerBuilderBase) -> None:
#              self.heightLerpWithTwoHeightMaps = builder.load_MF(
#                 "/Engine/Functions/Engine_MaterialFunctions02/Texturing/HeightLerpWithTwoHeightMaps",
#                 [ "Transistion Phase", "Height Texture 1", "Height Texture 2" ],
#                 [ "Alpha" ])