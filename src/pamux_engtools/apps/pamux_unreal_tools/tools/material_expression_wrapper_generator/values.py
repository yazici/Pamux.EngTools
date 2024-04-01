from pamux_unreal_tools.tools.material_expression_wrapper_generator.globals import *

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

    def to_py(self, ctor, pyGen):
        appended = False
        for item in self.__items:
            field_name = item.field_name(ctor)
            if not appended:
                pyGen.append_blank_line()
                appended = True
            pyGen.append_line(f"self.{field_name} = {ctor}(self, '{item.name}', '{item.type}')")
