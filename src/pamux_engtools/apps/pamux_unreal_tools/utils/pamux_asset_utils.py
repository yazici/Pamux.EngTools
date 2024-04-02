import unreal

class PamuxAssetUtils:
    @staticmethod
    def ensureAssetDirectoryExists(dir: str):
        if not unreal.EditorAssetLibrary.does_directory_exist(dir):
            unreal.EditorAssetLibrary.make_directory(dir)

    @staticmethod
    def split_asset_path(asset_path: str):
        last_slash = asset_path.rindex("/")
        return asset_path[0:last_slash], asset_path[last_slash+1:]