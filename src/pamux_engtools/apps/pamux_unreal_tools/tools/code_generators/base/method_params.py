class MethodParam:
    def __init__(self, overload_id, name, type, default_value = None) -> None:
        self.overload_id = overload_id
        self.name = name
        self.type = type
        self.default_value = default_value

    @property
    def field_name(self):
        if self.name in ["true", "false"]:
            return "_" + self.name
        return self.name

    @property
    def parameter_name(self):
        return f"_{self.field_name}"

    def get_ctor_code(self):
        return ''



class MethodParams:
    def __init__(self):
        self.params = []

    @property
    def is_empty(self):
        return len(self.params) == 0

    def append(self, param):
        self.params.append(param)

    def get_list_for_method_declaration(self, codeGen) -> str:
        result = ""
        isFirst = True

        for p in self.params:
            if isFirst:
                isFirst = False
            else:
                result += ", "

            result += codeGen.get_for_method_declaration(p)

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