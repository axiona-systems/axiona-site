# AXIONA site R69 audit notes

## Main issue found

The contact and support pages used real HTML forms with:

```html
<form action="mailto:hello@axiona.systems" method="post" enctype="text/plain">
```

That is not a normal secure HTTPS form submission. Even when the page itself is loaded over HTTPS, browsers can warn when a form is submitted through a non-standard or insecure endpoint/protocol. This can show as: “This form is not secure. Autofill has been turned off.”

## R69 fix

- Removed all real `<form>` elements from contact/support pages.
- Removed all `action="mailto:..."`, `method="post"` and `enctype="text/plain"` markers.
- Replaced the forms with local-only email draft panels.
- Visitor-entered data stays in the browser until the visitor explicitly opens/sends the email.
- The draft button builds a `mailto:` email body from the typed fields using local JavaScript only.
- CSS bumped to `styles.css?v=69`.

## Language and copy cleanup

- Public language switch now exposes only HU / EN / DE.
- FR / IT / ES pages are kept in the package but removed from the public language switch and sitemap.
- FR / IT / ES pages have `noindex, nofollow` until those translations are finished.
- DE visible pages were cleaned where English placeholder copy had leaked into the page.
- Contact/support copy was made less artificial and less internal.
- Mixed English options on HU/DE/FR/IT/ES contact forms were replaced or hidden from public navigation.

## Production recommendation

For a real submitted form later, use a proper HTTPS endpoint under the AXIONA domain, for example `/api/contact`, with validation, spam protection, rate limiting, privacy text and server-side mail delivery. Until that exists, the local-only email draft is safer and more honest than a fake form submit.

## Proof summary

- `OK_NO_INSECURE_FORM_MARKERS`
- `OK_DE_VISIBLE_TEXT_CLEAN`
- `OK_ONLY_HU_EN_DE_VISIBLE_ON_PUBLIC_SWITCHES`
- `OK_NO_INDEX_FR_IT_ES`
- `OK_SITEMAP_HU_EN_DE_ONLY`
- `styles.css?v=69`
