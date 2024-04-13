from pamux_engtools.apps.pamux_unreal_tools.tools.code_generators.py_code_generator import *
from pamux_engtools.apps.pamux_unreal_tools.tools.code_generators.base.method_params import *

from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.globals import *

class PropertyParam(MethodParam):
    def __init__(self, name: str, type: str = None, default_value: str = "None"):
        super().__init__(name, type, default_value)

    def append_assignment_lines(self, codeGen: PyCodeGenerator):
        codeGen.append_line(f"if {self.name} is not None:")
        codeGen.indent()
        codeGen.append_line(f"self.{self.name}.set({self.name})")
        codeGen.unindent()

class InputParam(MethodParam):
    def __init__(self, name: str, type: str = None, default_value: str = "None"):
        super().__init__(name, type, default_value)

    def append_assignment_lines(self, codeGen: PyCodeGenerator):
        codeGen.begin_if(f"{self.name} is not None")
        codeGen.append_line(f"self.{self.name}.comesFrom({self.name})")
        codeGen.end_if()

class ShouldAddRTParams(MethodParam):
    def __init__(self):
        super().__init__("shouldAddRTParams", "bool", "False")

    def append_assignment_lines(self, codeGen: PyCodeGenerator):
        codeGen.begin_if(f"shouldAddRTParams")
        func = lambda item: codeGen.append_line(f"self.{item}.add_rt()")
        MaterialAttributeFields.for_each(func, True,  ["Displacement"], "")
        codeGen.end_if()

class MakeMaterialAttributesParam(MethodParam):
    def __init__(self):
        super().__init__("materialAttributes", "BreakMaterialAttributes", "None")

    def append_assignment_lines(self, codeGen: PyCodeGenerator):
        codeGen.append_blank_line()
        codeGen.append_line(f"if {self.name} is not None:")
        codeGen.indent()
        func = lambda item: codeGen.append_line(f"self.{item}.comesFrom(materialAttributes.{item})")
        MaterialAttributeFields.for_each(func, True,  ["Displacement"], None)
        codeGen.unindent()

class RerouteInputParam(MethodParam):
    def __init__(self, name: str, type: str = None, default_value: str = "None"):
        super().__init__(name, type, default_value)

    def append_assignment_lines(self, codeGen: PyCodeGenerator):
        codeGen.begin_if(f"{self.name} is not None")
        codeGen.append_line(f"self.{self.name}.comesFrom({self.name})")
        codeGen.append_line(f"{self.name}.rt = self")
        codeGen.end_if()

class InputParamWithConstProperty(MethodParam):
    def __init__(self, name: str):
        super().__init__(name, None, "None")

    def append_assignment_lines(self, codeGen: PyCodeGenerator):
        codeGen.begin_if(f"{self.name} is not None")
        codeGen.begin_if(f"isinstance({self.name}, float)")
        codeGen.append_line(f"self.const_{self.name}.set({self.name})")
        codeGen.begin_else()
        codeGen.append_line(f"self.{self.name}.comesFrom({self.name})")
        codeGen.end_if()
        codeGen.end_if()
        
class RGBAMaskParam(MethodParam):
    def __init__(self):
        super().__init__("rgbaMask", "str", "None")

    def append_assignment_lines(self, codeGen: PyCodeGenerator):
        codeGen.begin_if(f"{self.name} is not None")
        codeGen.append_line(f"__mask = {self.name}.lower()")
        codeGen.append_line(f"self.r.set('r' in __mask)")
        codeGen.append_line(f"self.g.set('g' in __mask)")
        codeGen.append_line(f"self.b.set('b' in __mask)")
        codeGen.append_line(f"self.a.set('a' in __mask)")
        codeGen.begin_else()
        codeGen.append_line(f"self.r.set(True)")
        codeGen.append_line(f"self.g.set(True)")
        codeGen.append_line(f"self.b.set(False)")
        codeGen.append_line(f"self.a.set(False)")
        codeGen.end_if()

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
                         
    def append_assignment_lines(self, codeGen: PyCodeGenerator):
        for param in self.params:
            param.append_assignment_lines(codeGen)


def setup_ctor_params(pamux_wrapper_class_name):
    result = CTORParams()
    # if pamux_wrapper_class_name.endswith("Parameter"):
    #     if not pamux_wrapper_class_name in parameter_with_default_value_classes:
    #         if not pamux_wrapper_class_name in parameter_without_default_value_classes:
    #             print(pamux_wrapper_class_name)

    if pamux_wrapper_class_name in parameter_with_default_value_classes:
        result.append(PropertyParam("parameter_name", None, "None"))
        result.append(PropertyParam("default_value", None, "None"))

    elif pamux_wrapper_class_name in parameter_without_default_value_classes:
        result.append(PropertyParam("parameter_name", None, "None"))

    elif pamux_wrapper_class_name in unary_op_classes:
        result.append(InputParam("input", None, "None"))

    elif  pamux_wrapper_class_name == "BreakMaterialAttributes":
        result.append(InputParam("input", None, "None"))
        result.append(ShouldAddRTParams())

    elif pamux_wrapper_class_name == "StaticBool":
        result.append(PropertyParam('value', None, "None"))

    elif pamux_wrapper_class_name == "Desaturation":
        result.append(InputParam('input', None, "None"))
        result.append(InputParam('fraction', None, "None"))

    elif pamux_wrapper_class_name == "ComponentMask":
        result.append(InputParam("input", None, "None"))
        result.append(RGBAMaskParam())

    elif pamux_wrapper_class_name == "StaticSwitch":
        result.append(InputParam('true', None, "None"))
        result.append(InputParam('false', None, "None"))
        result.append(InputParam('value', None, "None"))

    elif pamux_wrapper_class_name == "TextureCoordinate":
        result.append(PropertyParam('u_tiling', None, "None"))
        result.append(PropertyParam('v_tiling', None, "None"))

    elif pamux_wrapper_class_name in binary_op_classes:
        result.append(InputParam("a", None, "None"))
        result.append(InputParam("b", None, "None"))

    elif pamux_wrapper_class_name in binary_op_classes_with_const:
        result.append(InputParamWithConstProperty("a"))
        result.append(InputParamWithConstProperty("b"))

    elif pamux_wrapper_class_name == "Constant":
        result.append(PropertyParam("r", None, "None"))

    elif pamux_wrapper_class_name == "Constant2Vector":
        result.append(PropertyParam("constant", None, "None"))

    elif pamux_wrapper_class_name == "Constant3Vector":
        result.append(PropertyParam("constant", None, "None"))

    elif pamux_wrapper_class_name == "Constant4Vector":
        result.append(PropertyParam("constant", None, "None"))

    elif pamux_wrapper_class_name == "TextureObject":
        result.append(PropertyParam("sampler_type", None, "None"))
        result.append(PropertyParam("texture", None, "None"))

    elif pamux_wrapper_class_name == "NamedRerouteDeclaration":
        result.append(PropertyParam("name", None, "None"))
        result.append(RerouteInputParam("input", None, "None"))
        #result.append(PropertyParam("variableGuid"))
        result.append(PropertyParam("nodeColor", None, "None"))

    elif pamux_wrapper_class_name == "NamedRerouteUsage":
        result.append(PropertyParam("declarationGuid", None, "None"))

    elif pamux_wrapper_class_name == "LinearInterpolate" or pamux_wrapper_class_name == "BlendMaterialAttributes":
        result.append(InputParamWithConstProperty("a"))
        result.append(InputParamWithConstProperty("b"))
        result.append(InputParamWithConstProperty("alpha"))

    elif pamux_wrapper_class_name == "Transform":
        result.append(InputParam("input", None, "None"))

    elif pamux_wrapper_class_name == "Power":
        result.append(InputParam("base", None, "None"))
        result.append(InputParam("exponent", None, "None"))

    elif pamux_wrapper_class_name == "LandscapeLayerWeight":
        result.append(PropertyParam("parameter_name", None, "None"))
        result.append(PropertyParam("preview_weight", "float", "None"))

    elif pamux_wrapper_class_name == "RuntimeVirtualTextureSampleParameter":
        result.append(PropertyParam("parameter_name", None, "None"))

    elif pamux_wrapper_class_name == "MakeMaterialAttributes":
        result.append(MakeMaterialAttributesParam())



    return result
