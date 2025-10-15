# Feature Expansion Breakdown for Raid Tools


## Roadmap & Feature Review (2025)

### Top 3 Most Critical / High-Impact Items (Open)
1. Champion JSON Query & Reporting Tool (see below)
2. Add Gear Recommendations (complete integration)
3. Continuous Integration (CI) — Coverage & Badge Integration

### Top 3 Easiest / Quick-Win Items (Open)
1. Pre-commit Hooks
2. Test Coverage Reporting
3. Documentation Site (mkdocs integration)

---

## 1. Champion JSON Query & Reporting Tool  <!-- High-Impact: #1 -->
<!-- Prioritized: This tool will provide immediate value for data quality, debugging, and future enhancements. -->
### a. Query and Report on Champion JSON Components
- **Purpose:** Provide a tool to query all champion JSON files for the presence and values of any component or feature, and generate a human-readable report. Supports searching for all components (using `logTemplate.json` as a baseline) and detecting additional fields in champion files. Can also search for a specific key (e.g., `rarity`) and sort the report by rarity.
- **Files/Paths:** Use `logTemplate.json` as baseline; scan all champion JSONs.
- **Scripts to Edit:** New script for query/reporting engine.
- **Dependencies:** Foundational files in place.
- **Tests:** Add tests for extraction, sorting, and reporting.
- **README Updates:** Document usage, options, and expected output.
- **Status:** Not started. Next major feature after core automation.
<!-- Feedback: Good idea, but avoid making the tool too broad or slow. Focus on actionable queries and clear output. -->

---

## 2. Champion Data Enhancements  <!-- High-Impact: #2 -->
<!-- Prioritized: Gear recommendations are highly actionable and directly improve the value of summaries and analysis. -->
### a. Add Gear Recommendations
- **Purpose:** Suggest best gear sets and stat priorities for each champion.
- **Files/Paths:** Update champion JSON schema to include a `gearRecommendations` field.
- **Scripts to Edit:** `champIntake.py` (add prompt for gear recommendations), `jsonToMdPerChamp.py` (include gear info in summaries).
- **Dependencies:** Schema validation in place.
- **Tests:** Update schema validation in `testChampionReviewAndComparison.py`.
- **README Updates:** Document new field and workflow.
- **Status:** In progress. Gear recommendations are partially included in JSON and summary outputs; further schema and UI integration planned.
<!-- Feedback: Good, but avoid overcomplicating with too many gear options. Focus on practical, high-value recommendations. -->

---

## 3. Continuous Integration (CI) — Coverage & Badge Integration  <!-- High-Impact: #3 -->
<!-- Prioritized: Ensures code quality, prevents regressions, and builds trust for contributors. -->
### a. Continuous Integration (CI)
- **Purpose:** Run lint, test, and coverage on every push/PR.
- **Files/Paths:** `.github/workflows/ci.yml`
- **Scripts to Edit:** None (uses Makefile/test scripts).
- **Dependencies:** None (uses existing tools).
- **Tests:** CI runs all tests.
- **README Updates:** Add badge and CI instructions.
- **Status:** In progress. Basic CI is in place; coverage and badge integration planned.
<!-- Feedback: Good. Add coverage and badge reporting for full value. -->

---

## 4. Pre-commit Hooks  <!-- Easy: #1 -->
<!-- Quick-Win: Adding pre-commit hooks is straightforward and improves code quality with minimal effort. -->
### a. Pre-commit Hooks
- **Purpose:** Enforce lint/format/test before commit.
- **Files/Paths:** `.pre-commit-config.yaml`
- **Scripts to Edit:** None.
- **Dependencies:** Add `pre-commit`.
- **Tests:** Pre-commit runs on staged files.
- **README Updates:** Add setup instructions.
- **Status:** Not started.
<!-- Feedback: Good. Only add if contributors are on board. -->

---

## 5. Test Coverage Reporting  <!-- Easy: #2 -->
<!-- Quick-Win: Adding pytest-cov and updating CI to report coverage is a small change with clear benefits. -->
### a. Test Coverage Reporting
- **Purpose:** Track and improve test coverage.
- **Files/Paths:** Add `pytest-cov` to requirements.
- **Scripts to Edit:** Test scripts.
- **Dependencies:** Add `pytest-cov`.
- **Tests:** Coverage report in CI.
- **README Updates:** Add badge and coverage instructions.
- **Status:** Not started.
<!-- Feedback: Good. Focus on meaningful coverage, not just numbers. -->

---

## 6. Documentation Site (mkdocs integration)  <!-- Easy: #3 -->
<!-- Quick-Win: If docs folder and structure are in place, setting up mkdocs is a quick win for user and contributor experience. -->
### a. Documentation Site
- **Purpose:** Provide browsable docs for users and contributors.
- **Files/Paths:** `docs/`, `mkdocs.yml`
- **Scripts to Edit:** None.
- **Dependencies:** Add `mkdocs`.
- **README Updates:** Add link to docs.
- **Status:** In progress. Docs folder and structure are in place; mkdocs integration planned.
<!-- Feedback: Good. Only add if docs are kept up to date. -->

---

## 7. Champion Data Enhancements (Expansion Needed)
*This section is a continuation of section 2, for features that are not yet prioritized or require further planning.*
### a. Track Ascension, Blessings, Faction Guardians
- **Purpose:** Track and report on champion ascension levels, blessings, and faction guardian status.
- **Files/Paths:** Update champion JSON schema to include `ascension`, `blessings`, and `factionGuardians` fields.
- **Scripts to Edit:** `champIntake.py` (add prompts for new fields), `jsonToMdPerChamp.py` (include new fields in summaries).
- **Dependencies:** Schema validation in place.
- **Tests:** Update schema validation tests.
- **README Updates:** Document new fields and workflow.
- **Status:** Not started.
<!-- Feedback: Good expansion, but ensure it doesn't complicate the champion JSON too much. Consider making blessings and faction guardians optional or separate objects. -->

### b. Masteries Optimization Suggestions
- **Purpose:** Suggest optimal masteries for each champion based on their role and gear.
- **Files/Paths:** Update champion JSON schema to include `masteries` field.
- **Scripts to Edit:** `champIntake.py` (add prompt for masteries), `jsonToMdPerChamp.py` (include masteries in summaries).
- **Dependencies:** Schema validation in place.
- **Tests:** Update schema validation tests.
- **README Updates:** Document new field and workflow.
- **Status:** Not started.
<!-- Feedback: Good, but avoid overcomplicating with too many mastery options. Focus on practical, high-value recommendations. -->

### c. Batch Processing
- **Purpose:** Enable processing of multiple champions or files in a single operation.
- **Files/Paths:** Update scripts to support batch processing (e.g., `champIntake.py`, `jsonToMdPerChamp.py`).
- **Scripts to Edit:** Modify existing scripts to handle lists of champions/files.
- **Dependencies:** None.
- **Tests:** Add tests for batch processing.
- **README Updates:** Document batch processing usage and examples.
- **Status:** Not started.
<!-- Feedback: Good idea, but ensure it doesn't complicate the code or reduce performance. -->

---

## 8. Optimal Skill Order & Battle Simulation
- **Purpose:** Determine and recommend the optimal skill order, expected damage, and buff/debuff support for each champion in the context of specific dungeon bosses, Cursed City, and Doom Tower battles.
- **Files/Paths:** Use a single `encounters.json` file or a `encounters/` folder with one JSON per encounter.
- **Scripts to Edit:** Simulation engine script, encounter data loader.
- **Dependencies:** Champion data enhancements, encounter data.
- **Tests:** Add tests for encounter logic, skill order optimization, and output accuracy.
- **README Updates:** Add a section describing encounter-based simulation and how to use it. Document boss/minion data sources and update process.
- **Status:** Not started.
<!-- Feedback: Good, but only if encounter data is available and simulation logic is robust. -->

---

## Index of Bad Ideas & Risky Features

1. PDF/HTML export: Large effort, consider using existing tools instead of custom code.
2. Automated synergy detection: Extremely complex, may produce unreliable results. Try manual/semi-automated first.
3. Artifact optimizer integration: Major project, may duplicate existing tools. Only if no good external solution.
4. Champion data as a Python package: Overkill unless there is a strong use case.
5. LLM integration: Major effort, may not provide reliable results. Only if clear, valuable use case.
6. Automated scraping: Fragile, may violate site terms. Only with permission and robust error handling.

## Priority Summary (2025)

### Top 3 Most Critical / High-Impact Items
1. Champion JSON Query & Reporting Tool (see section 2)
2. Add Gear Recommendations (complete integration) (see section 3)
3. Continuous Integration (CI) — Coverage & Badge Integration (see section 4)

### Top 3 Easiest / Quick-Win Items
1. Pre-commit Hooks (see section 5)
2. Test Coverage Reporting (see section 6)
3. Documentation Site (mkdocs integration) (see section 7)

> These items have been moved to the top of the main body for visibility and are recommended as the next focus for development. See comments in each section for rationale.

---

## 1. Champion JSON Query & Reporting Tool  <!-- High-Impact: #1 -->
<!-- Prioritized: This tool will provide immediate value for data quality, debugging, and future enhancements. -->
### a. Query and Report on Champion JSON Components
- **Purpose:** Provide a tool to query all champion JSON files for the presence and values of any component or feature, and generate a human-readable report. Supports searching for all components (using `logTemplate.json` as a baseline) and detecting additional fields in champion files. Can also search for a specific key (e.g., `rarity`) and sort the report by rarity.
- **Files/Paths:** Use `logTemplate.json` as baseline; scan all champion JSONs.
- **Scripts to Edit:** New script for query/reporting engine.
- **Dependencies:** Foundational files in place.
- **Tests:** Add tests for extraction, sorting, and reporting.
- **README Updates:** Document usage, options, and expected output.
- **Status:** Not started. Next major feature after core automation.
<!-- Feedback: Good idea, but avoid making the tool too broad or slow. Focus on actionable queries and clear output. -->

---


## 2. Champion Data Enhancements  <!-- High-Impact: #2 -->
<!-- Prioritized: Gear recommendations are highly actionable and directly improve the value of summaries and analysis. -->
### a. Add Gear Recommendations
- **Purpose:** Suggest best gear sets and stat priorities for each champion.
- **Files/Paths:** Update champion JSON schema to include a `gearRecommendations` field.
- **Scripts to Edit:** `champIntake.py` (add prompt for gear recommendations), `jsonToMdPerChamp.py` (include gear info in summaries).
- **Dependencies:** Schema validation in place.
- **Tests:** Update schema validation in `testChampionReviewAndComparison.py`.
- **README Updates:** Document new field and workflow.
- **Status:** In progress. Gear recommendations are partially included in JSON and summary outputs; further schema and UI integration planned.
<!-- Feedback: Good, but avoid overcomplicating with too many gear options. Focus on practical, high-value recommendations. -->

---


## 3. Continuous Integration (CI) — Coverage & Badge Integration  <!-- High-Impact: #3 -->
<!-- Prioritized: Ensures code quality, prevents regressions, and builds trust for contributors. -->
### a. Continuous Integration (CI)
- **Purpose:** Run lint, test, and coverage on every push/PR.
- **Files/Paths:** `.github/workflows/ci.yml`
- **Scripts to Edit:** None (uses Makefile/test scripts).
- **Dependencies:** None (uses existing tools).
- **Tests:** CI runs all tests.
- **README Updates:** Add badge and CI instructions.
- **Status:** In progress. Basic CI is in place; coverage and badge integration planned.
<!-- Feedback: Good. Add coverage and badge reporting for full value. -->

---


## 4. Pre-commit Hooks  <!-- Easy: #1 -->
<!-- Quick-Win: Adding pre-commit hooks is straightforward and improves code quality with minimal effort. -->
### a. Pre-commit Hooks
- **Purpose:** Enforce lint/format/test before commit.
- **Files/Paths:** `.pre-commit-config.yaml`
- **Scripts to Edit:** None.
- **Dependencies:** Add `pre-commit`.
- **Tests:** Pre-commit runs on staged files.
- **README Updates:** Add setup instructions.
- **Status:** Not started.
<!-- Feedback: Good. Only add if contributors are on board. -->

---


## 5. Test Coverage Reporting  <!-- Easy: #2 -->
<!-- Quick-Win: Adding pytest-cov and updating CI to report coverage is a small change with clear benefits. -->
### a. Test Coverage Reporting
- **Purpose:** Track and improve test coverage.
- **Files/Paths:** Add `pytest-cov` to requirements.
- **Scripts to Edit:** Test scripts.
- **Dependencies:** Add `pytest-cov`.
- **Tests:** Coverage report in CI.
- **README Updates:** Add badge and coverage instructions.
- **Status:** Not started.
<!-- Feedback: Good. Focus on meaningful coverage, not just numbers. -->

---


## 6. Documentation Site (mkdocs integration)  <!-- Easy: #3 -->
<!-- Quick-Win: If docs folder and structure are in place, setting up mkdocs is a quick win for user and contributor experience. -->
### a. Documentation Site
- **Purpose:** Provide browsable docs for users and contributors.
- **Files/Paths:** `docs/`, `mkdocs.yml`
- **Scripts to Edit:** None.
- **Dependencies:** Add `mkdocs`.
- **README Updates:** Add link to docs.
- **Status:** In progress. Docs folder and structure are in place; mkdocs integration planned.
<!-- Feedback: Good. Only add if docs are kept up to date. -->

---


## 7. Foundational Improvements

*All foundational improvements are complete.*
<!-- Feedback: Good foundation. No issues. -->

---


## 8. Testing & Validation

#### a. Implement Schema Validation
- **Purpose:** Enforce JSON schema for champion files.
- **Files/Paths:** `schemas/` directory for JSON schemas.
- **Scripts to Edit:** Update test scripts to use schema validation.
- **Dependencies:** Foundational files in place.
- **Tests:** Add schema validation tests.
- **README Updates:** Document schema validation.
- **Status:** Complete. Schema validation and related tests are implemented and passing.
<!-- Feedback: Good. Ensure schema is kept in sync with champion data changes. -->

#### b. Expand Automated Test Suite
- **Purpose:** Comprehensive coverage for all tools and features.
- **Files/Paths:** Add new test files as features are added.
- **Scripts to Edit:** Expand existing tests, add new ones for new features.
- **Dependencies:** Foundational files in place.
- **Tests:** Add/expand tests for new features.
- **README Updates:** Update testing instructions.
- **Status:** Complete. Automated tests cover all major workflows, including config validation and owned list parsing.
<!-- Feedback: Good. Focus on meaningful tests, not just coverage. -->

---


## 9. Champion Data Enhancements (Expansion Needed)
*This section is a continuation of section 2, for features that are not yet prioritized or require further planning.*
### a. Track Ascension, Blessings, Faction Guardians
- **Purpose:** Track and report on champion ascension levels, blessings, and faction guardian status.
- **Files/Paths:** Update champion JSON schema to include `ascension`, `blessings`, and `factionGuardians` fields.
- **Scripts to Edit:** `champIntake.py` (add prompts for new fields), `jsonToMdPerChamp.py` (include new fields in summaries).
- **Dependencies:** Schema validation in place.
- **Tests:** Update schema validation tests.
- **README Updates:** Document new fields and workflow.
- **Status:** Not started.
<!-- Feedback: Good expansion, but ensure it doesn't complicate the champion JSON too much. Consider making blessings and faction guardians optional or separate objects. -->

### b. Masteries Optimization Suggestions
- **Purpose:** Suggest optimal masteries for each champion based on their role and gear.
- **Files/Paths:** Update champion JSON schema to include `masteries` field.
- **Scripts to Edit:** `champIntake.py` (add prompt for masteries), `jsonToMdPerChamp.py` (include masteries in summaries).
- **Dependencies:** Schema validation in place.
- **Tests:** Update schema validation tests.
- **README Updates:** Document new field and workflow.
- **Status:** Not started.
<!-- Feedback: Good, but avoid overcomplicating with too many mastery options. Focus on practical, high-value recommendations. -->

### c. Batch Processing
- **Purpose:** Enable processing of multiple champions or files in a single operation.
- **Files/Paths:** Update scripts to support batch processing (e.g., `champIntake.py`, `jsonToMdPerChamp.py`).
- **Scripts to Edit:** Modify existing scripts to handle lists of champions/files.
- **Dependencies:** None.
- **Tests:** Add tests for batch processing.
- **README Updates:** Document batch processing usage and examples.
- **Status:** Not started.
<!-- Feedback: Good idea, but ensure it doesn't complicate the code or reduce performance. -->

---


## 10. Optimal Skill Order & Battle Simulation
- **Purpose:** Determine and recommend the optimal skill order, expected damage, and buff/debuff support for each champion in the context of specific dungeon bosses, Cursed City, and Doom Tower battles.
- **Files/Paths:** Use a single `encounters.json` file or a `encounters/` folder with one JSON per encounter.
- **Scripts to Edit:** Simulation engine script, encounter data loader.
- **Dependencies:** Champion data enhancements, encounter data.
- **Tests:** Add tests for encounter logic, skill order optimization, and output accuracy.
- **README Updates:** Add a section describing encounter-based simulation and how to use it. Document boss/minion data sources and update process.
- **Status:** Not started.
<!-- Feedback: Good, but only if encounter data is available and simulation logic is robust. -->

---


## 11. Bad Ideas & Risky Features (Moved to Bottom)

### Data Import/Export & Synergy
#### a. Export to PDF/HTML
- **Purpose:** Export summaries and analysis to PDF or HTML for sharing or printing.
- **Files/Paths:** Add export options to summary scripts.
- **Scripts to Edit:** `jsonToMdPerChamp.py` (add PDF/HTML export)
- **Dependencies:** Champion data enhancements.
- **Tests:** Add export tests.
- **README Updates:** Add usage and description to root and tools READMEs.
- **Status:** Not started.
<!-- BAD IDEA 1: PDF/HTML export is a large effort and may not be worth the maintenance unless users specifically request it. Consider using existing markdown-to-PDF/HTML tools instead of custom code. -->

#### b. Synergy Analyzer
- **Purpose:** Automatically detect and highlight champion synergies and combos.
- **Files/Paths:** `Champion Review and Comparison/Tools/synergyAnalyzer.py`
- **Scripts to Edit:** New script for synergy detection.
- **Dependencies:** Team builder tool.
- **Tests:** Create `testSynergyAnalyzer.py`
- **README Updates:** Document in root and tools READMEs.
- **Status:** Not started.
<!-- BAD IDEA 2: Automated synergy detection is extremely complex and may produce unreliable results. Consider a manual or semi-automated approach first. -->

#### c. Artifact Optimizer Integration
- **Purpose:** Suggest best gear from inventory for each champion.
- **Files/Paths:** `artifactData/` directory for imported gear data, `artifactOptimizerIntegration.py`
- **Scripts to Edit:** New integration script.
- **Dependencies:** Gear recommendations, team builder.
- **Tests:** Add tests for gear import and matching.
- **README Updates:** Add integration instructions.
- **Status:** Not started.
<!-- BAD IDEA 3: Artifact optimizer integration is a major project and may duplicate existing tools. Only pursue if there is a clear need and no good external solution. -->

### Best Practices & Modernization
#### a. Optional: Champion Data as a Python Package
- **Purpose:** Provide champion data as a Python package for easier integration and usage in other Python projects.
- **Files/Paths:** `setup.py`, `MANIFEST.in`, `champion_data/` package directory.
- **Scripts to Edit:** Create `setup.py` for packaging, `MANIFEST.in` to include data files.
- **Dependencies:** None.
- **Tests:** Test installation and import of the package.
- **README Updates:** Document package structure and usage.
- **Status:** Not started.
<!-- Feedback: Overkill unless there is a strong use case. Consider keeping champion data as simple JSON files. -->

### LLM Integration for Champion Analysis
*All LLM-related items are grouped here for clarity.*
#### a. Integrate LLM for Champion Analysis
- **Purpose:** Use LLM to analyze champion skills, stats, etc.
- **Files/Paths:** `llm/championAnalyzerLLM.py`
- **Scripts to Edit:** Accept champion JSON and analysis prompt, send to LLM, parse response, insert into champion JSON.
- **Dependencies:** LLM selector module, champion data enhancements.
- **Tests:** Add LLM integration tests.
- **README Updates:** Document LLM integration.
- **Status:** Not started.
<!-- BAD IDEA 5: LLM integration is a major effort and may not provide reliable or actionable results. Only proceed if you have a clear, valuable use case and can validate output quality. -->

#### b. Review and Improve Prompt/Module for LLM
- **Purpose:** Allow users to edit or approve the prompt before sending; modularize prompt templates.
- **Files/Paths:** Prompt templates in `llm/prompts/`
- **Dependencies:** LLM integration.
- **Tests:** Add prompt module tests.
- **README Updates:** Document prompt editing.
- **Status:** Not started.
<!-- Feedback: Good, but only if LLM integration is pursued. -->

#### c. Parse and Insert LLM Output
- **Purpose:** Extract structured data from LLM output and update champion JSON.
- **Scripts to Edit:** Parsing logic in `championAnalyzerLLM.py`
- **Dependencies:** LLM integration.
- **Tests:** Add output parsing tests.
- **README Updates:** Document output parsing.
- **Status:** Not started.
<!-- Feedback: Good, but only if LLM integration is pursued. -->

#### d. Testing
- **Purpose:** Ensure LLM integration, prompt formatting, and output parsing work as intended.
- **Files/Paths:** `Tests/testLLMIntegration.py`
- **Dependencies:** LLM integration.
- **Tests:** Add LLM integration tests.
- **README Updates:** Document LLM testing.
- **Status:** Not started.
<!-- Feedback: Good, but only if LLM integration is pursued. -->

#### e. Documentation
- **Purpose:** Document LLM setup, usage, and configuration.
- **README Updates:** Update root and relevant tool READMEs.
- **Status:** Not started.
<!-- Feedback: Good, but only if LLM integration is pursued. -->

---


### 7. Champion Data Scraping & Database System

#### a. Automated Champion Data Scraper & Database
- **Purpose:** Build and maintain a structured database of all champions, using the champion.json template and actual files, enriched with data scraped from known sites or fan resources.
- **Files/Paths:** `champion_database/` for database and scraping scripts.
- **Scripts to Edit:** `scrape_champion_data.py`, `champion_db.py`.
- **Dependencies:** Foundational improvements, champion data enhancements.
- **Tests:** Add tests for scraping accuracy, schema compliance, and database operations.
- **README Updates:** Add a section describing the champion database, scraping process, and how to use or update it. Document new dependencies (e.g., requests, BeautifulSoup, SQLAlchemy).
- **Status:** Not started.
<!-- BAD IDEA 6: Automated scraping is fragile and may violate site terms of service. Only proceed with explicit permission and robust error handling. -->

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
- **Status:** Not started.
<!-- Feedback: Good, but only if encounter data is available and simulation logic is robust. -->

---


## Index of Bad Ideas & Risky Features

1. PDF/HTML export: Large effort, consider using existing tools instead of custom code.
2. Automated synergy detection: Extremely complex, may produce unreliable results. Try manual/semi-automated first.
3. Artifact optimizer integration: Major project, may duplicate existing tools. Only if no good external solution.
4. Champion data as a Python package: Overkill unless there is a strong use case.
5. LLM integration: Major effort, may not provide reliable results. Only if clear, valuable use case.
6. Automated scraping: Fragile, may violate site terms. Only with permission and robust error handling.

---

### Copilot Instructions

- When updating this file, always update the Index of Bad Ideas & Risky Features.
- If a bad idea is improved or removed, update the index and remove or revise the inline comment.
- Add new feedback for any new or changed items.
- Keep all feedback and risk notes up to date as the project evolves.
