# AXIONA R138 smooth motion

R138 replaces viewport-edge reveal toggling with a smooth one-shot settled state.

- 18 px reveal travel on desktop, 12 px on mobile
- 900 ms transform duration on desktop, 760 ms on mobile
- cubic-bezier(.16,1,.3,1) easing
- once revealed, an element stays settled when scrolling away and back
- prefers-reduced-motion remains static
- continuous decorative motion remains unchanged

Binding: PASS
