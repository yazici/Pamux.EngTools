$($MyInvocation.MyCommand.Source)

function Script:SetAliases()
{
    Set-Alias python ${global:EngTools_python_exe} -scope Global
    Set-Alias pip ${global:EngTools_pip_exe} -scope Global
    Set-Alias qtd ${global:EngTools_QT_designer_exe} -scope Global
}


function global:petui()
{
    & ${global:EngTools_python_exe} ${global:EngTools_AppsRoot}\pamux_engtools_ui.py $args
}

SetAliases
