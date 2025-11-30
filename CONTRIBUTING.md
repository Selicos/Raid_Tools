# Contribution Guidelines for Raid Tools

> **All contributors (AI and human): For project-wide, workflow, and safety instructions, see `.github/ai-assistant-instructions.md` (universal, authoritative).**
# Contributing to Raid Tools

Thank you for your interest in contributing!

## Documentation Standards

### Mastery Documentation Policy

**All mastery information MUST use canonical reference format:**

✅ **DO:**
- Reference `input/Mechanic_Dictionary/Masteries/Masteries.md` for all mastery details
- Use simplified format: Build + Path + Why + Cost + Link
- See `MASTERY_REFERENCE_GUIDE.md` for templates and examples

❌ **DON'T:**
- Duplicate tier-by-tier mastery tables in champion reviews or boss guides
- Copy mastery sections from old champion entries
- Create new mastery documentation formats

**Format Example:**
```markdown
**Build:** Warmaster + Master Hexer (Offense + Support)
- **Path:** Deadly Precision → Keen Strike → ... → **Warmaster**
- **Why:** [Key synergies]
- **Cost:** 800 gems OR farm Minotaur's Labyrinth
- **Details:** [Masteries.md](../../input/Mechanic_Dictionary/Masteries/Masteries.md)
```

See `.github/copilot-instructions.md` Section 2 for complete policy.

---

## Getting Started

1. Fork the repository and clone your fork.
2. Run the setup script:
   ```sh
   python "Champion Review and Comparison/Setup_Environment.py"

\\insert the rest of the prompt here

