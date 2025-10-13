# Feature Expansion Breakdown for Raid Tools

## Recommended Implementation Order for Enhancements

---



**Benefit:** Establishes a robust, maintainable base for all future features, ensuring the project is stable and easy to extend.
### 1. Foundational Improvements

*All foundational improvements are complete.*

---


**Benefit:** Guarantees code quality and data integrity by enforcing schema validation and expanding automated test coverage, reducing bugs and regressions.
### 2. Testing & Validation

#### a. Implement Schema Validation
- **Purpose:** Enforce JSON schema for champion files.
- **Files/Paths:** `schemas/` directory for JSON schemas.
- **Scripts to Edit:** Update test scripts to use schema validation.
- **Dependencies:** Foundational files in place.
- **Tests:** Add schema validation tests.
- **README Updates:** Document schema validation.

#### b. Expand Automated Test Suite
- **Purpose:** Comprehensive coverage for all tools and features.
- **Files/Paths:** Add new test files as features are added.
- **Scripts to Edit:** Expand existing tests, add new ones for new features.
- **Dependencies:** Foundational files in place.
- **Tests:** Add/expand tests for new features.
- **README Updates:** Update testing instructions.

---


**Benefit:** Enables fast, flexible analysis and reporting on champion data, making it easy to audit, compare, and extract insights from all champion files.
### 3. Champion JSON Query & Reporting Tool

#### a. Query and Report on Champion JSON Components
- **Purpose:** Provide a tool to query all champion JSON files for the presence and values of any component or feature, and generate a human-readable report. Supports searching for all components (using `logTemplate.json` as a baseline) and detecting additional fields in champion files. Can also search for a specific key (e.g., `rarity`) and sort the report by rarity.
- **Files/Paths:** Use `logTemplate.json` as baseline; scan all champion JSONs.
- **Scripts to Edit:** New script for query/reporting engine.
- **Dependencies:** Foundational files in place.
- **Tests:** Add tests for extraction, sorting, and reporting.
- **README Updates:** Document usage, options, and expected output.

---


**Benefit:** Adds richer, more actionable data (gear, ascension, blessings, masteries, batch processing) to champion files, supporting deeper analysis and better recommendations.
### 4. Champion Data Enhancements

#### a. Add Gear Recommendations
- **Purpose:** Suggest best gear sets and stat priorities for each champion.
- **Files/Paths:** Update champion JSON schema to include a `gearRecommendations` field.
- **Scripts to Edit:** `champIntake.py` (add prompt for gear recommendations), `jsonToMdPerChamp.py` (include gear info in summaries).
- **Dependencies:** Schema validation in place.
- **Tests:** Update schema validation in `testChampionReviewAndComparison.py`.
- **README Updates:** Document new field and workflow.

#### b. Track Ascension, Blessings, Faction Guardians
- **Purpose:** More accurate champion analysis.
- **Files/Paths:** Extend champion JSONs with `ascension`, `blessing`, `factionGuardian` fields.
- **Scripts to Edit:** `champIntake.py`, `championAnalysis.py`, `jsonToMdPerChamp.py`.
- **Dependencies:** Schema validation in place.
- **Tests:** Add tests for presence and correct handling of new fields.
- **README Updates:** Update all relevant READMEs with new data fields.

#### c. Masteries Optimization Suggestions
- **Purpose:** Suggest optimal masteries for each champion.
- **Files/Paths:** Add `masterySuggestions` field to champion JSON.
- **Scripts to Edit:** `champIntake.py`, `jsonToMdPerChamp.py`.
- **Dependencies:** Schema validation in place.
- **Tests:** Validate presence and format in test scripts.
- **README Updates:** Document in root and summary tool READMEs.

#### d. Batch Processing
- **Purpose:** Allow intake, analysis, and summary generation for multiple champions at once.
- **Files/Paths:** Update existing scripts to accept batch input.
- **Scripts to Edit:** `champIntake.py`, `championAnalysis.py`, `jsonToMdPerChamp.py`.
- **Dependencies:** Champion data enhancements.
- **Tests:** Batch processing tests.
- **README Updates:** Add batch usage examples.

---


**Benefit:** Improves data sharing (PDF/HTML export), enables synergy analysis, and lays groundwork for gear optimization, making the tool more useful for team building and sharing results.
### 5. Data Import/Export & Synergy

#### a. Export to PDF/HTML
- **Purpose:** Export summaries and analysis to PDF or HTML for sharing or printing.
- **Files/Paths:** Add export options to summary scripts.
- **Scripts to Edit:** `jsonToMdPerChamp.py` (add PDF/HTML export)
- **Dependencies:** Champion data enhancements.
- **Tests:** Add export tests.
- **README Updates:** Add usage and description to root and tools READMEs.

#### b. Synergy Analyzer
- **Purpose:** Automatically detect and highlight champion synergies and combos.
- **Files/Paths:** `Champion Review and Comparison/Tools/synergyAnalyzer.py`
- **Scripts to Edit:** New script for synergy detection.
- **Dependencies:** Team builder tool.
- **Tests:** Create `testSynergyAnalyzer.py`
- **README Updates:** Document in root and tools READMEs.

#### c. Artifact Optimizer Integration
- **Purpose:** Suggest best gear from inventory for each champion.
- **Files/Paths:** `artifactData/` directory for imported gear data, `artifactOptimizerIntegration.py`
- **Scripts to Edit:** New integration script.
- **Dependencies:** Gear recommendations, team builder.
- **Tests:** Add tests for gear import and matching.
- **README Updates:** Add integration instructions.

---



**Benefit:** Aligns the project with industry standards (schema validation, CI, pre-commit hooks, coverage, docs, packaging), improving reliability, maintainability, and contributor experience.
### 6. Best Practices & Modernization

#### a. Schema Validation with Pydantic or JSONSchema
- **Purpose:** Enforce and auto-validate champion JSON structure.
- **Files/Paths:** `schemas/`, or a new `champion_data/` package.
- **Scripts to Edit:** Intake, test, and reporting scripts.
- **Dependencies:** Add `pydantic` or `jsonschema`.
- **Tests:** Add schema validation tests.
- **README Updates:** Document schema validation and error handling.

#### b. Continuous Integration (CI)
- **Purpose:** Run lint, test, and coverage on every push/PR.
- **Files/Paths:** `.github/workflows/ci.yml`
- **Scripts to Edit:** None (uses Makefile/test scripts).
- **Dependencies:** None (uses existing tools).
- **Tests:** CI runs all tests.
- **README Updates:** Add badge and CI instructions.

#### c. Pre-commit Hooks
- **Purpose:** Enforce lint/format/test before commit.
- **Files/Paths:** `.pre-commit-config.yaml`
- **Scripts to Edit:** None.
- **Dependencies:** Add `pre-commit`.
- **Tests:** Pre-commit runs on staged files.
- **README Updates:** Add setup instructions.

#### d. Test Coverage Reporting
- **Purpose:** Track and improve test coverage.
- **Files/Paths:** Add `pytest-cov` to requirements.
- **Scripts to Edit:** Test scripts.
- **Dependencies:** Add `pytest-cov`.
- **Tests:** Coverage report in CI.
- **README Updates:** Add badge and coverage instructions.

#### e. Documentation Site
- **Purpose:** Provide browsable docs for users and contributors.
- **Files/Paths:** `docs/`, `mkdocs.yml`
- **Scripts to Edit:** None.
- **Dependencies:** Add `mkdocs`.
- **README Updates:** Add link to docs.

#### f. Optional: Champion Data as a Python Package
- **Purpose:** Enable import, validation, and manipulation of champion data as a library.
- **Files/Paths:** `champion_data/`
- **Scripts to Edit:** Intake, analysis, and reporting scripts.
- **Dependencies:** Add `pydantic` or similar.
- **Tests:** Add import/validation tests.
- **README Updates:** Add usage examples.

---


**Benefit:** Leverages AI to automate and enhance champion analysis, enabling smarter recommendations, faster data entry, and more advanced features.
### 7. LLM Integration for Champion Analysis

#### a. Compare and Select LLM Options
- **Purpose:** Evaluate available LLM APIs (e.g., OpenAI GPT-4, Azure OpenAI, Google Gemini, local LLMs like Llama.cpp).
- **Files/Paths:** `llm/llm_selector.py` to abstract and select the LLM backend.
- **Dependencies:** Foundational improvements, champion data enhancements.
- **Tests:** Add LLM selection tests.
- **README Updates:** Document LLM selection.

#### b. Integrate LLM for Champion Analysis
- **Purpose:** Use LLM to analyze champion skills, stats, etc.
- **Files/Paths:** `llm/championAnalyzerLLM.py`
- **Scripts to Edit:** Accept champion JSON and analysis prompt, send to LLM, parse response, insert into champion JSON.
- **Dependencies:** LLM selector module, champion data enhancements.
- **Tests:** Add LLM integration tests.
- **README Updates:** Document LLM integration.

#### c. Review and Improve Prompt/Module for LLM
- **Purpose:** Allow users to edit or approve the prompt before sending; modularize prompt templates.
- **Files/Paths:** Prompt templates in `llm/prompts/`
- **Dependencies:** LLM integration.
- **Tests:** Add prompt module tests.
- **README Updates:** Document prompt editing.

#### d. Parse and Insert LLM Output
- **Purpose:** Extract structured data from LLM output and update champion JSON.
- **Scripts to Edit:** Parsing logic in `championAnalyzerLLM.py`
- **Dependencies:** LLM integration.
- **Tests:** Add output parsing tests.
- **README Updates:** Document output parsing.

#### e. Testing
- **Purpose:** Ensure LLM integration, prompt formatting, and output parsing work as intended.
- **Files/Paths:** `Tests/testLLMIntegration.py`
- **Dependencies:** LLM integration.
- **Tests:** Add LLM integration tests.
- **README Updates:** Document LLM testing.

#### f. Documentation
- **Purpose:** Document LLM setup, usage, and configuration.
- **README Updates:** Update root and relevant tool READMEs.

---

### 7. Champion Data Scraping & Database System

#### a. Automated Champion Data Scraper & Database
- **Purpose:** Build and maintain a structured database of all champions, using the champion.json template and actual files, enriched with data scraped from known sites or fan resources.
- **Files/Paths:** `champion_database/` for database and scraping scripts.
- **Scripts to Edit:** `scrape_champion_data.py`, `champion_db.py`.
- **Dependencies:** Foundational improvements, champion data enhancements.
- **Tests:** Add tests for scraping accuracy, schema compliance, and database operations.
- **README Updates:** Add a section describing the champion database, scraping process, and how to use or update it. Document new dependencies (e.g., requests, BeautifulSoup, SQLAlchemy).

---


**Benefit:** Provides actionable, encounter-specific recommendations for skill usage and team composition, maximizing in-game performance and strategic planning.
### 8. Optimal Skill Order & Battle Simulation

#### a. Simulate and Optimize Champion Skill Usage per Encounter
- **Purpose:** Determine and recommend the optimal skill order, expected damage, and buff/debuff support for each champion in the context of specific dungeon bosses, Cursed City, and Doom Tower battles.
- **Files/Paths:** Use a single `encounters.json` file or a `encounters/` folder with one JSON per encounter.
- **Scripts to Edit:** Simulation engine script, encounter data loader.
- **Dependencies:** Champion data enhancements, encounter data.
- **Tests:** Add tests for encounter logic, skill order optimization, and output accuracy.
- **README Updates:** Add a section describing encounter-based simulation and how to use it. Document boss/minion data sources and update process.

---
#### d. Parse and Insert LLM Output

- **Purpose:** Extract structured data from LLM output and update champion JSON.
