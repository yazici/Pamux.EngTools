# Should be sourced from C:\Users\baris\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

$($MyInvocation.MyCommand.Source)

$global:MyDocumentsRoot = [Environment]::GetFolderPath("MyDocuments")

$global:WorkspaceRoot = "c:\src"
$global:SrcRoot = $global:WorkspaceRoot

$global:EngTools_Root = "${global:SrcRoot}\Pamux.EngTools"

$global:EngTools_ScriptsRoot = "${global:EngTools_Root}\Scripts"
$global:EngTools_SrcRoot = "${global:EngTools_Root}\src"
$global:EngTools_PackagesRoot = "${global:EngTools_SrcRoot}\pamux_engtools"
$global:EngTools_AppsRoot = "${global:EngTools_PackagesRoot}\apps"
$global:EngEnv_Root = "${global:EngTools_SrcRoot}\pamux_engenv"

$global:EngTools_python_venv = "${global:EngTools_Root}\.venv"
$global:EngTools_python_exe = "${global:EngTools_python_venv}\Scripts\python.exe"
$global:EngTools_pip_exe = "${global:EngTools_python_venv}\Scripts\pip.exe"

$global:EngTools_QTApplications = "${global:EngTools_python_venv}\Lib\site-packages\qt6_applications"
$global:EngTools_QT_designer_exe = "${global:EngTools_QTApplications}\Qt\bin\designer.exe"

. "${global:EngEnv_Root}\Aliases.ps1"


$env:PATH="${env:PATH};${env:SYSINTERNALS_ROOT}"


Set-Location ${global:WorkspaceRoot}

