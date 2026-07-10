$($MyInvocation.MyCommand.Source)

function Script:SetAliases()
{
    Set-Alias python ${global:Global_python_exe} -scope Global
    Set-Alias pip ${global:Global_pip_exe} -scope Global
    Set-Alias qtd ${global:EngTools_QT_designer_exe} -scope Global

    # Set-Alias which where.exe
}


function global:petui()
{
    & ${global:EngTools_python_exe} ${global:EngTools_AppsRoot}\pamux_engtools_ui.py $args
}

function global:cland()
{
    & ${global:EngTools_python_exe} ${global:EngTools_AppsRoot}\pamux_clipboard_landscape.py $args
}

function build_all {
    cd C:\src\Cappadocia

    $previousTbbSetting = $env:TBB_MALLOC_DISABLE_REPLACEMENT

    try {
        $env:TBB_MALLOC_DISABLE_REPLACEMENT = "1"

        Write-Host ""
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host "       CAPPADOCIA ASSET BUILD" -ForegroundColor Cyan
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host ""

        & python -X utf8 ".\Scripts\build_all.py" --force 2>&1 |
            Tee-Object -FilePath ".\out.txt"

        $exitCode = $LASTEXITCODE

        Write-Host ""

        if ($exitCode -eq 0) {
            Write-Host "Build succeeded." -ForegroundColor Green
        }
        else {
            Write-Host "Build failed. Exit code: $exitCode" -ForegroundColor Red
        }

        $global:LASTEXITCODE = $exitCode
    }
    finally {
        if ($null -eq $previousTbbSetting) {
            Remove-Item Env:TBB_MALLOC_DISABLE_REPLACEMENT `
                -ErrorAction SilentlyContinue
        }
        else {
            $env:TBB_MALLOC_DISABLE_REPLACEMENT = $previousTbbSetting
        }
    }
}

# function run      { & ".\Binaries\Win64\Cappadocia.exe" }
# function editor   { & "C:\Program Files\Epic Games\UE_5.8\Engine\Binaries\Win64\UnrealEditor.exe" ".\Cappadocia.uproject" }
# function clean    { Remove-Item Binaries,Intermediate,Saved -Recurse -Force -ErrorAction SilentlyContinue }
# function rebuild  { clean; build_all }
# function gitgraph { git log --oneline --graph --decorate --all }

SetAliases
