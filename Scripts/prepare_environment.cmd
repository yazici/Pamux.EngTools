@echo off

cd %~dp0

set PAMUX_SCRIPTS_ROOT=%CD%
set PAMUX_VS_PYTHON_ROOT=%ProgramFiles(x86)%\Microsoft Visual Studio\Shared\Python36_64
set PAMUX_BLENDER_PYTHON_ROOT=C:\Apps\blender-2.80-18e5540a48b6-win64\2.80\python

set PAMUX_PYTHON_ROOT=%PAMUX_BLENDER_PYTHON_ROOT%

set PAMUX_PYTHON_BIN_ROOT=%PAMUX_BLENDER_PYTHON_ROOT%\bin
set PAMUX_PYTHON_SCRIPTS_ROOT=%PAMUX_BLENDER_PYTHON_ROOT%\scripts


set PAMUX_PYTHON_EXE=%PAMUX_PYTHON_BIN_ROOT%\python.exe
set PAMUX_PIP_EXE=%PAMUX_PYTHON_SCRIPTS_ROOT%\pip.exe

REM %PAMUX_PYTHON_EXE% get-pip.py
REM pipi pywin32
REM pipi patool
REM pipi pillow
REM pipi keyboard
doskey /MACROFILE=aliases.txt

"%PAMUX_PYTHON_EXE%" -c "from EnvironmentFactory import EnvironmentFactory; EnvironmentFactory.generate()"


doskey /MACROFILE=gen_aliases.txt
del gen_aliases.txt

call gen_env.cmd
del gen_env.cmd

GOTO :eof
