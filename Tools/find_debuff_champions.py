import json
from pathlib import Path

results = {'Dec ATK': [], 'Dec DEF': [], 'Inc DEF': []}

dir_path = Path('c:/GIT/Raid_Tools/input/Champion_Dictionary/Complete')
for json_file in dir_path.glob('*.json'):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    champ_name = data.get('name', '')
    
    for form in data.get('forms', []):
        for skill in form.get('skills', []):
            cd = skill.get('cooldown_booked')
            desc = skill.get('description', '').lower()
            skill_name = skill.get('name', '')
            
            # Check if cooldown is 3 or less (null = A1, which counts)
            if cd is None or (isinstance(cd, (int, float)) and 0 <= cd <= 3):
                cd_str = 'A1' if cd is None else str(int(cd))
                
                # Check for debuffs/buffs
                if 'decrease atk' in desc or 'decrease attack' in desc:
                    results['Dec ATK'].append(f'{champ_name} - {skill_name} (CD: {cd_str})')
                
                if 'decrease def' in desc:
                    results['Dec DEF'].append(f'{champ_name} - {skill_name} (CD: {cd_str})')
                
                if 'increase def' in desc:
                    results['Inc DEF'].append(f'{champ_name} - {skill_name} (CD: {cd_str})')

# Print results
print('=' * 80)
print('CHAMPIONS WITH DECREASE ATTACK (≤3 turn cooldown)')
print('=' * 80)
for champ in sorted(set(results['Dec ATK'])):
    print(champ)

print('\n' + '=' * 80)
print('CHAMPIONS WITH DECREASE DEFENSE (≤3 turn cooldown)')
print('=' * 80)
for champ in sorted(set(results['Dec DEF'])):
    print(champ)

print('\n' + '=' * 80)
print('CHAMPIONS WITH INCREASE DEFENSE (≤3 turn cooldown)')
print('=' * 80)
for champ in sorted(set(results['Inc DEF'])):
    print(champ)

print('\n' + '=' * 80)
total_dec_atk = len(set(results['Dec ATK']))
total_dec_def = len(set(results['Dec DEF']))
total_inc_def = len(set(results['Inc DEF']))
print(f'TOTAL: {total_dec_atk} Dec ATK | {total_dec_def} Dec DEF | {total_inc_def} Inc DEF')
print('=' * 80)
