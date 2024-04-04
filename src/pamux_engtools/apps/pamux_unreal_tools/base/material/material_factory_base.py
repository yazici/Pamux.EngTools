import unreal

from pamux_unreal_tools.base.material_expression.material_expression_container_factory_base import MaterialExpressionContainerFactoryBase

class MaterialFactoryBase(MaterialExpressionContainerFactoryBase):
    def __init__(elf, asset_class: unreal.Class, asset_factory: unreal.Factory, container_wrapper_class) -> None:
        super().__init__(asset_class, asset_factory, container_wrapper_class)

