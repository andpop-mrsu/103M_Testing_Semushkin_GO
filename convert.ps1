<#
.SYNOPSIS
    Convert Markdown files to DOCX using Pandoc

.DESCRIPTION
    Converts either a single .md file or all .md files in a directory to .docx

.USAGE
    .\Convert-MdToDocx.ps1 <directory>
    .\Convert-MdToDocx.ps1 <file.md>
#>

# Check if pandoc is installed
if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
    Write-Error "Error: pandoc is not installed.`nPlease install it using:" -Category NotInstalled
    Write-Host "   winget install JohnMacFarlane.pandoc" -ForegroundColor Yellow
    Write-Host "   or download from: https://pandoc.org/installing.html" -ForegroundColor Yellow
    exit 1
}

# Check arguments
if ($args.Count -lt 1) {
    Write-Host "Usage:" -ForegroundColor Cyan
    Write-Host "   $($MyInvocation.MyCommand.Name) <directory>  — convert all .md files in a directory"
    Write-Host "   $($MyInvocation.MyCommand.Name) <file.md>    — convert a single file"
    exit 1
}

function Convert-File {
    param([string]$SourceFile)

    $DestinationFile = [System.IO.Path]::ChangeExtension($SourceFile, ".docx")

    try {
        pandoc "$SourceFile" -o "$DestinationFile"
        Write-Host "OK: $SourceFile -> $DestinationFile" -ForegroundColor Green
    }
    catch {
        Write-Error "Failed to convert: $SourceFile"
    }
}

$target = $args[0]

# Case 1: Target is a directory
if (Test-Path $target -PathType Container) {
    $mdFiles = Get-ChildItem -Path $target -Filter "*.md" -File | Sort-Object Name

    if ($mdFiles.Count -eq 0) {
        Write-Error "No .md files found in '$target'"
        exit 1
    }

    $count = 0
    foreach ($file in $mdFiles) {
        Convert-File $file.FullName
        $count++
    }

    Write-Host "`nDone: $count file(s) converted" -ForegroundColor Green
}

# Case 2: Target is a single .md file
elseif (Test-Path $target -PathType Leaf -And $target -like "*.md") {
    Convert-File $target
}

# Invalid input
else {
    Write-Error "Error: '$target' is not a directory or a valid .md file"
    exit 1
}