#!/usr/bin/env node

/**
 * Puerto Prompt Analyzer Hook for Claude Code (v2.0)
 *
 * Analyzes user prompts before Claude processes them, providing:
 * - Task type classification (research, implementation, mixed)
 * - Instruction quality validation
 * - Intelligent plugin recommendations from Puerto marketplace
 * - Project context awareness
 * - Caching and performance optimization
 *
 * Part of the essentials plugin
 * @see plugins/essentials/hooks/README.md for documentation
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

// ============================================================================
// CONFIGURATION
// ============================================================================

const RESEARCH_KEYWORDS = [
  'explain', 'analyze', 'research', 'investigate', 'understand',
  'review', 'compare', 'summarize', 'describe', 'document',
  'learn', 'study', 'explore', 'examine', 'evaluate'
];

const IMPLEMENTATION_KEYWORDS = [
  'implement', 'create', 'build', 'fix', 'refactor', 'add',
  'modify', 'write', 'develop', 'code', 'make', 'update',
  'change', 'remove', 'delete', 'optimize', 'improve', 'deploy'
];

const STOP_WORDS = new Set([
  'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
  'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'be', 'been',
  'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should',
  'could', 'may', 'might', 'can', 'this', 'that', 'these', 'those'
]);

const VALIDATION_PATTERNS = {
  tooVague: {
    patterns: [/^(fix it|make it better|improve this|do it|help)$/i],
    suggestion: 'Be more specific about what you want to fix or improve'
  },
  missingContext: {
    patterns: [/\b(this|that|it)\b/i],
    minLength: 30,
    suggestion: 'Provide clear context - what specifically does "this" or "that" refer to?'
  },
  overlyBroad: {
    patterns: [/^(build an? app|create a (website|system)|make (something|a thing))$/i],
    suggestion: 'Break down your request into specific features or components'
  }
};

// Scoring weights (tuned for better results)
const WEIGHTS = {
  keywordMatch: 3,
  nameMatch: 5,
  descriptionOverlap: 2,
  categoryMatch: 4,
  taskTypeAlign: 5,
  projectTypeMatch: 3
};

const MIN_SCORE_THRESHOLD = 8;
const MAX_RECOMMENDATIONS = 3;
const CACHE_TTL = 60000; // 60 seconds
const SESSION_MEMORY_TTL = 3600000; // 1 hour

// ============================================================================
// CACHING & SESSION MANAGEMENT
// ============================================================================

const CACHE = {
  marketplace: null,
  marketplacePath: null,
  timestamp: 0,
  installedPlugins: null,
  installedTimestamp: 0
};

const SESSION_MEMORY = new Map(); // session_id -> { shown: Set, timestamp }

function cleanupOldSessions() {
  const now = Date.now();
  for (const [sessionId, data] of SESSION_MEMORY.entries()) {
    if (now - data.timestamp > SESSION_MEMORY_TTL) {
      SESSION_MEMORY.delete(sessionId);
    }
  }
}

function getSessionMemory(sessionId) {
  if (!SESSION_MEMORY.has(sessionId)) {
    SESSION_MEMORY.set(sessionId, {
      shown: new Set(),
      timestamp: Date.now()
    });
  }
  return SESSION_MEMORY.get(sessionId);
}

function markAsShown(sessionId, pluginName) {
  const memory = getSessionMemory(sessionId);
  memory.shown.add(pluginName);
  memory.timestamp = Date.now();
}

function wasRecentlyShown(sessionId, pluginName) {
  const memory = SESSION_MEMORY.get(sessionId);
  return memory && memory.shown.has(pluginName);
}

// ============================================================================
// MAIN ENTRY POINT
// ============================================================================

function main() {
  const perfStart = Date.now();

  try {
    // Cleanup old sessions periodically
    if (Math.random() < 0.1) { // 10% chance
      cleanupOldSessions();
    }

    // Read hook input from stdin
    const input = fs.readFileSync(0, 'utf-8');
    const hookInput = JSON.parse(input);

    // Analyze and generate output
    const result = analyzeInstruction(hookInput);

    // Output JSON to stdout
    console.log(JSON.stringify(result, null, 2));

    // Performance logging
    const elapsed = Date.now() - perfStart;
    if (elapsed > 500) {
      console.error(`[puerto-prompt-analyzer] SLOW execution: ${elapsed}ms`);
    }

  } catch (error) {
    // Fail open - log error but allow prompt to proceed
    console.error('[puerto-prompt-analyzer] Fatal error:', error.message);
    console.log(JSON.stringify(allowPrompt()));
    process.exit(0);
  }
}

// ============================================================================
// CORE ANALYSIS LOGIC
// ============================================================================

function analyzeInstruction(hookInput) {
  try {
    const { prompt, cwd, session_id } = hookInput;

    // Skip if empty or command
    if (!prompt || !prompt.trim()) {
      return allowPrompt();
    }

    if (prompt.trim().startsWith('/')) {
      return allowPrompt();
    }

    // Load configuration
    const config = loadConfiguration();

    // Classify task type
    const taskType = classifyTaskType(prompt);

    // Detect project context
    const projectContext = detectProjectContext(cwd);

    // Validate instruction quality
    const validation = validateInstruction(prompt);

    // Load and score plugins
    const recommendations = getPluginRecommendations(
      prompt,
      taskType,
      cwd,
      session_id,
      projectContext,
      config
    );

    // Mark shown plugins
    recommendations.forEach(p => markAsShown(session_id, p.name));

    // Generate markdown output
    const additionalContext = formatRecommendations(
      taskType,
      recommendations,
      validation,
      projectContext
    );

    return {
      decision: undefined,
      reason: 'Analysis complete',
      hookSpecificOutput: {
        hookEventName: 'UserPromptSubmit',
        additionalContext
      }
    };

  } catch (error) {
    console.error('[puerto-prompt-analyzer] Error during analysis:', error.message);
    return allowPrompt();
  }
}

// ============================================================================
// CONFIGURATION MANAGEMENT
// ============================================================================

function loadConfiguration() {
  const configPath = path.join(os.homedir(), '.claude', 'puerto-prompt-analyzer.json');

  const defaults = {
    minScore: MIN_SCORE_THRESHOLD,
    maxRecommendations: MAX_RECOMMENDATIONS,
    cacheMinutes: 1,
    blacklist: [],
    favoriteCategories: [],
    showScores: false
  };

  try {
    if (fs.existsSync(configPath)) {
      const userConfig = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
      return { ...defaults, ...userConfig };
    }
  } catch (error) {
    console.error('[puerto-prompt-analyzer] Error loading config:', error.message);
  }

  return defaults;
}

// ============================================================================
// PROJECT CONTEXT DETECTION
// ============================================================================

function detectProjectContext(cwd) {
  if (!cwd) return { type: 'unknown', files: [] };

  const context = {
    type: 'unknown',
    languages: [],
    frameworks: [],
    files: []
  };

  try {
    // Check for package.json (JavaScript/Node.js)
    if (fs.existsSync(path.join(cwd, 'package.json'))) {
      context.type = 'javascript';
      context.languages.push('javascript', 'nodejs');

      const pkg = JSON.parse(fs.readFileSync(path.join(cwd, 'package.json'), 'utf-8'));

      // Detect frameworks
      const deps = { ...pkg.dependencies, ...pkg.devDependencies };
      if (deps['react']) context.frameworks.push('react');
      if (deps['vue']) context.frameworks.push('vue');
      if (deps['next']) context.frameworks.push('nextjs');
      if (deps['express']) context.frameworks.push('express');
    }

    // Check for Python
    if (fs.existsSync(path.join(cwd, 'requirements.txt')) ||
        fs.existsSync(path.join(cwd, 'pyproject.toml'))) {
      context.type = 'python';
      context.languages.push('python');
    }

    // Check for Rust
    if (fs.existsSync(path.join(cwd, 'Cargo.toml'))) {
      context.type = 'rust';
      context.languages.push('rust');
    }

    // Check for Go
    if (fs.existsSync(path.join(cwd, 'go.mod'))) {
      context.type = 'go';
      context.languages.push('go', 'golang');
    }

    // Check for Ruby
    if (fs.existsSync(path.join(cwd, 'Gemfile'))) {
      context.type = 'ruby';
      context.languages.push('ruby');
    }

    // Check for Java/Kotlin
    if (fs.existsSync(path.join(cwd, 'pom.xml')) ||
        fs.existsSync(path.join(cwd, 'build.gradle'))) {
      context.type = 'java';
      context.languages.push('java');
    }

  } catch (error) {
    console.error('[puerto-prompt-analyzer] Error detecting project:', error.message);
  }

  return context;
}

// ============================================================================
// TEXT PROCESSING UTILITIES
// ============================================================================

function stem(word) {
  // Simple stemmer - remove common suffixes
  return word
    .replace(/ies$/, 'y')
    .replace(/ing$/, '')
    .replace(/ed$/, '')
    .replace(/s$/, '')
    .toLowerCase();
}

function tokenize(text) {
  return text
    .toLowerCase()
    .replace(/[^\w\s-]/g, ' ') // Keep hyphens
    .split(/\s+/)
    .map(stem)
    .filter(w => w.length > 2 && !STOP_WORDS.has(w));
}

// ============================================================================
// TASK CLASSIFICATION
// ============================================================================

function classifyTaskType(prompt) {
  const tokens = tokenize(prompt);
  const lower = prompt.toLowerCase();

  // Count keyword matches (using stemmed tokens)
  const researchScore = RESEARCH_KEYWORDS.filter(kw =>
    tokens.includes(stem(kw)) || lower.includes(kw)
  ).length;

  const implScore = IMPLEMENTATION_KEYWORDS.filter(kw =>
    tokens.includes(stem(kw)) || lower.includes(kw)
  ).length;

  // Enhanced classification
  if (implScore > researchScore * 1.5) {
    return 'Implementation';
  }
  if (researchScore > implScore * 1.5) {
    return 'Research';
  }
  if (researchScore > 0 && implScore > 0) {
    return 'Mixed';
  }

  return 'General';
}

// ============================================================================
// INSTRUCTION VALIDATION
// ============================================================================

function validateInstruction(prompt) {
  const suggestions = [];

  // Check for vague instructions
  if (VALIDATION_PATTERNS.tooVague.patterns.some(p => p.test(prompt))) {
    suggestions.push(VALIDATION_PATTERNS.tooVague.suggestion);
  }

  // Check for missing context (only if prompt is very short)
  const minLength = VALIDATION_PATTERNS.missingContext.minLength;
  if (prompt.length < minLength &&
      VALIDATION_PATTERNS.missingContext.patterns.some(p => p.test(prompt))) {
    suggestions.push(VALIDATION_PATTERNS.missingContext.suggestion);
  }

  // Check for overly broad requests
  if (VALIDATION_PATTERNS.overlyBroad.patterns.some(p => p.test(prompt))) {
    suggestions.push(VALIDATION_PATTERNS.overlyBroad.suggestion);
  }

  return { suggestions };
}

// ============================================================================
// INSTALLED PLUGINS DETECTION
// ============================================================================

function getInstalledPlugins() {
  const now = Date.now();

  // Use cache
  if (CACHE.installedPlugins && (now - CACHE.installedTimestamp) < CACHE_TTL) {
    return CACHE.installedPlugins;
  }

  const installed = new Set();

  try {
    const settingsPath = path.join(os.homedir(), '.claude', 'settings.json');

    if (fs.existsSync(settingsPath)) {
      const settings = JSON.parse(fs.readFileSync(settingsPath, 'utf-8'));

      if (settings.enabledPlugins) {
        Object.keys(settings.enabledPlugins).forEach(pluginId => {
          // Extract plugin name from "plugin@marketplace" format
          const pluginName = pluginId.split('@')[0];
          installed.add(pluginName);
        });
      }
    }
  } catch (error) {
    console.error('[puerto-prompt-analyzer] Error reading installed plugins:', error.message);
  }

  CACHE.installedPlugins = installed;
  CACHE.installedTimestamp = now;

  return installed;
}

// ============================================================================
// PLUGIN RECOMMENDATIONS
// ============================================================================

function getPluginRecommendations(prompt, taskType, cwd, sessionId, projectContext, config) {
  try {
    // Find and load marketplace.json (with caching)
    const marketplacePath = findMarketplaceJson(cwd);

    if (!marketplacePath) {
      console.error('[puerto-prompt-analyzer] marketplace.json not found');
      return [];
    }

    const marketplace = getMarketplaceData(marketplacePath);

    if (!marketplace || !marketplace.plugins || !Array.isArray(marketplace.plugins)) {
      console.error('[puerto-prompt-analyzer] Invalid marketplace format');
      return [];
    }

    const installedPlugins = getInstalledPlugins();

    // Score all plugins
    const scored = marketplace.plugins
      .map(plugin => ({
        ...plugin,
        score: scorePlugin(plugin, prompt, taskType, sessionId, projectContext, installedPlugins, config)
      }))
      .filter(p => p.score >= config.minScore) // Quality threshold
      .sort((a, b) => b.score - a.score);

    // Apply diversity (don't show too many similar plugins)
    const diverse = diversifyRecommendations(scored, config.maxRecommendations);

    // Add recommendation reasons
    return diverse.map(plugin => ({
      ...plugin,
      reason: generateReason(plugin, taskType, prompt, projectContext)
    }));

  } catch (error) {
    console.error('[puerto-prompt-analyzer] Error loading marketplace:', error.message);
    return [];
  }
}

function getMarketplaceData(marketplacePath) {
  const now = Date.now();

  // Check cache
  if (CACHE.marketplace &&
      CACHE.marketplacePath === marketplacePath &&
      (now - CACHE.timestamp) < CACHE_TTL) {
    return CACHE.marketplace;
  }

  // Load and cache
  try {
    CACHE.marketplace = JSON.parse(fs.readFileSync(marketplacePath, 'utf-8'));
    CACHE.marketplacePath = marketplacePath;
    CACHE.timestamp = now;
    return CACHE.marketplace;
  } catch (error) {
    console.error('[puerto-prompt-analyzer] Error parsing marketplace:', error.message);
    return null;
  }
}

function findMarketplaceJson(startDir) {
  if (!startDir) {
    return null;
  }

  let currentDir = startDir;

  // Search up to 5 levels up
  for (let i = 0; i < 5; i++) {
    const marketplacePath = path.join(currentDir, '.claude-plugin', 'marketplace.json');

    if (fs.existsSync(marketplacePath)) {
      return marketplacePath;
    }

    const parentDir = path.dirname(currentDir);
    if (parentDir === currentDir) {
      break; // Reached root
    }
    currentDir = parentDir;
  }

  return null;
}

function scorePlugin(plugin, prompt, taskType, sessionId, projectContext, installedPlugins, config) {
  const promptTokens = new Set(tokenize(prompt));
  const lower = prompt.toLowerCase();
  let score = 0;

  // Skip essentials plugin (it's already installed by definition)
  if (plugin.name === 'essentials') {
    return -1;
  }

  // Skip blacklisted plugins
  if (config.blacklist.includes(plugin.name)) {
    return -1;
  }

  // Skip installed plugins
  if (installedPlugins.has(plugin.name)) {
    return -1;
  }

  // Reduce score for recently shown plugins
  if (wasRecentlyShown(sessionId, plugin.name)) {
    score -= 5; // Penalty for repetition
  }

  // 1. Tokenized description overlap (better than simple word matching)
  if (plugin.description) {
    const descTokens = tokenize(plugin.description);
    const overlap = descTokens.filter(t => promptTokens.has(t)).length;
    score += overlap * WEIGHTS.descriptionOverlap;
  }

  // 2. Name match (strong signal)
  if (plugin.name) {
    const nameWords = plugin.name.split('-');
    const nameMatches = nameWords.filter(w =>
      promptTokens.has(stem(w)) || lower.includes(w)
    ).length;
    score += nameMatches * WEIGHTS.nameMatch;
  }

  // 3. Keywords match
  if (plugin.keywords && Array.isArray(plugin.keywords)) {
    const keywordMatches = plugin.keywords.filter(kw =>
      promptTokens.has(stem(kw)) || lower.includes(kw.toLowerCase())
    ).length;
    score += keywordMatches * WEIGHTS.keywordMatch;
  }

  // 4. Task type alignment
  if (taskType === 'Implementation') {
    if (plugin.description && /agent|specialist|builder|creator|developer/.test(plugin.description.toLowerCase())) {
      score += WEIGHTS.taskTypeAlign;
    }
  }

  if (taskType === 'Research') {
    if (plugin.description && /skill|knowledge|guide|reference|documentation/.test(plugin.description.toLowerCase())) {
      score += WEIGHTS.taskTypeAlign;
    }
  }

  // 5. Project context matching
  if (projectContext.type !== 'unknown') {
    const contextTerms = [
      ...projectContext.languages,
      ...projectContext.frameworks,
      projectContext.type
    ];

    contextTerms.forEach(term => {
      if (plugin.keywords && plugin.keywords.some(kw => kw.toLowerCase().includes(term))) {
        score += WEIGHTS.projectTypeMatch;
      }
      if (plugin.description && plugin.description.toLowerCase().includes(term)) {
        score += WEIGHTS.projectTypeMatch * 0.5;
      }
    });
  }

  // 6. Category boost for favorites
  if (config.favoriteCategories.length > 0 && plugin.category) {
    if (config.favoriteCategories.includes(plugin.category)) {
      score += 3;
    }
  }

  return Math.max(0, score); // Never negative
}

function diversifyRecommendations(plugins, maxCount) {
  const selected = [];
  const usedCategories = new Set();
  const usedKeywords = new Set();

  // First pass: pick best from different categories
  for (const plugin of plugins) {
    if (selected.length >= maxCount) break;

    const category = plugin.category || 'general';
    const primaryKeyword = (plugin.keywords && plugin.keywords[0]) || '';

    // Prefer different categories and keywords
    if (!usedCategories.has(category) || selected.length === 0) {
      selected.push(plugin);
      usedCategories.add(category);
      if (primaryKeyword) usedKeywords.add(primaryKeyword);
    }
  }

  // Second pass: fill remaining slots if needed
  if (selected.length < maxCount) {
    for (const plugin of plugins) {
      if (selected.length >= maxCount) break;
      if (!selected.includes(plugin)) {
        selected.push(plugin);
      }
    }
  }

  return selected;
}

function generateReason(plugin, taskType, prompt, projectContext) {
  const reasons = [];

  // Check for strong keyword matches
  if (plugin.keywords && Array.isArray(plugin.keywords)) {
    const matches = plugin.keywords.filter(kw =>
      prompt.toLowerCase().includes(kw.toLowerCase())
    );
    if (matches.length > 0) {
      reasons.push(`Matches keywords: ${matches.slice(0, 2).join(', ')}`);
    }
  }

  // Check for name matches
  const nameWords = plugin.name.split('-');
  const nameMatches = nameWords.filter(w =>
    prompt.toLowerCase().includes(w)
  );
  if (nameMatches.length > 0) {
    reasons.push(`Related to ${nameMatches.join(', ')}`);
  }

  // Project context match
  if (projectContext.type !== 'unknown') {
    const contextTerms = [...projectContext.languages, ...projectContext.frameworks];
    const matches = contextTerms.filter(term =>
      (plugin.description && plugin.description.toLowerCase().includes(term)) ||
      (plugin.keywords && plugin.keywords.some(kw => kw.toLowerCase().includes(term)))
    );

    if (matches.length > 0) {
      reasons.push(`Fits your ${projectContext.type} project`);
    }
  }

  // Task type alignment
  if (taskType === 'Implementation') {
    reasons.push('Provides specialized implementation tools');
  } else if (taskType === 'Research') {
    reasons.push('Offers expert knowledge and guidance');
  }

  // Default reason if nothing specific
  if (reasons.length === 0) {
    reasons.push('Relevant to your task based on description');
  }

  return reasons[0]; // Return the most specific reason
}

// ============================================================================
// OUTPUT FORMATTING
// ============================================================================

function formatRecommendations(taskType, plugins, validation, projectContext) {
  let md = '\n\n---\n\n## 🔍 Puerto Prompt Analysis\n\n';

  // Task type
  md += `**Task Type:** ${taskType}`;

  // Project context if detected
  if (projectContext.type !== 'unknown') {
    md += ` | **Project:** ${projectContext.type}`;
    if (projectContext.frameworks.length > 0) {
      md += ` (${projectContext.frameworks.slice(0, 2).join(', ')})`;
    }
  }
  md += '\n';

  // Validation suggestions
  if (validation.suggestions.length > 0) {
    md += `\n**💡 Suggestions:**\n`;
    validation.suggestions.forEach(s => {
      md += `- ${s}\n`;
    });
  }

  // Plugin recommendations
  if (plugins.length === 0) {
    md += '\n*No specific plugin recommendations found.*\n';
    md += '\n---\n\n';
    return md;
  }

  md += `\n**📦 Recommended Plugins:**\n\n`;

  plugins.forEach((plugin, idx) => {
    md += `### ${idx + 1}. \`${plugin.name}\`\n`;
    md += `**Description:** ${plugin.description}\n`;
    md += `**Why:** ${plugin.reason}\n`;

    // Show score if configured
    const config = loadConfiguration();
    if (config.showScores) {
      md += `**Score:** ${Math.round(plugin.score)}\n`;
    }

    md += `**Install:** \`/plugin install ${plugin.name}\`\n\n`;
  });

  md += '---\n\n';
  return md;
}

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

function allowPrompt() {
  return {
    decision: undefined,
    reason: 'Proceeding normally',
    hookSpecificOutput: {
      hookEventName: 'UserPromptSubmit',
      additionalContext: ''
    }
  };
}

// ============================================================================
// RUN
// ============================================================================

if (require.main === module) {
  main();
}

// Export for testing
module.exports = {
  classifyTaskType,
  validateInstruction,
  scorePlugin,
  analyzeInstruction,
  tokenize,
  stem,
  detectProjectContext
};
