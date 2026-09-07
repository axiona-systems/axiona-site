#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, json, re, shutil
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
HEADER = '/assets/brand/axiona-horizontal-fullcolor.svg'
FOOTER = '/assets/brand/axiona-horizontal-monochrome-white.svg'
SYMBOL = '/assets/brand/axiona-symbol-fullcolor.svg'
AUTH_COMMIT = 'aebf0f112bd5f4e589ef58f337a55d9be861b493'
ARTIFACT_DIGEST = 'sha256:3fbd354301b45ff0fe2e4edff425003eed300b812d228a82ddf798af40ebae0d'

PROVENANCE = '''# AXIONA Brand Consumer Boundary

Status: **R147 CANONICAL RUNTIME MIGRATION**

`axiona-systems/axiona-site` remains a public presentation/runtime consumer of AXIONA identity. It is not the authority for master brand geometry, brand rules, master export tooling or system-level brand governance.

## System authority

Canonical authority repository: `axiona-systems/AXIONA_BRAND`

Pinned authority commit: `aebf0f112bd5f4e589ef58f337a55d9be861b493`

Canonical source identities:

- horizontal master Git blob: `374cc2f8738cb0abd519016cac2759b1cc43be0d`
- standalone symbol Git blob: `1fbe0628bf1d6240495da75dfab2b51a28aac391`
- deterministic export artifact digest: `sha256:3fbd354301b45ff0fe2e4edff425003eed300b812d228a82ddf798af40ebae0d`
- authority workflow run: `34063542627`
- authority artifact: `9998217611` (`axiona-brand-master-v1`)

The site does not regenerate or redefine these masters. It consumes exact approved derivatives from the pinned authority package.

## R147 public runtime mapping

| Public placement | Runtime asset | Authority role |
| --- | --- | --- |
| Header / navigation | `assets/brand/axiona-horizontal-fullcolor.svg` | exact canonical horizontal master copy |
| Footer / dark surface | `assets/brand/axiona-horizontal-monochrome-white.svg` | exact approved monochrome-white derivative |
| Browser SVG favicon | `favicon.svg` | exact canonical symbol SVG copy |
| 16 px favicon | `favicon-16x16.png` | exact deterministic symbol derivative |
| 32 px favicon | `favicon-32x32.png` | exact deterministic symbol derivative |
| Legacy/browser ICO | `favicon.ico` | exact deterministic 16/32/48 multi-size ICO |
| Apple touch icon | `apple-touch-icon.png` | exact 180 px paper-background symbol derivative |
| PWA icon | `assets/brand/axiona-icon-192.png` | exact 192 px paper-background symbol derivative |
| PWA icon | `assets/brand/axiona-icon-512.png` | exact 512 px paper-background symbol derivative |
| Keeper product mark | `assets/brand/axiona-symbol-fullcolor.svg` | exact canonical standalone symbol |
| Social preview cards | `assets/social/*r147-*.png` | R92 composition retained; old identity replaced by canonical horizontal lockup; fresh URLs |

The site manifest uses canonical paper `#F1EEE6` and deep petrol `#082830`.

## Completeness

All 31 public HTML documents bind the full-color horizontal lockup in the header and the monochrome-white lockup in the footer. All 30 indexable HU/EN/DE pages bind locale-correct R147 social cards. The 404 page carries the same header/footer and browser identity.

Legacy runtime identity is prohibited after R147: `assets/axiona-mark.png`, any `assets/social/*r92-*.png`, and any public binding to those assets.

## Machine verification

`assets/brand/AXIONA_BRAND_RUNTIME_V1.json` records the pinned authority, placement mapping and exact SHA-256 hashes of every active brand/browser/social runtime asset. `scripts/verify_brand_consumer_boundary.py`, browser identity, social metadata, asset-reference and render-contract checks fail closed on drift.
'''

BRAND_VERIFY = r'''#!/usr/bin/env python3
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
  pages=sorted([*ROOT.glob('*.html'),*(ROOT/'en').glob('*.html'),*(ROOT/'de').glob('*.html')])
  if len(pages)!=31: fail(f'public brand page count drift: {len(pages)}')
  for p in pages:
    t=p.read_text(); label=p.relative_to(ROOT).as_posix()
    if '/assets/axiona-mark.png' in t or 'r92-' in t: fail(f'legacy brand binding remains: {label}')
    if t.count(f'src="{HEADER}"')!=1 or t.count(f'href="{HEADER}"')!=1: fail(f'header brand binding mismatch: {label}')
    if t.count(f'src="{FOOTER}"')!=1: fail(f'footer brand binding mismatch: {label}')
    sc=t.count(f'src="{SYMBOL}"')
    if label in {'keeper.html','en/keeper.html','de/keeper.html'}:
      if sc!=1: fail(f'Keeper product symbol binding mismatch: {label}')
    elif sc: fail(f'unexpected standalone product symbol: {label}')
  stale=list((ROOT/'assets/social').glob('*r92-*.png'))
  if stale: fail('legacy R92 social cards still exist')
  print('AXIONA_BRAND_CONSUMER_BOUNDARY=PASS'); print('SITE_BRAND_AUTHORITY=false'); print('SYSTEM_BRAND_AUTHORITY=axiona-systems/AXIONA_BRAND'); print('BRAND_AUTHORITY_COMMIT=aebf0f112bd5f4e589ef58f337a55d9be861b493'); print('BRAND_RUNTIME_RELEASE=R147'); print('PUBLIC_BRAND_PAGES=31'); print('VERIFIED_RUNTIME_ASSETS=16')
if __name__=='__main__': main()
'''

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise SystemExit(f'{label}: expected one exact replacement, found {text.count(old)}')
    return text.replace(old, new, 1)

def migrate_html() -> None:
    pages=sorted([*ROOT.glob('*.html'),*(ROOT/'en').glob('*.html'),*(ROOT/'de').glob('*.html')])
    if len(pages)!=31: raise SystemExit(f'public html count drift: {len(pages)}')
    brand_re=re.compile(r'(<a\b[^>]*\bclass="brand"[^>]*>).*?(</a>)',re.S)
    footer_re=re.compile(r'<div class="footer-brand">.*?</div>',re.S)
    for p in pages:
        t=p.read_text(encoding='utf-8')
        t=t.replace('/assets/axiona-mark.png', HEADER)
        t=t.replace('social-preview-r92-', 'social-preview-r147-')
        matches=list(brand_re.finditer(t))
        if len(matches)!=1: raise SystemExit(f'{p}: brand anchor count {len(matches)}')
        opening=matches[0].group(1)
        repl=opening+f'<img alt="" class="brand-lockup" height="67" src="{HEADER}" width="200"/></a>'
        t=brand_re.sub(repl,t,count=1)
        fm=list(footer_re.finditer(t))
        if len(fm)!=1: raise SystemExit(f'{p}: footer-brand count {len(fm)}')
        t=footer_re.sub(f'<div class="footer-brand"><img alt="AXIONA Systems" class="footer-brand-lockup" height="70" src="{FOOTER}" width="210"/></div>',t,count=1)
        if p.relative_to(ROOT).as_posix() in {'keeper.html','en/keeper.html','de/keeper.html'}:
            marker='class="keeper-product-lockup"'; idx=t.find(marker)
            if idx<0: raise SystemExit(f'{p}: keeper product lockup missing')
            end=t.find('</div>',idx); segment=t[idx:end]
            if HEADER not in segment: raise SystemExit(f'{p}: keeper product mark source missing')
            segment=segment.replace(HEADER,SYMBOL,1); t=t[:idx]+segment+t[end:]
        p.write_text(t,encoding='utf-8')

def migrate_css() -> None:
    p=ROOT/'assets/styles-r71.css'; t=p.read_text()
    t=replace_once(t,'.brand{grid-template-rows:22px 14px;grid-template-columns:40px auto;align-items:center;column-gap:11px;width:max-content;display:grid}.brand img{border-radius:7px;grid-row:1/3}.brand span{letter-spacing:.11em;font-size:16px;font-weight:900;line-height:1}.brand small{letter-spacing:.38em;font-size:9px;font-weight:700}', '.brand{align-items:center;width:max-content;min-height:48px;display:flex}.brand img{width:200px;height:auto;border-radius:0}.brand span,.brand small{display:none}','desktop brand css')
    t=replace_once(t,'.footer-brand{align-items:center;gap:14px;display:flex}.footer-brand img{border-radius:8px}.footer-brand strong{letter-spacing:.12em;font-size:15px;line-height:.95}', '.footer-brand{align-items:center;min-height:54px;display:flex}.footer-brand img{width:210px;height:auto;border-radius:0}.footer-brand strong{display:none}','footer brand css')
    t=replace_once(t,'.brand{grid-template-rows:18px 12px;grid-template-columns:34px auto}.brand img{width:34px;height:34px}.brand span{font-size:13px}.brand small{font-size:7px}', '.brand{min-height:42px}.brand img{width:168px;height:auto}','mobile brand css')
    p.write_text(t)

def migrate_text_contracts() -> None:
    p=ROOT/'site.webmanifest'; t=p.read_text().replace('"#f6efe3"','"#F1EEE6"').replace('"#142d31"','"#082830"'); p.write_text(t)
    p=ROOT/'README.md'; t=p.read_text(); anchor='Older release-numbered design/status documents remain historical evidence only. They are not active CI contracts and must not override the current public source.\n'
    addition='\n### Brand runtime authority\n\nThe website is a consumer of the private `axiona-systems/AXIONA_BRAND` authority, pinned at `aebf0f112bd5f4e589ef58f337a55d9be861b493`. R147 migrated the complete public identity surface to master-derived header/footer lockups, favicon/browser identity, Apple/PWA icons and fresh localized social cards. Exact runtime provenance and hashes are recorded in `assets/brand/AXIONA_BRAND_RUNTIME_V1.json` and `docs/status/AXIONA_BRAND_CONSUMER_PROVENANCE.md`.\n'
    if addition.strip() not in t: t=replace_once(t,anchor,anchor+addition,'README brand section')
    p.write_text(t); (ROOT/'docs/status/AXIONA_BRAND_CONSUMER_PROVENANCE.md').write_text(PROVENANCE)
    p=ROOT/'scripts/verify_social_metadata.py'; t=p.read_text().replace('social-preview-r92','social-preview-r147').replace('OK_AXIONA_SOCIAL_METADATA_R132','OK_AXIONA_SOCIAL_METADATA_R147')
    needle='''            if dims != (1200, 630):\n                errors.append(\n                    f"social image asset mismatch: {image_path.relative_to(root).as_posix()} -> {dims or '<invalid>'}"\n                )\n\n    return errors\n'''
    if 'legacy R92 social card still present' not in t:
        t=replace_once(t,needle,needle.replace('\n    return errors\n','\n    stale = sorted((root / "assets" / "social").glob("*r92-*.png"))\n    if stale:\n        errors.append("legacy R92 social card still present: " + ", ".join(path.name for path in stale))\n\n    return errors\n'),'social stale guard')
    p.write_text(t)
    p=ROOT/'scripts/verify_browser_identity.py'; t=p.read_text().replace('"background_color": "#f6efe3"','"background_color": "#F1EEE6"').replace('"theme_color": "#142d31"','"theme_color": "#082830"'); p.write_text(t)
    p=ROOT/'scripts/verify_asset_references.py'; t=p.read_text().replace("'assets/motion-r108.css')", "'assets/motion-r108.css', 'assets/axiona-mark.png')"); p.write_text(t)
    p=ROOT/'scripts/verify-all.sh'; t=p.read_text(); anchor='python3 scripts/verify_asset_references.py\n'
    if 'verify_brand_consumer_boundary.py' not in t: t=replace_once(t,anchor,anchor+'python3 scripts/verify_brand_consumer_boundary.py\n','verify-all brand hook')
    p.write_text(t); (ROOT/'scripts/verify_brand_consumer_boundary.py').write_text(BRAND_VERIFY); (ROOT/'scripts/verify_brand_consumer_boundary.py').chmod(0o755)
    p=ROOT/'scripts/verify_render_contract.mjs'; t=p.read_text()
    old="""          activeNav: document.querySelectorAll('.topbar nav a.active').length,\n          activeAfter: active ? getComputedStyle(active, '::after').display : null\n"""
    new="""          activeNav: document.querySelectorAll('.topbar nav a.active').length,\n          activeAfter: active ? getComputedStyle(active, '::after').display : null,\n          brandSrc: document.querySelector('.brand img')?.getAttribute('src') || '',\n          brandWidth: document.querySelector('.brand img')?.getBoundingClientRect().width || 0,\n          footerBrandSrc: document.querySelector('.footer-brand img')?.getAttribute('src') || '',\n          footerBrandWidth: document.querySelector('.footer-brand img')?.getBoundingClientRect().width || 0\n"""
    if 'brandSrc:' not in t: t=replace_once(t,old,new,'render brand fields')
    anchor="""      if (result.r137 !== 1 || result.motionCss !== 1 || result.motionJs !== 1 || result.stale !== 0) {\n        throw new Error(`${route} ${label}: canonical binding mismatch ${JSON.stringify(result)}`);\n      }\n"""
    add="""      if (result.brandSrc !== '/assets/brand/axiona-horizontal-fullcolor.svg' || result.footerBrandSrc !== '/assets/brand/axiona-horizontal-monochrome-white.svg') {\n        throw new Error(`${route} ${label}: brand lockup binding mismatch ${JSON.stringify(result)}`);\n      }\n      const expectedBrandWidth = label === 'mobile' ? 168 : 200;\n      if (Math.abs(result.brandWidth - expectedBrandWidth) > 2 || Math.abs(result.footerBrandWidth - 210) > 2) {\n        throw new Error(`${route} ${label}: brand lockup geometry mismatch ${JSON.stringify(result)}`);\n      }\n"""
    if 'brand lockup binding mismatch' not in t: t=replace_once(t,anchor,anchor+add,'render brand assertions')
    p.write_text(t)

def copy_brand(dist: Path) -> None:
    mapping=[('axiona-master-horizontal-fullcolor.svg','assets/brand/axiona-horizontal-fullcolor.svg'),('axiona-horizontal-monochrome-white.svg','assets/brand/axiona-horizontal-monochrome-white.svg'),('axiona-symbol-fullcolor.svg','assets/brand/axiona-symbol-fullcolor.svg'),('axiona-symbol-fullcolor.svg','favicon.svg'),('axiona-symbol-16.png','favicon-16x16.png'),('axiona-symbol-32.png','favicon-32x32.png'),('axiona-symbol.ico','favicon.ico'),('axiona-symbol-paper-180.png','apple-touch-icon.png'),('axiona-symbol-paper-192.png','assets/brand/axiona-icon-192.png'),('axiona-symbol-paper-512.png','assets/brand/axiona-icon-512.png')]
    for src,dst in mapping:
        out=ROOT/dst; out.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(dist/src,out)

def generate_social(dist: Path) -> None:
    logo=Image.open(dist/'axiona-master-horizontal-fullcolor.png').convert('RGBA'); tw=260; th=round(tw*logo.height/logo.width); logo=logo.resize((tw,th),Image.Resampling.LANCZOS)
    social=ROOT/'assets/social'
    for lang in ('hu','en','de'):
      for keeper in (False,True):
        old=social/(f'axiona-keeper-social-preview-r92-{lang}.png' if keeper else f'axiona-social-preview-r92-{lang}.png'); new=social/(f'axiona-keeper-social-preview-r147-{lang}.png' if keeper else f'axiona-social-preview-r147-{lang}.png')
        im=Image.open(old).convert('RGB')
        if im.size!=(1200,630): raise SystemExit(f'bad social size: {old}')
        px=im.load(); x0,y0,x1,y1=54,44,314,131
        for y in range(y0,y1):
          left,right=px[x0-1,y],px[x1,y]; width=x1-x0
          for i,x in enumerate(range(x0,x1)):
            f=(i+1)/(width+1); px[x,y]=tuple(round(left[c]*(1-f)+right[c]*f) for c in range(3))
        im.paste(logo,(54,44),logo); im.save(new,'PNG',optimize=True)
    for p in social.glob('*r92-*.png'): p.unlink()

def write_manifest() -> None:
    rels=['assets/brand/axiona-horizontal-fullcolor.svg','assets/brand/axiona-horizontal-monochrome-white.svg','assets/brand/axiona-symbol-fullcolor.svg','favicon.svg','favicon-16x16.png','favicon-32x32.png','favicon.ico','apple-touch-icon.png','assets/brand/axiona-icon-192.png','assets/brand/axiona-icon-512.png','assets/social/axiona-keeper-social-preview-r147-de.png','assets/social/axiona-keeper-social-preview-r147-en.png','assets/social/axiona-keeper-social-preview-r147-hu.png','assets/social/axiona-social-preview-r147-de.png','assets/social/axiona-social-preview-r147-en.png','assets/social/axiona-social-preview-r147-hu.png']
    m={'schema':'axiona.brand.runtime-consumer.v1','status':'canonical-runtime-consumer','release':'R147','authority':{'repository':'axiona-systems/AXIONA_BRAND','commit':AUTH_COMMIT,'artifact_run_id':34063542627,'artifact_id':9998217611,'artifact_digest':ARTIFACT_DIGEST,'master_git_blob_sha':'374cc2f8738cb0abd519016cac2759b1cc43be0d','symbol_git_blob_sha':'1fbe0628bf1d6240495da75dfab2b51a28aac391'},'placements':{'header':{'path':HEADER},'footer':{'path':FOOTER},'keeper_product_mark':{'path':SYMBOL},'favicon_svg':{'path':'/favicon.svg'},'apple_touch':{'path':'/apple-touch-icon.png'},'pwa_192':{'path':'/assets/brand/axiona-icon-192.png'},'pwa_512':{'path':'/assets/brand/axiona-icon-512.png'}},'social':{'release':'R147'},'sha256':{rel:sha256(ROOT/rel) for rel in rels}}
    p=ROOT/'assets/brand/AXIONA_BRAND_RUNTIME_V1.json'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(m,indent=2)+'\n')

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--brand-dist',required=True,type=Path); args=ap.parse_args(); dist=args.brand_dist
    migrate_html(); migrate_css(); migrate_text_contracts(); copy_brand(dist); generate_social(dist)
    legacy=ROOT/'assets/axiona-mark.png'
    if legacy.exists(): legacy.unlink()
    write_manifest(); print('R147_MATERIALIZE=PASS'); return 0
if __name__=='__main__': raise SystemExit(main())
