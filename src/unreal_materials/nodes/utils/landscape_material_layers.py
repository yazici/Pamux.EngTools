from unreal_materials.nodes.material_functions.commons.material_layer_function_call import MaterialLayerFunctionCall

class LandscapeMaterialLayers:
    ALL = [
        MaterialLayerFunctionCall("Dirt"),
        MaterialLayerFunctionCall("Grass"),
        MaterialLayerFunctionCall("Mud"),
        MaterialLayerFunctionCall("StonyGround"),
        MaterialLayerFunctionCall("Fields"),
        MaterialLayerFunctionCall("PlowedGround"),
        MaterialLayerFunctionCall("ForestGrounds"),
        MaterialLayerFunctionCall("HeavyMud")
    ]
