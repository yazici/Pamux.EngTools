import unreal

from pamux_unreal_tools.material_expression import MaterialExpression
from pamux_unreal_tools.material_expression_container import MaterialExpressionContainer

class NonaryOperation(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, expression_class, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, expression_class, node_pos_x, node_pos_y)


class UnaryOperation(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, expression_class, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, expression_class, node_pos_x, node_pos_y)

class BinaryOperation(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, expression_class, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, expression_class, node_pos_x, node_pos_y)

class TernaryOperation(MaterialExpression):
    def __init__(self, parent: MaterialExpressionContainer, expression_class, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, expression_class, node_pos_x, node_pos_y)

#region Nonary Operations

class PixelDepth(NonaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionPixelDepth, node_pos_x, node_pos_y)

class VertexNormalWS(NonaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionVertexNormalWS, node_pos_x, node_pos_y)

class AbsoluteWorldPosition(NonaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionAbsoluteWorldPosition, node_pos_x, node_pos_y)


#endregion
        
        
#region Unary Operations
#endregion
        
#region Binary Operations
class Add(BinaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionAdd, node_pos_x, node_pos_y)

class Subtract(BinaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionSubtract, node_pos_x, node_pos_y)

class Multiply(BinaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionMultiply, node_pos_x, node_pos_y)

class MultiplyAdd(BinaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionMultiplyAdd, node_pos_x, node_pos_y)

class Divide(BinaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionDivide, node_pos_x, node_pos_y)

class Power(BinaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionPower, node_pos_x, node_pos_y)

class Append(BinaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionMultiply, node_pos_x, node_pos_y)

#endregion
#region Ternary Operations

class Lerp(TernaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionLinearInterpolate, node_pos_x, node_pos_y)

class Clamp(TernaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionClamp, node_pos_x, node_pos_y)

class Fresnel(TernaryOperation):
    def __init__(self, parent: MaterialExpressionContainer, node_pos_x = 0, node_pos_y = 0):
        super().__init__(parent, unreal.MaterialExpressionFresnel, node_pos_x, node_pos_y)


#endregion