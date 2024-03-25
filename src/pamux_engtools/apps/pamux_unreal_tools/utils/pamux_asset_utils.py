import unreal

class PamuxAssetUtils:
    @staticmethod
    def ensureAssetDirectoryExists(dir):
        if not unreal.EditorAssetLibrary.does_directory_exist(dir):
            unreal.EditorAssetLibrary.make_directory(dir)
