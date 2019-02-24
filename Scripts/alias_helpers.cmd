call %1 %2 %3
GOTO :eof

:showEnvironment
    @echo off
    set > %PAMUX_ENGTOOLS_GENDATA%\env.txt
    "%PAMUX_NOTEPADPLUSPLUS_EXE%" %PAMUX_ENGTOOLS_GENDATA%\env.txt
    GOTO :eof 

:runPamwxHelloWorld
    @echo off
    "%PAMUX_PYTHON_EXE%"  "%PAMUX_PAMWX_ROOT%\HelloWorld.py"
    GOTO :eof

:pipInstallWxPython
    @echo off
    REM https://pip.pypa.io/en/stable/reference/pip_install/
    "%PAMUX_PIP_EXE%" install --upgrade wxPython
    GOTO :eof
    
    
:getPip
    @echo off
    "%PAMUX_PYTHON_EXE%"  "%PAMUX_SCRIPTS_ROOT%\get-pip.py"
    GOTO :eof