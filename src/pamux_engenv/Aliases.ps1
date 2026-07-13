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
# . "C:\src\Cappadocia\Scripts\build_aliases.ps1"
function mycodex()    { codex -a never -s workspace-write -C C:\src\Cappadocia }

# function run      { & ".\Binaries\Win64\Cappadocia.exe" }
# function editor   { & "C:\Program Files\Epic Games\UE_5.8\Engine\Binaries\Win64\UnrealEditor.exe" ".\Cappadocia.uproject" }
# function clean    { Remove-Item Binaries,Intermediate,Saved -Recurse -Force -ErrorAction SilentlyContinue }
# function rebuild  { clean; build_all }
# function gitgraph { git log --oneline --graph --decorate --all }

SetAliases

function Export-Cropout {
    $PluginSource = "C:\src\UnrealTools\BlueprintIrExporter"
    $PluginPackage = "C:\src\UnrealTools\Build\BlueprintIrExporter"
    $DeployedPlugin = "C:\src\CropoutSampleProject 5.8\Plugins\BlueprintIrExporter"
    $CropoutProject = "C:\src\CropoutSampleProject 5.8\CropoutSampleProject.uproject"
    $ExportOutput = "C:\src\UnrealTools\BlueprintExports"
    $TargetSourceRoot = "C:\src\Cappadocia\Source"

    $CommandletSource = Join-Path `
        $PluginSource `
        "Source\BlueprintIrExporter\Private\BlueprintIrExportCommandlet.cpp"

    Remove-Item `
        $PluginPackage `
        -Recurse `
        -Force `
        -ErrorAction SilentlyContinue

    & "C:\Program Files\Epic Games\UE_5.8\Engine\Build\BatchFiles\RunUAT.bat" `
        BuildPlugin `
        -Plugin="$PluginSource\BlueprintIrExporter.uplugin" `
        -Package="$PluginPackage" `
        -TargetPlatforms=Win64

    if ($LASTEXITCODE -ne 0) {
        throw "BlueprintIrExporter build failed with exit code $LASTEXITCODE."
    }

    Remove-Item `
        $DeployedPlugin `
        -Recurse `
        -Force `
        -ErrorAction SilentlyContinue

    Copy-Item `
        $PluginPackage `
        "C:\src\CropoutSampleProject 5.8\Plugins" `
        -Recurse `
        -Force

    & "C:\Program Files\Epic Games\UE_5.8\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" `
        $CropoutProject `
        -run=BlueprintIrExport `
        -root="/Game;/Cropout" `
        -output="$ExportOutput" `
        -source-root="$TargetSourceRoot" `
        -module="Cappadocia" `
        -include-data-only `
        -unattended `
        -nop4 `
        -nosplash `
        -nullrhi

    if ($LASTEXITCODE -ne 0) {
        throw "Blueprint export failed with exit code $LASTEXITCODE."
    }

    Write-Host ""
    Write-Host "Export completed."
    Write-Host "JSON: $ExportOutput"
    Write-Host "Headers: $TargetSourceRoot\Cappadocia\Public"
    Write-Host "Implementations: $TargetSourceRoot\Cappadocia\Private"
}


$ErrorActionPreference = "Stop"

$ProjectRoot = "C:\src\Cappadocia"
$ProjectFile = Join-Path $ProjectRoot "Cappadocia.uproject"
$EngineRoot = "C:\Program Files\Epic Games\UE_5.8"

$BuildBat = Join-Path $EngineRoot "Engine\Build\BatchFiles\Build.bat"
$UbtDll = Join-Path $EngineRoot "Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.dll"

function Assert-FileExists {
    param(
        [Parameter(Mandatory)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Required file was not found: $Path"
    }
}

function Invoke-CappadociaProjectFiles {
    Assert-FileExists $ProjectFile
    Assert-FileExists $UbtDll

    Push-Location $ProjectRoot

    try {
        & dotnet $UbtDll `
            -ProjectFiles `
            -Project="$ProjectFile" `
            -Game `
            -Engine `
            -Progress

        if ($LASTEXITCODE -ne 0) {
            throw "Generate project files failed with exit code $LASTEXITCODE"
        }
    }
    finally {
        Pop-Location
    }
}

function Invoke-CappadociaBuild {
    Assert-FileExists $ProjectFile
    Assert-FileExists $BuildBat

    Push-Location $ProjectRoot

    try {
        & $BuildBat `
            CappadociaEditor `
            Win64 `
            Development `
            -Project="$ProjectFile" `
            -WaitMutex

        if ($LASTEXITCODE -ne 0) {
            throw "Cappadocia build failed with exit code $LASTEXITCODE"
        }
    }
    finally {
        Pop-Location
    }
}

function bb {
    Invoke-CappadociaBuild
}

function bbg {
    Invoke-CappadociaProjectFiles
    Invoke-CappadociaBuild
}

function bbc {
    if (Test-Path $ProjectRoot) {
        Remove-Item (Join-Path $ProjectRoot "Binaries") `
            -Recurse -Force -ErrorAction SilentlyContinue

        Remove-Item (Join-Path $ProjectRoot "Intermediate") `
            -Recurse -Force -ErrorAction SilentlyContinue

        Remove-Item (Join-Path $ProjectRoot ".vs") `
            -Recurse -Force -ErrorAction SilentlyContinue
    }

    Invoke-CappadociaProjectFiles
    Invoke-CappadociaBuild
}

function capp {
    Assert-FileExists $ProjectFile

    $EditorExe = Join-Path `
        $EngineRoot `
        "Engine\Binaries\Win64\UnrealEditor.exe"

    Assert-FileExists $EditorExe

    & $EditorExe $ProjectFile
}