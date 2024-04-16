// This file is generated. Do not edit

#pragma once

__REQUIRED_INCLUDES__

#include "abstracts/MaterialExpressionWrapper.h"

namespace NS__CLASS_NAME__ {
    class Properties : public PropertiesBase {
    public:
        Properties()__PROPERTIES_INITIALIZERS__ {
        }

    public:
__DECLARE_EXPRESSION_PROPERTIES__
    };

    class Inputs : public InputsBase  {
    public:
        Inputs()__INPUTS_INITIALIZERS__ {
        }

    public:
__DECLARE_EXPRESSION_INPUTS__
    };

    class Outputs : public OutputsBase {
    public:
        Outputs()__OUTPUTS_INITIALIZERS__ {
        }

    public:
__DECLARE_EXPRESSION_OUTPUTS__
    };
}

class __CLASS_NAME__;
using __CLASS_NAME__Base = MaterialExpressionWrapper<__CLASS_NAME__, UMaterialExpression__CLASS_NAME__, NS__CLASS_NAME__::Properties, NS__CLASS_NAME__::Inputs, NS__CLASS_NAME__::Outputs>;
class __CLASS_NAME__ : public __CLASS_NAME__Base {
public:
    __CLASS_NAME__(__CTOR_PARAMETERS__)
        : __CLASS_NAME__Base(__BASE_CLASS_CTOR_PARAMETERS_VALUES__)__MAIN_INITIALIZERS__ {
    }
};