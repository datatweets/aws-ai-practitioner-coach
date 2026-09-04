#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml, csv, zipfile

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
skill = root / 'SKILL.md'
if not skill.exists():
    raise SystemExit('ERROR: SKILL.md missing')

text = skill.read_text(encoding='utf-8')
if not text.startswith('---\n'):
    raise SystemExit('ERROR: YAML frontmatter missing')
_, front, body = text.split('---', 2)
meta = yaml.safe_load(front) or {}
name = meta.get('name', '')
description = meta.get('description', '')

if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
    raise SystemExit('ERROR: invalid skill name')
if root.name != name:
    raise SystemExit(f'ERROR: folder name {root.name!r} must match skill name {name!r}')
if len(name) > 64:
    raise SystemExit('ERROR: name too long')
if not description:
    raise SystemExit('ERROR: description missing')
if len(description) > 200:
    raise SystemExit(f'ERROR: description is {len(description)} chars; Claude guidance allows max 200')

refs = [
    'references/aif-c01-taxonomy.yaml',
    'references/relationship-graph.csv',
    'references/decision-rules.yaml',
    'references/question-blueprints.yaml',
]
for ref in refs:
    if not (root / ref).exists():
        raise SystemExit(f'ERROR: missing {ref}')

taxonomy = yaml.safe_load((root / 'references/aif-c01-taxonomy.yaml').read_text()) or {}
domains = []
if taxonomy.get('domain_files'):
    for item in taxonomy['domain_files']:
        dp = root / 'references' / item['file']
        if not dp.exists():
            raise SystemExit(f'ERROR: missing taxonomy domain file {dp}')
        domains.append(yaml.safe_load(dp.read_text())['domain'])
elif taxonomy.get('domains'):
    domains = taxonomy['domains']
else:
    raise SystemExit('ERROR: taxonomy must provide domain_files or domains')

rules = yaml.safe_load((root / 'references/decision-rules.yaml').read_text())
blueprints = yaml.safe_load((root / 'references/question-blueprints.yaml').read_text())
with (root / 'references/relationship-graph.csv').open(newline='') as f:
    graph_rows = list(csv.DictReader(f))

if len(domains) != 5:
    raise SystemExit('ERROR: taxonomy must contain five AIF-C01 domains')
if not rules.get('rules'):
    raise SystemExit('ERROR: decision rules missing')
if not blueprints.get('blueprints'):
    raise SystemExit('ERROR: question blueprints missing')
if not graph_rows:
    raise SystemExit('ERROR: relationship graph is empty')

required_graph_edges = {
    ('aws-config', 'best-for', 'resource-configuration-compliance'),
    ('audit-manager', 'best-for', 'audit-evidence-collection'),
    ('trusted-advisor', 'best-for', 'optimization-recommendations'),
}
actual = {(r['subject'], r['relation'], r['object']) for r in graph_rows}
missing = sorted(required_graph_edges - actual)
if missing:
    raise SystemExit(f'ERROR: missing required governance graph edges: {missing}')

# If a packaged Claude ZIP exists, validate Anthropic's documented layout.
zip_path = root / 'downloads' / f'{name}.zip'
if zip_path.exists():
    with zipfile.ZipFile(zip_path) as zf:
        names = set(zf.namelist())
        expected = f'{name}/skill.md'
        if expected not in names:
            raise SystemExit(f'ERROR: Claude ZIP must contain {expected}')
        if 'skill.md' in names or 'SKILL.md' in names:
            raise SystemExit('ERROR: Claude ZIP must contain the skill folder, not loose root files')

print(f'OK: validated {name} | {len(domains)} domains | {len(graph_rows)} graph edges | '
      f'{len(rules.get("rules", []))} decision rules | {len(blueprints.get("blueprints", []))} blueprints')
