# AXIONA R137 UX render proof

R137 is the single canonical hotfix layer for the reported navigation and Systems section-01 defects.

Verified with Chromium/Playwright:
- exactly one R137 stylesheet binding on every topbar HTML page;
- no R135/R136 hotfix stylesheet bindings remain;
- exactly one desktop active navigation item on Overview, Systems, Process, Security, Solutions and Contact;
- active navigation pseudo-element is disabled, preventing doubled markers;
- the single persistent marker is the computed inset lower edge;
- Systems section 01 intro and visual have zero geometric overlap at 1280, 1440, 1512, 1728 and 1920 px viewport widths;
- below 1800 px the two blocks are stacked with at least 30 px measured clearance.

Result: PASS
