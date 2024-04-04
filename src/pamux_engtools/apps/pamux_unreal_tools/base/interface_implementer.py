import unreal
from pathlib import Path
import sys
import os
import shutil
import ast

sys.path.append(str(Path(__file__).parent.parent.parent.resolve()))

from importlib import * 

reloads = []
for  k, v in sys.modules.items():
    if k.startswith("pamux_unreal_tools"):
        reloads.append(v)

for module in reloads:
    reload(module)

import inspect
# from pamux_unreal_tools.interfaces.IHeightLerpWithTwoHeightMaps import IHeightLerpWithTwoHeightMaps
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.IBlendTwoMaterialsViaHighOpacityMap import IBlendTwoMaterialsViaHighOpacityMap
from pamux_unreal_tools.tools.py_code_generator.main import *
from pamux_unreal_tools.tools.py_code_generator.method_params import *
from pamux_unreal_tools.utils.types import *

import functools
from typing import Any, Callable

# def class_builder(func):
#     def _decorator(self, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         # access a from TestSample
#         func(self, *args, **kwargs)
#     return _decorator


# class class_builder:
#     def __init__(self, class_name):
#         self.class_name = class_name
#         print("A1 " + class_name)
#         #print("A1x " + str(self))

#     def __call__(self, f: Callable) -> Any:
#         @functools.wraps(wrapped=f)
#         def wrapper(calling_instance, *args, **kwargs):
#             print("A2 " + self.class_name)
#             print("A3 " + self.class_name)
#             print("A4 " + str(calling_instance))
#             # pre-logic goes here
#             response = f(calling_instance, *args, **kwargs)
#             # post-logic goes here
#             return response

class InterfaceImplementer:
    def __init__(self, interface):
        self.interface = interface
        self.function_name = None
        self.function_parameters = []
        self.function_return = None
        self.asset_path = None
        self.parameter_name_prefix = None

    def parse_interface(self):
        signature = inspect.signature(self.interface)

        self.function_name = self.interface.__name__
        self.function_parameters = signature.parameters
        self.function_return = signature.return_annotation

        if hasattr(self.interface, "_asset_path"):
            self.asset_path = self.interface._asset_path
        elif hasattr(self.interface, "_parameter_name_prefix"):
            self.parameter_name_prefix = self.interface._parameter_name_prefix

    @property
    def field_name(self):
        return self.function_name

    @class_builder("Dependencies")
    def implement_dependencies_object(self):
        pass

    @class_builder("Inputs")
    def implement_inputs_object(self):
        self.pyGen.append_line(f"self.{self.field_name} = builder.load_MF(\"{self.asset_path}\", [], [])")

    @class_builder("Outputs")
    def implement_outputs_object(self):
        pass

    def begin_class(self, class_name):
        self.pyGen.begin_class(class_name, None)
        self.pyGen.begin_ctor(["builder: ContainerBuilderBase"])

    def end_class(self):
        self.pyGen.end_ctor()
        self.pyGen.end_class()

    def implement(self):
        self.parse_interface()

        self.pyGen = PyCodeGenerator()

        self.pyGen.append_import("unreal")
        self.pyGen.append_blank_line()
        self.pyGen.append_import_from("pamux_unreal_tools.base.container_builder_base", "ContainerBuilderBase")
        self.pyGen.append_blank_line()

        #self.implement_dependencies_object()
        self.implement_inputs_object()
        #self.implement_outputs_object()

        self.pyGen.print_code()
        # print(".")
        # print(self.asset_path)
        # print(self.parameter_name_prefix)
        # print(self.function_name)
        # print(self.function_parameters)
        # print(self.function_return)
        # print(".")
        # print("******************************************************************")
        # print(".")


ii = InterfaceImplementer(IBlendTwoMaterialsViaHighOpacityMap)
ii.implement()

# class Dependencies:
#         def __init__(self, builder: ContainerBuilderBase) -> None:
#              self.heightLerpWithTwoHeightMaps = builder.load_MF(
#                 "/Engine/Functions/Engine_MaterialFunctions02/Texturing/HeightLerpWithTwoHeightMaps",
#                 [ "Transistion Phase", "Height Texture 1", "Height Texture 2" ],
#                 [ "Alpha" ])