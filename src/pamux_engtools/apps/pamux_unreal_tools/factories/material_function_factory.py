import unreal

from pamux_unreal_tools.impl.material_function_impl import MaterialFunctionImpl
from pamux_unreal_tools.factories.material_expression_container_factory import MaterialExpressionContainerFactory

class MaterialFunctionFactory(MaterialExpressionContainerFactory):
    def __init__(self):
        super().__init__(unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew(), MaterialFunctionImpl)
