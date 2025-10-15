# Champion Summary System and Data Sources

All champion summaries and downstream analysis in this module are generated from the authoritative completed prompt markdown files and champion JSON logs.

- Completed prompts (`output/completed_prompts/[champion]_prompt.completed.md`) are the human-readable, validated source for each champion.
- Champion JSONs (`output/Champions/[champion].json`) are generated from the completed prompts and provide a machine-readable, structured version of the same data.
- All summary and analysis scripts use these files as their only source of truth.
- If a completed prompt exists for a champion, it is never overwritten; prompt/JSON generation is skipped for that champion.

For details on the workflow, see the main `README.md` and `.github/copilot-instructions.md`.
