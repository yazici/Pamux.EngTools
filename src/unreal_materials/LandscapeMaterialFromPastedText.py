inFilePath = "C:/src/Pamux.EngTools/src/unreal_materials/paste.bp.txt"

with open(inFilePath, "rt") as inFile:
    for line in inFile.readlines():
        print(line)