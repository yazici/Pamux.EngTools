class MethodParam:
    def __init__(self, name, type, default_value = None) -> None:
        self.name = name
        self.type = type
        self.default_value = default_value


class MethodParams:
    def __init__(self):
        self.params = []

    def append(self, param):
        self.params.append(param)

    def get_declaration_code(self, codeGen) -> str:
        result = ""
        isFirst = True

        for p in self.params:
            if isFirst:
                isFirst = False
            else:
                result += ", "

            result += codeGen.get_declaration_code(p)

        return result
    
    def get_initializer_code(self, codeGen, class_name) -> str:
        result = ""
        isFirst = True

        for p in self.params:
            if isFirst:
                isFirst = False
            else:
                result += ", "

            result += codeGen.get_initializer_code(p)

        return result
    
    def ctor_declaration_code(self, codeGen) -> str:
        mps = MethodParams()
        for param in codeGen.required_initial_parameters:
            mps.append(param)
        
        for param in self.params:
            mps.append(param)

        mps.append(MethodParam("node_pos", "NodePos", "NULL"))
        
        return mps.get_declaration_code(codeGen)
                         
    def append_assignment_lines(self, codeGen):
        for param in self.params:
            param.append_assignment_lines(codeGen)

NO_PARAMS = MethodParams()