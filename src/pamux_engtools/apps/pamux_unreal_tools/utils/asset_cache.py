import unreal
EAL = unreal.EditorAssetLibrary

class AssetCache:
    __items = {}

    @staticmethod
    def get(key):
        if isinstance(AssetCache.__items[key], str):
            AssetCache.__items[key] = EAL.load_asset(AssetCache.__items[key])
        return AssetCache.__items[key]
    
    @staticmethod
    def set(key, asset_path):
        AssetCache.__items[key] =  asset_path

    @staticmethod
    def get_layer_texture(layer_name: str, texture_type: str):
        key = "layer" + layer_name + texture_type
        if key not in AssetCache.__items.keys():
            AssetCache.set(key, f"/Game/Megascans/Surfaces/{layer_name}/T_{layer_name}_{texture_type}")

        return AssetCache.get(key)