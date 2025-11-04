# Puerto Prompt Analyzer Hook Installer (Windows PowerShell)
#
# Automatically configures the Puerto Prompt Analyzer hook in your
# Claude Code settings.json file.
#
# Usage: .\install-hook.ps1

Write-Host "🔧 Puerto Prompt Analyzer Hook Installer" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Set paths
$SettingsFile = Join-Path $env:USERPROFILE ".claude\settings.json"
$PluginSearchDir = Join-Path $env:USERPROFILE ".claude\plugins"

# Step 1: Find the hook script
Write-Host "🔍 Step 1: Finding puerto-prompt-analyzer.js..." -ForegroundColor Yellow

$HookPath = Get-ChildItem -Path $PluginSearchDir -Recurse -Filter "puerto-prompt-analyzer.js" -ErrorAction SilentlyContinue |
            Select-Object -First 1 -ExpandProperty FullName

if (-not $HookPath) {
    Write-Host "❌ Error: Could not find puerto-prompt-analyzer.js" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please ensure the essentials plugin is installed:"
    Write-Host "  /plugin install essentials@puerto"
    exit 1
}

Write-Host "✅ Found hook at: $HookPath" -ForegroundColor Green
Write-Host ""

# Step 2: Check if Node.js is available
Write-Host "🔍 Step 2: Checking Node.js installation..." -ForegroundColor Yellow

try {
    $NodeVersion = & node --version 2>$null
    Write-Host "✅ Found Node.js: $NodeVersion" -ForegroundColor Green
    Write-Host ""
} catch {
    Write-Host "❌ Error: Node.js not found in PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Node.js >= v18.0.0"
    Write-Host "Visit: https://nodejs.org/"
    exit 1
}

# Step 3: Create or update settings.json
Write-Host "🔍 Step 3: Updating settings.json..." -ForegroundColor Yellow

# Check if settings file exists
if (-not (Test-Path $SettingsFile)) {
    Write-Host "📝 Creating new settings.json..." -ForegroundColor Cyan
    $SettingsDir = Split-Path $SettingsFile -Parent
    if (-not (Test-Path $SettingsDir)) {
        New-Item -ItemType Directory -Path $SettingsDir -Force | Out-Null
    }
    Set-Content -Path $SettingsFile -Value '{}'
}

# Backup original settings
$BackupFile = "$SettingsFile.backup.$(Get-Date -Format 'yyyyMMdd_HHmmss')"
Copy-Item $SettingsFile $BackupFile
Write-Host "📦 Backup created: $BackupFile" -ForegroundColor Cyan
Write-Host ""

# Read current settings
$CurrentSettings = Get-Content $SettingsFile -Raw

# Check if hook already exists
if ($CurrentSettings -match "puerto-prompt-analyzer") {
    Write-Host "⚠️  Hook configuration already exists in settings.json" -ForegroundColor Yellow
    Write-Host ""
    $Response = Read-Host "Do you want to update it? (y/N)"
    if ($Response -notmatch "^[Yy]$") {
        Write-Host "❌ Installation cancelled" -ForegroundColor Red
        exit 0
    }
}

# Update settings using PowerShell JSON handling
try {
    $Settings = Get-Content $SettingsFile -Raw | ConvertFrom-Json -AsHashtable

    # Ensure hooks object exists
    if (-not $Settings.ContainsKey("hooks")) {
        $Settings["hooks"] = @{}
    }

    # Add or update UserPromptSubmit hook
    $Settings["hooks"]["UserPromptSubmit"] = @(
        @{
            "hooks" = @(
                @{
                    "type" = "command"
                    "command" = "node $HookPath"
                    "timeout" = 60
                }
            )
        }
    )

    # Write back to file with proper formatting
    $Settings | ConvertTo-Json -Depth 10 | Set-Content $SettingsFile
    Write-Host "✅ Successfully updated settings.json" -ForegroundColor Green
} catch {
    Write-Host "❌ Error updating settings: $_" -ForegroundColor Red
    Write-Host "Your original settings have been backed up to: $BackupFile"
    exit 1
}

Write-Host ""
Write-Host "✅ Installation Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Restart Claude Code"
Write-Host "  2. Test by submitting any prompt (e.g., 'help me build a feature')"
Write-Host "  3. You should see '🔍 Instruction Analysis' in the response"
Write-Host ""
Write-Host "To uninstall:"
Write-Host "  1. Edit $SettingsFile"
Write-Host "  2. Remove the 'hooks' > 'UserPromptSubmit' section"
Write-Host "  3. Restart Claude Code"
Write-Host ""
Write-Host "Original settings backed up to:"
Write-Host "  $BackupFile"
Write-Host ""
