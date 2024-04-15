#include <cstdint>
#include "MaterialExpressionBase.h"
// #include "MaterialExpressionFactory.h"
// #include "Materials/MaterialExpressionAbs.h"
// #include "Materials/MaterialExpressionMaterialFunctionCall.h"

// #include "Materials/MaterialExpressionAdd.h"
// #include "generator/FunctionLoader.h"
// #include "Materials/MaterialExpressionArccosine.h"
// #include "generator/MaterialExpressions.h"
// #include "Materials/MaterialExpressionArcsine.h"
// #include "generator/MaterialTextureFactory.h"
// #include "Materials/MaterialExpressionArctangent.h"

__REQUIRED_INCLUDES__
using MaterialExpressionParametrizedBase 
    = MaterialExpressionBase<__CLASS_NAME__::Properties, __CLASS_NAME__::Inputs, __CLASS_NAME__::Outputs>;

class __CLASS_NAME__: public MaterialExpressionParametrizedBase {
public:
    class Properties : public PropertiesBase {
    public:
        Properties();

    public:
__DECLARE_EXPRESSION_PROPERTIES__
    };

    class Inputs : public InputsBase  {
    public:
        Inputs();

    public:
__DECLARE_EXPRESSION_INPUTS__
    };

    class Outputs : public OutputsBase {
    public:
        Outputs();

    public:
__DECLARE_EXPRESSION_OUTPUTS__
    };

public:
    __CLASS_NAME__(__CTOR_PARAMETERS__);
};