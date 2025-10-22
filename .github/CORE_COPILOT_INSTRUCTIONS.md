# GitHub Copilot Instructions - Setup Guide

> **Purpose:** This guide explains how to create and use the dual-file Copilot instruction system. Use this when setting up new projects or understanding the instruction architecture.

**Last Updated:** October 18, 2025  
**Version:** 2.0.0

---

## Quick Reference: Instruction System

| File | Location | Purpose | When to Edit |
|------|----------|---------|--------------|
| `Copilot_Instructions.md` | `.github/` | Universal AI assistant standards | Rarely (new universal standards) |
| `PROJECT_SPECIFIC_copilot-instructions.md` | `.github/` | Template for new projects | When creating new projects |
| `[ProjectName]_copilot-instructions.md` | `.github/` | Active project-specific instructions | Frequently (as project evolves) |

**Examples in This Repository:**
- `FireEmblem_copilot-instructions.md` - Fire Emblem game guides (522 lines)
- `Cosmoteer_copilot-instructions.md` - Cosmoteer patch notes (157 lines)
- `RAID_copilot-instructions.md` - RAID boss guides (685 lines)
- `YTDLP_copilot-instructions.md` - YT-DLP toolkit (395 lines)

---

## Table of Contents

1. [Dual-File System Overview](#dual-file-system-overview)
2. [How GitHub Copilot Reads These Files](#how-github-copilot-reads-these-files)
3. [Creating a New Project-Specific Instruction File](#creating-a-new-project-specific-instruction-file)
4. [Best Practices](#best-practices)
5. [File Naming Convention](#file-naming-convention)
6. [Troubleshooting](#troubleshooting)
7. [Maintenance Schedule](#maintenance-schedule)
8. [Version History](#version-history)

---

## Dual-File System Overview

This repository uses a **two-layer instruction system** to provide both universal AI standards and project-specific guidance to GitHub Copilot.

### Layer 1: Base Instructions (`Copilot_Instructions.md`)

**Purpose:** Universal AI assistant and GitHub Copilot behavioral standards applicable across **ALL** projects.

**Contains:**
- AI Assistant Behavior principles
- Safety & File Operations Policy
- Chat Response Standards
- Task Management & Progress Tracking
- Output Formatting & Style Standards
- Change Management & File Versioning
- Code Quality Standards
- Language-Specific Standards (Python, PowerShell, JavaScript/TypeScript)
- Long Processing & Memory Management
- Project Housekeeping & Shift-Left Workflow
- Validation & Documentation
- Data Privacy & Security

**When to Edit:**
- ❌ **Rarely** - only when establishing new universal standards
- ✅ When adding support for new programming languages used across multiple projects
- ✅ When updating organization-wide security or quality policies
- ✅ When establishing cross-project workflows or conventions

**Think of this as:** Your organization's "AI assistant constitution" - stable, broadly applicable rules.

---

### Layer 2: Project-Specific Instructions (`[ProjectName]_copilot-instructions.md`)

**Purpose:** **Extends** base instructions with domain-specific workflows, resources, and requirements unique to a specific project.

**Contains:**
- Project purpose, scope, and goals
- Project-specific language/tooling preferences
- Authoritative data sources (APIs, wikis, documentation URLs)
- Project-specific workflows (step-by-step processes)
- Data structures, file formats, and schemas
- Templates, boilerplate, and examples
- Quality gates and validation rules specific to this project
- Project notes, assumptions, edge cases, and known issues

**When to Edit:**
- ✅ **Frequently** - evolves as the project grows
- ✅ When starting a new project (create from template)
- ✅ When project workflows or requirements change
- ✅ When adding new data sources, APIs, or external dependencies
- ✅ When discovering new edge cases or validation needs

**Think of this as:** Your project's "field manual" - detailed, specific, constantly refined.

---

### How They Work Together

```
┌─────────────────────────────────────┐
│   Copilot_Instructions.md           │
│   (Universal Standards)              │
│   - How to behave as AI assistant    │
│   - Code quality standards           │
│   - Security best practices          │
└─────────────────────────────────────┘
                  ↓
          ┌───────────────┐
          │   EXTENDED BY │
          └───────────────┘
                  ↓
┌─────────────────────────────────────┐
│   FireEmblem_copilot-instructions.md│
│   (Project-Specific)                 │
│   - Use Fire Emblem Wiki as source  │
│   - Character guide format           │
│   - Recruitment workflow steps       │
└─────────────────────────────────────┘
```

**Key Principle:** Project files **reference** base standards, never duplicate them. If a standard applies to all projects, it belongs in `Copilot_Instructions.md`.

---

## How GitHub Copilot Reads These Files

GitHub Copilot automatically reads instruction files from the `.github/` folder with the following behavior:

**Single File Named `copilot-instructions.md`:**
- Copilot reads **ONLY** this file

**Multiple Instruction Files (Different Names):**
- Copilot reads **ALL** of them and applies standards from all files

### This Repository's Setup

We use multiple instruction files:
- `.github/Copilot_Instructions.md` (base/universal standards)
- `.github/[ProjectName]_copilot-instructions.md` (project-specific)

**Result:** Copilot reads **BOTH** files and layers the standards:
1. Base instructions provide universal behavior
2. Project instructions extend with domain-specific workflows
3. If there's a conflict, more specific (project) instructions take precedence

**Best Practice:** Project files explicitly reference the base file in their header:
```markdown
See .github/Copilot_Instructions.md for universal AI assistant standards.
This file extends those standards with [Project Name]-specific requirements.
```

---

## Creating a New Project-Specific Instruction File

> **New Process:** Project initialization now includes a comprehensive questionnaire to gather requirements and build strong project-specific instructions. See the "Project Initialization & Requirements Gathering" section in `PROJECT_SPECIFIC_copilot-instructions.md` for the full process.

### Recommended Approach: Interactive Initialization

**When starting a new project, the AI assistant should:**

1. **Initiate Questionnaire Process**
   - Run the "Initialization Questionnaire" from the project template
   - Ask 15 categories of questions covering all aspects
   - Gather comprehensive project context

2. **Synthesize Responses**
   - Organize responses by instruction file section
   - Identify gaps or ambiguities
   - Recommend AI model assignments based on project needs
   - Propose batching strategy based on scale

3. **Present Summary for Confirmation**
   - Show structured summary of gathered information
   - Request user confirmation before proceeding
   - Make corrections as needed

4. **Auto-Populate Instructions**
   - Use responses to fill in all template sections
   - Replace placeholders with actual project information
   - Add custom sections as needed
   - Generate initial changelog entry

5. **Finalize & Begin Work**
   - Create quick reference card
   - Confirm project readiness
   - Begin first task using established guidelines

**Benefits of this approach:**
- ✅ Comprehensive requirements captured upfront
- ✅ All instruction sections properly populated
- ✅ No missed edge cases or assumptions
- ✅ Clear AI model selection for different tasks
- ✅ Appropriate batching strategy from start
- ✅ Strong foundation for consistent work

---

### Alternative: Manual Template Population

If you prefer to manually create the instruction file:

#### Step 1: Copy the Template

```powershell
Copy-Item ".github\PROJECT_SPECIFIC_copilot-instructions.md" ".github\YourProjectName_copilot-instructions.md"
```

#### Step 2: Fill in the Template

Open the new file and replace all placeholders:

**Find and Replace:**
- `[Project Name]` → Your actual project name
- `[Language 1]` → Your primary programming language
- `[Output Type 1]` → Your project's main output format
- `[Source 1 Name]` → Your authoritative data source
- `[Workflow Name]` → Your project's workflows

**Complete Each Section:**
1. **Project Purpose & Scope**: Define what the project does
2. **Language & Tooling**: Specify versions, tools, dependencies
3. **Authoritative Data Sources**: List all external resources
4. **Workflows**: Document step-by-step processes
5. **Data Structures**: Define file formats and schemas
6. **Templates**: Provide examples and boilerplate
7. **Quality Gates**: Define validation and success criteria
8. **Project Notes**: Capture assumptions, limitations, edge cases

#### Step 3: Review and Validate

Check that:
- [ ] All `[placeholder]` text is replaced
- [ ] Table of Contents links work
- [ ] All workflows have clear steps
- [ ] All data sources have URLs
- [ ] Quality gates have pass/fail criteria
- [ ] Examples are project-specific and accurate
- [ ] Changelog has initial entry with current date

#### Step 4: Test with Copilot

After creating the file:
1. Open a file in your project
2. Ask Copilot to perform a task covered by your instructions
3. Verify Copilot follows your project-specific guidelines
4. Refine instructions based on Copilot's behavior

---

## Best Practices

### ✅ DO

- **Keep base instructions stable** - only update for universal standards
- **Make project instructions detailed** - more context = better Copilot responses
- **Document workflows step-by-step** - Copilot can follow processes
- **Include examples** - show Copilot what "good" looks like
- **Update regularly** - as project evolves, update instructions
- **Reference external sources** - link to docs, APIs, wikis
- **Define quality gates** - give Copilot clear success criteria
- **Use the template questionnaire** - ensures comprehensive project setup

### ❌ DON'T

- **Don't duplicate base instructions** - reference, don't repeat
- **Don't use vague language** - be specific and actionable
- **Don't forget to update** - stale instructions confuse Copilot
- **Don't over-constrain** - leave room for Copilot to be creative
- **Don't ignore edge cases** - document unusual scenarios
- **Don't skip the questionnaire** - comprehensive initialization prevents issues

---

## File Naming Convention

For project-specific instruction files, use this pattern:

```
.github/[ProjectName]_copilot-instructions.md
```

**Examples:**
- `.github/FireEmblem_copilot-instructions.md`
- `.github/Cosmoteer_copilot-instructions.md`
- `.github/RAID_copilot-instructions.md`
- `.github/YTDLP_copilot-instructions.md`

**Why this format?**
- GitHub Copilot recognizes files ending in `-instructions.md` or `_copilot-instructions.md`
- Project name prefix makes it easy to identify which project the file is for
- Consistent naming allows for easy scripting and tooling

---

## Troubleshooting

### Issue: Copilot not following instructions

**Possible Causes:**
1. Instructions are too vague or ambiguous
2. Instructions conflict with each other
3. Instructions are too long (Copilot has token limits)

**Solutions:**
- Be more specific and directive in language
- Review for conflicts between base and project instructions
- Prioritize most important instructions at the top

### Issue: Copilot ignoring project-specific file

**Possible Causes:**
1. File not in `.github` folder
2. File name doesn't end with `_copilot-instructions.md` or `-instructions.md`
3. File contains syntax errors

**Solutions:**
- Verify file location is `.github/[PROJECT]_copilot-instructions.md`
- Check file name follows naming convention
- Validate markdown syntax (no broken links, proper formatting)

### Issue: Instructions too long

**Possible Causes:**
1. Too much duplicated content from base instructions
2. Too many examples or verbose explanations
3. Including implementation details instead of guidelines

**Solutions:**
- Remove duplication; reference base instructions instead
- Summarize examples; link to full examples in project files
- Focus on "what" and "why", not "how" (let Copilot figure out "how")

---

## Maintenance Schedule

### Base Instructions (`Copilot_Instructions.md`)
- **Review:** Quarterly (every 3 months)
- **Update:** When establishing new universal standards
- **Owner:** Technical lead or architect

### Project-Specific Instructions
- **Review:** Monthly or per sprint
- **Update:** As project requirements change
- **Owner:** Project lead or product owner

---

## When to Use Each File

### Add to Base Instructions When:

- ✅ You want all projects to follow a new code review process
- ✅ You adopt a new language standard (e.g., TypeScript across org)
- ✅ You establish a company-wide security policy
- ✅ You define universal git commit message standards

### Add to Project-Specific Instructions When:

- ✅ Your project uses a specific API or data source
- ✅ Your project has unique output formats (reports, guides, configs)
- ✅ Your project has custom workflows (multi-step processes)
- ✅ Your project has domain-specific validation rules
- ✅ Your project has templates or boilerplate code

---

## Version History

- **2025-10-17:** Initial creation of dual-file Copilot instruction system and setup guide
- **2025-10-18:** Major refactoring - Moved "Long Processing & Memory Management" section to base Copilot_Instructions.md file. Simplified CORE guide to focus purely on setup and template usage. Reduced from 780 lines to ~350 lines. Removed behavioral specifications (now in base file). Updated to version 2.0.0.

---

**This guide helps you create and manage the dual-file Copilot instruction system. For universal AI behavioral standards, see `Copilot_Instructions.md`. For project-specific template, see `PROJECT_SPECIFIC_copilot-instructions.md`.**
