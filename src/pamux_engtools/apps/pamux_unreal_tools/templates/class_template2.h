// This file is generated. Do not edit

#pragma once

__REQUIRED_INCLUDES__

#include "abstracts/MaterialExpressionWrapper.h"

class __CLASS_NAME__Nest {
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
};

class __CLASS_NAME__ : public MaterialExpressionWrapper<__CLASS_NAME__, UMaterialExpression__CLASS_NAME__, __CLASS_NAME__Nest::Properties, __CLASS_NAME__Nest::Inputs, __CLASS_NAME__Nest::Outputs> {


public:
    __CLASS_NAME__(__CTOR_PARAMETERS__);
};