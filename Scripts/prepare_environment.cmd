@echo off
cd %~dp0
set ENGTOOLS_ROOT=%~dp0

"%ProgramFiles(x86)%\Microsoft Visual Studio\Shared\Python36_64\python.exe" -c "from EnvironmentFactory import EnvironmentFactory; EnvironmentFactory.generate()"

doskey /MACROFILE=gen_aliases.txt
del gen_aliases.txt

call gen_env.cmd
del gen_env.cmd