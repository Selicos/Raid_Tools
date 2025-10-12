# AI Assistant Instructions for Raid Tools Project

## Project Overview
Raid Tools is a Python-based project for analyzing Raid Shadow Legends champion data. The project generates JSON champion profiles, performs skill cycle analysis, and creates human-readable markdown summaries. This project follows modern Python practices with comprehensive testing, automation, and documentation standards.

**Optimized for:** Claude Sonnet 3.5/4.0, GPT-4, and other advanced coding LLMs with strong Python and project comprehension capabilities.

## Core Technical Standards

### Language & Code Quality
- **Python Version:** 3.9+ with type hints and f-string formatting
- **Code Formatting:** Black formatter (line length 88 characters)
- **Linting:** flake8 for code quality enforcement
- **Testing Framework:** pytest with 90%+ coverage target
- **Documentation:** Google-style docstrings for all public functions/classes
- **File Naming:** snake_case.py for all Python files

### Development Environment
- **Cross-Platform:** All scripts must work on Windows, macOS, and Linux
- **Virtual Environment:** Use .venv for isolation
- **Dependencies:** Minimal, well-documented in requirements.txt
- **Automation:** Makefile and VS Code tasks for common operations

### Dependencies
Current requirements include:
- **colorama** — Cross-platform colored terminal text
- **pyperclip** — Clipboard access for copy/paste functionality
- **pytest** — Testing framework
- **black** — Code formatter
- Additional packages as needed (always update `requirements.txt`)

### Environment Setup Process
1. Clone the repository
2. Run `make setup` or manually create and activate virtual environment
3. Install dependencies from `requirements.txt`
4. Copy `.env.example` to `.env` and configure any secrets
5. Run `make test` or `pytest` to verify setup
6. Start with a small feature or bugfix branch

### Code Style Guidelines
- **No Emojis:** Avoid emojis in code, documentation, or output
- **Error Handling:** Use Python exceptions with clear, actionable messages
- **Imports:** Use pathlib for file operations, organize imports logically
- **Functions:** Keep functions focused and small, prefer composition over inheritance

---

## Project Architecture

### Directory Structure
```
Raid_Tools/
├── Champion Review and Comparison/
│   ├── Champ_Intake.py  # Champion data intake script
│   ├── Tools/           # Data management and cleanup utilities
│   ├── Champions/       # JSON champion data files
│   ├── Comparisons/     # Champion comparison scripts
│   └── Tests/           # Module-specific tests
├── ChampionAnalysisTool/
│   ├── championAnalysis.py    # Skill cycle simulation
│   └── cooldown_analysis/     # Analysis output files
├── ChampionSummary/
│   ├── generateChampionSummaries.py  # Markdown generation
│   └── Summary/               # Human-readable summaries
├── root_Tests/          # Project-wide test cases
├── templates/           # JSON templates for new champions
├── .github/            # GitHub workflows and configuration
└── .vscode/            # VS Code tasks and settings
```

### Key Scripts and Their Purposes
- **Champ_Intake.py** — Main champion intake and prompt generation (located in `Champion Review and Comparison/`)
- **championAnalysis.py** — Skill cycle simulation and cooldown analysis
- **generateChampionSummaries.py** — Convert analysis to readable markdown
- **Setup_Environment.py** — Automated environment setup
- **cleanup_duplicate_champions.py** — Merge duplicate champion files (located in `Champion Review and Comparison/Tools/`)
- **Makefile** — Build automation and task management

---

## Data Flow and Processing

### Champion Data Pipeline
1. **Data Intake** (`Champ_Intake.py`)
   - Collect champion information from game sources
   - Generate structured JSON using templates/logTemplate.json
   - Validate against Raid Shadow Legends official data
   - Cross-reference with Ayumilove and Hellhades for accuracy

2. **Analysis Processing** (`championAnalysis.py`)
   - Parse champion skills and stats from JSON
   - Simulate skill rotation cycles
   - Calculate cooldown timings and optimal sequences
   - Generate analysis data for summary creation

3. **Summary Generation** (`generateChampionSummaries.py`)
   - Transform analysis into human-readable markdown
   - Structure: Executive summary, skill breakdown, notes
   - Output to ChampionSummary/Summary/ directory

### Data Validation Standards
- All champion JSONs must conform to the template structure
- Cross-reference multiple sources for data accuracy
- Implement schema validation for new champion fields
- Maintain data consistency across all output formats

---

## AI Assistant Behavior Guidelines

### Task Approach
- **Persistence:** Continue working on multi-step tasks for up to 4 cycles without asking for confirmation
- **Proactivity:** Suggest better solutions, tools, or implementations when applicable
- **Realism:** Clearly indicate when something is not possible or not recommended
- **Completeness:** Ensure full task completion before moving to next items
- **Context Awareness:** Leverage conversation history and project context for informed decisions
- **Tool Usage:** Prefer built-in tools over manual commands when available

### Code Generation Standards
- Always include type hints and docstrings for new functions
- Use pathlib for file operations instead of os.path
- Implement proper error handling with try/except blocks
- Follow the established naming conventions and file organization
- Update requirements.txt when adding new dependencies

### Testing Requirements
- Write pytest tests for all new features and bug fixes
- Place tests in appropriate directories (Tests/ or root_Tests/)
- Use descriptive test names and include docstrings
- Aim for 90%+ code coverage on core functionality
- Include schema validation tests for JSON data structures

---

## Common Task Patterns

### Champion JSON Creation
```python
# Use templates/logTemplate.json as the base structure
# Validate against multiple sources: Raid Shadow Legends, Ayumilove, Hellhades
# Ensure all required fields are present and correctly formatted
# Save to Champion Review and Comparison/Champions/
```

### Summary Generation
```python
# Read from Champions/ directory
# Process through championAnalysis.py if needed
# Generate markdown with clear structure:
#   - Executive Summary
#   - Skill Breakdown
#   - Usage Notes
#   - Statistical Analysis
# Output to ChampionSummary/Summary/
```

### Script Enhancement
```python
# Add type hints to all function parameters and returns
# Include comprehensive docstrings with Args/Returns/Raises
# Implement proper error handling
# Add corresponding test cases
# Update documentation and README files
```

---

## Automation and Workflow

### Makefile Commands
- `make setup` — Environment setup and dependency installation
- `make test` — Run complete test suite with pytest
- `make lint` — Code quality check with flake8
- `make format` — Code formatting with Black
- `make intake` — Run champion data intake process
- `make analysis` — Execute champion analysis pipeline
- `make summary` — Generate markdown summaries
- `make clean` — Clean up build artifacts and cache

### VS Code Integration
Available tasks via Command Palette or task runner:
- "Run Champion Intake" — Execute data collection workflow
- "Run Champion Comparison Tracker" — Compare owned champions
- "Cleanup Duplicate Champions" — Remove duplicate entries
- "Run Champion Analysis Tool" — Perform skill cycle analysis
- "Generate Champion Summaries" — Create readable summaries

### Claude/LLM Optimization
- **File Reading Strategy:** Read large meaningful chunks rather than small sections
- **Tool Usage:** Use semantic_search for project understanding, file_search for specific patterns
- **Code Generation:** Always include full context in code examples
- **Multi-step Tasks:** Break complex requests into logical sub-tasks
- **Error Handling:** Provide specific, actionable error messages and solutions

---

## Quality Assurance

### Code Review Checklist
- [ ] Type hints on all function signatures
- [ ] Google-style docstrings for public functions
- [ ] Proper error handling with meaningful messages
- [ ] Cross-platform compatibility (Windows/macOS/Linux)
- [ ] Test coverage for new functionality
- [ ] Updated documentation and README files
- [ ] Dependencies added to requirements.txt
- [ ] Black formatting applied
- [ ] flake8 linting passes

### Documentation Standards
- Use clear, concise language without emojis
- Include code examples for complex functions
- Document expected file formats and data structures
- Provide troubleshooting information for common issues
- Keep README files current with actual script behavior

---

## Security and Best Practices

### Data Handling
- Never commit secrets or API keys to the repository
- Use environment variables for sensitive configuration
- Validate all input data before processing
- Implement proper file permissions for output files

### Development Workflow
- Use feature branches for all changes
- Write descriptive commit messages (imperative mood)
- Test thoroughly before merging to main branch
- Follow semantic versioning for releases
- Document breaking changes clearly

---

## Integration Guidelines

### External Data Sources
- **Primary:** Raid Shadow Legends official game data
- **Secondary:** Ayumilove champion database
- **Tertiary:** Hellhades champion information
- **Resolution:** When sources conflict, use consensus of majority

### File Formats
- **Input:** JSON for structured champion data
- **Output:** Markdown for human-readable summaries
- **Templates:** JSON templates in templates/ directory
- **Logs:** Plain text with timestamps for debugging

---

## Troubleshooting Common Issues

### Path Resolution
- Always use absolute paths when possible
- Use pathlib.Path for cross-platform compatibility
- Check file existence before attempting operations
- Handle permission errors gracefully

### Data Consistency
- Validate JSON structure against templates
- Check for required fields before processing
- Handle missing or malformed data appropriately
- Log data quality issues for manual review

### Environment Issues
- Ensure Python 3.9+ is installed and accessible
- Verify virtual environment activation
- Check that all dependencies are installed
- Confirm cross-platform script execution

---

## Recent Changes & Updates

### Directory Structure Changes
- **ChampionSummary/** — Renamed from "Summarize Champion Results"
- **generateChampionSummaries.py** — Renamed from "jsonToMdPerChamp.py"
- All documentation updated to reflect new structure

### Tool Improvements
- Added comprehensive Makefile for automation
- Enhanced error handling and type hints in scripts
- Standardized docstrings and code formatting
- Updated VS Code tasks to match new directory structure

### Documentation Updates
- Consistent README files across all directories
- Updated script references and folder structures
- Improved onboarding instructions

---

## Future Development Considerations

### Planned Features
- Enhanced LLM integration for automated analysis
- Web interface for champion data management
- API endpoints for external tool integration
- Advanced statistical analysis capabilities

### Architecture Notes
- Keep AI/LLM components modular and configurable
- Design for extensibility in data source integration
- Maintain backward compatibility for existing data files
- Plan for scalable processing of large champion datasets

---

## Contact and Contribution
- Open issues for bugs or feature requests
- Follow the CC BY-NC 4.0 license for all contributions
- Attribute original authors in significant modifications
- Maintain project coding standards and documentation quality