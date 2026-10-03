# Public artifact for an isolated HTTP proof

`scripts/build_local_public_artifact.py` prepares a reproducible, uncompressed
USTAR archive from one exact 40-character Git commit. It reads committed Git
blobs, so local edits cannot silently replace the selected source bytes.

The product-owned public surface is explicit: the ten known pages in the root,
English and German directories; browser icons, robots/sitemap/manifest/humans,
security.txt and .nojekyll; regular public assets with admitted file extensions.
Symlinks, executables and unknown asset types fail closed. CNAME, engineering
metadata, workflows, scripts and documentation are excluded. Required pages and
root files must all exist. Existing output cannot be overwritten, and output
must be outside the source worktree.

The separate source manifest binds the exact commit/tree, every Git blob and
file SHA-256, recipe SHA-256 and archive bytes/digest. Stable paths/order, zero
timestamps, empty owner names and fixed file permissions make repeated builds
byte-identical. The manifest does not authenticate its caller or grant authority.

```sh
python3 -B scripts/build_local_public_artifact.py \
  --revision <exact-source-commit> --output <new-directory-outside-source>
```

This command prepares bytes only. Release admission remains PENDING and no
deployment is performed. The archive is intended for a separately admitted
isolated HTTP byte-proof target; it does not establish Pages publishing, visual
browser quality, application runtime health or production readiness. Browser
execution of bundled JavaScript requires separate product/network review.

The existing product verifier and public publisher retain their roles. Accepting
this recipe for a proof does not authorize pushing or merging into a branch that
automatically publishes the live website.
