# py "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/tools/generate_material_expressions_wrappers.py"
# https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-expressions-reference
import unreal
import os
import inspect
import types

import json
dump_folder = "C:/src/UNrealEngineClassDump/Class/Script"
py_out_filepath = "C:/src/Pamux.EngTools/src/pamux_engtools/apps/pamux_unreal_tools/generated/material_expression_wrappers.py"

class Value:
    def __init__(self, name, type, notes = ""):
        self.name = name
        self.type = type
        self.notes = notes
        self.underscorelessName = ""

        if "_" in self.name:
            for part in name.split("_"):
                self.underscorelessName += part[0:1].upper() + part[1:] + " "
        else:
            self.underscorelessName = self.name[0:1].upper() + self.name[1:]
        self.underscorelessName = self.underscorelessName.strip()

    def field_name(self, ctor):
        if self.name != "":
            if self.name == "UVs" or self.name == "ID" or self.name.startswith("RGB"):
                return self.name
            return self.name[0:1].lower() + self.name[1:]
        if ctor == "InSocket":
            return "input"
        elif ctor == "OutSocket":
            return "output"

    @property
    def is_input(self):
        return self.type == "StructProperty"

    @property
    def is_output(self):
        return False

    @property
    def is_property(self):
        return self.type == "ObjectProperty" or True
    
    @property
    def is_container(self):
        return self.type == "ObjectProperty" and (self.name == "Material" or self.name == "Function")

class Values:
    def __init__(self):
        self.__items = []

    def append(self, item):
        self.__items.append(item)

    @property
    def is_empty(self):
        return len(self.__items) == 0

    def to_py(self, ctor):
        result = ""

        for item in self.__items:
            result += (f"\n        self.{item.field_name(ctor)} = {ctor}(self, '{item.name}', '{item.type}')")  

        return result

class UnrealDump:
    def __init__(self, full_path):
        self.full_path = full_path.replace("\\", "/")
        self.lines = []
        self.class_path = None
        self.base_class_path = None

        self.inputs = Values()
        self.outputs = Values()
        self.properties = Values()

        with open(full_path, "rt") as file:
            for line in file.readlines():
                line = line.strip()
                if line == "":
                    continue
                
                if line.startswith("/"):
                    self.class_path = line
                    midx = self.class_path.find("MaterialExpression")

                    self.pamux_name = self.class_path[midx + len("MaterialExpression"):]
                    continue

                parts = line.split(" ")
                if len(parts) != 2:
                    self.lines.append(line)
                    continue

                value = Value(parts[0], parts[1].strip("()"))

                if value.is_container:
                    continue
                if value.is_input:
                    self.inputs.append(value)
                elif value.is_output:
                    self.outputs.append(value)
                elif value.is_property:
                    self.properties.append(value)

material_expressions_dump_data = {}

def read_dump_data():
    for path, subdirs, files in os.walk(dump_folder):
        for file in files:
            if not file.startswith("Engine.MaterialExpression"):
                #print(file)
                continue
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path):
                if "Brickadia" in full_path:
                    continue
                if "Engine" not in file:
                    continue
                if "MaterialExpression" not in file:
                    continue
                ud = UnrealDump(full_path)
                material_expressions_dump_data[ud.pamux_name] = ud

input_only_classes = []
output_only_classes = []

def setup_input_sockets(pamux_wrapper_class_name):
    result = Values()

    if pamux_wrapper_class_name in output_only_classes:
        return result

    if pamux_wrapper_class_name == "TextureSample":
        result.append(Value('UVs', 'StructProperty'))
        result.append(Value('Tex', 'StructProperty'))
        result.append(Value('ApplyViewMipBias', 'StructProperty'))

    elif pamux_wrapper_class_name == "AntialiasedTextureMask":
        result.append(Value('UVs', 'StructProperty'))
        result.append(Value('ApplyViewMipBias', 'StructProperty'))

    elif pamux_wrapper_class_name == "Saturate":
        result.append(Value('', 'StructProperty'))

    elif pamux_wrapper_class_name == "ComponentMask":
        result.append(Value('', 'StructProperty'))

    elif pamux_wrapper_class_name == "SetMaterialAttributes":
        result.append(Value('MaterialAttributes', 'StructProperty'))

        result.append(Value('BaseColor', 'StructProperty'))
        result.append(Value('Metallic', 'StructProperty'))
        result.append(Value('Specular', 'StructProperty'))
        result.append(Value('Roughness', 'StructProperty'))
        result.append(Value('Anisotropy', 'StructProperty'))
        result.append(Value('EmissiveColor', 'StructProperty'))
        result.append(Value('Opacity', 'StructProperty'))
        result.append(Value('OpacityMask', 'StructProperty'))
        result.append(Value('Normal', 'StructProperty'))
        result.append(Value('Tangent', 'StructProperty'))
        result.append(Value('WorldPositionOffset', 'StructProperty'))
        result.append(Value('WorldDisplacement', 'StructProperty'))
        result.append(Value('TessellationMultiplier', 'StructProperty'))
        result.append(Value('SubsurfaceColor', 'StructProperty'))
        result.append(Value('ClearCoat', 'StructProperty'))
        result.append(Value('ClearCoatRoughness', 'StructProperty'))
        result.append(Value('AmbientOcclusion', 'StructProperty'))
        result.append(Value('Refraction', 'StructProperty'))
        result.append(Value('CustomizedUVs', 'StructProperty'))
        result.append(Value('PixelDepthOffset', 'StructProperty'))
        result.append(Value('ShadingModel', 'StructProperty'))

    elif pamux_wrapper_class_name == "MakeMaterialAttributes":
        result.append(Value('BaseColor', 'StructProperty'))
        result.append(Value('Metallic', 'StructProperty'))
        result.append(Value('Specular', 'StructProperty'))
        result.append(Value('Roughness', 'StructProperty'))
        result.append(Value('Anisotropy', 'StructProperty'))
        result.append(Value('EmissiveColor', 'StructProperty'))
        result.append(Value('Opacity', 'StructProperty'))
        result.append(Value('OpacityMask', 'StructProperty'))
        result.append(Value('Normal', 'StructProperty'))
        result.append(Value('Tangent', 'StructProperty'))
        result.append(Value('WorldPositionOffset', 'StructProperty'))
        # result.append(Value('WorldDisplacement', 'StructProperty'))
        #result.append(Value('TessellationMultiplier', 'StructProperty'))
        result.append(Value('SubsurfaceColor', 'StructProperty'))
        result.append(Value('ClearCoat', 'StructProperty'))
        result.append(Value('ClearCoatRoughness', 'StructProperty'))
        result.append(Value('AmbientOcclusion', 'StructProperty'))
        result.append(Value('Refraction', 'StructProperty'))
        result.append(Value('CustomizedUV_0', 'StructProperty'))
        result.append(Value('CustomizedUV_1', 'StructProperty'))
        result.append(Value('CustomizedUV_2', 'StructProperty'))
        result.append(Value('CustomizedUV_3', 'StructProperty'))
        result.append(Value('CustomizedUV_4', 'StructProperty'))
        result.append(Value('CustomizedUV_5', 'StructProperty'))
        result.append(Value('CustomizedUV_6', 'StructProperty'))
        result.append(Value('CustomizedUV_7', 'StructProperty'))
        result.append(Value('PixelDepthOffset', 'StructProperty'))
        result.append(Value('ShadingModel', 'StructProperty'))
        result.append(Value('Displacement', 'StructProperty'))
    elif pamux_wrapper_class_name == "BreakMaterialAttributes":
        result.append(Value('', 'StructProperty'))

    elif pamux_wrapper_class_name == "GetMaterialAttributes":
        result.append(Value('', 'StructProperty'))

    elif pamux_wrapper_class_name == "OneMinus":
        result.append(Value('', 'StructProperty'))

    elif pamux_wrapper_class_name == "Desaturation":
        result.append(Value('', 'StructProperty'))
        result.append(Value('Fraction', 'StructProperty'))
    
    elif pamux_wrapper_class_name in material_expressions_dump_data:
         result = material_expressions_dump_data[pamux_wrapper_class_name].inputs

    if result.is_empty:
        result.append(Value("", "StructProperty"))
        
    return result

def setup_output_sockets(pamux_wrapper_class_name):
    result = Values()

    if pamux_wrapper_class_name in input_only_classes:
        return result

    if pamux_wrapper_class_name == "TextureSample":
        result.append(Value('RGB', 'StructProperty'))
        result.append(Value('R', 'StructProperty'))
        result.append(Value('G', 'StructProperty'))
        result.append(Value('B', 'StructProperty'))
        result.append(Value('A', 'StructProperty'))
        result.append(Value('RGBA', 'StructProperty'))

    elif pamux_wrapper_class_name == "GetMaterialAttributes":
        result.append(Value('MaterialAttributes', 'StructProperty'))

        result.append(Value('BaseColor', 'StructProperty'))
        result.append(Value('Metallic', 'StructProperty'))
        result.append(Value('Specular', 'StructProperty'))
        result.append(Value('Roughness', 'StructProperty'))
        result.append(Value('Anisotropy', 'StructProperty'))
        result.append(Value('EmissiveColor', 'StructProperty'))
        result.append(Value('Opacity', 'StructProperty'))
        result.append(Value('OpacityMask', 'StructProperty'))
        result.append(Value('Normal', 'StructProperty'))
        result.append(Value('Tangent', 'StructProperty'))
        result.append(Value('WorldPositionOffset', 'StructProperty'))
        result.append(Value('WorldDisplacement', 'StructProperty'))
        result.append(Value('TessellationMultiplier', 'StructProperty'))
        result.append(Value('SubsurfaceColor', 'StructProperty'))
        result.append(Value('ClearCoat', 'StructProperty'))
        result.append(Value('ClearCoatRoughness', 'StructProperty'))
        result.append(Value('AmbientOcclusion', 'StructProperty'))
        result.append(Value('Refraction', 'StructProperty'))
        result.append(Value('CustomizedUVs', 'StructProperty'))
        result.append(Value('PixelDepthOffset', 'StructProperty'))
        result.append(Value('ShadingModel', 'StructProperty'))

    elif pamux_wrapper_class_name == "BreakMaterialAttributes":
        result.append(Value('BaseColor', 'StructProperty'))
        result.append(Value('Metallic', 'StructProperty'))
        result.append(Value('Specular', 'StructProperty'))
        result.append(Value('Roughness', 'StructProperty'))
        result.append(Value('Anisotropy', 'StructProperty'))
        result.append(Value('EmissiveColor', 'StructProperty'))
        result.append(Value('Opacity', 'StructProperty'))
        result.append(Value('OpacityMask', 'StructProperty'))
        result.append(Value('Normal', 'StructProperty'))
        result.append(Value('Tangent', 'StructProperty'))
        result.append(Value('WorldPositionOffset', 'StructProperty'))
        # result.append(Value('WorldDisplacement', 'StructProperty'))
        #result.append(Value('TessellationMultiplier', 'StructProperty'))
        result.append(Value('SubsurfaceColor', 'StructProperty'))
        result.append(Value('ClearCoat', 'StructProperty'))
        result.append(Value('ClearCoatRoughness', 'StructProperty'))
        result.append(Value('AmbientOcclusion', 'StructProperty'))
        result.append(Value('Refraction', 'StructProperty'))
        result.append(Value('CustomizedUV0', 'StructProperty'))
        result.append(Value('CustomizedUV1', 'StructProperty'))
        result.append(Value('CustomizedUV2', 'StructProperty'))
        result.append(Value('CustomizedUV3', 'StructProperty'))
        result.append(Value('CustomizedUV4', 'StructProperty'))
        result.append(Value('CustomizedUV5', 'StructProperty'))
        result.append(Value('CustomizedUV6', 'StructProperty'))
        result.append(Value('CustomizedUV7', 'StructProperty'))
        result.append(Value('PixelDepthOffset', 'StructProperty'))
        result.append(Value('ShadingModel', 'StructProperty'))
        result.append(Value('Displacement', 'StructProperty'))

    elif pamux_wrapper_class_name == "MakeMaterialAttributes":
        result.append(Value('', 'StructProperty'))

    elif pamux_wrapper_class_name == "VectorParameter":
        result.append(Value('', 'StructProperty'))
        result.append(Value('r', 'StructProperty'))
        result.append(Value('g', 'StructProperty'))
        result.append(Value('b', 'StructProperty'))
        result.append(Value('a', 'StructProperty'))

    elif pamux_wrapper_class_name in material_expressions_dump_data:
        result = material_expressions_dump_data[pamux_wrapper_class_name].outputs

    if result.is_empty:
        result.append(Value("", "StructProperty"))

    return result

def setup_properties(doc):
    is_in_editor_properties = False
    result = Values()
    for doc_line in doc.split("\n"):
        if "Editor Properties" in doc_line:
            is_in_editor_properties = True
            continue

        if not is_in_editor_properties:
            continue

        doc_line = doc_line.strip()
        if not doc_line.startswith("-"):
            continue

        col = doc_line.find(":")
        if col == -1:
            print(doc_line)
            continue

        left = doc_line[0:col].strip().strip("-").strip().strip("`")
        notes = doc_line[col+1:].strip()

        col = left.find("`")
        if col == -1:
            print(doc_line)
            continue

        name = left[0:col]
        type = left[col+2:].strip().strip("()")

        if "[Read-Write]" in notes:
            is_rw = True
            notes = notes.replace("[Read-Write]", "")
        else:
            print(notes)

        if name != "material_expression_editor_x" and name != "material_expression_editor_y":
            result.append(Value(name, type, notes))

    if result.is_empty:
        result.append(Value("desc", "str"))
        
    return result

class CTORParams:
    class Param:
        def __init__(self, name, type):
            self.name = name
            self.type = type

    def __init__(self):
        self.params = []

    def appendProperty(self, name):
        self.params.append(CTORParams.Param(name, "property"))

    def appendInput(self, name):
        self.params.append(CTORParams.Param(name, "input"))

    def appendInputOrConst(self, name):
        self.params.append(CTORParams.Param(name, "iorc"))

    def declare(self):
        result = ""
        for param in self.params:
            result += f", {param.name} = None"
        return result
    
    def assign(self):
        result = ""
        for param in self.params:
            if param.type == "property":
                result += f"\n        if {param.name} is not None: self.{param.name}.set({param.name})"
            elif param.type == "input":
                result += f"\n        if {param.name} is not None: self.{param.name}.comesFrom({param.name})"
            elif param.type == "iorc":
                result += f"\n        if {param.name} is not None:"
                result += f"\n           if isinstance({param.name}, float):"
                result += f"\n              self.const_{param.name}.set({param.name})"
                result += f"\n           else:"
                result += f"\n              self.{param.name}.comesFrom({param.name})"
        return result
    
parameter_with_default_value_classes = [
    "StaticBoolParameter",
    "ScalarParameter",
    "StaticSwitchParameter",
    "VectorParameter",
    "ChannelMaskParameter",
    "CurveAtlasRowParameter",
    "DoubleVectorParameter"]

binary_op_classes = []

binary_op_classes_with_const = [
    "Add",
    "Multiply",
    "Subtract",
    "Divide",
    "Max",
    "Min"
]

unary_op_classes = [
    "Saturate",
    "OneMinus",
    "ComponentMask",
    "BreakMaterialAttributes"
]

def setup_ctor_params(pamux_wrapper_class_name):
    result = CTORParams()

    if pamux_wrapper_class_name in parameter_with_default_value_classes:
        result.appendProperty("parameter_name")
        result.appendProperty("default_value")
    elif pamux_wrapper_class_name in unary_op_classes:
        result.appendInput("input")
    elif pamux_wrapper_class_name in binary_op_classes:
        result.appendInput("a")
        result.appendInput("b")
    elif pamux_wrapper_class_name in binary_op_classes_with_const:
        result.appendInputOrConst("a")
        result.appendInputOrConst("b")
    elif pamux_wrapper_class_name == "Constant":
        result.appendProperty("r")
    elif pamux_wrapper_class_name == "LinearInterpolate" or pamux_wrapper_class_name == "BlendMaterialAttributes":
        result.appendInput("a")
        result.appendInput("b")
        result.appendInput("alpha")

    return result


def get_custom_code(pamux_wrapper_class_name):
    if pamux_wrapper_class_name == "FunctionInput":
        return """
    @staticmethod
    def create(input_name, input_type, preview):
        result = FunctionInput()
        result.input_name.set(input_name)
        result.input_type.set(input_type)

        if isinstance(preview, float):
            preview = Constant(preview)

        result.preview.comesFrom(preview)
        return result
"""
    if pamux_wrapper_class_name == "MakeMaterialAttributes":
        return """
    @staticmethod
    def create(materialAttributes):
        result = MakeMaterialAttributes()
        result.baseColor.comesFrom(materialAttributes.baseColor)
        result.metallic.comesFrom(materialAttributes.metallic)
        result.specular.comesFrom(materialAttributes.specular)
        result.roughness.comesFrom(materialAttributes.roughness)
        result.anisotropy.comesFrom(materialAttributes.anisotropy)
        result.emissiveColor.comesFrom(materialAttributes.emissiveColor)
        result.opacity.comesFrom(materialAttributes.opacity)
        result.opacityMask.comesFrom(materialAttributes.opacityMask)
        result.normal.comesFrom(materialAttributes.normal)
        result.tangent.comesFrom(materialAttributes.tangent)
        result.worldPositionOffset.comesFrom(materialAttributes.worldPositionOffset)
        result.subsurfaceColor.comesFrom(materialAttributes.subsurfaceColor)
        result.clearCoat.comesFrom(materialAttributes.clearCoat)
        result.clearCoatRoughness.comesFrom(materialAttributes.clearCoatRoughness)
        result.ambientOcclusion.comesFrom(materialAttributes.ambientOcclusion)
        result.refraction.comesFrom(materialAttributes.refraction)
        result.customizedUV_0.comesFrom(materialAttributes.customizedUV0)
        result.customizedUV_1.comesFrom(materialAttributes.customizedUV1)
        result.customizedUV_2.comesFrom(materialAttributes.customizedUV2)
        result.customizedUV_3.comesFrom(materialAttributes.customizedUV3)
        result.customizedUV_4.comesFrom(materialAttributes.customizedUV4)
        result.customizedUV_5.comesFrom(materialAttributes.customizedUV5)
        result.customizedUV_6.comesFrom(materialAttributes.customizedUV6)
        result.customizedUV_7.comesFrom(materialAttributes.customizedUV7)
        result.pixelDepthOffset.comesFrom(materialAttributes.pixelDepthOffset)
        result.shadingModel.comesFrom(materialAttributes.shadingModel)
        result.displacement.comesFrom(materialAttributes.displacement)
        return result
"""

    return None

def write_pamux_wrapper_class(py_file, c):
    pamux_wrapper_class_name = c.__name__[len("MaterialExpression"):]

    py_file.write("\n")

    inputs = setup_input_sockets(pamux_wrapper_class_name)
    outputs = setup_output_sockets(pamux_wrapper_class_name)
    properties = setup_properties(c.__doc__)
    ctor_params = setup_ctor_params(pamux_wrapper_class_name)
    custom_code = get_custom_code(pamux_wrapper_class_name)

    py_file.write("\n")
    py_file.write(f"class {pamux_wrapper_class_name}(MaterialExpression):")
    py_file.write("\n")
    py_file.write(f"    def __init__(self{ctor_params.declare()}, node_pos_x = 0, node_pos_y = 0):")
    py_file.write("\n")
    py_file.write(f"        super().__init__(unreal.{c.__name__}, node_pos_x, node_pos_y)")
    py_file.write("\n")
    py_file.write("\n")
    py_file.write(f"        # Properties")
    py_file.write(properties.to_py("Property"))
    py_file.write("\n")
    py_file.write("\n")

    py_file.write(f"        # Input Sockets")
    py_file.write(inputs.to_py("InSocket"))
    py_file.write("\n")
    py_file.write("\n")

    py_file.write(f"        # Output Sockets")
    py_file.write(outputs.to_py("OutSocket"))
    py_file.write("\n")
    py_file.write(f"{ctor_params.assign()}")

    if custom_code is not None:
        py_file.write(custom_code)

# See unreal.py
# many are deprecated: 'MaterialExpressionDisjointOver' was renamed to 'MaterialExpressionMaterialXDisjointOver'.
skip_these_classes= [    
    "MaterialExpressionAppend3Vector",
    "MaterialExpressionAppend4Vector",
    "MaterialExpressionBurn",
    "MaterialExpressionDifference",
    "MaterialExpressionDisjointOver",
    "MaterialExpressionDodge",
    "MaterialExpressionFractal3D",
    "MaterialExpressionIn",
    "MaterialExpressionLuminance",
    "MaterialExpressionMask",
    "MaterialExpressionMatte",
    "MaterialExpressionMinus",
    "MaterialExpressionOut",
    "MaterialExpressionOver",
    "MaterialExpressionOverlay",
    "MaterialExpressionPlace2D",
    "MaterialExpressionPlus",
    "MaterialExpressionPremult",
    "MaterialExpressionRampLeftRight",
    "MaterialExpressionRampTopBottom",
    "MaterialExpressionRemap",
    "MaterialExpressionRotate2D",
    "MaterialExpressionScreen",
    "MaterialExpressionSplitLeftRight",
    "MaterialExpressionSplitTopBottom",
    "MaterialExpressionTextureSampleParameterBlur",
    "MaterialExpressionUnpremult",
    "MaterialExpressionTerrainLayerCoords",
    "MaterialExpressionTerrainLayerSwitch",
    "MaterialExpressionTerrainLayerWeight",
    "MaterialExpressionMaterialXExponential",
    "MaterialExpressionMaterialXHsvToRgb",
    "MaterialExpressionMaterialXLength",
    "MaterialExpressionMaterialXLogarithm",
    "MaterialExpressionMaterialXRgbToHsv",
    "MaterialExpressionRamp4"
]

skip_these_classes = []
def create_py_from_unreal_module():
    with open(py_out_filepath, "w+t") as py_file:

        py_file.write("# This file is generated. Please do NOT modify.")
        py_file.write("\n")
        py_file.write("\n")
        py_file.write("import unreal")
        py_file.write("\n")
        py_file.write("\n")
        py_file.write("from pamux_unreal_tools.material_expression import MaterialExpression")
        py_file.write("\n")
        py_file.write("from pamux_unreal_tools.base.material_expression_container import *")
        py_file.write("\n")


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
            write_pamux_wrapper_class(py_file, c)

read_dump_data()
print(material_expressions_dump_data)
create_py_from_unreal_module()


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
