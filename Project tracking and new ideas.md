# Feature Expansion Breakdown for Raid Tools

## Recommended Implementation Order for Enhancements

---

### 1. Foundational Improvements

#### a. Add a `.gitignore` File
- **Purpose:** Prevent committing virtual environments, caches, and other artifacts.
- **New Files/Paths:** `.gitignore` at the repo root.
- **Dependencies:** None.
- **README Updates:** None.

#### b. Add a `LICENSE` File
- **Purpose:** Define the legal terms for using and contributing to the project.
- **New Files/Paths:** `LICENSE` at the repo root.
- **Dependencies:** None.
- **README Updates:** Add a license badge and section.

#### c. Add a `requirements.txt`
- **Purpose:** Allow users to install all dependencies with `pip install -r requirements.txt`.
- **New Files/Paths:** `requirements.txt` at the repo root.
- **Dependencies:** None.
- **README Updates:** Add installation instructions using `requirements.txt`.

#### d. Add a `.env.example` File
- **Purpose:** Document required environment variables (e.g., LLM API keys, configuration options).
- **New Files/Paths:** `.env.example` at the repo root.
- **Dependencies:** None.
- **README Updates:** Add a section on copying `.env.example` to `.env` and filling in values.

#### e. Add VS Code Workspace Settings
- **Purpose:** Recommend Python interpreter, linting, and formatting settings for contributors.
- **New Files/Paths:** `.vscode/settings.json`
- **Dependencies:** None.
- **README Updates:** Mention recommended VS Code settings.

#### f. Add a Sample Champion JSON
- **Purpose:** Provide an example for onboarding and testing.
- **New Files/Paths:** `samples/sampleChampion.json`
- **Dependencies:** None.
- **README Updates:** Add a section referencing the sample file.

#### g. Add Badges to README
- **Purpose:** Show build status, Python version, license, etc., at a glance.
- **New Files/Paths:** None (badges are Markdown links in `README.md`).
- **Dependencies:** None.
- **README Updates:** Add badge Markdown at the top of the file.

#### h. Add a `CONTRIBUTING.md`
- **Purpose:** Guide new contributors on how to set up, code style, and submit PRs.
- **New Files/Paths:** `CONTRIBUTING.md` at the repo root.
- **Dependencies:** None.
- **README Updates:** Add a link to `CONTRIBUTING.md`.

#### i. Add a `Makefile` or Shell Script for Common Tasks
- **Purpose:** Simplify setup, testing, and running tools with single commands.
- **New Files/Paths:** `Makefile` or `scripts/setup.sh`
- **Dependencies:** None.
- **README Updates:** Add usage instructions for the Makefile or shell script.

---

### 2. Testing & Validation

#### a. Implement Schema Validation
- **Purpose:** Enforce JSON schema for champion files.
- **New Files/Paths:** `schemas/` directory for JSON schemas.
- **Scripts to Edit:** Update test scripts to use schema validation.
- **Dependencies:** Foundational files in place.
- **README Updates:** Document schema validation.

#### b. Expand Automated Test Suite
- **Purpose:** Comprehensive coverage for all tools and features.
- **New Files/Paths:** Add new test files as features are added.
- **Scripts to Edit:** Expand existing tests, add new ones for new features.
- **Dependencies:** Foundational files in place.
- **README Updates:** Update testing instructions.

---

### 3. Champion Data Enhancements

#### a. Add Gear Recommendations
- **Purpose:** Suggest best gear sets and stat priorities for each champion.
- **New Files/Paths:** Update champion JSON schema to include a `gearRecommendations` field.
- **Scripts to Edit:** `champIntake.py` (add prompt for gear recommendations), `jsonToMdPerChamp.py` (include gear info in summaries).
- **Tests:** Update schema validation in `testChampionReviewAndComparison.py`.
- **Dependencies:** Schema validation in place.
- **README Updates:** Document new field and workflow.

#### b. Track Ascension, Blessings, Faction Guardians
- **Purpose:** More accurate champion analysis.
- **New Files/Paths:** Extend champion JSONs with `ascension`, `blessing`, `factionGuardian` fields.
- **Scripts to Edit:** `champIntake.py`, `championAnalysis.py`, `jsonToMdPerChamp.py`.
- **Tests:** Add tests for presence and correct handling of new fields.
- **Dependencies:** Schema validation in place.
- **README Updates:** Update all relevant READMEs with new data fields.

#### c. Masteries Optimization Suggestions
- **Purpose:** Suggest optimal masteries for each champion.
- **New Files/Paths:** Add `masterySuggestions` field to champion JSON.
- **Scripts to Edit:** `champIntake.py`, `jsonToMdPerChamp.py`.
- **Tests:** Validate presence and format in test scripts.
- **Dependencies:** Schema validation in place.
- **README Updates:** Document in root and summary tool READMEs.

---

### 4. User Experience Improvements

#### a. Batch Processing
- **Purpose:** Allow intake, analysis, and summary generation for multiple champions at once.
- **New Files/Paths:** Update existing scripts to accept batch input.
- **Scripts to Edit:** `champIntake.py`, `championAnalysis.py`, `jsonToMdPerChamp.py`.
- **Tests:** Batch processing tests.
- **Dependencies:** Champion data enhancements.
- **README Updates:** Add batch usage examples.

#### b. Interactive Prompt Generator
- **Purpose:** Step-by-step intake with validation and suggestions.
- **New Files/Paths:** `Champion Review and Comparison/Tools/interactivePrompt.py`
- **Scripts to Edit:** New script for guided champion intake.
- **Tests:** Add prompt flow tests.
- **Dependencies:** Champion data enhancements.
- **README Updates:** Document new intake method.

#### c. Web Dashboard or GUI
- **Purpose:** Visualize champion data, summaries, and analysis results.
- **New Files/Paths:** `dashboard/` directory for web or GUI code.
- **Scripts to Edit:** New dashboard app (e.g., Flask, Streamlit, or Tkinter).
- **Tests:** UI tests, integration tests.
- **Dependencies:** Champion data enhancements, batch processing.
- **README Updates:** Add dashboard usage and setup.

---

### 5. Advanced Analysis Tools

#### a. Team Builder Tool
- **Purpose:** Suggest optimal teams for specific content based on owned champions.
- **New Files/Paths:** `Champion Review and Comparison/Tools/teamBuilder.py`
- **Scripts to Edit:** New script for team suggestions.
- **Tests:** Create `testTeamBuilder.py` in `Tests/`
- **Dependencies:** Champion data enhancements.
- **README Updates:** Add usage and description to root and tools READMEs.

#### b. Synergy Analyzer
- **Purpose:** Automatically detect and highlight champion synergies and combos.
- **New Files/Paths:** `Champion Review and Comparison/Tools/synergyAnalyzer.py`
- **Scripts to Edit:** New script for synergy detection.
- **Tests:** Create `testSynergyAnalyzer.py`
- **Dependencies:** Team builder tool.
- **README Updates:** Document in root and tools READMEs.

#### c. Artifact Optimizer Integration
- **Purpose:** Suggest best gear from inventory for each champion.
- **New Files/Paths:** `artifactData/` directory for imported gear data, `artifactOptimizerIntegration.py`
- **Scripts to Edit:** New integration script.
- **Tests:** Add tests for gear import and matching.
- **Dependencies:** Gear recommendations, team builder.
- **README Updates:** Add integration instructions.

---

### 6. Data Import/Export

#### a. Import from In-Game Data
- **Purpose:** Import champion and gear data from external tools.
- **New Files/Paths:** `importers/` directory for data import scripts.
- **Scripts to Edit:** New scripts for parsing RSL Helper, HellHades, or screenshot data.
- **Tests:** Import validation tests.
- **Dependencies:** Champion data enhancements, artifact optimizer.
- **README Updates:** Add import instructions.

#### b. Export to PDF/HTML
- **Purpose:** Export summaries and analysis to PDF or HTML for sharing or printing.
- **New Files/Paths:** Add export options to summary scripts.
- **Scripts to Edit:** `jsonToMdPerChamp.py` (add PDF/HTML export)
- **Tests:** Export format tests.
- **Dependencies:** Summary generator enhancements.
- **README Updates:** Document export features.

---

### 7. Automation & Integration

#### a. Scheduled Updates
- **Purpose:** Automatically check for outdated champion data and prompt for review.
- **New Files/Paths:** `Champion Review and Comparison/Tools/scheduledUpdate.py`
- **Scripts to Edit:** New script for checking outdated data.
- **Tests:** Add tests for scheduling logic.
- **Dependencies:** Champion data enhancements.
- **README Updates:** Add automation instructions.

#### b. API Endpoints
- **Purpose:** Allow external tools or scripts to query champion data and analysis.
- **New Files/Paths:** `api/` directory for Flask/FastAPI code.
- **Scripts to Edit:** New API server script.
- **Tests:** API endpoint tests.
- **Dependencies:** Champion data enhancements, analysis tools.
- **README Updates:** Document API usage.

---

### 8. User Interface

#### a. Web Dashboard or GUI (if not already implemented above)
- **Purpose:** Visualize champion data, summaries, and analysis results.
- **New Files/Paths:** `dashboard/` directory for web or GUI code.
- **Scripts to Edit:** New dashboard app (e.g., Flask, Streamlit, or Tkinter).
- **Tests:** UI tests, integration tests.
- **Dependencies:** Data import/export, automation.
- **README Updates:** Add dashboard usage and setup.

---

### 9. Documentation & Onboarding

#### a. Interactive Setup Script
- **Purpose:** Guide new users through environment setup and initial configuration.
- **New Files/Paths:** `setupWizard.py`
- **Scripts to Edit:** New onboarding script.
- **Tests:** Setup flow tests.
- **Dependencies:** Foundational improvements.
- **README Updates:** Add onboarding section.

#### b. Video or Step-by-Step Tutorials
- **Purpose:** Provide visual and written guides for onboarding and usage.
- **New Files/Paths:** `docs/tutorials/` directory for guides and videos.
- **Scripts to Edit:** N/A (documentation only)
- **Tests:** N/A
- **Dependencies:** All major features in place.
- **README Updates:** Link to tutorials in all relevant READMEs.

---

### 10. LLM Integration for Champion Analysis

#### a. Compare and Select LLM Options
- **Purpose:** Evaluate available LLM APIs (e.g., OpenAI GPT-4, Azure OpenAI, Google Gemini, local LLMs like Llama.cpp).
- **New Files/Paths:** `llm/llm_selector.py` to abstract and select the LLM backend.
- **Dependencies:** Foundational improvements, champion data enhancements.

#### b. Integrate LLM for Champion Analysis
- **Purpose:** Use LLM to analyze champion skills, stats, etc.
- **New Files/Paths:** `llm/championAnalyzerLLM.py`
- **Scripts to Edit:** Accept champion JSON and analysis prompt, send to LLM, parse response, insert into champion JSON.
- **Dependencies:** LLM selector module, champion data enhancements.

#### c. Review and Improve Prompt/Module for LLM
- **Purpose:** Allow users to edit or approve the prompt before sending; modularize prompt templates.
- **New Files/Paths:** Prompt templates in `llm/prompts/`
- **Dependencies:** LLM integration.

#### d. Parse and Insert LLM Output
- **Purpose:** Extract structured data from LLM output and update champion JSON.
- **Scripts to Edit:** Parsing logic in `championAnalyzerLLM.py`
- **Dependencies:** LLM integration.

#### e. Testing
- **Purpose:** Ensure LLM integration, prompt formatting, and output parsing work as intended.
- **New Files/Paths:** `Tests/testLLMIntegration.py`
- **Dependencies:** LLM integration.

#### f. Documentation
- **Purpose:** Document LLM setup, usage, and configuration.
- **README Updates:** Update root and relevant tool READMEs.

---

## Suggested New Names and Folder Structure

```text
Raid_Tools/
├── champion_manager/                # Champion intake, review, and management
│   ├── champion_manager.py
│   ├── tools/
│   ├── prompts/
│   ├── summaries/
│   ├── templates/
│   └── [README.md](http://_vscodecontentref_/0)
├── skill_cycle_analyzer/            # Skill cycle simulation and analysis
│   ├── skill_cycle_analyzer.py
│   ├── cooldown_analysis/
│   └── [README.md](http://_vscodecontentref_/1)
├── summary_generator/               # Markdown and report generation
│   ├── summary_generator.py
│   └── [README.md](http://_vscodecontentref_/2)
├── llm_champion_analyzer/           # LLM integration for champion analysis
│   ├── llm_selector.py
│   ├── champion_analyzer_llm.py
│   └── [README.md](http://_vscodecontentref_/3)
├── tests/
│   ├── test_champion_manager.py
│   ├── test_skill_cycle_analyzer.py
│   ├── test_summary_generator.py
│   ├── test_llm_integration.py
│   └── test_script_paths.py
├── docs/
│   └── tutorials/
├── .venv/
└── [README.md](http://_vscodecontentref_/4)
```

