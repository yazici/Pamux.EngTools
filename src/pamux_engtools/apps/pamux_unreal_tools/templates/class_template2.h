// This file is generated. Do not edit

#pragma once

__REQUIRED_INCLUDES__

#include "abstracts/MaterialExpressionWrapper.h"


template<>
struct traits<class __CLASS_NAME__> {
	static inline FString Name = "__CLASS_NAME__";

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

    using UMaterialExpression_t = UMaterialExpression__CLASS_NAME__;
    using Properties_t = Properties;
    using Inputs_t = Inputs;
    using Outputs_t = Outputs;
};

class __CLASS_NAME__ : public MaterialExpressionWrapper<__CLASS_NAME__> {
public:
__ALL_CTORS__
public:
    MXInputSocket& input;
    MXOutputSocket& output;
};