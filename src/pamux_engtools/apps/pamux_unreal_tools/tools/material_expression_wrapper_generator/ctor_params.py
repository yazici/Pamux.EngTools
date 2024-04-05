from pamux_unreal_tools.tools.py_code_generator.main import *
from pamux_unreal_tools.tools.py_code_generator.method_params import *

from pamux_unreal_tools.tools.material_expression_wrapper_generator.globals import *

class PropertyParam(MethodParam):
    def __init__(self, name: str, type: str = None, default_value: str = "None"):
        super().__init__(name, type, default_value)

    def append_assignment_lines(self, pyGen: PyCodeGenerator):
        pyGen.append_line(f"if {self.name} is not None:")
        pyGen.indent()
        pyGen.append_line(f"self.{self.name}.set({self.name})")
        pyGen.unindent()

class InputParam(MethodParam):
    def __init__(self, name: str, type: str = None, default_value: str = "None"):
        super().__init__(name, type, default_value)

    def append_assignment_lines(self, pyGen: PyCodeGenerator):
        pyGen.begin_if(f"{self.name} is not None")
        pyGen.append_line(f"self.{self.name}.comesFrom({self.name})")
        pyGen.end_if()

class RerouteInputParam(MethodParam):
    def __init__(self, name: str, type: str = None, default_value: str = "None"):
        super().__init__(name, type, default_value)

    def append_assignment_lines(self, pyGen: PyCodeGenerator):
        pyGen.begin_if(f"{self.name} is not None")
        pyGen.append_line(f"self.{self.name}.comesFrom({self.name})")
        pyGen.append_line(f"{self.name}.rt = self")
        pyGen.end_if()

class InputParamWithConstProperty(MethodParam):
    def __init__(self, name: str):
        super().__init__(name)

    def append_assignment_lines(self, pyGen: PyCodeGenerator):
        pyGen.begin_if(f"{self.name} is not None")
        pyGen.begin_if(f"isinstance({self.name}, float)")
        pyGen.append_line(f"self.const_{self.name}.set({self.name})")
        pyGen.begin_else()
        pyGen.append_line(f"self.{self.name}.comesFrom({self.name})")
        pyGen.end_if()
        pyGen.end_if()
        
class RGBAMaskParam(MethodParam):
    def __init__(self):
        super().__init__("rgbaMask", "str", "None")

    def append_assignment_lines(self, pyGen: PyCodeGenerator):
        pyGen.begin_if(f"{self.name} is not None")
        pyGen.append_line(f"__mask = {self.name}.lower()")
        pyGen.append_line(f"self.r.set('r' in __mask)")
        pyGen.append_line(f"self.g.set('g' in __mask)")
        pyGen.append_line(f"self.b.set('b' in __mask)")
        pyGen.append_line(f"self.a.set('a' in __mask)")
        pyGen.begin_else()
        pyGen.append_line(f"self.r.set(True)")
        pyGen.append_line(f"self.g.set(True)")
        pyGen.append_line(f"self.b.set(False)")
        pyGen.append_line(f"self.a.set(False)")
        pyGen.end_if()

class CTORParams:
    def __init__(self) -> None:
        self.params = list()

    def append(self, param: MethodParam) -> None:
        self.params.append(param)

    @property
    def declaration_code(self) -> str:
        codes = [ "self" ]
        for param in self.params:
            codes.append(param.code)

        codes.append("node_pos: NodePos = None")
        return codes
                         
    def append_assignment_lines(self, pyGen: PyCodeGenerator):
        for param in self.params:
            param.append_assignment_lines(pyGen)


def setup_ctor_params(pamux_wrapper_class_name):
    result = CTORParams()
    if pamux_wrapper_class_name.endswith("Parameter"):
        if not pamux_wrapper_class_name in parameter_with_default_value_classes:
            if not pamux_wrapper_class_name in parameter_without_default_value_classes:
                print(pamux_wrapper_class_name)

    if pamux_wrapper_class_name in parameter_with_default_value_classes:
        result.append(PropertyParam("parameter_name"))
        result.append(PropertyParam("default_value"))

    elif pamux_wrapper_class_name in parameter_without_default_value_classes:
        result.append(PropertyParam("parameter_name"))
    elif pamux_wrapper_class_name in unary_op_classes:
        result.append(InputParam("input"))

    elif pamux_wrapper_class_name == "StaticBool":
        result.append(PropertyParam('value'))

    elif pamux_wrapper_class_name == "ComponentMask":
        result.append(InputParam("input"))
        result.append(RGBAMaskParam())

    elif pamux_wrapper_class_name == "StaticSwitch":
        result.append(InputParam('true'))
        result.append(InputParam('false'))
        result.append(InputParam('value'))

    elif pamux_wrapper_class_name == "TextureCoordinate":
        result.append(PropertyParam('u_tiling'))
        result.append(PropertyParam('v_tiling'))

    elif pamux_wrapper_class_name in binary_op_classes:
        result.append(InputParam("a"))
        result.append(InputParam("b"))

    elif pamux_wrapper_class_name in binary_op_classes_with_const:
        result.append(InputParamWithConstProperty("a"))
        result.append(InputParamWithConstProperty("b"))

    elif pamux_wrapper_class_name == "Constant":
        result.append(PropertyParam("r"))

    elif pamux_wrapper_class_name == "Constant2Vector":
        result.append(PropertyParam("constant"))

    elif pamux_wrapper_class_name == "Constant3Vector":
        result.append(PropertyParam("constant"))

    elif pamux_wrapper_class_name == "Constant4Vector":
        result.append(PropertyParam("constant"))

    elif pamux_wrapper_class_name == "TextureObject":
        result.append(PropertyParam("sampler_type"))
        result.append(PropertyParam("texture"))

    elif pamux_wrapper_class_name == "NamedRerouteDeclaration":
        result.append(PropertyParam("name"))
        result.append(RerouteInputParam("input", None, "None"))
        #result.append(PropertyParam("variableGuid"))
        result.append(PropertyParam("nodeColor", None))

    elif pamux_wrapper_class_name == "NamedRerouteUsage":
        result.append(PropertyParam("declarationGuid"))

    elif pamux_wrapper_class_name == "LinearInterpolate" or pamux_wrapper_class_name == "BlendMaterialAttributes":
        result.append(InputParamWithConstProperty("a"))
        result.append(InputParamWithConstProperty("b"))
        result.append(InputParamWithConstProperty("alpha"))

    elif pamux_wrapper_class_name == "Transform":
        result.append(InputParam("input"))

    return result