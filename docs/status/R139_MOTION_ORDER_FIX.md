# AXIONA R139 motion execution-order correction

The common one-shot motion coordinator now runs as the final deferred script.
This guarantees that page-specific deferred scripts can mark their reveal nodes first.

- common motion coordinator remains `assets/js/motion-r138.js`
- cache-busted script binding uses `?release=R139`
- script is `defer` and remains last in document order
- dynamic reveal attributes on Security, Solutions, Contact, Support, Keeper and policy pages are visible to the coordinator

Binding: PASS
