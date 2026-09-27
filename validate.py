#!/usr/bin/env python3
"""Validate the release's declarative module contract with no dependencies."""
import json
from pathlib import Path
p=Path(__file__).with_name('curve-tab-folders.json')
assert p.stat().st_size <= 65_536
m=json.loads(p.read_text())
assert set(m)=={'schemaVersion','id','name','author','summary','tabLayout','sidebarFolders'}
assert m['schemaVersion']==2 and m['id']=='curve.tab-folders'
assert m['sidebarFolders'] is True and m['tabLayout']=='standard'
assert 0<len(m['name'])<=80 and len(m['author'])<=80 and len(m['summary'])<=300
print('PASS: Curve Tab Folders API 2 package')
