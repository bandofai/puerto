#!/usr/bin/env bash

#######################################################################
# Puerto Prompt Analyzer Hook Installer
#
# Automatically configures the Puerto Prompt Analyzer hook in your
# Claude Code settings.json file.
#
# Usage: ./install-hook.sh
#######################################################################

set -e

echo "🔧 Puerto Prompt Analyzer Hook Installer"
echo "========================================="
echo ""

# Detect OS
OS="$(uname -s)"
case "$OS" in
    Darwin*)  OS_TYPE="macOS";;
    Linux*)   OS_TYPE="Linux";;
    CYGWIN*|MINGW*|MSYS*) OS_TYPE="Windows";;
    *)        OS_TYPE="Unknown";;
esac

echo "📍 Detected OS: $OS_TYPE"
echo ""

# Set paths based on OS
if [ "$OS_TYPE" = "Windows" ]; then
    SETTINGS_FILE="$USERPROFILE/.claude/settings.json"
    PLUGIN_SEARCH_DIR="$USERPROFILE/.claude/plugins"
else
    SETTINGS_FILE="$HOME/.claude/settings.json"
    PLUGIN_SEARCH_DIR="$HOME/.claude/plugins"
fi

# Step 1: Find the hook script
echo "🔍 Step 1: Finding puerto-prompt-analyzer.js..."

if [ "$OS_TYPE" = "macOS" ] || [ "$OS_TYPE" = "Linux" ]; then
    HOOK_PATH=$(find "$PLUGIN_SEARCH_DIR" -name "puerto-prompt-analyzer.js" 2>/dev/null | head -1)
else
    echo "⚠️  Windows detected. Please run the PowerShell version: install-hook.ps1"
    exit 1
fi

if [ -z "$HOOK_PATH" ]; then
    echo "❌ Error: Could not find puerto-prompt-analyzer.js"
    echo ""
    echo "Please ensure the essentials plugin is installed:"
    echo "  /plugin install essentials@puerto"
    exit 1
fi

echo "✅ Found hook at: $HOOK_PATH"
echo ""

# Step 2: Check if Node.js is available
echo "🔍 Step 2: Checking Node.js installation..."

if ! command -v node &> /dev/null; then
    echo "❌ Error: Node.js not found in PATH"
    echo ""
    echo "Please install Node.js >= v18.0.0"
    echo "Visit: https://nodejs.org/"
    exit 1
fi

NODE_VERSION=$(node --version)
echo "✅ Found Node.js: $NODE_VERSION"
echo ""

# Step 3: Create or update settings.json
echo "🔍 Step 3: Updating settings.json..."

# Check if settings file exists
if [ ! -f "$SETTINGS_FILE" ]; then
    echo "📝 Creating new settings.json..."
    mkdir -p "$(dirname "$SETTINGS_FILE")"
    echo '{}' > "$SETTINGS_FILE"
fi

# Backup original settings
BACKUP_FILE="${SETTINGS_FILE}.backup.$(date +%Y%m%d_%H%M%S)"
cp "$SETTINGS_FILE" "$BACKUP_FILE"
echo "📦 Backup created: $BACKUP_FILE"
echo ""

# Read current settings
CURRENT_SETTINGS=$(cat "$SETTINGS_FILE")

# Check if hook already exists
if echo "$CURRENT_SETTINGS" | grep -q "puerto-prompt-analyzer"; then
    echo "⚠️  Hook configuration already exists in settings.json"
    echo ""
    read -p "Do you want to update it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Installation cancelled"
        exit 0
    fi
fi

# Use Python to safely merge JSON
python3 << PYTHON_EOF
import json
import sys

try:
    # Read current settings
    with open("$SETTINGS_FILE", "r") as f:
        settings = json.load(f)

    # Ensure hooks object exists
    if "hooks" not in settings:
        settings["hooks"] = {}

    # Add or update UserPromptSubmit hook
    settings["hooks"]["UserPromptSubmit"] = [
        {
            "hooks": [
                {
                    "type": "command",
                    "command": "node $HOOK_PATH",
                    "timeout": 60
                }
            ]
        }
    ]

    # Write back to file
    with open("$SETTINGS_FILE", "w") as f:
        json.dump(settings, f, indent=2)
        f.write("\n")

    print("✅ Successfully updated settings.json")
    sys.exit(0)

except Exception as e:
    print(f"❌ Error updating settings: {e}")
    print(f"Your original settings have been backed up to: $BACKUP_FILE")
    sys.exit(1)

PYTHON_EOF

if [ $? -ne 0 ]; then
    echo ""
    echo "Installation failed. Your original settings are safe in:"
    echo "  $BACKUP_FILE"
    exit 1
fi

echo ""
echo "✅ Installation Complete!"
echo ""
echo "Next steps:"
echo "  1. Restart Claude Code"
echo "  2. Test by submitting any prompt (e.g., 'help me build a feature')"
echo "  3. You should see '🔍 Instruction Analysis' in the response"
echo ""
echo "To uninstall:"
echo "  1. Edit $SETTINGS_FILE"
echo "  2. Remove the 'hooks' > 'UserPromptSubmit' section"
echo "  3. Restart Claude Code"
echo ""
echo "Original settings backed up to:"
echo "  $BACKUP_FILE"
echo ""
