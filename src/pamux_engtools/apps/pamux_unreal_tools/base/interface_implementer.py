import unreal
from pathlib import Path
import sys
import os
import shutil
import ast
import types

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
from pamux_unreal_tools.examples.M_Landscape_Master.interfaces.IForestGround import IForestGround


from pamux_unreal_tools.tools.py_code_generator.main import *
from pamux_unreal_tools.tools.py_code_generator.method_params import *
from pamux_unreal_tools.utils.types import *

import functools
from typing import Any, Callable

type_to_function_output_map = { "SomeType": "varName" }
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

        self.field_name = self.function_name[1].lower() + self.function_name[2:]

        self.function_parameters = signature.parameters

        names = []
        for p in signature.parameters:
            names.append("'" +str(p) + "'")

        if len(names) == 0:
            self.function_inputs = ''
        else:
            self.function_inputs = ', '.join(names)

        names = []

        if isinstance(signature.return_annotation, types.GenericAlias):
            type_str = str(signature.return_annotation)
            if type_str.startswith("tuple"):
                type_str = type_str[len("tuple["):-1]

            for t in type_str.split(','):
                t = t.strip()
                t = t[t.rindex(".")+1:]

                if t.startswith("T"):
                    function_output_name = t[1].lower() + t[2:]
                elif t in type_to_function_output_map.keys():
                    function_output_name = type_to_function_output_map[t]
                else:
                    function_output_name = t

                names.append("'" + function_output_name + "'")
        else:
            names.append("'" + signature.return_annotation.__name__ + "'")

        if len(names) == 0:
            self.function_outputs = ''
        else:
            self.function_outputs = ', '.join(names)

        if hasattr(self.interface, "_asset_path"):
            self.asset_path = self.interface._asset_path
        elif hasattr(self.interface, "_parameter_name_prefix"):
            self.parameter_name_prefix = self.interface._parameter_name_prefix

    @class_builder("Dependencies")
    def implement_dependencies_object(self):
        self.pyGen.append_line(f"self.{self.field_name} = builder.load_MF(\"{self.asset_path}\", [], [])")


    @class_builder("Inputs")
    def implement_inputs_object(self):
        self.pyGen.append_line(f"self.{self.field_name} = builder.load_MF(\"{self.asset_path}\", [{self.function_inputs}], [{self.function_outputs}])")

    @class_builder("Outputs")
    def implement_outputs_object(self):
        self.pyGen.append_line(f"self.{self.field_name} = builder.load_MF(\"{self.asset_path}\", [], [])")

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

        self.implement_dependencies_object()
        self.implement_inputs_object()
        self.implement_outputs_object()

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


ii = InterfaceImplementer(IForestGround)
ii.implement()

# class Dependencies:
#         def __init__(self, builder: ContainerBuilderBase) -> None:
#              self.heightLerpWithTwoHeightMaps = builder.load_MF(
#                 "/Engine/Functions/Engine_MaterialFunctions02/Texturing/HeightLerpWithTwoHeightMaps",
#                 [ "Transistion Phase", "Height Texture 1", "Height Texture 2" ],
#                 [ "Alpha" ])