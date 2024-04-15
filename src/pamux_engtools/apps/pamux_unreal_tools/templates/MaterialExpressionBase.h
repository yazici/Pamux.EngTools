// Temp code to help with syntax highlighting. Will be removed by template generator
class SimpleMaterialExpressionBase {
};

template <typename TProperties, typename TInputs, typename TOutputs>
class MaterialExpressionBase : public SimpleMaterialExpressionBase {
protected:
    MaterialExpressionBase()
        : p(properties), i(inputs), o(outputs) {
    }
public:
    TProperties properties;
    TInputs inputs;
    TOutputs outputs;

    TProperties& p;
    TInputs& i;
    TOutputs& o;
};

class ExpressionValueBase {
};

class PropertiesBase : public ExpressionValueBase {
public:
protected:
};

class InputsBase : public ExpressionValueBase {
public:
protected:
};

class OutputsBase : public ExpressionValueBase {
public:
protected:
};

class EditorProperty : public ExpressionValueBase {
public:
    EditorProperty(const char *name, const char *type) {
    }
protected:
};

class InputSocket : public ExpressionValueBase {
public:
    InputSocket(const char *name, const char *type) {
    }
protected:
};

class OutputSocket : public ExpressionValueBase {
public:
    OutputSocket(const char *name, const char *type) {
    }

protected:
};

#define __CTOR_PARAMETERS__
#define __BASE_CLASS_CTOR_PARAMETERS_VALUES__

#define __DECLARE_EXPRESSION_PROPERTIES__
#define __DECLARE_EXPRESSION_INPUTS__
#define __DECLARE_EXPRESSION_OUTPUTS__

#define __INITIALIZERS__
#define __REQUIRED_INCLUDES__

struct Hello
{
    int helloworld() { return 0; }
};

struct Generic {};    

// SFINAE test https://en.cppreference.com/w/cpp/language/sfinae
template <typename T>
class has_helloworld
{
    typedef char one;
    struct two { char x[2]; };

    template <typename C> static one test( decltype(&C::helloworld) ) ;
    template <typename C> static two test(...);    

public:
    enum { value = sizeof(test<T>(0)) == sizeof(char) };
};
// std::cout << has_helloworld<Hello>::value << std::endl;
