# Makefile for Raid Tools

.PHONY: help setup test lint format intake analysis summary clean

help:
	@echo "Available targets:"
	@echo "  setup     - Set up Python venv and install requirements"
	@echo "  test      - Run all tests with pytest"
	@echo "  lint      - Run flake8 linter"
	@echo "  format    - Run Black code formatter"
	@echo "  intake    - Run champion intake tool"
	@echo "  analysis  - Run champion analysis tool"
	@echo "  summary   - Generate champion summaries"
	@echo "  clean     - Remove .venv and __pycache__ folders"

setup:
	python Tools/Setup_Environment.py

intake:
	python "Champion Review and Comparison/Tools/champIntake.py"

analysis:
	python ChampionAnalysisTool/championAnalysis.py


# Generate champion summaries (now in ChampionSummary)
summary:
	python ChampionSummary/generateChampionSummaries.py

help:
	@echo "Available targets:"
	@echo "  setup     - Set up Python venv, install requirements, and configure VS Code integration"
	@echo "  test      - Run all tests with pytest (activate .venv first for best results)"
	@echo "  lint      - Run flake8 linter"
	@echo "  format    - Run Black code formatter"
	@echo "  intake    - Run champion intake tool"
	@echo "  analysis  - Run champion analysis tool"
	@echo "  summary   - Generate champion summaries"
	@echo "  clean     - Remove .venv and __pycache__ folders"
	@echo ""
	@echo "After running 'make setup', open the folder in VS Code and select the .venv Python interpreter when prompted."
	@echo "Activate the virtual environment before running tests in the terminal:"
	@echo "  Windows: .venv\\Scripts\\activate"
	@echo "  macOS/Linux: source .venv/bin/activate"
format:
	black .

clean:
	rmdir /S /Q .venv || true
	rmdir /S /Q __pycache__ || true
	rmdir /S /Q Champion\ Review\ and\ Comparison\__pycache__ || true
	rmdir /S /Q ChampionAnalysisTool\__pycache__ || true
	rmdir /S /Q Summarize\ Champion\ Results\__pycache__ || true
