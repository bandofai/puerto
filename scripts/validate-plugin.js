#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Validates a Claude Code plugin structure and manifest
 * Usage: node validate-plugin.js <plugin-directory>
 */

function validatePlugin(pluginDir) {
  const errors = [];
  const warnings = [];

  // Check if directory exists
  if (!fs.existsSync(pluginDir)) {
    errors.push(`Plugin directory does not exist: ${pluginDir}`);
    return { valid: false, errors, warnings };
  }

  // Check for .claude-plugin directory
  const pluginMetaDir = path.join(pluginDir, '.claude-plugin');
  if (!fs.existsSync(pluginMetaDir)) {
    errors.push('Missing .claude-plugin directory');
    return { valid: false, errors, warnings };
  }

  // Check for plugin.json
  const pluginJsonPath = path.join(pluginMetaDir, 'plugin.json');
  if (!fs.existsSync(pluginJsonPath)) {
    errors.push('Missing .claude-plugin/plugin.json');
    return { valid: false, errors, warnings };
  }

  // Validate plugin.json structure
  try {
    const pluginJson = JSON.parse(fs.readFileSync(pluginJsonPath, 'utf8'));

    // Required fields
    const requiredFields = ['name', 'version', 'description'];
    requiredFields.forEach(field => {
      if (!pluginJson[field]) {
        errors.push(`Missing required field in plugin.json: ${field}`);
      }
    });

    // Validate name format (lowercase, alphanumeric, hyphens)
    if (pluginJson.name && !/^[a-z0-9-]+$/.test(pluginJson.name)) {
      errors.push('Plugin name must be lowercase alphanumeric with hyphens only');
    }

    // Validate version format (semver)
    if (pluginJson.version && !/^\d+\.\d+\.\d+/.test(pluginJson.version)) {
      warnings.push('Version should follow semver format (e.g., 1.0.0)');
    }

    // Check for author
    if (!pluginJson.author) {
      warnings.push('Missing recommended field: author');
    } else if (typeof pluginJson.author === 'string') {
      errors.push('author must be an object with a "name" property, not a string');
    } else if (typeof pluginJson.author === 'object' && !pluginJson.author.name) {
      errors.push('author object must have a "name" property');
    }

  } catch (err) {
    errors.push(`Invalid JSON in plugin.json: ${err.message}`);
    return { valid: false, errors, warnings };
  }

  // Check for README.md
  if (!fs.existsSync(path.join(pluginDir, 'README.md'))) {
    warnings.push('Missing README.md - highly recommended for documentation');
  }

  // Validate optional directories if they exist
  const optionalDirs = ['commands', 'agents', 'skills', 'hooks'];
  optionalDirs.forEach(dir => {
    const dirPath = path.join(pluginDir, dir);
    if (fs.existsSync(dirPath)) {
      if (!fs.statSync(dirPath).isDirectory()) {
        errors.push(`${dir} should be a directory, not a file`);
      }
    }
  });

  // Validate commands/*.md if commands directory exists
  const commandsDir = path.join(pluginDir, 'commands');
  if (fs.existsSync(commandsDir)) {
    const commandFiles = fs.readdirSync(commandsDir).filter(f => f.endsWith('.md'));
    if (commandFiles.length === 0) {
      warnings.push('commands/ directory exists but contains no .md files');
    }
  }

  return {
    valid: errors.length === 0,
    errors,
    warnings
  };
}

// CLI execution
if (require.main === module) {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.error('Usage: node validate-plugin.js <plugin-directory>');
    process.exit(1);
  }

  const pluginDir = path.resolve(args[0]);
  const result = validatePlugin(pluginDir);

  console.log(`\nValidating plugin: ${pluginDir}\n`);

  if (result.errors.length > 0) {
    console.log('❌ ERRORS:');
    result.errors.forEach(err => console.log(`  - ${err}`));
  }

  if (result.warnings.length > 0) {
    console.log('\n⚠️  WARNINGS:');
    result.warnings.forEach(warn => console.log(`  - ${warn}`));
  }

  if (result.valid) {
    console.log('\n✅ Plugin validation passed!\n');
    process.exit(0);
  } else {
    console.log('\n❌ Plugin validation failed\n');
    process.exit(1);
  }
}

module.exports = { validatePlugin };
