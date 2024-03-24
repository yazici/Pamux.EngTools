# python 3.9.13
# 
# pip install userpaths
# https://pypi.org/project/PyQt6/    pip install PyQt6
# https://pypi.org/project/pyqt6-tools/   pip install pyqt6-tools

import re
import shlex

filePath = "C:/src/Pamux.EngTools/Data/UnrealMaterials/m_ground_grass.clipboard"

class Object:
    def __init__(self, parent = None):
        self.Name = None
        self.Class = None
        self.NodeGuid = None
        self.attributes = {}
        self.lines = []
        self.parent = parent
        if parent is not None:
            self.parent.children.append(self)
        self.children = []


    def parseCustomPropertiesPin(self, line):
        self.customProperties = line
        # splitter = shlex.shlex(line)
        # splitter.whitespace += ","
        # splitter.whitespace_split = True
        # attributes = list(splitter)

        # for attribute in attributes:
        #     nameValue = attribute.split("=")
        #     if len(nameValue) != 2:
        #         print(nameValue)
        #         #print(attributes)
        #         continue

    def parse(self, line):
        attributes = shlex.split(line)

        for attribute in attributes:
            nameValue = attribute.split("=")

            if len(nameValue) != 2:
                nameValue = attribute.split("=(")
                if len(nameValue) != 2:
                    continue
                if not nameValue[1].endswith(")"):
                    continue
                nameValue[1] = nameValue[1][:-1]

            name = nameValue[0]
            value = nameValue[1]

            if name == "Class":
                self.Class = value
            elif name == "Name":
                self.Name = value
            elif name == "NodeGuid":
                self.NodeGuid = value
            elif name == "NodePosX":
                self.NodePosX = value
            elif name == "NodePosY":
                self.NodePosY = value
            elif name == "NodeHeight":
                self.NodeHeight = value
            elif name == "NodeWidth":
                self.NodeWidth = value
            elif name == "Material":
                self.Material = value
            elif name == "MaterialExpressionEditorX":
                self.MaterialExpressionEditorX = value
            elif name == "MaterialExpressionEditorY":
                self.MaterialExpressionEditorY = value
            elif name == "MaterialExpressionGuid":
                self.MaterialExpressionGuid = value
            elif name == "MaterialExpressionComment":
                self.MaterialExpressionComment = value
            elif name == "bCommentBubblePinned":
                self.bCommentBubblePinned = value
            elif name == "bCommentBubbleVisible":
                self.bCommentBubbleVisible = value
            elif name == "NodeComment":
                self.NodeComment = value
            elif name == "Text":
                self.Text = value
            elif name == "SizeY":
                self.SizeY = value
            elif name == "SizeX":
                self.SizeX = value
            elif name == "ExportPath":
                self.ExportPath = value

            elif name == "bCommentBubbleVisible_InDetailsPanel":
                self.bCommentBubbleVisible_InDetailsPanel = value
            elif name == "bCanRenameNode":
                self.bCanRenameNode = value
            elif name == "ExpressionGUID":
                self.ExpressionGUID = value
            elif name == "UTiling":
                self.UTiling = value
            elif name == "AdvancedPinDisplay":
                self.AdvancedPinDisplay = value
            elif name == "VTiling":
                self.VTiling = value
            elif name == "MaterialExpression":
                self.MaterialExpression = value
            elif name == "Texture":
                self.Texture = value
            elif name == "Coordinates":
                self.Coordinates = value

            elif name == "ConstB":
                self.ConstB = value
            elif name == "A":
                self.A = value
            elif name == "B":
                self.B = value
            elif name == "G":
                self.G = value
            elif name == "R":
                self.R = value
            elif name == "Alpha":
                self.Alpha = value
            elif name == "DefaultValue":
                self.DefaultValue = value

            elif name == "ParameterName":
                self.ParameterName = value
            elif name == "SamplerType":
                self.SamplerType = value
            elif name == "Desc":
                self.Desc = value
            elif name == "Input":
                self.Input = value
            elif name == "ConstA":
                self.ConstA = value
            elif name == "Constant":
                self.Constant = value
            else:
                self.attributes[name] = value
                # print(name)

        self.lines.append(line)

    def dump(self):
        if self.Class == "/Script/Engine.MaterialExpressionLinearInterpolate":
            print(self.Name)
            print(self.Class)
        for child in self.children:
            child.dump()

root = Object()
current = root


with open(filePath, "rt") as file:
    lines = []
    for line in file.readlines():
        line = line.strip()

        if line.startswith("Begin Object "):
            child = Object(current)
            current = child
            current.parse(line[len("Begin Object "): ])
            continue


        if line.startswith("End Object"):
            current = current.parent
            continue

        idx = line.find("CustomProperties Pin (")
        if idx == -1:
            current.parse(line)
            continue

        

        line = line[idx + len("CustomProperties Pin ("):-1]

        line = line.replace('NSLOCTEXT("MaterialGraphNode", "Space", " ")', "MaterialGraphNode")

        current.parseCustomPropertiesPin(line)
        


root.dump()