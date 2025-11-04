# Documentation Style Guide
> Part of the [Contributing Guide](index.md).

Clear documentation is a core part of the Puerto experience. Use this guide to keep tone, structure, and formatting consistent across guides, READMEs, and tutorials.

---

## Principles

- **Task-driven** – Lead with what the reader wants to accomplish.
- **Scannable** – Use headings, bullets, and tables for quick comprehension.
- **Actionable** – Provide commands, code snippets, and checklists.
- **Honest** – Describe current behaviour, not future plans.
- **Accessible** – Avoid jargon when possible; explain acronyms on first use.

---

## Structure

1. **Title (`#`)** – Clear and descriptive.
2. **Intro paragraph** – 1–2 sentences summarising the page.
3. **Headings (`##`)** – Organise content by task or concept.
4. **Bullets & tables** – Present lists and comparisons concisely.
5. **Callouts** – Use bold or italic text for important warnings; avoid fancy syntax that may not render everywhere.
6. **Next steps** – Link to related docs so readers know where to go next.

---

## Formatting Rules

- 80–100 character line length for Markdown bodies.
- Use sentence case for headings (capitalize the first word, not every word).
- Prefer American English spelling (customise vs customise).
- Use backticks for commands (`/plugin install`) and filenames (`plugin.json`).
- Label code fences with language (` ```bash`, ` ```json`, ` ```tsx`).
- Insert a blank line between paragraphs and headings.
- Avoid HTML inside Markdown unless necessary for alignment or images.

---

## Tone & Voice

- Friendly, confident, and concise—write like a teammate guiding you through a task.
- Use active voice (“Run the validator”) instead of passive (“The validator should be run”).
- Encourage success (“You’re ready to publish!”) without being overly casual.

---

## Content Patterns

### Guides & Tutorials
- Outline prerequisites up front.
- Break work into numbered steps.
- Include expected output or screenshots when relevant.
- Finish with “Next steps” pointing to deeper topics.

### Reference Pages
- Provide summaries, tables, and schema definitions.
- Keep examples canonical—copy/paste should work.
- Cross-link to guides that show real-world usage.

### Troubleshooting
- Present symptom → cause → resolution in table form.
- Add quick commands to collect logs or reset state.

---

## Link Style

- Use relative links for local docs such as `../plugin-development/commands.md`.
- When referencing GitHub issues or external docs, include the protocol (`https://`).
- Keep link text descriptive (avoid “click here”).

---

## Images & Media

- Place images in the same directory as the doc unless shared globally.
- Use meaningful alt text.
- Optimise file sizes; prefer SVG/PNG for diagrams, GIF/MP4 for demos.

Example:

```markdown
![Screenshot showing the plugin catalog search results](./images/catalog-search.png)
```

---

## Review Checklist

- [ ] Title and intro explain the document’s purpose.
- [ ] Sections organised logically with descriptive headings.
- [ ] Commands and code blocks tested or verified.
- [ ] Links resolve correctly.
- [ ] Tone aligns with Puerto voice (helpful, confident, concise).
- [ ] Next steps or related links provided.

---

## Related Docs

- [Contributing Overview](index.md)
- [Code Style Guide](code-style.md)
- [Best Practices](../plugin-development/best-practices.md)
