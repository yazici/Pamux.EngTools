@echo off

cd %~dp0

set PAMUX_ENGTOOLS_ROOT=%~dp0
set PAMUX_PYTHON_ROOT=%ProgramFiles(x86)%\Microsoft Visual Studio\Shared\Python36_64
set PAMUX_PYTHON_EXE=%PAMUX_PYTHON_ROOT%\python.exe
set PAMUX_PIP_EXE=%PAMUX_PYTHON_ROOT%\scripts\pip.exe

"%PAMUX_PYTHON_EXE%" -c "from EnvironmentFactory import EnvironmentFactory; EnvironmentFactory.generate()"

doskey /MACROFILE=gen_aliases.txt
del gen_aliases.txt

call gen_env.cmd
del gen_env.cmd

GOTO :eof
