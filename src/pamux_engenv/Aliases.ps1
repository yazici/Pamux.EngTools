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
    param(
        [string]$EngineRoot = "C:\Program Files\Epic Games\UE_5.8"
    )

    $PluginSource = "C:\src\UnrealTools\UnrealIrExporter"
    $PluginPackage = "C:\src\UnrealTools\Build\UnrealIrExporter"
    $CropoutRoot = "C:\src\CropoutSampleProject 5.8"
    $DeployedPlugin = Join-Path $CropoutRoot "Plugins\UnrealIrExporter"
    $CropoutProject = Join-Path $CropoutRoot "CropoutSampleProject.uproject"
    $ExportOutput = "C:\src\UnrealTools\UnrealIrExports"
    $TargetSourceRoot = "C:\src\Cappadocia\Source"
    $LogPath = "C:\src\UnrealTools\log.txt"

    $State = [pscustomobject]@{
        Succeeded      = $false
        FailureMessage = $null
    }

    $LogDirectory = Split-Path $LogPath -Parent
    New-Item $LogDirectory -ItemType Directory -Force | Out-Null

    [System.IO.File]::WriteAllText(
        $LogPath,
        "",
        [System.Text.UTF8Encoding]::new($false)
    )

    & {
        try {
            Write-Output "Export-Cropout started: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
            Write-Output "Log: $LogPath"
            Write-Output ""

            $RunUat = Join-Path $EngineRoot "Engine\Build\BatchFiles\RunUAT.bat"
            $EditorCmd = Join-Path $EngineRoot "Engine\Binaries\Win64\UnrealEditor-Cmd.exe"
            $PluginFile = Join-Path $PluginSource "UnrealIrExporter.uplugin"
            $CropoutPlugins = Join-Path $CropoutRoot "Plugins"
            $OldDeployedPlugin = Join-Path $CropoutPlugins "BlueprintIrExporter"

            foreach ($RequiredFile in @(
                $RunUat
                $EditorCmd
                $PluginFile
                $CropoutProject
            )) {
                Assert-FileExists $RequiredFile
            }

            New-Item $CropoutPlugins -ItemType Directory -Force | Out-Null

            Remove-Item `
                $PluginPackage `
                -Recurse `
                -Force `
                -ErrorAction SilentlyContinue

            Write-Output ""
            Write-Output "Building UnrealIrExporter..."

            & $RunUat `
                BuildPlugin `
                -Plugin="$PluginFile" `
                -Package="$PluginPackage" `
                -TargetPlatforms=Win64 `
                -NoUBA 2>&1

            $BuildExitCode = $LASTEXITCODE

            if ($BuildExitCode -ne 0) {
                throw "UnrealIrExporter build failed with exit code $BuildExitCode."
            }

            Assert-FileExists (Join-Path $PluginPackage "UnrealIrExporter.uplugin")

            Remove-Item `
                $DeployedPlugin `
                -Recurse `
                -Force `
                -ErrorAction SilentlyContinue

            Remove-Item `
                $OldDeployedPlugin `
                -Recurse `
                -Force `
                -ErrorAction SilentlyContinue

            Write-Output ""
            Write-Output "Deploying UnrealIrExporter..."

            Copy-Item `
                $PluginPackage `
                $DeployedPlugin `
                -Recurse `
                -Force `
                -ErrorAction Stop

            Assert-FileExists (Join-Path $DeployedPlugin "UnrealIrExporter.uplugin")

            Remove-Item `
                $ExportOutput `
                -Recurse `
                -Force `
                -ErrorAction SilentlyContinue

            New-Item `
                $ExportOutput `
                -ItemType Directory `
                -Force `
                -ErrorAction Stop |
                Out-Null

            Write-Output ""
            Write-Output "Exporting Cropout Unreal IR..."

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
                -stdout `
                -FullStdOutLogOutput `
                -log 2>&1

            $ExportExitCode = $LASTEXITCODE

            if ($ExportExitCode -ne 0) {
                throw "Unreal IR export failed with exit code $ExportExitCode."
            }

            Write-Output ""
            Write-Output "Export completed."
            Write-Output "IR JSON: $ExportOutput"
            Write-Output "Headers: $TargetSourceRoot\Cappadocia\Generated\Public"
            Write-Output "Implementations: $TargetSourceRoot\Cappadocia\Generated\Private"

            $State.Succeeded = $true
        }
        catch {
            $State.FailureMessage = $_.Exception.Message
            Write-Output ""
            Write-Output "ERROR: $($State.FailureMessage)"
        }
        finally {
            Write-Output ""
            Write-Output "Export-Cropout finished: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
            Write-Output "Complete log: $LogPath"
        }
    } *>&1 | ForEach-Object {
        $Line = $_ | Out-String
        $Line = $Line.TrimEnd("`r", "`n")

        Write-Host $Line
        [System.IO.File]::AppendAllText(
            $LogPath,
            $Line + [Environment]::NewLine,
            [System.Text.UTF8Encoding]::new($false)
        )
    }

    Write-Host ""
    Write-Host "Complete log: $LogPath"

    if (-not $State.Succeeded) {
        if (-not [string]::IsNullOrWhiteSpace($State.FailureMessage)) {
            throw $State.FailureMessage
        }

        throw "Export-Cropout failed without a captured exception. See $LogPath."
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

    $Log = "C:\src\bblog.txt"

    Push-Location $ProjectRoot

    try {
        & $BuildBat `
            CappadociaEditor `
            Win64 `
            Development `
            -Project="$ProjectFile" `
            -WaitMutex 2>&1 |
            Tee-Object -FilePath $Log

        if ($LASTEXITCODE -ne 0) {
            throw "Cappadocia build failed with exit code $LASTEXITCODE"
        }
    }
    finally {
        Pop-Location
    }

    Write-Host ""
    Write-Host "Build log: $Log"
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

function Remove-AllFiles {
    [CmdletBinding(SupportsShouldProcess)]
    param (
        [Parameter(Mandatory, Position = 0)]
        [ValidateNotNullOrEmpty()]
        [string]$Path
    )

    $ResolvedPath = Resolve-Path -LiteralPath $Path -ErrorAction Stop

    if (-not (Test-Path -LiteralPath $ResolvedPath -PathType Container)) {
        throw "Path is not a directory: $ResolvedPath"
    }

    Get-ChildItem `
        -LiteralPath $ResolvedPath `
        -File `
        -Recurse `
        -Force `
        -ErrorAction Stop |
    ForEach-Object {
        if ($PSCmdlet.ShouldProcess($_.FullName, "Delete file")) {
            Remove-Item -LiteralPath $_.FullName -Force -ErrorAction Stop
        }
    }
}


Remove-AllFiles C:\src\Cappadocia\Source\Cappadocia\Private\Blueprint
Remove-AllFiles C:\src\Cappadocia\Source\Cappadocia\Private\Characters
Remove-AllFiles C:\src\Cappadocia\Source\Cappadocia\Private\IslandGenerator
Remove-AllFiles C:\src\Cappadocia\Source\Cappadocia\Private\UI

Remove-AllFiles C:\src\Cappadocia\Source\Cappadocia\Public\Blueprint
Remove-AllFiles C:\src\Cappadocia\Source\Cappadocia\Public\Characters
Remove-AllFiles C:\src\Cappadocia\Source\Cappadocia\Public\IslandGenerator
Remove-AllFiles C:\src\Cappadocia\Source\Cappadocia\Public\UI
 
SetAliases
