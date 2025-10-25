#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Generates marketplace.json by scanning all plugins in the plugins/ directory
 */

function generateCatalog() {
  const pluginsDir = path.join(__dirname, '..', 'plugins');
  const marketplaceJsonPath = path.join(__dirname, '..', '.claude-plugin', 'marketplace.json');

  // Ensure plugins directory exists
  if (!fs.existsSync(pluginsDir)) {
    console.error('plugins/ directory not found');
    process.exit(1);
  }

  // Read all plugin directories
  const pluginDirs = fs.readdirSync(pluginsDir)
    .filter(name => {
      const fullPath = path.join(pluginsDir, name);
      return fs.statSync(fullPath).isDirectory() && !name.startsWith('.');
    });

  const plugins = [];

  // Process each plugin
  for (const pluginName of pluginDirs) {
    const pluginPath = path.join(pluginsDir, pluginName);
    const pluginJsonPath = path.join(pluginPath, '.claude-plugin', 'plugin.json');

    // Skip if no plugin.json
    if (!fs.existsSync(pluginJsonPath)) {
      console.warn(`⚠️  Skipping ${pluginName}: missing .claude-plugin/plugin.json`);
      continue;
    }

    try {
      const pluginJson = JSON.parse(fs.readFileSync(pluginJsonPath, 'utf8'));

      plugins.push({
        name: pluginJson.name || pluginName,
        source: `./plugins/${pluginName}`,
        description: pluginJson.description || 'No description provided'
      });

      console.log(`✅ Added plugin: ${pluginJson.name || pluginName}`);
    } catch (err) {
      console.error(`❌ Error reading ${pluginName}/plugin.json: ${err.message}`);
    }
  }

  // Sort plugins alphabetically by name
  plugins.sort((a, b) => a.name.localeCompare(b.name));

  // Create marketplace manifest
  const marketplace = {
    name: 'puerto',
    owner: {
      name: 'Puerto'
    },
    plugins
  };

  // Write to file
  fs.writeFileSync(
    marketplaceJsonPath,
    JSON.stringify(marketplace, null, 2) + '\n',
    'utf8'
  );

  console.log(`\n✅ Generated marketplace.json with ${plugins.length} plugin(s)\n`);
}

// CLI execution
if (require.main === module) {
  generateCatalog();
}

module.exports = { generateCatalog };
