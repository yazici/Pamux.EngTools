$($MyInvocation.MyCommand.Source)

function Script:SetAliases()
{
    Set-Alias python ${global:EngTools_python_exe}
    Set-Alias pip ${global:EngTools_pip_exe}
}

function global:petui()
{
    & ${global:EngTools_python_exe} ${global:EngToolsUI_Root}\main.py $args
}

SetAliases
