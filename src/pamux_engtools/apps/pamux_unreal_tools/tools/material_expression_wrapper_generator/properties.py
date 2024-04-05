from pamux_unreal_tools.tools.material_expression_wrapper_generator.values import *
from pamux_unreal_tools.tools.material_expression_wrapper_generator.globals import *

def setup_properties(pamux_wrapper_class_name, doc):
    result = Values()
    if pamux_wrapper_class_name == "NamedRerouteDeclaration":
         result.append(PropertyInfo('name', 'Name'))
         # result.append(PropertyInfo('desc', 'str'))
         result.append(PropertyInfo('nodeNolor', 'LinearColor'))
         result.append(PropertyInfo('variableGuid', 'Guid'))
         return result

    if pamux_wrapper_class_name == "NamedRerouteUsage":
        # result.append(PropertyInfo(('name', 'Name'))
        result.append(PropertyInfo('declarationGuid', 'Guid'))
        return result
    
    if pamux_wrapper_class_name == "StaticBool":
        result.append(PropertyInfo('Value', 'bool'))
        return result
    

    is_in_editor_properties = False
    
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
            #print(doc_line)
            continue

        left = doc_line[0:col].strip().strip("-").strip().strip("`")
        notes = doc_line[col+1:].strip()

        col = left.find("`")
        if col == -1:
            #print(doc_line)
            continue

        name = left[0:col]
        type = left[col+2:].strip().strip("()")

        if "[Read-Write]" in notes:
            is_rw = True
            notes = notes.replace("[Read-Write]", "")
        else:
            #print(notes)
            pass

        # if name != "material_expression_editor_x" and name != "material_expression_editor_y":
        result.append(PropertyInfo(name, type, notes))

    # if result.is_empty:
    #     result.append(PropertyInfo("desc", "str"))
        
    return result