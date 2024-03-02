# Should be sourced from C:\Users\baris\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

$($MyInvocation.MyCommand.Source)

$global:MyDocumentsRoot = [Environment]::GetFolderPath("MyDocuments")

$global:WorkspaceRoot = "c:\src"
$global:SrcRoot = $global:WorkspaceRoot

$global:EngTools_Root = "${global:SrcRoot}\Pamux.EngTools"

$global:EngTools_ScriptsRoot = "${global:EngTools_Root}\Scripts"
$global:EngTools_SrcRoot = "${global:EngTools_Root}\src"
$global:EngToolsUI_Root = "${global:EngTools_SrcRoot}\pamux_engtools_ui"
$global:EngEnv_Root = "${global:EngTools_SrcRoot}\pamux_engenv"

$global:EngTools_python_venv = "${global:EngTools_Root}\.venv"
$global:EngTools_python_exe = "${global:EngTools_python_venv}\Scripts\python.exe"
$global:EngTools_pip_exe = "${global:EngTools_python_venv}\Scripts\pip.exe"


. "${global:EngEnv_Root}\Aliases.ps1"


$env:PATH="${env:PATH};${env:SYSINTERNALS_ROOT}"


Set-Location ${global:WorkspaceRoot}

