$($MyInvocation.MyCommand.Source)

$ErrorActionPreference = "Stop"

$ProjectRoot = "C:\src\Cappadocia"
$ProjectFile = Join-Path $ProjectRoot "Cappadocia.uproject"
$EngineRoot = "C:\Program Files\Epic Games\UE_5.8"

$BuildBat = Join-Path $EngineRoot "Engine\Build\BatchFiles\Build.bat"
$UbtDll = Join-Path $EngineRoot "Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.dll"

function Script:SetAliases {
    Set-Alias python ${global:Global_python_exe} -Scope Global
    Set-Alias pip ${global:Global_pip_exe} -Scope Global
    Set-Alias qtd ${global:EngTools_QT_designer_exe} -Scope Global
}

function global:petui {
    & ${global:EngTools_python_exe} ${global:EngTools_AppsRoot}\pamux_engtools_ui.py $args
}

function global:cland {
    & ${global:EngTools_python_exe} ${global:EngTools_AppsRoot}\pamux_clipboard_landscape.py $args
}

function build_all {
    Push-Location $ProjectRoot

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
            Remove-Item Env:TBB_MALLOC_DISABLE_REPLACEMENT -ErrorAction SilentlyContinue
        }
        else {
            $env:TBB_MALLOC_DISABLE_REPLACEMENT = $previousTbbSetting
        }

        Pop-Location
    }
}

function mycodex {
    codex -a never -s workspace-write -C $ProjectRoot
}

function Assert-FileExists {
    param(
        [Parameter(Mandatory)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Required file was not found: $Path"
    }
}

function Export-Cropout-BP {
    $PluginSource = "C:\src\UnrealTools\BlueprintIrExporter"
    $PluginPackage = "C:\src\UnrealTools\Build\BlueprintIrExporter"
    $CropoutRoot = "C:\src\CropoutSampleProject 5.8"
    $DeployedPlugin = Join-Path $CropoutRoot "Plugins\BlueprintIrExporter"
    $CropoutProject = Join-Path $CropoutRoot "CropoutSampleProject.uproject"
    $ExportOutput = "C:\src\UnrealTools\BlueprintExports"
    $TargetSourceRoot = "C:\src\Cappadocia\Source"

    $RunUat = Join-Path $EngineRoot "Engine\Build\BatchFiles\RunUAT.bat"
    $EditorCmd = Join-Path $EngineRoot "Engine\Binaries\Win64\UnrealEditor-Cmd.exe"
    $PluginFile = Join-Path $PluginSource "BlueprintIrExporter.uplugin"
    $CropoutPlugins = Join-Path $CropoutRoot "Plugins"

    foreach ($requiredFile in @($RunUat, $EditorCmd, $PluginFile, $CropoutProject)) {
        Assert-FileExists $requiredFile
    }

    New-Item $CropoutPlugins -ItemType Directory -Force | Out-Null

    Remove-Item $PluginPackage -Recurse -Force -ErrorAction SilentlyContinue

    Write-Host ""
    Write-Host "Building BlueprintIrExporter..."

    & $RunUat `
        BuildPlugin `
        -Plugin="$PluginFile" `
        -Package="$PluginPackage" `
        -TargetPlatforms=Win64

    if ($LASTEXITCODE -ne 0) {
        throw "BlueprintIrExporter build failed with exit code $LASTEXITCODE."
    }

    Remove-Item $DeployedPlugin -Recurse -Force -ErrorAction SilentlyContinue

    Copy-Item `
        $PluginPackage `
        $DeployedPlugin `
        -Recurse `
        -Force

    Remove-Item $ExportOutput -Recurse -Force -ErrorAction SilentlyContinue
    New-Item $ExportOutput -ItemType Directory -Force | Out-Null

    Write-Host ""
    Write-Host "Exporting Cropout Blueprint IR..."

    & $EditorCmd `
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
        -nullrhi `
        -log

    if ($LASTEXITCODE -ne 0) {
        throw "Blueprint export failed with exit code $LASTEXITCODE."
    }

    Write-Host ""
    Write-Host "Export completed."
    Write-Host "JSON: $ExportOutput"
    Write-Host "Headers: $TargetSourceRoot\Cappadocia\Public"
    Write-Host "Implementations: $TargetSourceRoot\Cappadocia\Private"
}

function Export-Cropout {
    $PluginSource = "C:\src\UnrealTools\UnrealIrExporter"
    $PluginPackage = "C:\src\UnrealTools\Build\UnrealIrExporter"
    $CropoutRoot = "C:\src\CropoutSampleProject 5.8"
    $DeployedPlugin = Join-Path $CropoutRoot "Plugins\UnrealIrExporter"
    $CropoutProject = Join-Path $CropoutRoot "CropoutSampleProject.uproject"
    $ExportOutput = "C:\src\UnrealTools\UnrealIrExports"
    $TargetSourceRoot = "C:\src\Cappadocia\Source"

    $RunUat = Join-Path $EngineRoot "Engine\Build\BatchFiles\RunUAT.bat"
    $EditorCmd = Join-Path $EngineRoot "Engine\Binaries\Win64\UnrealEditor-Cmd.exe"
    $PluginFile = Join-Path $PluginSource "UnrealIrExporter.uplugin"
    $CropoutPlugins = Join-Path $CropoutRoot "Plugins"
    $OldDeployedPlugin = Join-Path $CropoutPlugins "BlueprintIrExporter"

    foreach ($requiredFile in @($RunUat, $EditorCmd, $PluginFile, $CropoutProject)) {
        Assert-FileExists $requiredFile
    }

    New-Item $CropoutPlugins -ItemType Directory -Force | Out-Null

    Remove-Item $PluginPackage -Recurse -Force -ErrorAction SilentlyContinue

    Write-Host ""
    Write-Host "Building UnrealIrExporter..."

    & $RunUat `
        BuildPlugin `
        -Plugin="$PluginFile" `
        -Package="$PluginPackage" `
        -TargetPlatforms=Win64 `
        -NoUBA

    if ($LASTEXITCODE -ne 0) {
        throw "UnrealIrExporter build failed with exit code $LASTEXITCODE."
    }

    Remove-Item $DeployedPlugin -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item $OldDeployedPlugin -Recurse -Force -ErrorAction SilentlyContinue

    Write-Host ""
    Write-Host "Deploying UnrealIrExporter..."

    Copy-Item `
        $PluginPackage `
        $DeployedPlugin `
        -Recurse `
        -Force

    Remove-Item $ExportOutput -Recurse -Force -ErrorAction SilentlyContinue
    New-Item $ExportOutput -ItemType Directory -Force | Out-Null

    Write-Host ""
    Write-Host "Exporting Cropout Unreal IR..."

    & $EditorCmd `
        $CropoutProject `
        -run=UnrealIrExport `
        -root="/Game;/Cropout;/IslandGenerator" `
        -output="$ExportOutput" `
        -source-root="$TargetSourceRoot" `
        -module="Cappadocia" `
        -include-data-only `
        -unattended `
        -nop4 `
        -nosplash `
        -nullrhi `
        -log

    if ($LASTEXITCODE -ne 0) {
        throw "Unreal IR export failed with exit code $LASTEXITCODE."
    }

    Write-Host ""
    Write-Host "Export completed."
    Write-Host "IR JSON: $ExportOutput"
    Write-Host "Headers: $TargetSourceRoot\Cappadocia\Generated\Public"
    Write-Host "Implementations: $TargetSourceRoot\Cappadocia\Generated\Private"
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
        Remove-Item (Join-Path $ProjectRoot "Binaries") -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item (Join-Path $ProjectRoot "Intermediate") -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item (Join-Path $ProjectRoot ".vs") -Recurse -Force -ErrorAction SilentlyContinue
    }

    Invoke-CappadociaProjectFiles
    Invoke-CappadociaBuild
}

function capp {
    Assert-FileExists $ProjectFile

    $EditorExe = Join-Path $EngineRoot "Engine\Binaries\Win64\UnrealEditor.exe"

    Assert-FileExists $EditorExe

    & $EditorExe $ProjectFile
}

SetAliases
