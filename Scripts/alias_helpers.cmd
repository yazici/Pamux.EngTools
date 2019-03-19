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

:pythonVersion
    @echo off
    "%PAMUX_PYTHON_EXE%"  --version
    GOTO :eof

:pipInstallWxPython
    @echo off
    REM https://pip.pypa.io/en/stable/reference/pip_install/
    "%PAMUX_PIP_EXE%" install --upgrade wxPython
    GOTO :eof
    
:pipInstallPaTools
    @echo off
    REM https://pip.pypa.io/en/stable/reference/pip_install/
    "%PAMUX_PIP_EXE%" install --upgrade patools
    GOTO :eof
    
    
:pipInstall
    @echo off
    REM https://pip.pypa.io/en/stable/reference/pip_install/
    "%PAMUX_PIP_EXE%" install --upgrade %1
    GOTO :eof
    
:getPip
    @echo off
    "%PAMUX_PYTHON_EXE%"  "%PAMUX_SCRIPTS_ROOT%\get-pip.py"
    GOTO :eof
    
:runCrawler
    @echo off
    "%PAMUX_PYTHON_EXE%"  "%PAMUX_SCRIPTS_ROOT%\Crawler.py"
    GOTO :eof
    
:makeSeamlessTexture
    @echo off
    "%PAMUX_PYTHON_EXE%" -c "from ImageProcessing import ImageProcessing; ImageProcessing.MakeSeamlessTexture('%1')"

    GOTO :eof
    
    
    
:convertAndSanitize
    @echo off
    "%PAMUX_PYTHON_EXE%" -c "from AssetUtils import AssetUtils; AssetUtils.ConvertAndSanitizeAll('%1')"

    GOTO :eof
    
    
    
    
:symmetrizeHuman
    @echo off
    "%PAMUX_PYTHON_EXE%" -c "from MakeHuman import MakeHuman; MakeHuman.SymmetrizeHuman('%1')"

    GOTO :eof
    
    
    
    
:createCMakeBasedCppProject
    @echo off
    "%PAMUX_PYTHON_EXE%" -c "from Wizards import CMakeBasedCppWizard; wizard = CMakeBasedCppWizard('%1'); wizard.Run()"

    GOTO :eof