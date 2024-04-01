import os
from pamux_unreal_tools.tools.material_expression_wrapper_generator.globals import *
from pamux_unreal_tools.tools.material_expression_wrapper_generator.values import *

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