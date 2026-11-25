#!/usr/bin/env python3
from pathlib import Path
import hashlib, json
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'assets/brand/AXIONA_BRAND_RUNTIME_V1.json'
FORBIDDEN_AUTHORITY=(ROOT/'brand', ROOT/'.github/workflows/brand-master-package.yml', ROOT/'scripts/verify_brand_master.py')
HEADER='/assets/brand/axiona-horizontal-fullcolor.svg'; FOOTER='/assets/brand/axiona-horizontal-monochrome-white.svg'; SYMBOL='/assets/brand/axiona-symbol-fullcolor.svg'
def fail(msg): print('STOP_AXIONA_BRAND_CONSUMER_BOUNDARY:',msg); raise SystemExit(1)
def sha256(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
  for p in FORBIDDEN_AUTHORITY:
    if p.exists(): fail(f'site contains system-level brand authority: {p.relative_to(ROOT)}')
  if (ROOT/'assets/axiona-mark.png').exists(): fail('legacy runtime identity still present: assets/axiona-mark.png')
  if not MANIFEST.is_file(): fail('missing machine-readable runtime brand manifest')
  m=json.loads(MANIFEST.read_text()); a=m.get('authority',{})
  expected={'repository':'axiona-systems/AXIONA_BRAND','commit':'aebf0f112bd5f4e589ef58f337a55d9be861b493','artifact_digest':'sha256:3fbd354301b45ff0fe2e4edff425003eed300b812d228a82ddf798af40ebae0d','master_git_blob_sha':'374cc2f8738cb0abd519016cac2759b1cc43be0d','symbol_git_blob_sha':'1fbe0628bf1d6240495da75dfab2b51a28aac391'}
  for k,v in expected.items():
    if a.get(k)!=v: fail(f'authority mismatch: {k}={a.get(k)!r}')
  if m.get('release')!='R147': fail('runtime release mismatch')
  hashes=m.get('sha256',{})
  if len(hashes)!=16: fail(f'runtime asset hash inventory drift: {len(hashes)}')
  for rel,expected_hash in sorted(hashes.items()):
    p=ROOT/rel
    if not p.is_file(): fail(f'runtime identity asset missing: {rel}')
    if sha256(p)!=expected_hash: fail(f'runtime identity hash drift: {rel}')
  # v4: minden tartalmi oldal fejléce és lábléce a kanonikus, sötét háttérre szánt fekvő logót használja.
  pages=[]
  for p in sorted(ROOT.rglob('*.html')):
    rel=p.relative_to(ROOT)
    if {'.git','node_modules','.claude','BUILD'} & set(rel.parts): continue
    t=p.read_text()
    if 'http-equiv="refresh"' in t: continue
    pages.append((rel.as_posix(),t))
  if len(pages)<15: fail(f'public brand page count drift: {len(pages)}')
  for label,t in pages:
    if '/assets/axiona-mark.png' in t or 'r92-' in t: fail(f'legacy brand binding remains: {label}')
    if t.count(f'src="{FOOTER}"')!=2: fail(f'header/footer brand binding mismatch: {label}')
    if f'src="{HEADER}"' in t or f'src="{SYMBOL}"' in t: fail(f'unexpected brand variant: {label}')
  stale=list((ROOT/'assets/social').glob('*r92-*.png'))
  if stale: fail('legacy R92 social cards still exist')
  print('AXIONA_BRAND_CONSUMER_BOUNDARY=PASS'); print('SITE_BRAND_AUTHORITY=false'); print('SYSTEM_BRAND_AUTHORITY=axiona-systems/AXIONA_BRAND'); print('BRAND_AUTHORITY_COMMIT=aebf0f112bd5f4e589ef58f337a55d9be861b493'); print('BRAND_RUNTIME_RELEASE=R147'); print(f'PUBLIC_BRAND_PAGES={len(pages)}'); print('VERIFIED_RUNTIME_ASSETS=16')
if __name__=='__main__': main()
