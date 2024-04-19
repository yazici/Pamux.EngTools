from pamux_unreal_tools.tools.code_generators.base.code_generator_base import *
from pamux_unreal_tools.tools.code_generators.base.method_params import MethodParam, MethodParams

from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.globals import *

class PropertyParam(MethodParam):
    def __init__(self, overload_id, name: str, type: str, default_value: str = "NULL"):
        super().__init__(overload_id, name, type, default_value)

    def append_assignment_lines(self, codeGen: CodeGeneratorBase):
        codeGen.append_line(f"if {self.name} is not None:")
        codeGen.indent()
        codeGen.append_line(f"self.{self.name}.set({self.name})")
        codeGen.unindent()

    def get_ctor_code(self):
        return f"properties.{self.field_name}.Set({self.parameter_name});"

class InputParam(MethodParam):
    def __init__(self, overload_id, name: str, ):
        super().__init__(overload_id, name, "MXOutputSocket&", None)

    def append_assignment_lines(self, codeGen: CodeGeneratorBase):
        codeGen.begin_if(f"{self.name} is not None")
        codeGen.append_line(f"self.{self.name}.comesFrom({self.name})")
        codeGen.end_if()

    def get_ctor_code(self):
        return f"inputs.{self.field_name}.ComesFrom({self.parameter_name});"

class RGBAMaskParam(MethodParam):
    def __init__(self, overload_id):
        super().__init__(overload_id, "rgbaMask", "FString", "NULL")

    def append_assignment_lines(self, codeGen: CodeGeneratorBase):
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

    def get_ctor_code(self):
        return f"""
        auto mask = _rgbaMask.ToLower();
        properties.r.Set(mask.Contains("r"));
        properties.g.Set(mask.Contains("g"));
        properties.b.Set(mask.Contains("b"));
        properties.a.Set(mask.Contains("a"));"""


class RerouteInputParam(MethodParam):
    def __init__(self, overload_id, name: str, type: str = None, default_value: str = "NULL"):
        super().__init__(overload_id, name, type, default_value)

    def append_assignment_lines(self, codeGen: CodeGeneratorBase):
        codeGen.begin_if(f"{self.name} is not None")
        codeGen.append_line(f"self.{self.name}.comesFrom({self.name})")
        codeGen.append_line(f"{self.name}.rt = self")
        codeGen.end_if()

    def get_ctor_code(self):
        return f"""
        auto mask = _rgbaMask.ToLower();
        properties.r.Set(mask.Contains("r"));
        properties.g.Set(mask.Contains("g"));
        properties.b.Set(mask.Contains("b"));
        properties.a.Set(mask.Contains("a"));"""

class ShouldAddRTParams(MethodParam):
    def __init__(self, overload_id):
        super().__init__(overload_id, "shouldAddRTParams", "bool", "False")

    def append_assignment_lines(self, codeGen: CodeGeneratorBase):
        codeGen.begin_if(f"shouldAddRTParams")
        func = lambda item: codeGen.append_line(f"self.{item}.add_rt()")
        MaterialAttributeFields.for_each(func, True,  ["Displacement"], "")
        codeGen.end_if()


class MakeMaterialAttributesParam(MethodParam):
    def __init__(self, overload_id):
        super().__init__(overload_id, "materialAttributes", "BreakMaterialAttributes", "NULL")

    def append_assignment_lines(self, codeGen: CodeGeneratorBase):
        codeGen.append_blank_line()
        codeGen.append_line(f"if {self.name} is not None:")
        codeGen.indent()
        func = lambda item: codeGen.append_line(f"self.{item}.comesFrom(materialAttributes.{item})")
        MaterialAttributeFields.for_each(func, True,  ["Displacement"], None)
        codeGen.unindent()



class InputParamWithConstProperty(MethodParam):
    def __init__(self, overload_id, name: str):
        super().__init__(overload_id, name, "MXOutputSocket *", "NULL")

    def append_assignment_lines(self, codeGen: CodeGeneratorBase):
        codeGen.begin_if(f"{self.name} is not None")
        codeGen.begin_if(f"isinstance({self.name}, float)")
        codeGen.append_line(f"self.const_{self.name}.set({self.name})")
        codeGen.begin_else()
        codeGen.append_line(f"self.{self.name}.comesFrom({self.name})")
        codeGen.end_if()
        codeGen.end_if()


def setup_ctor_params(pamux_wrapper_class_name) -> MethodParams:
    result = MethodParams()

    if pamux_wrapper_class_name in parameter_with_default_value_classes:
        result.append(PropertyParam(0, "parameter_name", "FString", "NULL"))
        result.append(PropertyParam(0, "default_value", "LinearColor", "NULL"))

    elif pamux_wrapper_class_name in parameter_without_default_value_classes:
        result.append(PropertyParam(0, "parameter_name", "FString", "NULL"))

    elif pamux_wrapper_class_name in unary_op_classes:
        result.append(InputParam(0, "input"))

    elif  pamux_wrapper_class_name == "BreakMaterialAttributes":
        result.append(InputParam(0, "input"))
        result.append(ShouldAddRTParams(0))

    elif  pamux_wrapper_class_name == "GetMaterialAttributes":
        result.append(InputParam(0, "materialAttributes"))

    elif pamux_wrapper_class_name == "LinearInterpolate":
        result.append(InputParam(10, "a"))
        result.append(InputParam(10, "b"))
        result.append(InputParam(10, "alpha"))

        result.append(PropertyParam(20, "const_a", "float"))
        result.append(InputParam(20, "b"))
        result.append(InputParam(20, "alpha"))

        result.append(InputParam(30, "a"))
        result.append(PropertyParam(30, "const_b", "float"))
        result.append(InputParam(30, "alpha"))

        result.append(PropertyParam(40, "const_a", "float"))
        result.append(PropertyParam(40, "const_b", "float"))
        result.append(InputParam(40, "alpha"))

    elif pamux_wrapper_class_name == "BlendMaterialAttributes":
        result.append(InputParam(10, "a"))
        result.append(InputParam(10, "b"))
        result.append(InputParam(10, "alpha"))

    elif pamux_wrapper_class_name in binary_op_classes:
        result.append(InputParam(0, "a"))
        result.append(InputParam(0, "b"))

    elif pamux_wrapper_class_name in binary_op_classes_with_const:
        result.append(InputParam(10, "a"))
        result.append(InputParam(10, "b"))

        result.append(PropertyParam(20, "const_a", "float"))
        result.append(InputParam(20, "b"))

        result.append(InputParam(30, "a"))
        result.append(PropertyParam(30, "const_b", "float"))

        result.append(PropertyParam(40, "const_a", "float"))
        result.append(PropertyParam(40, "const_b", "float"))

    elif pamux_wrapper_class_name == "StaticBool":
        result.append(PropertyParam(0, 'value', "bool", "NULL"))

    elif pamux_wrapper_class_name == "Desaturation":
        result.append(InputParam(0, 'input'))
        result.append(InputParam(0, 'fraction'))

    elif pamux_wrapper_class_name == "ComponentMask":
        result.append(InputParam(0, "input"))
        result.append(RGBAMaskParam(0))

    elif pamux_wrapper_class_name == "StaticSwitch":
        result.append(InputParam(0, 'true'))
        result.append(InputParam(0, 'false'))
        result.append(InputParam(0, 'value'))

    elif pamux_wrapper_class_name == "TextureCoordinate":
        result.append(PropertyParam(0, 'u_tiling', "float", "NULL"))
        result.append(PropertyParam(0, 'v_tiling', "float", "NULL"))

    elif pamux_wrapper_class_name == "Constant":
        result.append(PropertyParam(0, "r", "float", "NULL"))

    elif pamux_wrapper_class_name == "Constant2Vector":
        result.append(PropertyParam(0, "constant", "FVector2f", "NULL"))

    elif pamux_wrapper_class_name == "Constant3Vector":
        result.append(PropertyParam(0, "constant", "FVector3f", "NULL"))

    elif pamux_wrapper_class_name == "Constant4Vector":
        result.append(PropertyParam(0, "constant", "FVector4f", "NULL"))

    elif pamux_wrapper_class_name == "TextureObject":
        result.append(PropertyParam(0, "sampler_type", "EMaterialSamplerType", "NULL"))
        result.append(PropertyParam(0, "texture", "UTexture*", "NULL"))

    elif pamux_wrapper_class_name == "NamedRerouteDeclaration":
        result.append(PropertyParam(0, "name", "FName", "NULL"))
        result.append(InputParam(0, "input"))
        # result.append(PropertyParam(0, "variableGuid", "FGuid"))
        result.append(PropertyParam(0, "nodeColor", "FLinearColor", "NULL"))

    elif pamux_wrapper_class_name == "NamedRerouteUsage":
        result.append(PropertyParam(0, "declarationGuid", "FString", "NULL"))

    elif pamux_wrapper_class_name == "Transform":
        result.append(InputParam(0, "input"))

    elif pamux_wrapper_class_name == "Power":
        result.append(InputParam(0, "base"))
        result.append(InputParam(0, "exponent"))

    elif pamux_wrapper_class_name == "LandscapeLayerWeight":
        result.append(PropertyParam(0, "parameter_name", "FString", "NULL"))
        result.append(PropertyParam(0, "preview_weight", "float", "NULL"))

    elif pamux_wrapper_class_name == "RuntimeVirtualTextureSampleParameter":
        result.append(PropertyParam(0, "parameter_name", "FString", "NULL"))

    elif pamux_wrapper_class_name == "MakeMaterialAttributes":
        result.append(MakeMaterialAttributesParam(0))

    return result
