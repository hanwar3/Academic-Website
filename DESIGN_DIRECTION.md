# Design direction (overrides CLAUDE.md §5 and §6)

Haider rejected the immersive scrollytelling concept. The new brief is: **simple yet sophisticated.** Where this file conflicts with CLAUDE.md or the original brief in §14, this file wins. The facts in CLAUDE.md §2 and the open questions in §12 still apply in full.

## What changes
- **No scroll journey.** No fullscreen chapters, canvas terrain, elevation rail, parallax or scroll-driven animation. `assets/js/terrain.js` and `tools/terrain*.py` are archived. Do not use them.
- **No dark slate hero.** The whole site uses one light palette.
- **Fewer gimmicks:** no switcher tabs, no slide-over drawers, no reader modal. Use plain pages and plain links instead.
- **The maps stay, used small.** `assets/maps/*.svg` can sit next to the relevant project as a quiet figure. They are optional.

## The feel
A well-made university press page or a museum's research page. Calm, typographic, generous white space, with every element doing a job. Sophistication comes from type, spacing and restraint, not effects. A search committee member finds the CV in one click and the papers in two.

## Structure (multi-page static site)
- **Home**: name; one-line positioning ("Social scientist studying disaster risk, recovery and cultural heritage"); a 3–4 sentence bio; a real portrait (the environmental tan-blazer photo, §3); links to CV (PDF), email and LinkedIn. Below that, three short research areas, each with one paragraph and a link:
  1. Volunteers and emergency management in search and rescue (the dissertation)
  2. Cultural heritage and disaster risk (Built Heritage review, the Texas workshop, Gilgit-Baltistan)
  3. Equitable recovery and climate adaptation (Austin, Mayfield, Lumberton, WWF, UNDRR)
- **Research**: one section per area, with projects, roles and figures from §2.
- **Publications**: a grouped list (published, accepted, under review, in progress, conferences, reviewer service). Each entry has a small "Abstract" toggle (`<details>`), and copy BibTeX / APA buttons.
- **Methods & data**: fieldwork methods first, then 2–3 entries linking to the GitHub lab (`#hma`, `#floods`), each with one thumbnail and one finding.
- **Teaching & service**
- **Writing** (blog): a simple list of posts, each on its own page. Markdown files plus Sveltia/Decap `/admin` as in §9.
- **Contact**: email shown as text, a short Web3Forms form with a topic dropdown, a mailto fallback, and a Cal.com link if Haider provides one.
- **CV**: a PDF download, plus an HTML version.

## Visual system
- Background `#FAF7F2` and ink `#18181B`, secondary text `#57534E`. Use **one** accent only, Indus teal `#0F766E`, for links and focus. Terracotta is optional, at most one tiny use.
- Type: Newsreader for headings and Source Sans 3 for body (self-hosted). JetBrains Mono is not needed. Use a modular scale, a body size of 18 px, line-height 1.6 and a max measure of 66ch.
- Layout: a single centered column about 720 px wide for text, widening to about 1040 px only for the publications list or figures. Content is left-aligned.
- Thin hairline rules between sections. No cards, shadows, gradients, rounded boxes, icons-as-decoration, ALL-CAPS eyebrows or emoji.
- Motion: none, apart from link hover and the `<details>` open state. Respect reduced motion.
- References for the feel (not to copy): princeton.edu faculty pages done well, Getty Research Institute pages, and Owlstown-style academic sites at their best.

## Quality bar
Responsive down to 360 px, keyboard accessible, AA contrast, fast (no JS framework; under about 100 KB of JS total), Lighthouse 95+ on mobile, and working links. Every number must trace to CLAUDE.md §2. Use the corrected figures: Recharge Pakistan US$77.8M with targets, the ISA heritage paper as "accepted", NIST as Chapter 3 co-authorship.
