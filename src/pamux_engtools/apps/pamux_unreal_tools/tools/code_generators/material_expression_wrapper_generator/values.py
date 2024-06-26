from pamux_unreal_tools.tools.code_generators.material_expression_wrapper_generator.globals import *

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
            
            if self.name == "Default" or self.name == "True" or self.name == "False":
                return "_" + self.name[0:1].lower() + self.name[1:]
            

            return self.name[0:1].lower() + self.name[1:]
        
        if ctor == "InSocket":
            return "input"
        if ctor == "OutSocket":
            return "output"
        return "X"
        
    @property
    def traits_type(self):
        if self.type == "str":
            return "TString"
        if self.type == "bool":
            return "TStaticBool"
        if self.type == "float":
            return "TFloat"
        if self.type == "int32":
            return "TInt32"
        if self.type == "LinearColor":
            return "TLinearColor"
        
        if self.type == "Name":
            return "TName"
        if self.type == "StructProperty":
            return None
        if self.type == "MaterialVectorCoordTransformSource":
            return "TMaterialVectorCoordTransformSource"
        if self.type == "MaterialVectorCoordTransform":
            return "TMaterialVectorCoordTransform"
        if self.type == "MaterialAttributeBlend":
            return "TMaterialAttributeBlend"
        if self.type == "MaterialFunctionInterface":
            return "TMaterialFunctionInterface"
        
        if self.type == "Array[Guid]":
            return "TGuidArray"
        
        return self.type

    @property
    def cpp_type(self):
        if self.type == "str":
            return "const char*"
        if self.type == "int32":
            return "int32_t"
        return self.type

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

class PropertyInfo(Value):
    def __init__(self, name, type, notes = ""):
        super().__init__(name, type, notes)


class InputSocketInfo(Value):
    def __init__(self, name, type, notes = ""):
        super().__init__(name, type, notes)

class OutputSocketInfo(Value):
    def __init__(self, name, type, notes = ""):
        super().__init__(name, type, notes)

class Values:
    def __init__(self):
        self.__items = []

    def append(self, item):
        self.__items.append(item)

    @property
    def is_empty(self):
        return len(self.__items) == 0
    
    @property
    def items(self):
        return self.__items

    def to_py(self, ctor, codeGen):
        appended = False
        for item in self.__items:
            field_name = item.field_name(ctor)

            if ctor == "MaterialExpressionEditorPropertyImpl":
                if field_name == "desc" or field_name.startswith("material_expression_editor_"):
                    continue
            elif ctor == "InSocketImpl":
                if field_name == "input":
                    continue
            elif ctor == "OutSocketImpl":
                if field_name == "output":
                    continue

            if not appended:
                codeGen.append_blank_line()
                appended = True
            codeGen.append_line(f"self.{field_name} = {ctor}(self, '{item.name}', '{item.type}')")
