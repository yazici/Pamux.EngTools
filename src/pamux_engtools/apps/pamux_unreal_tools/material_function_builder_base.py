from pamux_unreal_tools.material_function import MaterialFunction

LandscapeMaterialFunctionPackage = "/Game/Materials/Pamux/Landscape/Functions"

class MaterialFunctionBuilderBase:
    def __init__(self, function_name: str, package_name: str = LandscapeMaterialFunctionPackage):
        self.function_name = function_name
        self.package_name = package_name

    def build(self, material_function: MaterialFunction):
        raise "Implement and build materialFunction blueprint here"

    def get(self):
        result = MaterialFunction.loadOrCreate(self.function_name, self.package_name, True)

        self.build(result)

        result.save()
        return result
