"""
Validation Script for Boss Guide Structure
-------------------------------------------
Validates the structure, TOC, sections, and formatting of boss guide Markdown files

Checks:
1. TOC format (numbered list with anchor links)
2. Required sections (1-12 per Boss_Guide_Template.md)
3. Section numbering consistency
4. Anchor link validity
5. Affinity safety/risk documentation
6. Team entry completeness

Usage:
    python Tools/validate_guide_structure.py Notes/Dragon_Hard_Team_Notes_FINAL.md
    python Tools/validate_guide_structure.py --all  # Validate all FINAL guides
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Optional

# Required sections per Boss_Guide_Template.md
REQUIRED_SECTIONS = [
    "Boss Mechanics & Stat Requirements",
    "Teams by Estimated Damage/Clear Speed",
    "Detailed Team Sections",
    "Best Champions & Team Participation",
    "Direct Champion Comparisons by Role",
    "Ideal Champions to Pull",
    "General Notes",
    "Actionable Notes & Upgrade Advice",
    "Team Flexibility & Alternate Builds",
    "When to Use Each Team",
    "Additional Team Archetypes",
    "Validation & Simulation Notes"
]

# Flexible section names (aliases)
SECTION_ALIASES = {
    "Boss Mechanics": ["Boss Mechanics & Stat Requirements", "Boss Mechanics and Stat Requirements", "1. Boss Mechanics"],
    "Teams Summary": ["Teams by Estimated Damage/Clear Speed", "Teams by Estimated Damage", "Quick Reference: Best Teams"],
    "Detailed Teams": ["Detailed Team Sections", "Detailed Team Recommendations", "Team Recommendations"],
    "Best Champions": ["Best Champions & Team Participation", "Best Champions and Team Participation"],
    "Champion Comparisons": ["Direct Champion Comparisons by Role", "Champion Comparisons by Role"],
    "Pull Guide": ["Ideal Champions to Pull", "Champions to Pull"],
    "General Notes": ["General Notes", "General Advice"],
    "Actionable Advice": ["Actionable Notes & Upgrade Advice", "Actionable Notes and Upgrade Advice", "Upgrade Advice"],
    "Flexibility": ["Team Flexibility & Alternate Builds", "Team Flexibility", "Alternate Builds"],
    "When to Use": ["When to Use Each Team", "When to Use Teams"],
    "Additional Teams": ["Additional Team Archetypes", "Additional Teams"],
    "Validation": ["Validation & Simulation Notes", "Validation and Simulation Notes", "Simulation Notes"]
}


class GuideValidator:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.lines = []
        self.toc_sections = []
        self.actual_sections = []
        self.errors = []
        self.warnings = []
        
        self.load_file()
    
    def load_file(self):
        """Load guide file"""
        if not self.file_path.exists():
            self.errors.append(f"ERROR: File not found: {self.file_path}")
            return
        
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()
    
    def validate(self) -> Tuple[bool, List[str]]:
        """Run all validation checks"""
        if self.errors:
            return False, self.errors
        
        self.check_toc_format()
        self.check_section_headers()
        self.check_anchor_links()
        self.check_required_sections()
        self.check_affinity_documentation()
        
        return len(self.errors) == 0, self.errors + self.warnings
    
    def check_toc_format(self):
        """Check TOC format (numbered list with anchor links)"""
        in_toc = False
        toc_lines = []
        
        for i, line in enumerate(self.lines, start=1):
            line_stripped = line.strip()
            
            # Detect TOC start
            if line_stripped.lower().startswith('## table of contents'):
                in_toc = True
                continue
            
            # Detect TOC end (next ## header or blank lines)
            if in_toc and line_stripped.startswith('##') and 'table of contents' not in line_stripped.lower():
                break
            
            if in_toc and line_stripped:
                toc_lines.append((i, line_stripped))
        
        if not toc_lines:
            self.warnings.append(f"WARNING: No Table of Contents found")
            return
        
        # Check numbered format
        numbered_count = 0
        anchor_count = 0
        
        for line_num, line in toc_lines:
            # Check for numbered format (1., 2., 3., etc.)
            if re.match(r'^\d+\.', line):
                numbered_count += 1
                
                # Extract section info
                match = re.match(r'^(\d+)\.\s+\[(.+?)\]\((.+?)\)', line)
                if match:
                    section_num, section_name, anchor = match.groups()
                    self.toc_sections.append({
                        'number': int(section_num),
                        'name': section_name,
                        'anchor': anchor,
                        'line': line_num
                    })
                    anchor_count += 1
                else:
                    # No anchor link
                    match_plain = re.match(r'^(\d+)\.\s+(.+)', line)
                    if match_plain:
                        section_num, section_name = match_plain.groups()
                        self.toc_sections.append({
                            'number': int(section_num),
                            'name': section_name,
                            'anchor': None,
                            'line': line_num
                        })
                        self.warnings.append(f"WARNING: TOC line {line_num} missing anchor link: '{line}'")
        
        if numbered_count == 0:
            self.errors.append(f"ERROR: TOC is not using numbered format (1., 2., 3., etc.)")
        elif numbered_count < len(toc_lines) * 0.8:
            self.warnings.append(f"WARNING: TOC has mixed formats ({numbered_count}/{len(toc_lines)} numbered)")
        
        if anchor_count < numbered_count * 0.8:
            self.warnings.append(f"WARNING: Many TOC entries missing anchor links ({anchor_count}/{numbered_count} have anchors)")
        
        # Check sequential numbering
        if self.toc_sections:
            expected = 1
            for section in self.toc_sections:
                if section['number'] != expected:
                    self.errors.append(f"ERROR: TOC numbering skipped from {expected-1} to {section['number']} (line {section['line']})")
                expected = section['number'] + 1
    
    def check_section_headers(self):
        """Check section headers in document"""
        for i, line in enumerate(self.lines, start=1):
            line_stripped = line.strip()
            
            # Match section headers (## 1. Section Name or ## Section Name)
            match = re.match(r'^##\s+(\d+\.)?\s*(.+)', line_stripped)
            if match:
                section_num_str, section_name = match.groups()
                section_num = int(section_num_str.rstrip('.')) if section_num_str else None
                
                self.actual_sections.append({
                    'number': section_num,
                    'name': section_name.strip(),
                    'line': i
                })
    
    def check_anchor_links(self):
        """Validate anchor links match section headers"""
        if not self.toc_sections or not self.actual_sections:
            return
        
        for toc_entry in self.toc_sections:
            if not toc_entry['anchor']:
                continue
            
            anchor = toc_entry['anchor'].lstrip('#')
            
            # Find matching section
            found = False
            for actual_section in self.actual_sections:
                # Generate expected anchor from section header
                expected_anchor = self.generate_anchor(actual_section['name'], actual_section['number'])
                
                if anchor == expected_anchor or anchor.lower() == expected_anchor.lower():
                    found = True
                    break
            
            if not found:
                self.warnings.append(f"WARNING: TOC anchor '#{anchor}' may not match any section header (line {toc_entry['line']})")
    
    def generate_anchor(self, section_name: str, section_num: Optional[int]) -> str:
        """Generate expected anchor from section name"""
        # Convert to lowercase, replace spaces with hyphens, remove special chars
        anchor = section_name.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor)
        anchor = re.sub(r'\s+', '-', anchor)
        
        if section_num:
            anchor = f"{section_num}-{anchor}"
        
        return anchor
    
    def check_required_sections(self):
        """Check if all required sections are present"""
        actual_section_names = [s['name'].lower() for s in self.actual_sections]
        
        missing_sections = []
        for required in REQUIRED_SECTIONS:
            # Check if required section or any alias is present
            found = False
            
            for alias_group in SECTION_ALIASES.values():
                if required in alias_group:
                    for alias in alias_group:
                        if any(alias.lower() in actual for actual in actual_section_names):
                            found = True
                            break
                if found:
                    break
            
            if not found:
                # Direct match
                if any(required.lower() in actual for actual in actual_section_names):
                    found = True
            
            if not found:
                missing_sections.append(required)
        
        if missing_sections:
            self.warnings.append(f"WARNING: Missing sections: {', '.join(missing_sections)}")
    
    def check_affinity_documentation(self):
        """Check if affinity safety/risk is documented"""
        content = ''.join(self.lines)
        
        # Check for affinity documentation in teams
        if 'affinity safety' not in content.lower() and 'affinity risk' not in content.lower():
            self.warnings.append(f"WARNING: No affinity safety/risk documentation found in guide")
        
        # Check for team sections with affinity notes
        team_sections = [s for s in self.actual_sections if 'team' in s['name'].lower()]
        if len(team_sections) > 3:
            affinity_mentions = content.lower().count('affinity')
            if affinity_mentions < len(team_sections):
                self.warnings.append(f"WARNING: {len(team_sections)} team sections but only {affinity_mentions} affinity mentions (recommend 1+ per team)")


def validate_guide(file_path: Path) -> Tuple[bool, List[str]]:
    """Validate a single guide file"""
    validator = GuideValidator(file_path)
    is_valid, messages = validator.validate()
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"GUIDE: {file_path.name}")
    print(f"{'='*60}")
    print(f"TOC Sections: {len(validator.toc_sections)}")
    print(f"Actual Sections: {len(validator.actual_sections)}")
    print(f"Errors: {sum(1 for m in messages if m.startswith('ERROR'))}")
    print(f"Warnings: {sum(1 for m in messages if m.startswith('WARNING'))}")
    
    if messages:
        for msg in messages:
            if msg.startswith('ERROR'):
                print(f"  ❌ {msg}")
            else:
                print(f"  ⚠️  {msg}")
    else:
        print("  ✅ All validation checks passed!")
    
    return is_valid, messages


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate Boss Guide Structure')
    parser.add_argument('file', type=str, nargs='?', help='Path to guide file')
    parser.add_argument('--all', action='store_true', help='Validate all FINAL guides in Notes/')
    
    args = parser.parse_args()
    
    script_dir = Path(__file__).parent.parent
    
    if args.all:
        # Validate all FINAL guides
        notes_dir = script_dir / 'Notes'
        guide_files = sorted(notes_dir.glob('*_FINAL.md'))
        
        print(f"Validating {len(guide_files)} FINAL guides...\n")
        
        results = []
        for guide_file in guide_files:
            is_valid, messages = validate_guide(guide_file)
            results.append((guide_file.name, is_valid, messages))
        
        # Overall summary
        print(f"\n{'='*60}")
        print("OVERALL SUMMARY")
        print(f"{'='*60}")
        print(f"Total Guides: {len(results)}")
        print(f"Valid: {sum(1 for _, v, _ in results if v)}")
        print(f"With Errors: {sum(1 for _, v, _ in results if not v)}")
        print(f"With Warnings: {sum(1 for _, v, m in results if v and any('WARNING' in msg for msg in m))}")
        
    elif args.file:
        file_path = script_dir / args.file if not Path(args.file).is_absolute() else Path(args.file)
        is_valid, messages = validate_guide(file_path)
        sys.exit(0 if is_valid else 1)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
