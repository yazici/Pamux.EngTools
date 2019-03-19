@echo off

cd %~dp0

set PAMUX_DRIVE=%~d0
set PAMUX_SCRIPTS_ROOT=%~dp0
set PAMUX_ENGTOOLS_ROOT=%PAMUX_SCRIPTS_ROOT%..\

set PAMUX_SRC_ROOT=%PAMUX_ENGTOOLS_ROOT%..
set PAMUX_ASSETS_ROOT=%PAMUX_DRIVE%\assets
set PAMUX_APPS_ROOT=%PAMUX_DRIVE%\apps

REM echo %PAMUX_DRIVE% 
REM echo %PAMUX_ENGTOOLS_ROOT% 
REM echo %PAMUX_SCRIPTS_ROOT%
REM echo %PAMUX_SRC_ROOT%
REM echo %PAMUX_ASSETS_ROOT%
REM echo %PAMUX_APPS_ROOT%



set PAMUX_VS_PYTHON_ROOT=%ProgramFiles(x86)%\Microsoft Visual Studio\Shared\Python36_64
set PAMUX_BLENDER_PYTHON_ROOT=%PAMUX_APPS_ROOT%\blender-2.80\2.80\python

set PAMUX_PYTHON_ROOT=%PAMUX_BLENDER_PYTHON_ROOT%

set PAMUX_PYTHON_BIN_ROOT=%PAMUX_BLENDER_PYTHON_ROOT%\bin
set PAMUX_PYTHON_SCRIPTS_ROOT=%PAMUX_BLENDER_PYTHON_ROOT%\scripts


set PAMUX_PYTHON_EXE=%PAMUX_PYTHON_BIN_ROOT%\python.exe
set PAMUX_PIP_EXE=%PAMUX_PYTHON_SCRIPTS_ROOT%\pip.exe

%PAMUX_PYTHON_EXE% get-pip.py
%PAMUX_PIP_EXE% install -r %PAMUX_SCRIPTS_ROOT%/requirements.txt


doskey /MACROFILE=aliases.txt

"%PAMUX_PYTHON_EXE%" -c "from EnvironmentFactory import EnvironmentFactory; EnvironmentFactory.generate()"


doskey /MACROFILE=gen_aliases.txt
del gen_aliases.txt

call gen_env.cmd
del gen_env.cmd

GOTO :eof
