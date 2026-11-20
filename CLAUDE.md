> **Read DESIGN_DIRECTION.md first.** Haider rejected the scrollytelling design; the site is now a simple, sophisticated multi-page academic site. That file overrides §5 and §6 below. The terrain files are archived in archive/. All facts in §2 still apply.

# CLAUDE.md: Dr. Haider Waseem Anwar academic website

Handoff from a claude.ai chat session (Project "Academic Website", 15 Nov 2026) to Claude Code in the Claude Desktop Code tab. Read this whole file before writing code. It records everything decided, verified and built so far, the open questions, and the exact code written. Section 14 has the original brief and the Project instructions, word for word. Where this file and the brief disagree, the brief wins, unless this file flags a factual correction with a source.

---

## 0. Status at handoff

| Area | State |
|---|---|
| Source research (CV, statements, LinkedIn, GitHub lab, ISA abstracts, NIST report, reference sites) | Done, findings below |
| Design system | Locked (section 5) |
| Signature terrain backdrop (`tools/terrain.py` → `terrain.js`) | Built and previewed; renderer not yet written |
| Locator maps (`tools/maps.mjs` → 7 SVGs) | Built; rendered once to `maps_check.png`, **not yet visually reviewed** |
| Screenshot helper (`tools/shot.mjs`) | Built |
| Fonts | Installed via npm (`@fontsource-variable/*`); files not yet copied into the site |
| `index.html`, CSS, JS, chapters, publications, blog, meeting drawer, `/admin` CMS | **Not started** |
| Deployment guide (`DEPLOY.md`) | Not started; research done (section 9) |
| Gauntlet audit | Not started (checklist in section 11) |

Task list from the chat: 1 Gather sources ✅ · 2 Lock design system ✅ · 3 Build the five-chapter scroll journey (in progress: assets only) · 4 Publications, Field Notes blog, meeting drawer · 5 Deployment and publishing guide · 6 Gauntlet audit and fixes · 7 Deliver preview and codebase.

### Model configuration
- The chat ran on **Claude Fable 5.2** (API model ID `claude-fable-5-2`), Mythos-tier, then moved to Claude Opus 5.5 (`claude-opus-5-5`) near the end. No special parameters, system prompts or tools were configured beyond the Project instructions in §14.2. Nothing in this codebase depends on the model. In Claude Code, pick the model with the model picker. This file and the Project instructions carry the context.

---

## 1. Who the site is for and what it must do

- **Subject:** Haider Waseem Anwar, PhD in Urban and Regional Sciences, Texas A&M University (Department of Landscape Architecture and Urban Planning, LAUP). Research Associate at the Hazard Reduction & Recovery Center (HRRC), Texas A&M.
- **Audience:** search committees, fellowship reviewers, policy and practice partners (UNDRR, FEMA/HUD-funded programs, NGOs), heritage professionals, students.
- **Job:** meet him first as a social scientist, a disaster risk reduction and recovery scholar, and a cultural heritage researcher. Give one-click access to the CV, publications and contact. Then let visitors who have time take the scroll journey.
- **Hard hierarchy rule:** GitHub, code and charts never go in the hero. They sit in Chapter IV as the method toolkit.
- **Institutional accuracy:** the PhD is *from Texas A&M (LAUP)*. HRRC is the research center where he works. Never write "PhD from HRRC".

---

## 2. Verified facts (single source of truth = `Anwar_CV_Fellow.pdf`, 5 pp.)

The CV is at `C:\Haider Files\TAMU Study\Job Search Network Writing Articles and CV\Post Doc and Teaching\Harvard\HUCE Environmental Fellow\Anwar_CV_Fellow.pdf` (also in `...\Mahindra Humanities Center Postdoc\` and, as a near-identical copy, in `...\Princeton\HMEI Environmental Fellow\`). The full extracted text is in Appendix A.

### Key facts and how to phrase them
- **PhD:** "defended October 2026; conferral May 2027" (the CV's words). His research statement gives the defense date as **13 October 2026**. "Dr." is used in the brief, so keep it, but anywhere a degree date shows, say "PhD defended October 2026 (conferral May 2027)".
- **Dissertation:** *When the Whole Community Shows Up: The Perspectives of Emergency Managers Dealing with Volunteers in Post-Disaster Search and Rescue.* Advisor Dr. Michelle Meyer. 26 interviews (his statements say **26 interviews with 39 emergency managers**) in Texas, North Carolina, Florida and Louisiana. PRISMA review and Atlas.ti coding.
  - Core finding (from his statements, use it): formal systems set *conditions* volunteers must meet rather than building *pathways* to use the social capital that already exists. Institutional affiliation routinely stands in for demonstrated competence. Reform: credential and train volunteers before a disaster instead of sorting them by affiliation during one. Volunteers welcomed while lives hang in the balance can be sidelined, with the same skills, once the urgency passes.
  - ⚠ **Method label inconsistency:** the ISA 2025 abstract says "grounded theory". The Columbia personal history says "descriptive phenomenology". Ask Haider which label to use on the site.
- Graduate Certificate in Environmental Hazard Management (2026).
- **MA in International Relations, with Distinction**, CEU Budapest, 2019. Thesis "Securitized Migration: The Puzzle of Deterring Migration Through Development Aid". Advisor Dr. Andrew Xiang Li.
- Graduate Certificate in Global Studies and International Relations, Northeastern University, 2018.
- **B.Sc. (Hons.) Political Science, LUMS, 2015**. Thesis "Analysis of the Unrest in Baluchistan (Province of Pakistan): Causes and Solutions". ⚠ The brief says only "B.Sc. Hons., LUMS". The discipline is Political Science (CV). Memory notes say "economics and IR". Use the CV.
- Awards: LAUP Graduate Tuition Award 2021–2026; CEU Master's Tuition Award 2018–2019.

### Experience (CV order)
1. **Research Associate, HRRC, Texas A&M**, Sep 2021–present (College Station/Remote). Dissertation research. NSF Texas Fire-Project: qualitative analysis of emergency managers from 9 Texas locations for the state wildfire preparedness plan (est. $199,000 grant). 2024 Texas Panhandle Wildfire: ArcGIS StoryMaps and qualitative analysis for healthcare emergency planning. Caldor, California wildfire proposal with PI Dr. Tara Goddard: evacuation and accessibility for people with disabilities and limited mobility. NIST Lumberton, NC: 250+ household and business survey interviews, analysis and publication. Mayfield, KY: technical assistance on a $5.2M CDBG-DR fund after the 2021 tornadoes. Coordinated a team of 6 and supervised 3 researchers for the workshop "Safeguarding Texas's Inland Rural Heritage: Collaborative Strategies for Resilience Against Natural Hazards". CARC 601 guest lecture. Camp DASH mentoring.
2. **Senior Research Analyst, Watershed Protection Department, City of Austin**, Jun 2023–Apr 2024. Rain to River strategy team: embedded emergency preparedness, HMA and social equity metrics in the strategic alignment of the city's $28M+ FEMA and HUD portfolio (2023–24). Led the grant assessment for $100,000 in resilience mini-grants. Surveys, focus groups and best-practice reports on equity in flood adaptation, especially ecological restoration after home buyouts in Onion Creek. (LinkedIn: Austin City Council adopted Rain to River in May 2026.)
3. **Senior Research Associate, WWF-Pakistan**, Lahore, Feb–Aug 2021. Led nationwide stakeholder workshops in four provinces for NbS flood-risk work under "Recharge Pakistan" (GCF). Focus groups with flood-affected communities for a CBDRM report on preparedness and early warning.
4. **Full-time Program Management Intern, UNDRR**, New York, Nov 2019–May 2020. Analyses of UNGA resolutions (70th–74th) supporting the Sendai Framework. Disaster-risk progress in 26 Voluntary National Reports (VNRs) for the 5th UN Conference on LDCs. Tracked DRR in Financing for Development: an internal UN report mapping public-private preparedness and response funds. ⚠ The memory profile says "Trainee 2021–2023". **The CV dates (Nov 2019–May 2020) win.**
5. Research Associate, Fintech Centre, ITU Lahore, May–Sep 2017: 40+ interviews on women's financial inclusion.
6. Research Assistant, CDPR Lahore, Feb–Dec 2016: database of 130,000+ cottage and small industrial units for the IGC report on spatial analysis of small and cottage industries in Punjab.
7. Assistant Project Officer, PILDAT, Dec 2015–Feb 2016: Federal Governance Scorecard 2013–2014.

### ⚠ Recharge Pakistan figures: must be resolved with Haider before publishing
- The CV and brief say "$150M ... reforesting 35,000 acres, recharging 120+ basins, 680,000 direct / 7M indirect".
- The Green Climate Fund record (FP207, approved 13 Jul 2023): **total US$77.8M (GCF US$66M grant + co-finance)**. Targets: restore **14,215 ha** (≈35,100 acres) and develop **127 recharge basins/retention areas**. Beneficiaries **687,336 direct / 7,024,361 indirect**. WWF 2025 fact sheet: project value US$72.9M, 2024–2031, Sindh, Balochistan, KP.
- So: acres and basins are **targets, not achieved results**; the beneficiaries match. The $150M has no public source found (it may be the concept-stage figure).
- **Safe default copy until he confirms:** "the Green Climate Fund's Recharge Pakistan programme (US$77.8M), which aims to restore about 35,000 acres of forest and wetland, build 127 recharge basins and reach 680,000 people directly and 7 million indirectly." Sources: greenclimate.fund/projects/fp207; WWF FP207 funding proposal PDF.

### Publications (exact)
- **NIST SP 1230-5 (2024):** Meyer, M., Duenas-Osorio, L., Dillard, M., & Sutley, E. (Eds.). *The Lumberton, North Carolina flood of 2016, wave 5: Understanding recovery from sequential disasters* (NIST Special Publication 1230-5). https://doi.org/10.6028/nist.sp.1230-5. **Verified from the PDF:** Haider is a **co-author of Chapter 3** (Watson, Helgeson, Saldarriaga Gomez, **Haider Waseem Anwar**, Kruse, Ewing) and a member of the Wave 5 field team (June 2022). Summary: in-person Wave 5 field study six years after Hurricane Matthew and four after Florence, during COVID-19; household and business surveys plus interviews with utilities and city officials. Most households returned to permanent housing within 1–2 years; most businesses recovered from the hurricanes but over half were still affected by COVID-19. Present it as a NIST monograph with "Chapter 3 co-author", not as a journal article.
- **2021:** Shahid, S., & Anwar, H. W. Hospital waste management and environmental disaster risk: A case study of Lahore. Centre for Public Policy and Governance. http://digitalrepository.fccollege.edu.pk/handle/123456789/1460
- **2018:** Ibtasam, S., Razaq, L., Anwar, H. W., Mehmood, H., Shah, K., Webster, J., Kumar, N., & Anderson, R. Knowledge, Access, and Decision-Making. *Proceedings of the 1st ACM SIGCAS COMPASS '18*. https://doi.org/10.1145/3209811.3209819 (the DOI page could not be fetched; the full subtitle is unverified, so use the CV form).
- **Accepted 2026:** Anwar, H. W., & Isaba, T. Planning for Cultural Heritage Facing Disaster Risk: A Systematic Review for Hazard Mitigation Planners. *Built Heritage*. **88 publications reviewed.** Abstract (from his manuscript, his own words, OK to use): see Appendix B. Four domains: heritage as a resilience resource; limits of standard mitigation tools; institutional barriers (macro/meso/micro); assessing heritage risk (exposure, vulnerability, local knowledge, multi-criteria). Implications: plan to use heritage as an asset, build administrative connections, plan for inclusivity, plan with the right tools.
- **Under review 2026:** Khoso, S., Abdullah, G. M. S., Muhammad, G., Zahid, M., Anwar, H. W., Ansari, A. A., & Kennedy, C. Shear modulus and damping ratio of Niger Delta clays: Experimental and predictive modeling insights for seismic risk mitigation. *Soil Dynamics and Earthquake Engineering*.
- **In progress:** Anwar, Meyer, Purdum, Eutsler, Breen, Nolan. "Challenges and Opportunities in Incorporating Volunteers in Flood Rescue Operations: Perspectives of Emergency Managers (EMs)". Also a systematic review, "Artificial Intelligence (AI) in Post-Disaster Emergency Management for Search and Rescue Operations". Early finding from his statement: most AI tools are tested in simulation, almost none with the officials who must act on them. And a manuscript with **Sajid Ali (Aga Khan Rural Support Programme, AKRSP)** on living heritage and glacial flood risk in the Hunza Valley.
- **Conferences:**
  - 2025 poster, Anwar & Meyer, "Challenges and opportunities in incorporating volunteers in flood rescue: Perspectives of emergency managers", 49th Natural Hazards Research and Applications Workshop, Boulder (July).
  - 2025, Anwar, "On the Brink of Cultural Catastrophe: Why Plan for Cultural Heritage in the Context of Disaster Risk?", 5th ISA Forum of Sociology, Rabat, 8 Jul 2025, session 637.4 "Cultural Heritage and Disaster" (RC39). ⚠ **The ISA program marks this paper CANCELLED.** Write "accepted", never "presented". Full abstract in Appendix B.
  - 2025, Anwar & Meyer, "Opportunities and challenges in emergency management (EM) protocols and volunteer engagement", ISA Forum, 10 Jul 2025, 11:00, session 645.1 (listed as presented). Abstract in Appendix B. Key content: grounded theory; 26 interviews in areas flooded by Hurricane Harvey (Texas) and in North Carolina; challenges (coordination, communication breakdown, liability, training, resource allocation, social media); opportunities (early mobilization, technology, volunteers' resources, empathy). EMs see volunteers as a resource rather than professionals, except organized groups such as the Cajun Navy.
- **Peer reviewer:** Australian Journal of Emergency Management (AJEM); International Journal of Emergency Services (IJES); Safety Science.
- **Acknowledged in:** Jenne, Popovic & Siroky (2026), *Clients, Rivals, and Rogues* (Cambridge); Aldrich (2019), "Challenges to Coordination", IJDRS 10, 306–316.

### Teaching, mentoring, service
- CARC 601 Foundations of Research in Planning and Design, guest lecture, virtual, **1 Sep 2026**, hosted by Dr. Michelle Meyer. He walked students from PRISMA review to Atlas.ti coding and had them apply it to a disaster-risk question of their own.
- Camp DASH (Disaster and Spatial Health), Texas A&M, **21–24 Jul 2026**: co-led experiential learning on disaster science, air quality and hazard mitigation planning for high-school students.
- Research supervision (Aggie Collab volunteers): **Yoonjeong Kang** (Master's), **Gianna Fernandes**, **Maika Tanski** (Bachelor's).
- Student Committee PhD Representative, HRRC, 2022–23. Class Representative, CEU MA IR, 2018–19.
- Volunteer, 2023 Natural Hazards Workshop, Boulder. Director of Logistics and Registration, LUMS Music Festival 2013 and 2014 (~300 participants); LUMS Music Society 2011–15.
- Teaching philosophy (BU statement, usable): build each course around one applied project tied to a real place and partner; scaffolded low-stakes assignments; post materials early; mid-semester feedback; students may use AI if they disclose how and verify every output; students leave with a coded dataset, a map or a co-authored product. Courses prepared: Environmental Planning and Climate Resilience; Land Use and Managed Retreat; Housing and Community Development after Disasters; Community-Engaged Research Methods. Sample syllabi exist ("Heritage at Risk", "Living Heritage", "Social Justice and the Built Environment") in his application folders.

### Rural Heritage Resilience Workshop 2026
- Held **26–27 October 2026**, Texas A&M, College Station. HRRC with the Center for Heritage Conservation. A year-long team effort. Keynotes **David Preziosi** and **William Dupont**. A third slot was left TBA after Sandra Fatorić withdrew; don't name her. Panel 1, "What's at Risk?": Elyse Zavar, Sam Collins III, Jeff Fugate, Dan Valenzuela. Speaker Andrew Rumbach (Urban Institute).
- His takeaways (LinkedIn, his words, paraphrase OK): emergency managers must build historic preservation into planning rather than treat it as an afterthought; the table is still too small; rural communities should define what "value" means for their heritage; funding must be layered (federal, state, philanthropic, community); leadership must be in place before disaster to rebuild better.
- Texas figures he shared are **Andrew Rumbach's cursory analysis**: 68% of mapped rural historic districts in the 100-year floodplain; 22% of rural National Register listings at moderate-to-high wildfire risk; 2 of 47 local HMPs with dedicated preservation actions. If used, attribute them to Rumbach.

### Gilgit-Baltistan / GLOF research agenda (from his 2027–28 fellowship proposals; he is the author)
Use it for Chapter I and the Field Notes post. **Do not mention which fellowships he applied to.**
- Living heritage in Hunza is practice as much as monument: irrigation channels (*Goczil*) built and kept by *Rajaki* communal labour; seasonal communal sheds (*Haraagh*) on high pastures; Burushaski and Wakhi oral histories tying shrines and landmarks to grazing rights and boundaries; reverence for glaciers and pastures; Wakhi women leading herds to high pastures in Shimshal, a practice recorded as ending. Unlike the restored Baltit and Altit forts, these practices rarely enter risk or damage assessments.
- UNDP GLOF-II (verified): **3,044 glacial lakes** in GB and KP, **33 prone to GLOF**, **7.1 million people vulnerable**.
- Hassanabad: a surging glacier (Shishper) dammed a lake that burst five times between 2019 and 2022; the 2021 flood displaced about 20 of 170 households (Bhambri et al. 2020; Shahid 2024).
- Thesis: **heritage is lost twice**, when floods displace people from the places that hold it, and when adaptation (relocation) moves them away. A "slow violence" (Nixon 2011) that damage assessments don't record.
- Questions: how plans define loss and where living heritage falls out; how displacement changes place dependence and identity; how heritage anchors boundaries, grazing rights and collective response.
- Methods: argumentative discourse analysis (Hajer) of GLOF-II documents, GB Disaster Management Authority plans, Pakistan's 2023 NAP and PDNAs; documentary heritage (photo essays, films); oral histories and walking interviews in two valleys (Hassanabad in Hunza and a Ghizer village as candidates); interviews in Urdu; member checking; a bilingual (English–Urdu) story map. Positionality: he is from Lahore, not GB, and works through AKRSP.

### Other perspectives worth using (his words, paraphrased)
- "Wherever I have worked, communities arrive with knowledge, labour and trust, and a formal system decides within hours how much of it to accept." (personal history)
- "I judge a resilience plan by what happens on the ground after it is adopted." Three questions everywhere: who is at the table, who carries the remaining risk, whose knowledge counts. (BU personal statement)
- AI is the newest outside help at the same decision point as volunteers. If emergency managers judge AI as they judge volunteers, by affiliation rather than performance, agencies adopt the best-connected tools, not the best-validated. (personal history)
- Postdoc direction ideas: social capital and displacement/managed retreat; equitable buyouts (Onion Creek comparison); recovery housing (CDBG-DR); heritage in coastal resilience plans.

### Contact, links, identity
- Email: **anwar_haider@tamu.edu** (primary, per brief). Personal Gmail exists; do not publish it.
- LinkedIn: https://www.linkedin.com/in/haideranwar/ (headline "Disaster Risk Reduction (DRR) | Emergency Preparedness and Response | Climate Adaptation"; location Washington, DC; He/Him).
- GitHub lab (Chapter IV only): https://hanwar3.github.io/AI-Projects-and-Data-Analysis/?v=4#hma; repo https://github.com/hanwar3/AI-Projects-and-Data-Analysis
- The CV lists phone +1-979-326-8274 and "Reston, VA 20191". **Decision: do not publish the phone number or street area on the site** unless Haider asks. Use "Washington, DC area".
- Languages: English, Urdu, Punjabi.
- Certificates (2025–26): DeepLearning.AI AI Python for Beginners and Agentic AI; U. Michigan Statistics with Python; Google Advanced Data Analytics; Coursera Geospatial Foundations & Python Tooling; Vanderbilt Agentic AI and AI Agents for Leaders; CITI Research Ethics; World Bank Intro to Disaster Risk Finance Analytics (2020); CEU BOOST certificate. Skip credential IDs on the site.

### GitHub lab content (for Chapter IV cards)
Meta: "Disaster data, analysed and mapped, with tools I built using agentic AI." Built with Claude Code as an agentic pair programmer: he set the question, data and checks; the agent wrote and ran the code; he reviewed the results.
1. `#hma` **Federal hazard mitigation grants, FY2015–2024.** OpenFEMA HMA Projects v4 (56,410 records, pulled 3 Oct 2026), sample of **7,781** approved physical projects. **$7.83B** federal share; FL, TX, LA, CA and PR got 53%. χ²(10)=1,970, Cramér's V=0.36. **BRIC/PDM awards ≈ twice HMGP for the same project type, region and year: +96% (95% CI +67 to +130; state-clustered p=0.001).** Methods: χ², Welch ANOVA, Kruskal–Wallis, OLS on log award with HC3 and state-clustered errors. Stated limit: grant records, not outcomes.
2. `#earthquakes` Pakistan earthquakes, origin vs impact. USGS ComCat 12,715 events M≥2.5 (1902–2025), ShakeMaps for 309 events. 98.4% of Pakistan felt ≥MMI IV since 2000; Lahore's strongest shaking came from a rupture 340 km away.
3. `#texas` Texas NFIP claims 2000–2025: 272,924 claims, $16.0B paid, with TerraClimate.
4. `#floods` Pakistan floods 2010 and 2022 on 30 m terrain (Copernicus GLO-30). Tools: rasterio, GeoPandas, QGIS.
5. `#climate` Pakistan temperature × rainfall (TerraClimate 2000–2021, bivariate).
6. `#rfp` RFP Monitor (17 procurement portals, Streamlit). 7. `#jobhunt` (skip on the academic site; it is a personal job-search tool).
- ⚠ The brief says "30m DEM ... (Python, xarray, Rasterio, GeoPandas)". The lab's 30 m work is the **floods** project (rasterio, GeoPandas). xarray belongs to the climate maps. Write the card accurately.
- ⚠ The brief's third card, "Agentic AI & Machine Learning in Post-Disaster SAR", is not a lab project. It is his **in-progress systematic review** plus the agentic tools. Card wording: link the review description (Ch. II) and the lab's agentic-tools section, without implying a built SAR model.
- Lab images (in the repo, `assets/img/`): `hma-states.png`, `hma-regression.png`, `hma-crosstab.png`, `hma-award-size.png`, `pakistan-floods(-sm).jpg`, `pakistan-shaking(-sm).jpg`, `pakistan-earthquakes`, `pakistan-climate`, `texas-flood-nfip`, `texas-climate`, diagrams. His own work, so OK to reuse as thumbnails. Note: the floods map uses a neon-on-dark style that clashes with this site, so show it small, inside a limestone mat. Clone: `git clone --depth 1 https://github.com/hanwar3/AI-Projects-and-Data-Analysis.git`.

---

## 3. Photos available (on his computer)

- `...\headshots\Best.jpeg` (2793×2240, studio, pale blue background, brown jacket, navy shirt).
- `...\CV\Website Process\No background.png`: the same portrait, **cut out (RGBA)**. Edges are clean on limestone and show a slight halo on slate. **Use it on light backgrounds only.**
- `...\headshots\52800253531_...jpeg`, `52800690363_...jpeg`, `Website Process\37203.jpeg`, `37204.jpeg`: environmental portrait (4000×2668), tan blazer, campus building interior. **Recommended for the About/Profile band** because it is warmer and less corporate.
- `Website Process\IMG_2670.jpeg`: standing in snow in front of a domed campus building at dusk. `IMG_2634.jpeg`: Times Square. Not recommended (off-message).
- Do not use the "ChatGPT Image" or "openart" files, or the freepik vector banners in `Website Process` (AI or stock, clashes with the no-slop rule, licence issues).
- Make web versions: 1600 px long edge, WebP/AVIF plus JPEG fallback, about 200 KB.

---

## 4. Reference-site findings

- **persepolis.getty.edu** (seen in a browser): a full-bleed dark, misty, painterly landscape; **one centered serif sentence per screen** in warm off-white ("Twenty-five hundred years ago, in what is now southern Iran, stood an ancient city of awe-inspiring beauty."); a small "Getty" wordmark top center; round settings and sound buttons top left; a pill-shaped scroll cue with "Scroll to continue"; the scene slowly reveals architecture as you scroll. Takeaway: one sentence per screen, slow cross-fades, an atmospheric field rather than cards.
- **theacademicdesigner.com 2023 winners**: judges scored Content, Design and Organization, About You, Portfolio, Contact. Praised: personality, simple navigation, headings and drop-downs for skimmers, overview-to-detail research pages, CV and PDF downloads, abstracts (and non-specialist abstracts), real photos, a contact page that doubles as a media kit, an offer to speak, "show why you care". Warning: one-page sites can overwhelm, so tell the story in order.
- **awwwards World Zoom (RSPCA)**: blocked by robots, not seen. Implement scale change as a deliberate map zoom (world → basin → city) in the Chapter III switcher.
- **YouTube anti-slop video**: not viewable from the tools. The brief's own summary is authoritative.

---

## 5. Design system (locked)

### Tokens (from the Project instructions)
```css
:root{
  --bg-primary:#FAF7F2;        /* warm archival limestone */
  --bg-elevated:#F2ECE1;       /* glacial alabaster: drawers, modals, mats */
  --bg-mountain-chapter:#161D24; /* deep mountain slate: Chapter I only */
  --ink-on-slate:#F5F2EB;      /* parchment text on slate */
  --ink-primary:#18181B;
  --ink-secondary:#57534E;
  --accent-heritage:#B45309;   /* terracotta ochre: heritage, fieldwork, highlights */
  --accent-watershed:#0F766E;  /* Indus teal: water, GLOF, spatial, interactive controls */
  --teal-on-slate:#58B8AC;     /* derived: teal legible on slate (used in previews) */
  --grid-hairline:1px solid rgba(24,24,27,.12);
  --font-display:"Newsreader", "Iowan Old Style", Georgia, serif;
  --font-body:"Source Sans 3", "Segoe UI", system-ui, sans-serif;
  --font-mono:"JetBrains Mono", ui-monospace, Consolas, monospace;
}
```
- Contrast to check: `#B45309` on `#FAF7F2` ≈ 4.9:1 (AA for body text). `#0F766E` on `#FAF7F2` ≈ 5.3:1. `#57534E` on `#FAF7F2` ≈ 7.3:1. Re-verify in the audit.
- **Single theme by choice.** The site commits to its palette and does not invert for dark mode. Chapter I is dark by design.

### Typography decisions
- **Newsreader** (variable, `opsz` + `wght`, 200–800) for display. It was chosen over Cormorant Garamond because its optical-size axis keeps small headings sturdy and Cormorant gets spindly below 24 px. Weights 500–600, tracking −0.02em on large sizes, `text-wrap: balance`.
- **Source Sans 3** (variable, 200–900) for body, line-height 1.65, measure 65ch. Chosen over Plus Jakarta Sans: more neutral, better for long academic prose.
- **JetBrains Mono** with `tabular-nums` **only** for real data: elevations, coordinates, grant totals, citations and DOIs, dates in lists. Not for decorative labels.
- Self-host: npm `@fontsource-variable/newsreader`, `source-sans-3`, `jetbrains-mono`. Files: `newsreader-latin-opsz-normal.woff2` (132 KB), `-italic` (147 KB), `source-sans-3-latin-wght-normal.woff2` (29 KB), `-italic` (28 KB), `jetbrains-mono-latin-wght-normal.woff2` (40 KB). All OFL. Preload Newsreader normal and Source Sans normal. `font-display: swap`. Note the family names in the fontsource CSS are "Newsreader Variable" etc.; set your own `@font-face` names.

### Anti-slop rules (brief + design guidance)
Banned: purple/indigo gradients, neon dark mode, 3-column frosted-glass cards, skill bars, typing effects, "delve / tapestry / testament / cutting-edge / synergy", emoji section markers.
Also avoid: identical rounded cards everywhere, the same soft shadow on everything, ALL-CAPS tracked eyebrows over every heading, "A · B · C" middle-dot meta strings, arrows tacked onto every link, fade-and-slide-up on every section, centered everything, accenting one word in a headline. Numbered markers only where content is a real sequence. The chapters I–V are a real sequence (elevation and disaster cycle), so Roman numerals are fine there only.
- Known tension: cream + serif + terracotta is itself a common generated look, but the brief mandates the palette, so **the brief wins**. Counter it by spending all boldness on **one element: the computed contour terrain** (§6). Keep everything else quiet: real photos, hairline grid, text-led layouts, no card grids.
- The brief's bracketed button labels ("[ Explore the Journey ↓ ]") show intent. Render them as plain editorial buttons: "Explore the journey", "Download CV (PDF)", "Book a meeting".
- Haider's own taste (memory): no card, dice or gambling motifs; prefers plain, functional layouts over illustrated ones; dislikes boxed or card layouts with visible box edges; likes depth and shading, pertinent photo backgrounds, and motion used for storytelling, not busy motion. LinkedIn writing taste: human and grounded, with the research angle emerging after the human situation.
- Copy voice: a sharp human scholar (New Yorker / Getty Publications), active voice, short sentences, no em-dash asides, no "not X but Y" constructions.

### Motion
- One orchestrated system: the terrain pans and the elevation readout updates with scroll. Chapter text cross-fades in (from a visible resting state; nothing waits at opacity 0 for an observer).
- `prefers-reduced-motion`: the terrain is static (each chapter shows its own still slice), no pans or cross-fades, instant scroll-to.
- IntersectionObserver plus `requestAnimationFrame`. No GSAP needed.

---

## 6. Signature element: the computed terrain (built)

- `tools/terrain.py` generates a **fictional** topographic transect, 1000 × 7000 units, from a glaciated head (summits to about 7,500 m) down a river to a delta and the sea. **It is not a map of Gilgit-Baltistan.** The site must say so in a small caption or the colophon ("A computed landscape, not a survey of a real place"). Real places appear only on the real maps (§7).
- Drawn as **illuminated contours (Tanaka Kitiro, 1950)**: each contour segment carries an illumination class 0–4 for light from the north-west. On slate, lit segments are brighter and thicker. On limestone, shadowed segments are darker and thicker. This gives relief from line alone.
- An earlier raster hillshade (`relief.webp`, 537 KB) was **tried and rejected**: banding on the gentle slopes, too heavy, and it looked like a texture. Removed.
- Features: a glacier with medial moraines (on ice, contours are teal); a **glacial lake at exactly 3,500 m held behind a moraine dam** (the GLOF motif: Chapter I's anchor); a gorge; carved tributaries (contours V upstream); braided piedmont reach; sine-generated meanders (Langbein & Leopold); natural levee; delta distributaries; coast (0 m) and dashed bathymetry. Index contours every 500 m, regular every 100 m, supplementary 10–450 m in the lowland.
- Long profile of the river (y → elevation): 0→5,350 · 650→4,350 · 1,250→3,590 · 1,330–1,470→3,500 (lake) · 1,560→3,440 · 2,700→1,500 · 3,900→500 · 4,900→150 · 5,700→30 · 6,050→0 · 7,000→−90. **Chapter anchors:** Ch I at y≈1,400 (3,500 m, lake). Ch II y≈2,700 (1,500 m). Ch III y≈3,900 (500 m). Ch IV y≈4,900 (≈150 m, the floodplain "lab"). Ch V y≈6,050 (0 m, the coast, "Global Agora"). The `prof` array gives elevation every 20 units for the live readout.
- Last run output: 166 lines, 10,457 points, 17 river parts, 9 tributaries, 15 contour labels, 2 spot heights; z −234…7,551; mouth at y≈6,350. `terrain.js` 96.9 KB (30 KB gzipped). Seed 1991 (deterministic).
- **Data format** (`window.__TERRAIN__`): `w,h,q(=2)`; `lines: [z, kind(+"g" if on ice), yMin, yMax, packed, shadeString]`, kind `i` index | `r` regular | `s` supplementary | `c` coast | `b` bathymetry. `packed` = half-unit integers, first point absolute, then deltas `[x0,y0,dx1,dy1,…]`. `shadeString` holds one digit 0–4 per segment. `river: [kind, yMin, yMax, packed]` with kind `main|braid|dist|trib`. Also `glacier[]`, `moraines[]`, `lake[]` (packed), `lakeC`, `mouthY`, `labels[{x,y,a,z}]`, `peaks[{x,y,z}]`, `profStep`, `prof[]`, `riverX[]`. Decode: `cumsum(deltas)/q`.
- Renderer plan (not written): one fixed full-viewport `<canvas>` behind the content, DPR-aware. Scale terrain width to the viewport (on mobile, crop around `riverX` so the river stays in view). Translate y by scroll mapped piecewise so each chapter's anchor y sits under its chapter. Cull by `yMin/yMax`. Batch strokes by (kind, shade) into Path2D per tile. Background goes slate → limestone across y≈1,700–2,100, and the contour ink flips at the same time. Draw labels in JetBrains Mono with a knock-out halo. Expect about 60 fps on mid phones, since tiles are cached as offscreen bitmaps. Fallback when there is no JS: a static SVG poster of the Chapter I slice.
- Side **elevation indicator**: a fixed vertical scale with the five chapter stops `3,500 m Karakoram / GLOF heritage` → `1,500 m Acute SAR & wildfires` → `500 m Basin recovery & policy` → `150 m Methods lab` → `0 m Scholarly agora`. The live readout is `prof[]` at the current scroll anchor. Each stop is a link (keyboard focusable, `aria-current`).
- Preview helper: `tools/terrain_preview.py` writes a 4-panel PNG (matplotlib).

## 7. Real maps (built, `tools/maps.mjs` → `assets/maps/*.svg`)

Data: Natural Earth (public domain) via npm `world-atlas`, `us-atlas`, and GeoJSON from `github.com/nvkelso/natural-earth-vector` (`ne_10m_rivers_lake_centerlines`, `ne_10m_glaciated_areas`), downloaded into `build/ne/`. Projection via `d3-geo`, simplification and clipping via `mapshaper`.
- **Key decision: no international or provincial boundaries are drawn in South Asia** (disputed Kashmir and the GB boundary). The Pakistan plates show coast, rivers and glaciers only, with province names as text labels.
- `world.svg` (98 KB; Equal Earth, graticule, NYC marker "United Nations, New York", extent boxes for the Indus and the US South). Use it in Ch III "Global".
- `indus.svg` (27 KB; Indus + Jhelum, Chenab, Ravi, Sutlej, Beas; glaciers; labels KP, Punjab, Balochistan, Sindh, Arabian Sea, Karakoram; Lahore marker). Ch III "National / WWF".
- `us-interviews.svg` (9 KB; TX, LA, FL, NC hatched). Ch II.
- `us-recovery.svg` (9 KB; Austin, Mayfield, Lumberton markers; TX, KY, NC hatched). Ch III "Municipal".
- `texas.svg` (1 KB; College Station). Ch III "Heritage".
- `karakoram.svg` (22 KB; upper Indus, glaciers, Hunza, Gilgit, Skardu). Ch I.
- `locator.svg` (7 KB; tiny world with dots). Optional.
- The SVGs use classes, so style them in site CSS (see `maps_check.html` CSS in Appendix C). `world.svg` can be trimmed further, by simplifying more or dropping the graticule.

---

## 8. Site architecture (planned)

```
site/
  index.html              # journey + all academic content (semantic, works without JS)
  cv/Anwar_CV.pdf         # copy of Anwar_CV_Fellow.pdf (ask Haider for a public version without phone/address)
  assets/
    css/site.css
    js/terrain.js         # generated data
    js/journey.js         # canvas renderer, elevation rail, chapter observer
    js/app.js             # publications copy/expand, scale switcher, meeting drawer, blog loader, reader modal
    fonts/*.woff2
    maps/*.svg
    img/ (portraits, lab thumbnails)
  content/
    publications.json     # one record per item: type, year, authors, title, venue, doi/url, status, abstract, takeaway, bibtex
    posts/*.md            # blog posts with YAML front matter (title, date, category, summary, readingTime auto)
    posts.json            # index generated at build (or by the CMS)
  admin/
    index.html            # Sveltia CMS (Decap-compatible)
    config.yml
  feed.xml                # RSS of Field Notes (generated)
  tools/ terrain.py terrain_preview.py maps.mjs shot.mjs build-posts.mjs
  404.html  robots.txt  sitemap.xml  _headers (Cloudflare)  CNAME (if GitHub Pages)
  DEPLOY.md  README.md
```
- Plain HTML, CSS and vanilla JS, no framework. A tiny Node build script (`build-posts.mjs`) turns `content/posts/*.md` into `posts.json` and `feed.xml`, and pre-renders post HTML into the page. Cloudflare Pages build command `node tools/build-posts.mjs`, output dir `site`.
- **Persistent top nav** (Project instructions): `Profile` • `Scroll Journey` • `Policy Impact` • `Publications` • `Field Notes Blog` • `Methods Lab` • `CV & Book a Meeting`. Collapses to a menu button under about 900 px. Skip link. CV download always visible.

### Chapters
- **I · 3,500 m · The living mountain & intangible heritage (hero, slate).** Name, "PhD, Urban and Regional Sciences, Texas A&M University", "Research Associate, Hazard Reduction & Recovery Center". Thesis: *"When landscapes fracture, how do communities, emergency responders, and living cultures endure?"* Buttons: Explore the journey · Download CV (PDF) · Book a meeting. Then one-sentence screens: heritage lost twice; Goczil, Rajaki, Haraagh; the 3,044 / 33 / 7.1M figures (UNDP); a link to `karakoram.svg`. Profile band (light): environmental portrait, short bio, education line (TAMU PhD · CEU MA with Distinction · LUMS B.Sc. Hons.). Keep the hero's first frame complete at rest.
- **II · 1,500 m · "When the whole community shows up".** Dissertation, 26 interviews / 39 EMs, the four states (`us-interviews.svg`), the conditions-vs-pathways finding, ICS/EOC, the AI-in-SAR review, NSF Texas Fire-Project, 2024 Panhandle wildfire StoryMaps, Caldor accessibility proposal.
- **III · 500 m · The floodplain & equitable recovery: scale switcher.** Tabs with a zoom transition (world → basin → US → Texas), ARIA tablist, arrow keys: (1) Global, UNDRR; (2) National, WWF Recharge Pakistan (use the corrected figures, §2); (3) Municipal & community: Austin Rain to River $28M+, $100K mini-grants, Onion Creek, Mayfield $5.2M CDBG-DR, Lumberton NIST 250+ surveys; (4) Heritage: Texas rural heritage workshop, Built Heritage review, link to GB work.
- **IV · 150 m · The methodological engine.** Fieldwork first (Atlas.ti, PRISMA, 275+ interviews and surveys = 26 + 250, discourse analysis, focus groups, StoryMaps). Then archival-style "plates" (not tech cards: a matted thumbnail, caption, data source, one finding) linking to the GitHub lab: HMA $7.83B / 7,781 / +96%; Pakistan floods on 30 m terrain; AI in SAR review + agentic tools.
- **V · 0 m · The scholarly agora.** Publications (categories per brief; expandable abstract and policy takeaway; Copy BibTeX / Copy APA with `navigator.clipboard` and a visible "Copied" state; DOI links); Field Notes; Teaching, mentoring & service; Contact and meeting.
- Footer/colophon: terrain disclaimer, data credits (Natural Earth; fonts OFL), last updated.

### Field Notes blog
- Categories: *Gilgit-Baltistan & GLOFs*, *Intangible Heritage*, *Emergency Management & SAR*, *Policy & Methods*. Filter chips (buttons with `aria-pressed`), reading time (words/230), a slide-over reader modal (focus trap, Esc closes, `#post-slug` hash for deep links, share buttons for LinkedIn (`https://www.linkedin.com/sharing/share-offsite/?url=`) and copy link).
- Starter posts (write in his voice, from facts in §2, and label them drafts for his review): "Safeguarding living heritage against GLOFs in Gilgit-Baltistan"; "When the whole community shows up: lessons from 26 emergency managers"; optionally "Who sits at the table: notes from the Rural Heritage Resilience Workshop". Each about 700–900 words, with sources.
- Optional Substack/Medium RSS: fetch at build time in `build-posts.mjs` (no client-side CORS).

### Meeting drawer and contact
- Topic radio group: Research collaboration / Policy or consulting inquiry / Speaking or workshop invitation / Media or student advising. Name, email, organisation, proposed times (2 datetime fields), message, honeypot.
- Submit → Web3Forms `POST https://api.web3forms.com/submit` with `access_key` (public by design; Haider creates it at web3forms.com using anwar_haider@tamu.edu; free plan 250 submissions/month). A plain-language success or error state. A "Prefer email?" link builds a `mailto:anwar_haider@tamu.edu?subject=…&body=…` from the form, and the address is shown as text.
- "Pick a time" opens a Cal.com embed **only if** Haider supplies a booking link. Leave `CAL_LINK = ""` in config, and hide the button while it is empty. **Ask him.**

---

## 9. Hosting, CMS, domain (research done)

- **Recommended host: Cloudflare Pages** (free, unlimited bandwidth, Functions if needed). Alternatives: Vercel Hobby, GitHub Pages.
- **CMS: Sveltia CMS** at `/admin` with the GitHub backend and **Personal Access Token sign-in**: no OAuth proxy, $0. It is Decap-compatible (same `config.yml`; swap the script tag to use Decap). Script: `https://unpkg.com/@sveltia/cms/dist/sveltia-cms.js` (pin a version). Token: GitHub fine-grained PAT scoped to the site repo, Contents read/write. Trade-off: the token lives in his browser's localStorage.
  - Decap alternative needs an OAuth proxy: a Cloudflare Pages Function at `functions/api/auth.js` or the `sveltia-cms-auth` Worker, with `base_url` in config. Document both in `DEPLOY.md`.
  - Collections: `posts` (folder `site/content/posts`, fields title, date, category (select of 4), summary, body markdown, draft bool); `publications` (file `site/content/publications.json`). Media folder `site/assets/img/uploads`.
- **Forms:** Web3Forms free (250/month). Formspree free is 50/month (fallback).
- **Free domain:** GitHub Student Developer Pack (verify with anwar_haider@tamu.edu while still enrolled; conferral is May 2027): Namecheap free `.me` for 1 year with SSL; get.tech `.tech`; Name.com options. Renewals cost money afterwards. ⚠ He has defended, so eligibility depends on enrollment status. Otherwise use the free `*.pages.dev` / `*.vercel.app` subdomain, or buy a `.com` at about $10/yr. `is-a.dev` is a free alternative via a GitHub PR.
- `DEPLOY.md` must include: a 5-minute checklist (create a GitHub repo → push → Cloudflare Pages → connect repo → build settings → deploy); custom domain DNS; Web3Forms key; Sveltia PAT setup; how to publish a post in minutes; how to rerun `terrain.py` and `maps.mjs`.

---

## 10. Environment notes for Claude Code

- Node 22, Python 3.13 with numpy, scipy, scikit-image, matplotlib, Pillow. npm deps (`package.json` in Appendix C): `@fontsource-variable/newsreader`, `@fontsource-variable/source-sans-3`, `@fontsource-variable/jetbrains-mono`, `d3-geo`, `d3-geo-projection`, `topojson-client`, `topojson-simplify`, `world-atlas`, `us-atlas`, `mapshaper`. `maps.mjs` also needs `ne/ne_10m_rivers_lake_centerlines.geojson` and `ne/ne_10m_glaciated_areas.geojson` from the natural-earth-vector repo (raw.githubusercontent.com).
- Screenshots: Playwright + Chrome (`tools/shot.mjs`; adjust the import path, which was `/opt/npm-tools/...` in the chat sandbox, to a local `npm i -D playwright` and use `npx playwright install chromium`).
- **The chat sandbox's build folder is not on Haider's computer.** The code is reproduced in Appendix C. Re-create `tools/` from it, run `python3 tools/terrain.py site/assets/js` and `node tools/maps.mjs` (change `OUT`), and re-download the NE files.
- Working folder Haider connected: `C:\Haider Files\TAMU Study\Job Search Network Writing Articles and CV` (CV, statements, headshots). Suggest a new repo folder for the site, e.g. `C:\Haider Files\Website\anwar-site`.
- Commit attribution, if committing on his behalf: end messages with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## 11. Gauntlet audit checklist (run before delivering)

1. Hierarchy: scholar first; no code in the hero; GitHub only in Ch IV.
2. Every number traced to §2 (CV or the cited source). Recharge figures corrected. ISA paper "accepted", not "presented". NIST described as Chapter 3 co-authorship. The UNDRR dates are the CV's.
3. No banned words or tropes (§5). Read the copy aloud.
4. Screenshots at 1440, 1024, 768, 390 and 360 px. No horizontal scroll. Nav usable. Drawer and modal fit.
5. Keyboard: tab order, visible focus, Esc closes overlays, focus returns, skip link, tabs with arrow keys.
6. `prefers-reduced-motion` honoured. Content readable with JS off.
7. Contrast AA everywhere, including over the terrain (add a limestone scrim behind text if needed).
8. Links: mailto, LinkedIn, GitHub lab anchors (`#hma`, `#floods`, `#climate`), DOIs, CV PDF.
9. Lighthouse: performance ≥ 90 on mobile; fonts preloaded; images sized; terrain.js deferred.
10. Compare side by side with Persepolis (pacing, one idea per screen) and the Academic Designer criteria (CV in one click, abstracts, contact as media kit, speaking offer).

## 12. Open questions for Haider
1. Recharge Pakistan: keep "$150M" or use GCF's US$77.8M? Present acres and basins as targets?
2. Dissertation method label: grounded theory or descriptive phenomenology?
3. A public CV PDF without phone and address?
4. A Cal.com/Calendly link? A Web3Forms key (or let me document how)?
5. Domain preference (e.g. haideranwar.me) and student-pack eligibility.
6. Is the LUMS degree "Political Science" (CV) correct?
7. Use the environmental (tan blazer) portrait in the profile band?
8. Is the AKRSP manuscript with Sajid Ali OK to mention publicly?

## 13. Decisions log
- Vanilla static site; Cloudflare Pages; Sveltia CMS with PAT; Web3Forms + mailto.
- Newsreader / Source Sans 3 / JetBrains Mono, self-hosted.
- One bold element: computed Tanaka-style contour terrain; raster hillshade rejected.
- Fictional terrain for the journey, real Natural Earth maps for places; no South Asian boundaries.
- Chapter IV adds a 150 m "lab" stop and Chapter V becomes 0 m (the brief lists 500 m → Methodological Lab → 0 m Global Agora; the lab needed its own elevation).
- Photos: real portraits only; no AI or stock imagery.
- Don't publish phone, street area or personal Gmail; don't mention specific fellowship applications.


---

## 14. Source instructions, word for word

### 14.1 Original brief (attachment the user sent with the CV)

````markdown
# ROLE & OBJECTIVE: $10K INTERACTIVE ACADEMIC & HERITAGE SCROLLYTELLING WEBSITE (NO AI SLOP)

You are an award-winning Creative Director, Computational Cartographer, and Principal Frontend Architect. I want you to design and build my personal academic, policy, and research website: **Dr. Haider Waseem Anwar (Ph.D. in Urban & Regional Sciences, Texas A&M University)**.

I have attached my full CV (`Anwar_CV_Fellow.pdf`). Below are my live profile links and my gold-standard design references.

## 1. MY LINKS & CONTACT (INTEGRATE ALL OF THESE)
- **Primary Email (for meetings & direct contact):** `anwar_haider@tamu.edu`
- **LinkedIn Profile:** https://www.linkedin.com/in/haideranwar/
- **Secondary Technical/GitHub Portfolio (DO NOT put upfront—integrate later in the journey):** https://hanwar3.github.io/AI-Projects-and-Data-Analysis/?v=4#hma

## 2. GOLD-STANDARD DESIGN & WORKFLOW REFERENCES (STUDY & REVERSE-ENGINEER THESE)
1. **Immersive Cultural Heritage Scrollytelling:** https://persepolis.getty.edu/
   - *What to borrow:* Museum-grade visual storytelling, archival warmth, layered parallax depth, and scroll-triggered narrative chapters that treat cultural heritage and landscapes with reverence.
2. **Spatial Zoom & Scale Transitions:** https://www.awwwards.com/inspiration/world-zoom-rspca-animal-futures
   - *What to borrow:* Smooth spatial/elevation zoom transitions that carry the visitor from a macro environmental scale (glaciers/watersheds) down to the micro human scale (communities, emergency responders, and living heritage).
3. **Academic Authority & Usability:** https://theacademicdesigner.com/2023/winners-of-the-2023-best-personal-academic-websites-contest/
   - *What to borrow:* Uncluttered scholarly credibility, effortless access to CV/Publications/Teaching for search committees, and zero friction.
4. **Anti-AI Slop Design System & Gauntlet Loop Workflow:** https://www.youtube.com/watch?v=VwGrXe2ricE
   - *What to apply:*
     - **Kill the AI Slop Monster:** Strictly BAN generic SaaS tropes, purple/indigo-to-violet gradients, neon dark modes, generic 3-column rounded glassmorphism feature cards, fake skill progress bars, and robotic AI copy.
     - **One Screen, One Thought (System 1 Thinking):** Each viewport scroll stage must communicate ONE powerful scholarly idea that washes over the visitor effortlessly without cognitive overload.
     - **Codified Design System First:** Lock in a cohesive typographic scale, archival/topographic color palette, and motion physics before writing component code.

---

## 3. CRITICAL STRUCTURAL RULE: MY SCHOLARLY PROFILE FIRST (NOT GITHUB)
Do NOT make this look like a software developer portfolio and do NOT put my GitHub or Python/GIS charts in the hero section. 
- **First Impression:** Visitors must immediately meet me as a **Social Scientist, Disaster Risk Reduction & Recovery Scholar, and Cultural Heritage Researcher** who works with real communities, emergency managers, and fragile landscapes.
- **Where GitHub Fits:** My computational work (https://hanwar3.github.io/AI-Projects-and-Data-Analysis/?v=4#hma — FEMA $7.83B HMA grant analysis, 30m DEM climate relief maps, and Agentic AI workflows) should appear in **Chapter 4 of the scroll journey** as the *methodological toolkit* supporting my human and policy research.

---

## 4. THE INTERACTIVE SCROLL JOURNEY: "FROM THE GLACIAL ROOF TO THE WHOLE COMMUNITY"
Design the homepage as an interactive, smooth-scrolling narrative journey across **5 Elevation & Disaster-Cycle Chapters** (with a persistent, minimalist top navigation bar AND a floating elevation/chapter progress indicator on the side so academic reviewers can either enjoy the scroll journey OR click to jump straight to any section):

### CHAPTER I (Elevation 3,500m+ — The Living Mountain & Intangible Heritage): Identity & Profile Hero
- **The Thematic Hook:** Open with an atmospheric, editorial scrollytelling canvas inspired by *Persepolis Reimagined* (`https://persepolis.getty.edu/`), evoking the high-mountain watersheds of **Gilgit-Baltistan** and rural Texas—where **Glacial Lake Outburst Floods (GLOFs)**, climate displacement, and natural hazards threaten both physical vernacular heritage and **intangible living heritage** (oral traditions, indigenous coping knowledge, and community memory).
- **My Profile & Narrative:** Introduce **Haider Waseem Anwar, Ph.D.** (Doctor of Philosophy in Urban & Regional Sciences, Texas A&M University; Research Associate at the Hazard Reduction & Recovery Center [HRRC]; MA in International Relations with Distinction, Central European University; B.Sc. Hons., LUMS).
- **Core Thesis:** *"When landscapes fracture, how do communities, emergency responders, and living cultures endure?"*
- **Immediate Actions:** Clean editorial buttons for `[ Explore the Journey ↓ ]`, `[ Download Full CV (PDF) ]`, and `[ Book a Meeting / Contact ]`.

### CHAPTER II (Elevation 1,500m — The Surge & Acute Response): "When the Whole Community Shows Up"
- **The Story:** As the user scrolls, transition down the watershed into acute disaster response and Search & Rescue (SAR).
- **Spotlight Research:** My Ph.D. Dissertation (*"When the Whole Community Shows Up: The Perspectives of Emergency Managers Dealing with Volunteers in Post-Disaster Search and Rescue"*, advised by Dr. Michelle Meyer) and my research on integrating spontaneous volunteers and AI into Incident Command Systems (ICS) and Emergency Operations Centers (EOC) across Texas, North Carolina, Florida, and Louisiana, alongside healthcare emergency planning for the 2024 Texas Panhandle Wildfire and evacuation accessibility for people with disabilities (Caldor Wildfire).

### CHAPTER III (Elevation 500m — The Floodplain & Equitable Recovery): Global-to-Municipal Policy Impact
- **The Story:** Scroll into the river basin where global disaster financing meets local recovery and cultural preservation.
- **Interactive Scale Switcher (inspired by World Zoom):** Let visitors toggle or scroll across three scales of my real-world impact from my CV & LinkedIn (`https://www.linkedin.com/in/haideranwar/`):
  1. **Global & Multilateral (UNDRR, New York):** Analyzing UNGA resolutions (70th–74th) for the Sendai Framework 2030, evaluating 26 Least Developed Countries (LDCs) Voluntary National Reports, and tracking disaster risk financing.
  2. **National & Ecosystem Scale (WWF-Pakistan):** Leading nationwide stakeholder workshops across four provinces for the **$150M Green Climate Fund (GCF) "Recharge Pakistan"** Nature-Based Solutions (NbS) flood risk project (35,000 acres reforested, 120+ basins recharged, 680,000 direct / 7M indirect beneficiaries).
  3. **Municipal & Community Recovery (City of Austin WPD & TAMU HRRC):** Embedding hazard mitigation (HMA) and social equity metrics into Austin's **$28M+ FEMA & HUD "Rain to River" portfolio**, leading $100K resilience mini-grants, ecological restoration after home buyouts in Onion Creek, advising Mayfield, KY on **$5.2M CDBG-DR** post-tornado housing reconstruction, and conducting 250+ household/business longitudinal recovery surveys in Lumberton, NC (NIST).
  4. **Safeguarding Cultural & Rural Heritage:** Leading the stakeholder workshop on *"Safeguarding Texas's Inland Rural Heritage"* and my accepted 2026 *Built Heritage* systematic review for hazard mitigation planners, connecting directly to my ongoing work on GLOFs and intangible heritage in Gilgit-Baltistan.

### CHAPTER IV (The Methodological Engine): Mixed-Methods, Spatial Science & AI Lab
- **The Story:** Show *how* I answer these questions—combining deep human fieldwork (Atlas.ti qualitative coding, PRISMA systematic reviews, 275+ field interviews/surveys) with advanced computational and geospatial analytics.
- **Interactive Bridge to My GitHub (`https://hanwar3.github.io/AI-Projects-and-Data-Analysis/?v=4#hma`):** Present tasteful, archival-styled interactive preview cards (not flashy tech widgets) that link directly to my live GitHub lab:
  - *US Federal Hazard Mitigation Grants ($7.83B OpenFEMA HMA Analysis, FY2015–2024 across 7,781 projects)*
  - *High-Resolution 30m DEM Climate & Topographic Relief Modeling (Python, xarray, Rasterio, GeoPandas)*
  - *Agentic AI & Machine Learning in Post-Disaster Search and Rescue Operations*

### CHAPTER V (The Scholarly Agora): Publications, Field Notes Blog, Teaching & Contact
1. **Publications & Peer Review Showcase:** Categorized cleanly (*Journal Articles & NIST Monograph*, *Accepted / Under Review*, *Working Papers*, *Conferences*, and *Peer Reviewer Service* for AJEM, IJES, and Safety Science) with expandable abstracts and one-click `[ Copy BibTeX / APA ]` buttons.
2. **"Field Notes & Reflections" Blog System:**
   - Build a clean, built-in blog section right on the site with category filters (*Gilgit-Baltistan & GLOFs*, *Intangible Heritage*, *Emergency Management*, *Methods & Policy*), reading time, and an interactive **Article Reader Modal** (so clicking a post opens a distraction-free, *New Yorker*-style essay view with social/LinkedIn share buttons).
   - Provide a **zero-cost, easy-to-manage backend architecture** (e.g., a `posts.json` / Markdown loader paired with a free **Decap CMS `/admin` configuration** OR an automatic RSS sync option from Substack/Medium) so I can publish new blog posts in minutes without editing raw HTML.
3. **Teaching, Mentoring & Service:** Highlight CARC 601 Guest Lectures, Camp DASH youth mentoring at Texas A&M, student supervision, and LUMS/CEU/HRRC leadership.
4. **Direct Meeting Scheduler & Contact Hub (`anwar_haider@tamu.edu`):**
   - Build a **"Request a Meeting / Office Hours"** interactive component that allows visitors to select a meeting purpose (*Research Collaboration*, *Policy/Consulting Inquiry*, *Speaking/Workshop Invitation*, *Media/Student Advising*), pick a proposed time or launch a Cal.com/Calendly embed modal, and submit a message directly to **`anwar_haider@tamu.edu`** via a free serverless form endpoint (Web3Forms / Formspree + fallback `mailto:anwar_haider@tamu.edu` pre-filled generator).

---

## 5. AESTHETIC & TYPOGRAPHIC DESIGN SYSTEM (NO AI SLOP)
- **Color Palette ("Karakoram Stone, Glacial Silt & Archival Ink"):**
  - Primary Background: Warm Archival Limestone (`#FAF7F2`)
  - Elevated Section / Card Surface: Glacial Alabaster (`#F2ECE1`)
  - Deep Immersion Chapter Background (for the Gilgit-Baltistan / GLOF scroll transition): Deep Mountain Slate (`#161D24`) with warm parchment text (`#F5F2EB`)
  - Primary Ink: Charcoal Obsidian (`#18181B`)
  - Accent 1 (Heritage & Earth): Terracotta Ochre (`#B45309`)
  - Accent 2 (Glacial Water & Flood Risk): Indus Teal (`#0F766E`)
  - Borders: Exposed architectural hairline grid (`1px solid rgba(24, 24, 27, 0.12)`)
- **Typography:**
  - *Display / Chapter Titles:* `Cormorant Garamond` or `Newsreader` (authoritative, museum-exhibition serif)
  - *Body & Academic Prose:* `Plus Jakarta Sans` or `Source Sans 3` (effortless readability)
  - *Elevation Meters, Coordinates, Dates & Citations:* `JetBrains Mono` (`tabular-nums`)
- **Interactive Visual Touches:**
  - Subtle SVG topographic contour lines and elevation markers (`3,500m → 1,500m → 500m → Sea Level`) that animate gently as the user scrolls down the page.
  - Smooth scroll-triggered reveals using IntersectionObserver / GSAP-style CSS transitions—silky, restrained, and respectful of `prefers-reduced-motion`.

---

## 6. DELIVERABLES I NEED FROM YOU NOW
1. **Complete, Production-Ready Codebase:** Build the full, working interactive website (clean HTML/CSS/JS or modular single-file architecture ready for instant deployment) containing **100% of my real CV data** (never use "Lorem Ipsum" or placeholder text).
2. **Easy Blog Backend Setup:** Include the blog reader UI, sample starter posts based on my real research (e.g., *"Safeguarding Living Heritage Against GLOFs in Gilgit-Baltistan"* and *"When the Whole Community Shows Up: Lessons from 26 Emergency Managers"*), and the exact plug-and-play setup for publishing new posts effortlessly.
3. **Zero-Cost Deployment & Free Custom Domain Guide:** Give me a 5-minute step-by-step checklist to deploy this immediately for **$0** on **Vercel / Cloudflare Pages / GitHub Pages**, plus how to claim my free custom domain using my **`anwar_haider@tamu.edu`** academic email via the GitHub Education Pack (or free `.vercel.app` / `.is-a.dev` domain).
4. **Run the "Gauntlet Design & De-Slop Loop":** Before showing me the final output, audit your own code and copy against `https://persepolis.getty.edu/` and `https://theacademicdesigner.com/2023/winners-of-the-2023-best-personal-academic-websites-contest/` to ensure zero AI clichés, crisp editorial hierarchy, and mobile responsiveness.
````

The user's message alongside it: "Make me the best damn academic website based on my research, perspectives, and interest." Then: "I've given you website instructions and my latest CV and other links in prompt follow that prompt."

### 14.2 claude.ai Project "Academic Website" instructions

````markdown
# CLAUDE PROJECT INSTRUCTIONS: DR. HAIDER WASEEM ANWAR — ACADEMIC, HERITAGE & DISASTER RESILIENCE WEBSITE

## 1. ROLE & CORE MISSION
You are the Principal Creative Director, Computational Cartographer, and Frontend Architect for **Dr. Haider Waseem Anwar**. Across every conversation in this project, your mission is to design, code, refine, and maintain a $10,000-caliber interactive scrollytelling academic website that combines museum-grade cultural heritage storytelling with rigorous disaster risk reduction (DRR) scholarship.

Always consult the uploaded `Anwar_CV_Fellow.pdf` in Project Knowledge as the single source of truth for all biographical facts, dates, grants, publications, and institutional affiliations. Never fabricate metrics, degrees, or placeholder "Lorem Ipsum" text.

---

## 2. CRITICAL IDENTITY & HIERARCHY GUARDRAILS
1. **Scholar & Field Researcher First (NEVER Lead with GitHub/Code):**
   - Always present Dr. Haider Waseem Anwar first and foremost as a **Social Scientist, Disaster Risk Reduction & Post-Disaster Recovery Scholar, and Cultural Heritage Researcher**.
   - NEVER style the hero section like a SaaS startup or software engineering portfolio.
   - Keep his computational and geospatial showcase (`https://hanwar3.github.io/AI-Projects-and-Data-Analysis/?v=4#hma`) in **Chapter IV (The Methodological Engine)** as the analytical toolkit supporting his qualitative fieldwork and policy research.
2. **Institutional Accuracy:**
   - Clearly distinguish that his **Ph.D. in Urban and Regional Sciences** is from **Texas A&M University (Department of Landscape Architecture and Urban Planning)**, while the **Hazard Reduction & Recovery Center (HRRC)** is the research center at Texas A&M where he works as a **Research Associate** (do not state he earned his Ph.D. "from HRRC").
3. **Core Thematic Thread ("From the Glacial Roof to the Whole Community"):**
   - Frame the site's visual and narrative journey around elevation, watersheds, and the disaster cycle—connecting his work on **Glacial Lake Outburst Floods (GLOFs), climate displacement, and safeguarding intangible & vernacular heritage in Gilgit-Baltistan and rural Texas** down to **emergency management, spontaneous volunteer integration in Search & Rescue (SAR), and equitable flood/wildfire recovery**.

---

## 3. MANDATORY GOLD-STANDARD DESIGN REFERENCES
Every layout, animation, and typographic choice must be benchmarked against these four references:
1. **Cultural Heritage Scrollytelling:** https://persepolis.getty.edu/
   - Use museum-exhibition pacing, layered parallax depth, archival warmth, and scroll-triggered chapter transitions.
2. **Spatial Zoom & Scale Transitions:** https://www.awwwards.com/inspiration/world-zoom-rspca-animal-futures
   - Use smooth scale/elevation transitions (`3,500m Glacial Roof → 1,500m SAR Response → 500m Floodplain & Policy → Methodological Lab`) that guide the visitor from macro landscapes to human communities.
3. **Academic Usability & Authority:** https://theacademicdesigner.com/2023/winners-of-the-2023-best-personal-academic-websites-contest/
   - Maintain a persistent, zero-friction top navigation bar (`Profile` • `Scroll Journey` • `Policy Impact` • `Publications` • `Field Notes Blog` • `Methods Lab` • `CV & Book a Meeting`) so busy search committees or fellowship reviewers can skip animations and access the CV or papers in one click.
4. **Anti-AI Slop System & Gauntlet Design Loop:** https://www.youtube.com/watch?v=VwGrXe2ricE
   - **One Screen, One Point (System 1 Thinking):** Each scroll viewport must communicate ONE clear scholarly thesis without cognitive overload.
   - **Kill the AI Slop Monster:** Strictly BAN indigo/purple-to-violet gradients, neon cyberpunk dark modes, generic 3-column frosted-glass SaaS cards, skill percentage bars, typing text effects, and robotic AI marketing clichés.

---

## 4. CODIFIED DESIGN SYSTEM (LOCKED TOKENS)
Always apply these exact design tokens unless explicitly asked to test an alternative:

### Color Palette ("Karakoram Stone, Glacial Silt & Archival Ink")
- `--bg-primary`: `#FAF7F2` (Warm Archival Limestone)
- `--bg-elevated`: `#F2ECE1` (Glacial Alabaster for drawers, cards, and modals)
- `--bg-mountain-chapter`: `#161D24` (Deep Mountain Slate—used exclusively for the immersive Gilgit-Baltistan / GLOF scrollytelling transition with `#F5F2EB` parchment text)
- `--ink-primary`: `#18181B` (Charcoal Obsidian)
- `--ink-secondary`: `#57534E` (Muted Stone)
- `--accent-heritage`: `#B45309` (Terracotta Ochre — cultural heritage, fieldwork, & highlights)
- `--accent-watershed`: `#0F766E` (Indus Teal — GLOFs, hydrology, spatial analysis, & interactive controls)
- `--grid-hairline`: `1px solid rgba(24, 24, 27, 0.12)` (Exposed Swiss architectural grid dividers)

### Typography
- **Display & Chapter Headings:** `'Cormorant Garamond'` or `'Newsreader'` (Google Fonts, serif, authoritative editorial weights 500–600, tight tracking `-0.02em`).
- **Body & Academic Prose:** `'Plus Jakarta Sans'` or `'Source Sans 3'` (clean, highly legible sans-serif, `line-height: 1.65`, comfortable `65ch` measure).
- **Elevation Markers, Coordinates, Grant Totals & Citations:** `'JetBrains Mono'` (`font-variant-numeric: tabular-nums`).

### Signature Visual Motifs
- Animated SVG topographic contour lines in the background (`opacity: 0.06` to `0.12`) that shift subtly with scroll position.
- A persistent **Left/Right Elevation Scroll Indicator** displaying current narrative altitude (`3,500m Karakoram / GLOF Heritage` → `1,500m Acute SAR & Wildfires` → `500m Basin Recovery & Policy` → `0m Global Agora`).

---

## 5. REQUIRED FUNCTIONAL SYSTEMS (ALWAYS MAINTAIN IN CODE)
1. **All External Profile Links Integrated:**
   - Primary Email: `anwar_haider@tamu.edu`
   - LinkedIn: https://www.linkedin.com/in/haideranwar/
   - GitHub Data & GIS Lab (integrated in Chapter IV): https://hanwar3.github.io/AI-Projects-and-Data-Analysis/?v=4#hma
2. **"Field Notes & Reflections" Blog System:**
   - Include an interactive on-site blog section with category filtering (*Gilgit-Baltistan & GLOFs*, *Intangible Heritage*, *Emergency Management & SAR*, *Policy & Methods*) and a distraction-free, *New Yorker*-style slide-over **Article Reader Modal**.
   - Architect the blog so it reads from a clean, easily editable `posts.json` / Markdown folder compatible with **Decap CMS (free Git-based visual `/admin` editor)** and optional **Substack / Medium RSS auto-fetch**, requiring $0 in database costs.
3. **Direct Meeting Scheduler & Contact System (`anwar_haider@tamu.edu`):**
   - Provide an interactive **"Book a Meeting / Request Office Hours"** drawer where visitors select a topic (*Research Collaboration*, *Policy/Consulting*, *Speaking/Workshop*, *Academic/Student Inquiry*), choose a time via an embedded Cal.com/Calendly modal, or send a direct message to `anwar_haider@tamu.edu` via Web3Forms (serverless $0 form API) with an instant pre-filled `mailto:anwar_haider@tamu.edu` fallback.
4. **Zero-Friction Academic Utilities:**
   - Every publication must include expandable `[ + Abstract / Policy Takeaway ]` and one-click `[ Copy BibTeX ]` / `[ Copy APA ]` clipboard buttons.
5. **Zero-Cost Hosting & Domain Architecture:**
   - Write clean, portable, dependency-light code (vanilla HTML5/CSS3/JS or static-export ready) that deploys in 60 seconds for **$0** on **Cloudflare Pages**, **Vercel**, or **GitHub Pages**, and supports custom domains claimed via the **GitHub Student/Academic Developer Pack** (`anwar_haider@tamu.edu`).

---

## 6. SELF-CRITIQUE "GAUNTLET LOOP" BEFORE EVERY OUTPUT
Before delivering or updating code in any turn:
1. Verify that **profile, fieldwork, heritage, and disaster recovery** lead the narrative, and GitHub/coding is positioned as a supporting method in Chapter IV.
2. Check that all copy reads like a sharp human scholar (*The New Yorker* / *MIT Senseable City Lab* / *Getty Publications*), stripping out any AI-generated buzzwords ("delve", "tapestry", "testament", "cutting-edge synergy").
3. Confirm mobile responsiveness, keyboard accessibility, `prefers-reduced-motion` support, and working links to `anwar_haider@tamu.edu`, LinkedIn, and GitHub.
````

---

## Appendix A. CV text (pdftotext -layout of Anwar_CV_Fellow.pdf)

```text
                                                                                                                          Anwar CV 1

                                          HAIDER WASEEM ANWAR
                                            Curriculum Vitae (CV)
Hazard Reduction & Recovery Center (HRRC)                              Email: anwar_haider@tamu.edu
Department of Landscape Architecture and Urban Planning (LAUP)         GitHub: hanwar3.github.io/AI-Projects-and-Data-Analysis
Texas A&M University (TAMU)                                            LinkedIn: linkedin.com/in/haideranwar
Current Address: Reston, VA 20191                                      Phone: +1-979-326-8274


RESEARCH INTERESTS
My research interests include disaster risk reduction and post-disaster recovery, especially through social capital and community
resilience; volunteer integration into emergency management and search and rescue operations; the use of AI in post-disaster search and
rescue; protecting cultural heritage against hazards, especially in rural areas; understanding the impact of climate adaptation and
displacement on intangible heritage; and equity in climate adaptation.

EDUCATION
2026     Texas A&M University, College Station, TX, USA
         Doctor of Philosophy (PhD) in Urban and Regional Sciences (defended October 2026; conferral May 2027)
                 Dissertation: ‘When the Whole Community Shows Up: The Perspectives of Emergency Managers Dealing with
                 Volunteers in Post-Disaster Search and Rescue’
                 Advisor: Dr. Michelle Meyer
         Graduate Certificate in Environmental Hazard Management (2026)

2019     Central European University (CEU), Budapest, Hungary
         Master of Arts (MA) International Relations, with Distinction
                  Thesis title: ‘Securitized Migration: The Puzzle of Deterring Migration Through Development Aid’
                  Advisor: Dr. Andrew Xiang Li

2018     Northeastern University, Boston, MA, USA
         Graduate Certificate in Global Studies and International Relations

2015     Lahore University of Management Sciences (LUMS), Lahore, Pakistan
         Bachelor of Science (B.Sc.) Hons. in Political Science
                 Thesis title: ‘Analysis of the Unrest in Baluchistan (Province of Pakistan): Causes and Solutions’

PROFESSIONAL EXPERIENCE
Sep 2021 – Present
        Research Associate
        Hazard Reduction & Recovery Center (HRRC), Texas A&M University
        College Station, TX/ Remote, USA
         Led in-depth PhD dissertation research using PRISMA literature review, coding (Atlas.ti), and analysis of 26 interviews
            with emergency managers across Texas, North Carolina, Florida, and Louisiana, strengthening Incident Command
            System (ICS) and Emergency Operations Center (EOC) volunteer integration frameworks for search and rescue
            operations
         Contributed to the state-level wildfire emergency preparedness plan through qualitative analysis of emergency managers
            from 9 locations in Texas, for an estimated $199,000 Texas Fire-Project grant by the National Science Foundation
            (NSF)
         Improved healthcare emergency planning through ArcGIS StoryMaps and qualitative analysis for a project on the 2024
            Texas Panhandle Wildfire
         Conducted research and helped write a grant proposal for Caldor, California Wildfire Research with PI Dr. Tara Goddard
            - Evacuation and Accessibility for People with Disabilities and Lack of Mobility During Wildfire.
                                                                                                                          Anwar CV 2

            Helped with 250+ household and business survey interviews, data analysis, and publication for the National Institute of
             Standards and Technology (NIST) resiliency project on longitudinal flood recovery in Lumberton, North Carolina
            Provided technical assistance with the HRRC team to planners in Mayfield, KY, on the CDBG-DR $5.2M fund that
             contributed to equitable low-income housing development and sustainable reconstruction following the 2021 tornadoes
            Coordinated a team of 6 and supervised 3 researchers to plan a stakeholder workshop on ‘Safeguarding Texas's Inland
             Rural Heritage: Collaborative Strategies for Resilience Against Natural Hazards’
            Served as guest lecturer for CARC 601 (Foundations of Research in Planning and Design), where I delivered a PhD
             dissertation research lecture facilitating hands-on disaster risk research methodology for students
            Conducted teaching camp exercise and mentoring at Camp DASH Texas A&M University resulting in air quality, and
             hazard mitigation planning activities and knowledge improvement for high school youth campers

Jun 2023 – Apr 2024
        Senior Research Analyst
        Watershed Protection Department (WPD), City of Austin
        Austin, TX, USA
         Served in the planning and strategy development team of the WPD city plan ‘Rain to River’ to embed emergency
            preparedness, hazard mitigation assessment (HMA), and social equity metrics and knowledge base into the strategic
            alignment for different projects in the city’s $28M+ FEMA and HUD portfolio during 2023-2024
         Led grant assessment to allocate $100,000 in mini grant funds to community organizations to help build resilience
         Helped design surveys and conduct focus group workshops to incorporate learnings for FEMA HMA and wrote best
            practice reports for equity in flood adaptation, especially to embed in ecological restoration after home buyout in Onion
            Creek, Austin

Feb 2021 – Aug 2021
        Senior Research Associate
        World Wildlife Fund (WWF-Pakistan)
        Lahore, Punjab, Pakistan
         Led nationwide stakeholder workshops to implement nature-based solutions (NbS) initiatives for reducing flood risk
            across four provinces of Pakistan under the $150M ‘Recharge Pakistan’ Green Climate Fund (GCF) project, resulting in
            reforesting 35,000 acres, recharging 120+ basins, and benefiting a population of 680,000 directly and 7 million indirectly
         Conducted focus-group interviews with flood-affected communities across four provinces of Pakistan to form
            community-based disaster risk management (CBDRM) report for preparedness and early warning systems

Nov 2019 – May 2020
       Full-time Program Management Intern
       United Nations Office for Disaster Risk Reduction (UNDRR)
       New York City, NY, USA
        Produced analyses of UNGA resolutions (70th–74th) to support enhancement of the Sendai Framework 2030
        Analyzed disaster risk progress in 26 Voluntary National Reports (VNRs) for the 5th UN Conference on Least
            Developed Countries (LDCs), to prepare LDCs against disasters, and prevent retraction after graduation
        Tracked DRR agenda in Financing for Development (FfD), resulting in an internal UN report to map public-private
            emergency preparedness and response funds for pre- and post-disasters

May 2017 – Sep 2017
       Research Associate
       Fintech Centre, Information Technology University (ITU)
       Lahore, Punjab, Pakistan
        Designed and conducted interviews with 40+ men and women, for peer-reviewed publication on women’s financial
            inclusion

Feb 2016 – Dec 2016
        Research Assistant
        Consortium for Development Policy Research (CDPR)
                                                                                                                        Anwar CV 3

        Lahore, Punjab, Pakistan
         Developed a database by digitizing data from 10 administrative districts and 130,000+ cottage and small industrial units
            for the International Growth Center (IGC) report titled ‘Spatial analysis of small and cottage industries in Punjab,
            Pakistan’

Dec 2015 – Feb 2016
       Assistant Project Officer
       Pakistan Institute of Legislative Development and Transparency (PILDAT)
       Lahore, Punjab, Pakistan
        Collected data from various Federal Ministries in Pakistan, to perform qualitative and quantitative analysis to deliver the
            Federal Governance Scorecard 2013-2014 Report

AWARDS
2021 – 2026      Landscape Architecture and Urban Planning (LAUP) Graduate Tuition Award
2018 – 2019      CEU Master's Tuition Award


PUBLICATIONS
JOURNAL ARTICLES
2024    Meyer, M., Duenas-Osorio, L., Dillard, M., & Sutley, E. (Eds.). (2024). The Lumberton, North Carolina flood of 2016, wave
        5: Understanding recovery from sequential disasters (NIST Special Publication 1230-5). National Institute of Standards and
        Technology. https://doi.org/10.6028/nist.sp.1230-5
2021    Shahid, S., & Anwar, H. W. (2021). Hospital waste management and environmental disaster risk: A case study of Lahore.
        Centre for Public Policy and Governance. http://digitalrepository.fccollege.edu.pk/handle/123456789/1460
2018    Ibtasam, S., Razaq, L., Anwar, H. W., Mehmood, H., Shah, K., Webster, J., Kumar, N., & Anderson, R. (2018). Knowledge,
        Access, and Decision-Making. Proceedings of the 1st ACM SIGCAS (COMPASS) - COMPASS ’18.
        https://doi.org/10.1145/3209811.3209819

ACCEPTED
2026    Anwar, H.W., Isaba, T. (2026). Planning for Cultural Heritage Facing Disaster Risk: A Systematic Review for Hazard
        Mitigation Planners. Built Heritage (accepted)

UNDER PEER-REVIEW
2026    Khoso, S., Abdullah, G. M. S., Muhammad, G., Zahid, M., Anwar, H. W., Ansari, A. A., & Kennedy, C. (2026). Shear
        modulus and damping ratio of Niger Delta clays: Experimental and predictive modeling insights for seismic risk mitigation.
        Soil Dynamics and Earthquake Engineering

IN PROGRESS
2026    Anwar, Haider, Michelle Meyer, J. Carlee Purdum, Tyler Eutsler, Kyle Breen, Stuart Nolan. “Challenges and Opportunities
        in Incorporating Volunteers in Flood Rescue Operations: Perspectives of Emergency Managers (EMs)”
2026    Systematic literature review paper on ‘Artificial Intelligence (AI) in Post-Disaster Emergency Management for Search and
        Rescue Operations’

CONFERENCE
2025    Anwar, H. W., & Meyer, M. (2025, July). Challenges and opportunities in incorporating volunteers in flood rescue:
        Perspectives of emergency managers [Conference poster]. 49th Annual Natural Hazards Research and Applications
        Workshop, Natural Hazards Center, University of Colorado Boulder
                                                                                                                             Anwar CV 4

2025    Anwar, H. W. (2025, July 8). On the Brink of Cultural Catastrophe: Why Plan for Cultural Heritage in the Context of
        Disaster Risk? [Conference paper accepted]. ISA - 5th ISA Forum of Sociology (6-11 July 2025).
        https://isaconf.confex.com/isaconf/forum2025/meetingapp.cgi/Paper/160628
2025    Anwar, H. W., & Meyer, M. (2025, July 10). Opportunities and challenges in emergency management (EM) protocols and
        volunteer engagement [Conference paper accepted]. ISA - 5th ISA Forum of Sociology (6-11 July 2025).
        https://isaconf.confex.com/isaconf/forum2025/meetingapp.cgi/Paper/164952

PROFESSIONAL SERVICE
Teaching                  Guest Lecturer, CARC 601: Foundations of Research in Planning and Design, Texas A&M
                          University (Hosted by Dr. Michelle Annette Meyer), Virtual, September 1, 2026


                          Mentor / Instructor, Camp DASH (Disaster and Spatial Health), Texas A&M University (July 21–
                          24, 2026). Co-led experiential learning activities and mentoring of high school students on
                          disaster science, air quality, and hazard mitigation planning.
Reviewer                  Australian Journal of Emergency Management (AJEM)
                          International Journal of Emergency Services (IJES)
                          Safety Science (SS)
Acknowledged              Book: Jenne, E. K., Popovic, M., & Siroky, D. S. (2026, February 1). Clients, rivals, and rogues.
                          Cambridge Core. https://www.cambridge.org/core/books/abs/clients-rivals-and-rogues/clients-
                          rivals-and-rogues/0FE0334FAE9637B86FCA3DB084E48631


                          Journal Article: Aldrich, D.P. Challenges to Coordination: Understanding Intergovernmental
                          Friction During Disasters. Int J Disaster Risk Sci 10, 306–316 (2019).
                          https://doi.org/10.1007/s13753-019-00225-1
Research Supervision      Aggie Collab Group Volunteer Researchers for Workshop Paper Research ‘Safeguarding Texas's
                          Inland Rural Heritage: Collaborative Strategies for Resilience Against Natural Hazards:
                          Yoonjeong Kang (Master’s Student), Gianna Fernandes (Bachelor’s Student), Maika Tanski
                          (Bachelor’s Student)
Leadership Position       Student Committee PhD Representative (2022 – 2023), HRRC, TAMU
                          Class Representative (2018 – 2019) of MA in International Relations, CEU
Volunteer Work            Conference Participation as Volunteer Help for 2023 Natural Hazards Workshop in University of
                          Colorado, US
                          Director Logistics and Registration LUMS Music Festival 2013 and 2014 (Hosted ~300
                          Participants), Member LUMS Music Society 2011-2015


CERTIFICATES & LICENSES
2026             AI Python for Beginners, DeepLearning.AI, Credential ID: 56c3d6d8-f634-4219-9209-1801456df98f
2026             Agentic AI, DeepLearning.AI, Credential ID: 9d70de3b-3414-4f95-9912-5c1ca0be9785
2026             Statistics with Python Specialization, University of Michigan, Credential ID: 40AQEZPDKHIG
                      Includes Courses: Data Visualization, Inferential Statistical Analysis, and Fitting Statistical Models to Data
                                                                                                                        Anwar CV 5

2026             Google Advanced Data Analytics, Google, Credential ID 1ED5Z9N7SGPI
                     Includes Courses: Go Beyond the Numbers: Translate Data into Insights, The Power of Statistics, Regression
                      Analysis, The Nuts and Bolts of Machine Learning, Google Advanced Data Analytics Capstone
2026             Geospatial Foundations & Python Tooling, Coursera, Credential ID: JLSKS7TJA2TS
                     Includes Courses: Python Geo Stack, Master GDAL CLI, Decode Rasters with Rasterio, Crunch Vectors with
                      GeoPandas, Map in QGIS, Query Spatial with PostGIS, Automate QGIS with PyQGIS, Manage Geo Projects
2025 – 2026      Agentic AI and AI Agents for Leaders Specialization, Vanderbilt University, Credential ID: 19RYVILG5YOK
                     Includes Courses: Agentic AI Primer, OpenAI Custom AI Assistants, and Prompt Engineering for ChatGPT
2021 – 2026      CITI Program Research Ethics, CITI Program
                     Includes Courses: Humanities RCR (ID: 46131681); RCR Basic (ID: 72587583); Social and Behavioral
                      Research Investigators and Key Personnel (ID: 46131680)
2020             Introduction to Disaster Risk Finance (DRF) Analytics, The World Bank Group (WBG)
2018-2020        Bringing Objective, Options and Strategy Together (BOOST) Certificate (non-degree), 8.5 ECTS (European Credit
                 Transfer and Accumulation System), Department of Economics and Business, Central European University


SKILLS
Qualitative Research and Coding (Atlas.ti), Survey Design and Interviewing (CITI Certified), Quantitative Research (Stata, Python
Specialization, University of Michigan), Data Analysis and Visualization (Google Advanced Data Analytics), Geospatial Analysis
(QGIS, PyQGIS, Python: GeoPandas, Rasterio, GDAL CLI), Visual Storytelling (ArcGIS StoryMaps), AI (Prompt Engineering,
Agentic Workflows, Model Context Protocol (MCP), Retrieval-Augmented Generation (RAG), Multi-Agent Systems, LLM
Evaluation, Orchestration; DeepLearning.AI and Vanderbilt University), Languages: English (full professional proficiency), Urdu
(mother tongue), Punjabi (mother tongue)
```

## Appendix B. Abstracts and source documents

### B.1 Built Heritage systematic review (accepted). Abstract from his manuscript ("Draft for Revision", `Writing Sample.pdf`)

Cultural heritage holds both tangible and intangible, irreplaceable historic value, and the significance of place attachment. However, as climate change intensifies the frequency and severity of hazard events, cultural heritage faces an escalating disaster risk. Unfortunately, hazard mitigation planners, those working across local, state, and federal levels to develop Hazard Mitigation Plans (HMPs), often prioritize critical infrastructure while viewing historic preservation as a secondary concern. This systematic literature review synthesizes evidence to demonstrate why hazard mitigation planners must prioritize integrating both heritage typologies into HMPs and related risk-reduction strategies. The review draws on international disaster risk management (DRM) literature and translates its concepts into the terminology and institutional framework of U.S. hazard mitigation planning. The study identifies four thematic domains: cultural heritage as a resilience resource, the limits of standard mitigation tools for heritage preservation, institutional barriers to integrating heritage into hazard mitigation planning, and methods for assessing heritage risk. Heritage assets function as critical social infrastructure, enhancing community resilience through traditional knowledge and social cohesion. The review exposes significant institutional and systemic barriers that hinder the inclusion of heritage in mainstream hazard mitigation planning. Findings indicate that while technological tools such as GIS are invaluable for mapping the exposure of heritage to hazards, their effectiveness is limited by policy gaps and interagency coordination challenges. Furthermore, the research evaluates emerging methods for assessing heritage risk and vulnerability, emphasizing the shift toward multi-criteria frameworks. The study concludes that hazard mitigation planners must adopt a systems-thinking approach, engaging tangible and intangible heritage through typology-appropriate tools, recognizing them not merely as vulnerable artifacts but as vital drivers of community resilience and proactive risk reduction.

Keywords: Cultural Heritage; Hazard Mitigation Planning; Disaster Risk Reduction; Preservation; Resilience; Disaster Recovery; Systematic Literature Review.

### B.2 ISA 2025, paper 160628 (marked CANCELLED in the program; Tue 8 Jul 2025 09:45, session 637 "Cultural Heritage and Disaster", RC39)

Cultural heritage holds both tangible and intangible irreplaceable historic value and significance of place attachment, however, with the exacerbating impact of climate change induced and other disasters, culture heritage is under threat. This literature review paper synthesizes key findings on the intersection of cultural heritage preservation and disaster risk reduction (DRR), emphasizing the need for proactive planning. The study identifies critical themes, including vulnerability assessment, policy gaps, and resilience-building strategies. Research reveals that cultural heritage is highly vulnerable to disasters, often overlooked during recovery efforts in favor of essential infrastructure. Preservation efforts are further hampered by institutional and procedural barriers, such as conflicting priorities between local, state, and federal agencies. These challenges are compounded by the limited flexibility for long-term resilience planning, as alterations to heritage sites often compromise the historic value of cultural heritage.

A seminal research question addressed in this literature review paper is: How can urban planners balance the urgent demands of disaster recovery with the need to preserve the historical and cultural integrity of heritage sites? Preliminary findings indicate that while technological tools such as GIS are invaluable for mapping vulnerability, their effectiveness is limited by gaps in policy and interagency coordination. Barriers at institutional and procedural levels often overshadowed need for recovery of heritage against critical infrastructure. The research also indicates lack of comprehensive guidelines that cater to the unique requirements of heritage sites, particularly in terms of adapting to long-term climate threats. The literature review also posits that enhancing early warning systems and fostering stronger cross-sector collaboration are essential to safeguard cultural assets. By bridging the current gaps in policy and practice, this paper contributes to a more nuanced understanding of how urban planning can better integrate cultural heritage into disaster resilience frameworks, ultimately to aid preservation of both tangible and intangible heritage.

### B.3 ISA 2025, paper 164952 (Thu 10 Jul 2025 11:00–11:15, session 645.1; the program page lists Michelle Meyer)

The post-disaster Emergency Management (EM) protocol and volunteer management is infused with a complicated relationship, concerns of perception, and issues of integration in disaster response and rescue efforts. Upholding procedural justice in utilizing this human resource and understanding the social capital of volunteer aid can help build resilience against disasters. This research particularly explores the challenges and opportunities for volunteer integration in EM protocols during disaster 'rescue' efforts.

'Volunteerism' in the context of disaster emergency is regarded as direct and indirect service for other people and things with no self-interest. Even though the 'emergent' volunteers can offset several unmet needs, proliferate a sense of community, and bring in resources, they also raise issues in coordination, liability and safety, lack of training, or misconduct in protocols. Integrating volunteers into disaster rescue efforts also experiences external factors such as social media and inter agency interaction.

Therefore, by using grounded theory and performing qualitative analysis on 26 in-depth interviews with emergency managers in areas flooded by Hurricane Harvey in Texas and North Carolina, this study analyzes the challenges and opportunities faced by EM protocols in volunteer rescue efforts. The analysis also looks at the perception of volunteer groups among emergency managers – 'Cajun Navy' in comparison to other volunteer groups. The preliminary results indicate coordination issues, communication-breakdown, liability issues, lack of training, resource-allocation, and social-media as the main challenges impacting volunteer's rescue efforts. The study also reveals the opportunity in early mobilization, social media and technology, resources brought by volunteers, and empathy of volunteers. Volunteers are also perceived as a resource instead of professionals, by the EMs and this poses issues in the integration of volunteers in EM protocols, however, this perception differs between organized groups such as Cajun Navy and other spontaneous volunteer groups/ individuals, as former is given professional importance.

### B.4 Source documents on his computer (for richer copy)
Under `C:\Haider Files\TAMU Study\Job Search Network Writing Articles and CV\Post Doc and Teaching\`:
- `Harvard\Mahindra Humanities Center Postdoc\Anwar_ResearchStatement_MahindraFellow_Harvard.pdf` (GB heritage project, humanities framing) and `Writing Sample.pdf` (the full Built Heritage manuscript, 37 pp.)
- `Harvard\HUCE Environmental Fellow\Anwar_ResearchProposal_HUCEFellow_Harvard.pdf` (GB project, mixed methods, hypotheses H1–H3, timeline)
- `Princeton\HMEI Environmental Fellow\Anwar_ResearchProposal_HMEIFellow_Princeton.pdf`; `Columbia Climate School\Anwar_ResearchProposal_ClimateSchool_Columbia.pdf` and `Anwar_PersonalHistory_ClimateSchool_Columbia.pdf` (AI-in-SAR framing)
- `Boston University\Assistant Professor City Planning and Urban Affairs\` research, teaching and personal statements
- `University of Southern California\Heritage Conservation Faculty\` cover letter and sample syllabi (Heritage at Risk, Living Heritage)
- `Earth Commons Georgetown\PostDoc Research Abstract.pdf` (social capital and climate mobility)

## Appendix C. Code written so far (word for word)

Re-create these under `tools/`. Paths inside them assume they run from the build folder (`node_modules`, `ne/`, outputs `tout/` and `maps/`).

### C.1 package.json
```json
{
  "name": "build",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "@fontsource-variable/jetbrains-mono": "^5.3.0",
    "@fontsource-variable/newsreader": "^5.3.0",
    "@fontsource-variable/source-sans-3": "^5.3.1",
    "d3-geo": "^3.1.2",
    "d3-geo-projection": "^4.0.0",
    "mapshaper": "^0.7.101",
    "topojson-client": "^3.1.0",
    "topojson-simplify": "^3.0.3",
    "us-atlas": "^3.0.1",
    "world-atlas": "^2.0.2"
  }
}
```

### C.2 tools/terrain.py
```python
#!/usr/bin/env python3
"""
Builds the site's backdrop: a computed, fictional topographic transect from a
glaciated mountain head (7,000 m summits) to the sea, with one river through it.

Output
  terrain.js     contour polylines, river network, glacier, lake, labels (canvas data).
                 Every contour segment carries an illumination class (0 shadow .. 4 lit,
                 light from the north-west) so the renderer can draw illuminated
                 contours in the manner of Tanaka Kitiro (1950): relief from line alone.

This is not a survey of a real place. It is a designed terrain whose river passes
through the elevations the site's chapters use: 3,500 m, 1,500 m, 500 m, 150 m, 0 m.

Usage: python3 terrain.py <out_dir>
Needs: numpy, scipy, scikit-image
"""
import json, math, os, sys
import numpy as np
from scipy import ndimage as ndi
from scipy.interpolate import PchipInterpolator
from skimage import measure

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
SEED = 1991
rng = np.random.default_rng(SEED)

W, H = 1000.0, 7000.0          # terrain units
NX, NY = 250, 1750             # grid
CELL = W / NX                  # 4 units per cell
xs = (np.arange(NX) + 0.5) * CELL
ys = (np.arange(NY) + 0.5) * CELL
X, Y = np.meshgrid(xs, ys)
t = ys / H

def smooth_noise_1d(n, sigma, amp):
    v = ndi.gaussian_filter1d(rng.standard_normal(n), sigma, mode="reflect")
    return v / (np.abs(v).max() + 1e-9) * amp

# ------------------------------------------------------------------ river centreline
# Sine-generated curve (Langbein & Leopold 1966): the channel's direction angle swings
# sinusoidally along its path. Nearly straight under the ice and in the gorge, loose in the plain.
def sine_generated():
    x, y, ph, k = 0.0, 0.0, 0.9, 0
    ds = 2.0
    wob = smooth_noise_1d(9000, 140, 0.16)
    pts = [(x, y)]
    while y < H + 40:
        tt = min(1.0, max(0.0, y / H))
        th_max = float(np.interp(tt, [0, .19, .26, .40, .52, .62, .80, .88, 1], [.06, .08, .22, .34, .62, .98, 1.04, .62, .34]))
        lam    = float(np.interp(tt, [0, .26, .45, .60, .80, 1],                [300, 300, 350, 430, 500, 520]))
        ph += 2 * math.pi * ds / lam
        th = th_max * math.sin(ph) + wob[min(k, 8999)] * min(1.0, th_max * 2.2)
        x += math.sin(th) * ds; y += math.cos(th) * ds
        pts.append((x, y)); k += 1
    return np.array(pts)

_c = sine_generated()
xr_raw = np.interp(ys, _c[:, 1], _c[:, 0])
xr_raw -= ndi.gaussian_filter1d(xr_raw, 190, mode="nearest")     # stop the belt axis wandering off the sheet
xr = 705 + xr_raw + smooth_noise_1d(NY, 150, 30)
xr = np.clip(ndi.gaussian_filter1d(xr, 2.5, mode="nearest"), 520, 900)

# ------------------------------------------------------------------ long profile (thalweg)
prof_y = [0,    650,  1250, 1330, 1470, 1560, 2700, 3900, 4900, 5700, 6050, 6400, 7000]
prof_z = [5350, 4350, 3590, 3500, 3500, 3440, 1500, 500,  150,  30,   0,    -30,  -90]
profile = PchipInterpolator(prof_y, prof_z)
z_thal = profile(ys)

# ------------------------------------------------------------------ valley cross-section
D = np.abs(X - xr[:, None])
floor_w = np.interp(t, [0, .10, .19, .26, .40, .58, .78, .92, 1], [58, 62, 40, 16, 20, 150, 300, 420, 420])[:, None]
relief  = np.interp(t, [0, .20, .38, .56, .72, .86, 1],           [1950, 2150, 1650, 600, 150, 34, 20])[:, None]
power   = np.interp(t, [0, .25, .45, .65, 1],                     [1.25, 1.15, 1.0, 1.3, 1.6])[:, None]
u = np.clip((D - floor_w) / 620.0, 0, None)
side = relief * np.power(u, power)

# ------------------------------------------------------------------ fractal relief
def fbm(sigmas, weights, aniso=1.0):
    out = np.zeros((NY, NX))
    for s_, w in zip(sigmas, weights):
        f = ndi.gaussian_filter(rng.standard_normal((NY, NX)), (s_, s_ * aniso), mode="reflect")
        out += w * f / (f.std() + 1e-9)
    return out / sum(weights)

n_big   = fbm([42, 22], [1.0, 0.6], aniso=1.9)        # spurs and side valleys run toward the river
n_mid   = fbm([11, 6],  [1.0, 0.55], aniso=1.5)
n_small = fbm([3.2],    [1.0], aniso=1.2)
ridged  = 1.0 - np.abs(np.tanh(n_big * 0.9))
mount   = np.clip(side / 900.0, 0, 1)
amp     = 0.36 * side + 14 * np.clip(side / 60.0, 0, 1)

Z = z_thal[:, None] + side \
    + amp * (0.62 * n_big + 0.26 * n_mid + 0.07 * n_small) \
    + mount * relief * 0.30 * (ridged - 0.55)

# named-height summits on the valley shoulders
summits = []
for sy in (190, 560, 900, 1230, 1580, 1900, 2260, 2620):
    row = min(NY - 1, int(sy / CELL))
    for sgn in (-1, 1):
        if rng.random() < 0.72:
            sx = xr[row] + sgn * rng.uniform(250, 430)
            if 60 < sx < W - 60:
                summits.append((sx, sy + rng.uniform(-90, 90), rng.uniform(380, 900) * float(np.interp(sy, [0, 1500, 2700], [1.0, 0.85, 0.45])), rng.uniform(46, 84)))
for sx, sy, sh, sr in summits:
    r2 = ((X - sx) / (sr * 1.25)) ** 2 + ((Y - sy) / sr) ** 2
    Z += sh * np.exp(-r2 ** 0.9)

# floodplain micro-relief: scroll bars, a natural levee, backswamp
low = np.clip(1 - side / 160.0, 0, 1) * np.clip((t[:, None] - .50) / .12, 0, 1)
Z += low * (np.sin(D / 46.0 + 2.4 * n_mid) * 5.5 + n_mid * 7.5)
Z += low * (9.0 * np.exp(-((D - 34) / 26.0) ** 2))

# the channel sits below its floodplain, so every contour notches upstream at the river
inc_d = np.interp(t, [0, .21, .26, .45, .60, .85, 1], [0, 0, 34, 26, 11, 4, 0])[:, None]
inc_w = np.interp(t, [0, .26, .45, .60, 1],            [8, 9, 12, 15, 18])[:, None]
Z -= inc_d * np.exp(-(D / inc_w) ** 2)

# delta lobe pushing the coast seaward around the mouth
Z += 34.0 * np.exp(-((X - xr[:, None]) / 235.0) ** 2) * np.clip((Y - 5350) / 500.0, 0, 1) * np.clip((6900 - Y) / 800.0, 0, 1)

# glacier: a smooth ice surface, slightly convex across the tongue
gl_half = np.interp(ys, [0, 120, 500, 950, 1180, 1262], [60, 64, 54, 40, 26, 9])
gl_edge = gl_half[:, None] + 7 * ndi.gaussian_filter(rng.standard_normal((NY, NX)), (9, 3))
glacier_mask = (D < gl_edge) & (Y < 1264)
ice = z_thal[:, None] + 26 * np.cos(np.clip(D / np.maximum(gl_edge, 1), 0, 1) * np.pi / 2)
Z = np.where(glacier_mask, 0.25 * Z + 0.75 * ice, Z)

# glacial lake: dead-level water held behind a moraine
lake_cy, lake_ry, lake_rx = 1392, 86, 34
lx = float(xr[int(lake_cy / CELL)])
lake_mask = ((X - lx - 6 * np.sin(Y / 31.0)) / lake_rx) ** 2 + ((Y - lake_cy) / lake_ry) ** 2 < 1.0
Z += 36 * np.exp(-((Y - (lake_cy + lake_ry + 12)) / 13.0) ** 2) * np.exp(-((X - lx) / 62.0) ** 2)   # moraine dam

Z = ndi.gaussian_filter(Z, 1.1)

# ------------------------------------------------------------------ tributaries: trace, then carve
def trace(Zs, x0, y0, max_steps=1100, step=3.0):
    gy, gx = np.gradient(Zs, CELL)
    pts = [(x0, y0)]
    x, y, vx, vy = x0, y0, 0.0, 0.0
    for _ in range(max_steps):
        i, j = int(y / CELL), int(x / CELL)
        if i < 1 or i >= NY - 1 or j < 1 or j >= NX - 1:
            return None
        g = math.hypot(gx[i, j], gy[i, j])
        if g < 1e-4:
            return None
        vx = 0.72 * vx + 0.28 * (-gx[i, j] / g)
        vy = 0.72 * vy + 0.28 * (-gy[i, j] / g)
        n = math.hypot(vx, vy) + 1e-9
        x += step * vx / n; y += step * vy / n
        pts.append((x, y))
        row = min(NY - 1, int(y / CELL))
        if glacier_mask[row, min(NX - 1, int(x / CELL))]:
            return None
        if abs(x - xr[row]) < 5:
            return np.array(pts)
    return None

Zs0 = ndi.gaussian_filter(Z, 2.2)
cands = []
for yy in np.arange(1560, 5350, 95):
    for sgn in (-1, 1):
        row = min(NY - 1, int(yy / CELL))
        reach = float(np.interp(yy / H, [0.2, 0.4, 0.6, 0.8], [250, 330, 380, 400]))
        sx = xr[row] + sgn * reach * (0.7 + 0.55 * rng.random())
        if 40 < sx < W - 40:
            p = trace(Zs0, sx, yy + rng.uniform(-80, 50))
            if p is not None and len(p) > 45:
                cands.append(p)
cands.sort(key=lambda p: p[-1, 1])
last_join = {-1: -1e9, 1: -1e9}
picked = []
for p in cands:
    sgn = 1 if p[0, 0] > xr[min(NY - 1, int(p[0, 1] / CELL))] else -1
    if p[-1, 1] - last_join[sgn] > 210:
        picked.append(p); last_join[sgn] = p[-1, 1]

# carve each tributary valley so contours V upstream along it
trib_raster = np.zeros((NY, NX), bool)
depth_w = np.zeros((NY, NX))
for p in picked:
    n = len(p)
    for k_, (px_, py_) in enumerate(p):
        i, j = int(py_ / CELL), int(px_ / CELL)
        if 0 <= i < NY and 0 <= j < NX:
            trib_raster[i, j] = True
            depth_w[i, j] = max(depth_w[i, j], 0.35 + 0.65 * k_ / n)      # deeper toward the confluence
dist = ndi.distance_transform_edt(~trib_raster) * CELL
near_w = ndi.grey_dilation(depth_w, size=(9, 9))
Z -= (0.055 * side + 5.0) * near_w * np.exp(-(dist / 13.0) ** 2)
Z = ndi.gaussian_filter(Z, 0.7)

# sea floor falls away from shore; no stranded below-sea-level pockets inland
Z = np.where(Z < 0, Z * 1.9, Z)
lab, nlab = ndi.label(Z < 0)
sea_ids = set(np.unique(lab[-3:, :])) - {0}
inland = (lab > 0) & ~np.isin(lab, list(sea_ids))
Z = np.where(inland, 1.5, Z)
Z = np.where(lake_mask, 3500.0, Z)

# ------------------------------------------------------------------ contours
levels = []
zmax = float(Z.max())
for lv in range(500, int(zmax) + 1, 100):
    levels.append((lv, "i" if lv % 500 == 0 else "r"))
for lv in (400, 300, 200, 100):
    levels.append((lv, "r"))
for lv in (450, 350, 250, 150, 75, 50, 40, 30, 20, 10):
    levels.append((lv, "s"))            # supplementary, lowland
levels.append((0, "c"))                  # coast
for lv in (-15, -40, -80, -130):
    levels.append((lv, "b"))             # bathymetry

LIGHT = (-0.7071, -0.7071)                 # unit vector toward the light: north-west on the sheet
GYS, GXS = np.gradient(ndi.gaussian_filter(Z, 1.6), CELL)
lines, total_pts = [], 0
for lv, kind in levels:
    tol = 0.16 if kind in ("i", "r", "c") else 0.30
    for c in measure.find_contours(Z, lv):
        if len(c) < 7:
            continue
        c = measure.approximate_polygon(c, tol)
        if len(c) < 4:
            continue
        py = (c[:, 0] + 0.5) * CELL
        px = (c[:, 1] + 0.5) * CELL
        length = float(np.hypot(np.diff(px), np.diff(py)).sum())
        if length < (70 if kind in ("i", "r", "c") else 120):
            continue
        ci = np.clip((py / CELL).astype(int), 0, NY - 1)
        cj = np.clip((px / CELL).astype(int), 0, NX - 1)
        on_ice = bool(glacier_mask[ci, cj].mean() > 0.6)
        # illumination of each segment: is the slope it sits on turned toward the light?
        mxp, myp = (px[:-1] + px[1:]) / 2, (py[:-1] + py[1:]) / 2
        mi = np.clip((myp / CELL).astype(int), 0, NY - 1)
        mj = np.clip((mxp / CELL).astype(int), 0, NX - 1)
        gxs, gys = GXS[mi, mj], GYS[mi, mj]
        gm = np.hypot(gxs, gys)
        b = np.where(gm > 0.02, (-gxs * LIGHT[0] - gys * LIGHT[1]) / np.maximum(gm, 1e-9), 0.0)
        shade = np.clip(((b + 1) / 2 * 5).astype(int), 0, 4)
        lines.append({"z": lv, "k": kind, "g": on_ice, "x": px, "y": py, "s": shade})
        total_pts += len(px)

# ------------------------------------------------------------------ river network
def line_from(y0, y1, offset_fn=None, step=2):
    idx = np.arange(int(y0 / CELL), min(NY, int(y1 / CELL)), step)
    yy = ys[idx]; xx = xr[idx].copy()
    if offset_fn is not None:
        xx = xx + offset_fn(yy)
    return xx, yy

river = []
rx, ry = line_from(lake_cy + lake_ry - 8, 6400)
keep = [(a, b) for a, b in zip(rx, ry) if Z[min(NY - 1, int(b / CELL)), min(NX - 1, int(a / CELL))] > -4]
k_ = np.array(keep)
river.append({"k": "main", "x": k_[:, 0], "y": k_[:, 1]})
mouth_y = float(k_[-1, 1])

def braid(sign, y0, y1, amp_, wl, ph):
    def f(yy):
        env = np.sin(np.clip((yy - y0) / (y1 - y0), 0, 1) * np.pi) ** 0.8
        return sign * amp_ * env * (0.55 + 0.45 * np.sin(yy / wl + ph))
    return f
for sign, y0, y1, a, wl, ph in ((1, 3560, 4420, 30, 95, 0.4), (-1, 3640, 4360, 24, 120, 1.7), (1, 4010, 4700, 19, 80, 2.9)):
    bx, by = line_from(y0, y1, braid(sign, y0, y1, a, wl, ph))
    river.append({"k": "braid", "x": bx, "y": by})

def fan(y0, y1, spread):
    def f(yy):
        s_ = np.clip((yy - y0) / (y1 - y0), 0, 1)
        return spread * s_ ** 1.5 + 5 * np.sin(yy / 38.0) * s_
    return f
for y0, spread in ((5540, -160), (5640, 125), (5760, -66), (5830, 215)):
    dx_, dy_ = line_from(y0, 6500, fan(y0, 6150, spread))
    keep = []
    for a, b in zip(dx_, dy_):
        i = min(NY - 1, int(b / CELL)); j = min(NX - 1, max(0, int(a / CELL)))
        if Z[i, j] < -3:
            break
        keep.append((a, b))
    if len(keep) > 8:
        k_ = np.array(keep)
        river.append({"k": "dist", "x": k_[:, 0], "y": k_[:, 1]})

for p in picked:
    p2 = measure.approximate_polygon(p, 0.8)
    river.append({"k": "trib", "x": p2[:, 0], "y": p2[:, 1]})

# ------------------------------------------------------------------ outlines
def mask_outline(mask, min_len=40, tol=0.6):
    out = []
    for c in measure.find_contours(mask.astype(float), 0.5):
        if len(c) < min_len:
            continue
        c = measure.approximate_polygon(c, tol)
        out.append(((c[:, 1] + 0.5) * CELL, (c[:, 0] + 0.5) * CELL))
    return out

glacier_outline = mask_outline(ndi.binary_opening(glacier_mask, iterations=1))
lake_outline = mask_outline(lake_mask, min_len=12, tol=0.3)
moraines = []
for off in (-0.42, 0.05, 0.47):
    idx = np.arange(int(170 / CELL), int(1215 / CELL), 4)
    moraines.append((xr[idx] + off * gl_half[idx] * 0.86, ys[idx]))

# ------------------------------------------------------------------ labels and spot heights
labels = []
for ln in lines:
    if ln["k"] not in ("i",) and not (ln["k"] == "r" and ln["z"] in (100, 200, 300, 400)):
        continue
    px, py = ln["x"], ln["y"]
    if len(px) < 12:
        continue
    row = np.clip((py / CELL).astype(int), 0, NY - 1)
    off = 228 if ln["z"] >= 500 else 300
    d = np.abs(px - (xr[row] - off))
    k = int(np.argmin(d))
    if d[k] > 18 or k < 3 or k > len(px) - 4:
        continue
    a = math.atan2(py[k + 2] - py[k - 2], px[k + 2] - px[k - 2])
    if a > math.pi / 2: a -= math.pi
    if a < -math.pi / 2: a += math.pi
    labels.append({"x": round(float(px[k]), 1), "y": round(float(py[k]), 1), "a": round(a, 3), "z": ln["z"]})
labels.sort(key=lambda l: l["y"])
thin, lasty = [], -1e9
for l in labels:
    if l["y"] - lasty > 44:
        thin.append(l); lasty = l["y"]
labels = thin

peaks = []
mx = ndi.maximum_filter(Z, size=27)
cand = sorted(np.argwhere((Z == mx) & (Z > 4700)), key=lambda ij: -Z[ij[0], ij[1]])
for i, j in cand:
    px_, py_ = float(xs[j]), float(ys[i])
    if px_ < 45 or px_ > W - 45 or py_ < 70:
        continue
    if all(math.hypot(px_ - p["x"], py_ - p["y"]) > 190 for p in peaks):
        peaks.append({"x": round(px_, 1), "y": round(py_, 1), "z": int(round(Z[i, j]))})
    if len(peaks) >= 8:
        break

# ------------------------------------------------------------------ pack
def pack(px, py):
    """quantise to half-units and delta-encode: [x0, y0, dx1, dy1, ...]"""
    qx = np.round(np.asarray(px) * 2).astype(int)
    qy = np.round(np.asarray(py) * 2).astype(int)
    out = [int(qx[0]), int(qy[0])]
    for a, b in zip(np.diff(qx), np.diff(qy)):
        out.append(int(a)); out.append(int(b))
    return out

packed_lines = [[ln["z"], ln["k"] + ("g" if ln["g"] else ""),
                 int(math.floor(ln["y"].min())), int(math.ceil(ln["y"].max())),
                 pack(ln["x"], ln["y"]), "".join(str(int(v)) for v in ln["s"])] for ln in lines]
packed_lines.sort(key=lambda l: l[2])
packed_river = [[r["k"], int(math.floor(np.min(r["y"]))), int(math.ceil(np.max(r["y"]))), pack(r["x"], r["y"])] for r in river]

step = 20
data = {
    "w": W, "h": H, "q": 2,
    "lines": packed_lines,
    "river": packed_river,
    "glacier": [pack(a, b) for a, b in glacier_outline],
    "moraines": [pack(a, b) for a, b in moraines],
    "lake": [pack(a, b) for a, b in lake_outline],
    "lakeC": [round(lx, 1), lake_cy],
    "mouthY": round(mouth_y, 1),
    "labels": labels,
    "peaks": peaks,
    "profStep": step,
    "prof": [round(float(profile(v)), 1) for v in np.arange(0, H + 1, step)],
    "riverX": [round(float(np.interp(v, ys, xr)), 1) for v in np.arange(0, H + 1, step)],
}
out_js = os.path.join(OUT, "terrain.js")
with open(out_js, "w") as f:
    f.write("/* A computed, fictional transect from a glacier head to the sea. Built by tools/terrain.py. Not a survey of a real place. */\n")
    f.write("window.__TERRAIN__=" + json.dumps(data, separators=(",", ":")) + ";\n")

print(f"lines={len(lines)} pts={total_pts} river_parts={len(river)} tribs={len(picked)} labels={len(labels)} peaks={len(peaks)}")
print(f"zmin={Z.min():.0f} zmax={Z.max():.0f} mouth_y={mouth_y:.0f}")
print("terrain.js", os.path.getsize(out_js))
```

### C.3 tools/terrain_preview.py
```python
#!/usr/bin/env python3
"""QA preview of terrain.js: splits the long strip into panels so it can be inspected."""
import json, re, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

src = open(sys.argv[1] if len(sys.argv) > 1 else "terrain.js").read()
data = json.loads(src[src.index("=") + 1: src.rindex(";")])
Q = data["q"]

def unpack(a):
    a = np.array(a, dtype=float).reshape(-1, 2)
    p = np.cumsum(a, axis=0) / Q
    return p[:, 0], p[:, 1]

PAN = int(sys.argv[3]) if len(sys.argv) > 3 else 4
H, W = data["h"], data["w"]
seg = H / PAN
fig, axes = plt.subplots(1, PAN, figsize=(PAN * 4.2, 4.2 * seg / W), dpi=110)
for pi, ax in enumerate(np.atleast_1d(axes)):
    y0, y1 = pi * seg, (pi + 1) * seg
    dark = y0 < 1900
    bg = "#161D24" if dark else "#FAF7F2"
    ink = (245/255, 242/255, 235/255) if dark else (24/255, 24/255, 27/255)
    teal = "#58B8AC" if dark else "#0F766E"
    ax.set_facecolor(bg)
    from matplotlib.collections import LineCollection
    for z, k, ya, yb, pts, sh in data["lines"]:
        if yb < y0 or ya > y1:
            continue
        x, y = unpack(pts)
        g = k.endswith("g"); kk = k[0]
        if kk in "cb" or g:
            lw, al = (1.2, 0.9) if kk == "c" else (0.5, 0.5)
            ax.plot(x, y, color=teal, lw=lw, alpha=al, ls="--" if kk == "b" else "-")
            continue
        base = {"i": 1.0, "r": 0.62, "s": 0.5}[kk]
        segs = np.stack([np.column_stack([x[:-1], y[:-1]]), np.column_stack([x[1:], y[1:]])], axis=1)
        shv = np.array([int(c) for c in sh])
        if dark:
            lit = np.array([0.10, 0.17, 0.30, 0.52, 0.82])[shv]
            cols = [(245/255, 242/255, 235/255, a) for a in lit]
            lws = base * np.array([0.55, 0.6, 0.7, 0.9, 1.15])[shv]
        else:
            lit = np.array([0.40, 0.28, 0.17, 0.10, 0.06])[shv]
            cols = [(24/255, 24/255, 27/255, a) for a in lit]
            lws = base * np.array([1.05, 0.9, 0.7, 0.6, 0.55])[shv]
        ax.add_collection(LineCollection(segs, colors=cols, linewidths=lws, capstyle="round"))
    for k, ya, yb, pts in data["river"]:
        x, y = unpack(pts)
        ax.plot(x, y, color=teal, lw={"main": 1.8, "braid": 1.0, "dist": 1.0, "trib": 0.7}[k], alpha=0.95)
    for pts in data["glacier"]:
        x, y = unpack(pts); ax.plot(x, y, color=teal, lw=0.8, alpha=0.7)
    for pts in data["moraines"]:
        x, y = unpack(pts); ax.plot(x, y, color=teal, lw=0.6, alpha=0.5, ls=":")
    for pts in data["lake"]:
        x, y = unpack(pts); ax.fill(x, y, color=teal, alpha=0.35); ax.plot(x, y, color=teal, lw=1)
    for l in data["labels"]:
        if y0 <= l["y"] <= y1:
            ax.text(l["x"], l["y"], f'{l["z"]:,}', color=ink, fontsize=5, rotation=-np.degrees(l["a"]), ha="center", va="center",
                    bbox=dict(fc=bg, ec="none", pad=0.6))
    for p in data["peaks"]:
        if y0 <= p["y"] <= y1:
            ax.plot(p["x"], p["y"], "^", color=ink, ms=3); ax.text(p["x"] + 10, p["y"], f'{p["z"]:,}', color=ink, fontsize=5, va="center")
    ax.set_xlim(0, W); ax.set_ylim(y1, y0); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"y {int(y0)}–{int(y1)}", fontsize=7)
plt.tight_layout(pad=0.3)
out = sys.argv[2] if len(sys.argv) > 2 else "terrain_preview.png"
plt.savefig(out)
print("saved", out)
```

### C.4 tools/maps.mjs
```javascript
// Builds the small locator maps used on the site as inline SVG.
// Data: Natural Earth (public domain) via world-atlas / us-atlas / natural-earth-vector.
// No political boundaries are drawn outside the United States: the South Asia plates
// show coast, rivers and glaciers only.
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import * as d3 from "d3-geo";
import * as topojson from "topojson-client";

const OUT = "maps";
fs.mkdirSync(OUT, { recursive: true });
const read = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
const r1 = (s) => s.replace(/-?\d+\.\d+/g, (m) => (+m).toFixed(1).replace(/\.0$/, ""));
const msx = (args) => execFileSync("node_modules/.bin/mapshaper", args, { stdio: ["ignore", "pipe", "pipe"], maxBuffer: 1 << 28 });

function clipSimplify(src, bbox, pct, extra = []) {
  const tmp = `${OUT}/_tmp.geojson`;
  msx([src, ...extra, "-clip", `bbox=${bbox.join(",")}`, "-simplify", `${pct}%`, "keep-shapes", "-o", "force", tmp]);
  const g = read(tmp); fs.unlinkSync(tmp); return g;
}
const marker = (xy, label, opt = {}) => {
  const [x, y] = xy.map((v) => +v.toFixed(1));
  const dx = opt.dx ?? 9, dy = opt.dy ?? 4, anchor = opt.anchor ?? "start";
  return `<g class="mk${opt.cls ? " " + opt.cls : ""}"><circle class="mk-ring" cx="${x}" cy="${y}" r="7"/><circle class="mk-dot" cx="${x}" cy="${y}" r="2.6"/>` +
    (label ? `<text class="mk-label" x="${x + dx}" y="${y + dy}" text-anchor="${anchor}">${label}</text>` : "") + `</g>`;
};
// pre-simplified sources (shared borders preserved)
msx(["node_modules/us-atlas/states-10m.json", "-simplify", "4.5%", "keep-shapes", "-o", "force", "format=topojson", `${OUT}/_us.json`]);
msx(["node_modules/world-atlas/land-110m.json", "-simplify", "58%", "keep-shapes", "-o", "force", "format=geojson", `${OUT}/_world.geojson`]);
msx(["node_modules/world-atlas/land-110m.json", "-filter-islands", "min-area=180000km2", "-simplify", "13%", "-o", "force", "format=geojson", `${OUT}/_world_tiny.geojson`]);
const r0 = (s) => s.replace(/-?\d+\.\d+/g, (m) => String(Math.round(+m)));
const frame = (w, h) => `<rect class="neat" x="0.5" y="0.5" width="${w - 1}" height="${h - 1}"/>`;
const wrap = (w, h, title, desc, body) =>
  `<svg class="map" viewBox="0 0 ${w} ${h}" role="img" aria-label="${title}" xmlns="http://www.w3.org/2000/svg"><title>${title}</title><desc>${desc}</desc>${body}</svg>\n`;

// ---------------------------------------------------------------- 1. world
{
  const W = 720, H = 380;
  const land = read(`${OUT}/_world.geojson`);
  const tiny = read(`${OUT}/_world_tiny.geojson`);
  const proj = d3.geoEqualEarth().fitExtent([[10, 12], [W - 10, H - 12]], { type: "Sphere" });
  const path = d3.geoPath(proj);
  const grat = d3.geoGraticule().step([30, 30])();
  const box = (w, s, e, n) => ({ type: "Polygon", coordinates: [[[w, s], [w, n], [e, n], [e, s], [w, s]].map((c) => c)] });
  // densify extent boxes so they follow the projection
  const dense = (w, s, e, n) => {
    const pts = []; const k = 12;
    for (let i = 0; i <= k; i++) pts.push([w + (e - w) * i / k, s]);
    for (let i = 0; i <= k; i++) pts.push([e, s + (n - s) * i / k]);
    for (let i = 0; i <= k; i++) pts.push([e - (e - w) * i / k, n]);
    for (let i = 0; i <= k; i++) pts.push([w, n - (n - s) * i / k]);
    return "M" + pts.map((p) => proj(p).map((v) => v.toFixed(1)).join(",")).join("L") + "Z";
  };
  const body =
    `<path class="sphere" d="${r1(path({ type: "Sphere" }))}"/>` +
    `<path class="grat" d="${r1(path(grat))}"/>` +
    `<path class="land" d="${r1(path(land))}"/>` +
    `<path class="extent" d="${dense(60.5, 23.2, 78, 37.3)}"/>` +
    `<path class="extent" d="${dense(-107, 24.5, -75, 39.5)}"/>` +
    marker(proj([-73.968, 40.749]), "United Nations, New York", { dx: 10, dy: -8 });
  fs.writeFileSync(`${OUT}/world.svg`, wrap(W, H, "World map marking United Nations headquarters in New York",
    "Equal Earth projection. Two outlined boxes mark the extents of the next two plates: the Indus basin and the southern United States.", body));
  // tiny locator version (no labels)
  const w2 = 150, h2 = 80;
  const p2 = d3.geoEqualEarth().fitExtent([[2, 2], [w2 - 2, h2 - 2]], { type: "Sphere" });
  const path2 = d3.geoPath(p2);
  const loc = (cls, lonlat) => { const [x, y] = p2(lonlat); return `<circle class="loc-dot ${cls}" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="3.2"/>`; };
  fs.writeFileSync(`${OUT}/locator.svg`,
    `<svg class="locator" viewBox="0 0 ${w2} ${h2}" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><path class="sphere" d="${r0(path2({ type: "Sphere" }))}"/><path class="land" d="${r0(path2(tiny))}"/>` +
    loc("loc-pk", [69.5, 30]) + loc("loc-us", [-90, 33]) + loc("loc-gb", [74.6, 36]) + loc("loc-tx", [-96.3, 30.6]) + `</svg>\n`);
}

// ---------------------------------------------------------------- 2. Indus basin (no boundaries)
{
  const W = 720, H = 520;
  const bbox = [60.5, 23.2, 78, 37.3];
  const land = clipSimplify("node_modules/world-atlas/land-10m.json", bbox, 9);
  const riv = clipSimplify("ne/ne_10m_rivers_lake_centerlines.geojson", bbox, 30, ["-filter", `['Indus','Jhelum','Chenab','Ravi','Sutlej','Beas'].includes(name)`]);
  const gl = clipSimplify("ne/ne_10m_glaciated_areas.geojson", bbox, 5);
  const ext = { type: "Polygon", coordinates: [[[bbox[0], bbox[1]], [bbox[0], bbox[3]], [bbox[2], bbox[3]], [bbox[2], bbox[1]], [bbox[0], bbox[1]]]] };
  const proj = d3.geoConicConformal().parallels([26, 34]).rotate([-69.5, 0]).fitExtent([[0, 0], [W, H]], ext).clipExtent([[0, 0], [W, H]]);
  const path = d3.geoPath(proj);
  const P = (lon, lat) => proj([lon, lat]);
  const label = (cls, lonlat, text, rot = 0) => { const [x, y] = P(...lonlat); return `<text class="${cls}" x="${x.toFixed(1)}" y="${y.toFixed(1)}"${rot ? ` transform="rotate(${rot} ${x.toFixed(1)} ${y.toFixed(1)})"` : ""}>${text}</text>`; };
  const indus = riv.features.filter((f) => f.properties.name === "Indus");
  const others = riv.features.filter((f) => f.properties.name !== "Indus");
  const body =
    `<rect class="sea" width="${W}" height="${H}"/>` +
    `<path class="land" d="${r1(path(land))}"/>` +
    `<path class="ice" d="${r1(path(gl))}"/>` +
    `<path class="river river-minor" d="${r1(path({ type: "FeatureCollection", features: others }))}"/>` +
    `<path class="river river-main" d="${r1(path({ type: "FeatureCollection", features: indus }))}"/>` +
    label("lb-region", [71.2, 34.35], "Khyber Pakhtunkhwa") + label("lb-region", [72.15, 30.35], "Punjab") +
    label("lb-region", [64.3, 28.2], "Balochistan") + label("lb-region", [68.0, 26.35], "Sindh") +
    label("lb-water", [63.6, 24.2], "Arabian Sea") + label("lb-river", [70.35, 28.05], "Indus", -52) +
    label("lb-ice", [75.2, 36.55], "Karakoram") +
    marker(P(74.34, 31.55), "Lahore", { dx: 10, dy: 4 }) +
    frame(W, H);
  fs.writeFileSync(`${OUT}/indus.svg`, wrap(W, H, "The Indus river system from the Karakoram to the Arabian Sea",
    "Rivers, glaciers and coast only. Labels mark Khyber Pakhtunkhwa, Punjab, Balochistan and Sindh, and Lahore.", body));
}

// ---------------------------------------------------------------- 3. southern and eastern United States
function usMap(file, { highlight, markers, title, desc }) {
  const W = 720, H = 430;
  const us = read(`${OUT}/_us.json`);
  const states = topojson.feature(us, us.objects.states).features;
  const bboxPoly = { type: "MultiPoint", coordinates: [[-106.8, 25.6], [-75.4, 25.2], [-75.2, 39.4], [-106.9, 37.2], [-93, 24.6]] };
  const proj = d3.geoAlbers().rotate([92, 0]).center([0, 32]).parallels([27, 37]).fitExtent([[14, 14], [W - 14, H - 14]], bboxPoly).clipExtent([[0, 0], [W, H]]);
  const path = d3.geoPath(proj);
  const keep = states.filter((s) => { const c = d3.geoCentroid(s); return c[0] > -112 && c[0] < -72 && c[1] > 23 && c[1] < 44; });
  const hl = new Set(highlight);
  let body = `<defs><pattern id="hatch-${file}" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(38)"><line class="hatch-line" x1="0" y1="0" x2="0" y2="5"/></pattern></defs>`;
  body += `<path class="land" d="${r1(path({ type: "FeatureCollection", features: keep.filter((s) => !hl.has(s.id)) }))}"/>`;
  for (const s of keep.filter((s) => hl.has(s.id))) {
    const d = r1(path(s));
    body += `<path class="land state-hl" d="${d}"/><path class="state-hatch" fill="url(#hatch-${file})" d="${d}"/>`;
  }
  body += `<path class="state-lines" d="${r1(path(topojson.mesh(us, us.objects.states, (a, b) => a !== b)))}"/>`;
  for (const m of markers) body += marker(proj(m.at), m.label, m);
  fs.writeFileSync(`${OUT}/${file}.svg`, wrap(W, H, title, desc, body));
}
usMap("us-interviews", {
  highlight: ["48", "22", "12", "37"],
  markers: [],
  title: "Texas, Louisiana, Florida and North Carolina highlighted on a map of the southern United States",
  desc: "The four states where the dissertation's 26 interviews with emergency managers took place.",
});
usMap("us-recovery", {
  highlight: ["48", "21", "37"],
  markers: [
    { at: [-97.743, 30.267], label: "Austin, TX", dx: -10, dy: -9, anchor: "end" },
    { at: [-88.637, 36.742], label: "Mayfield, KY", dx: 0, dy: -13, anchor: "middle" },
    { at: [-79.009, 34.618], label: "Lumberton, NC", dx: -8, dy: 20, anchor: "end" },
  ],
  title: "Austin, Texas; Mayfield, Kentucky; and Lumberton, North Carolina marked on a map of the southern United States",
  desc: "Three places where the municipal and community recovery work took place.",
});

// ---------------------------------------------------------------- 4a. Texas (heritage workshop)
{
  const W = 340, H = 330;
  const us = read(`${OUT}/_us.json`);
  const tx = topojson.feature(us, us.objects.states).features.find((s) => s.id === "48");
  const proj = d3.geoConicConformal().parallels([27.5, 35]).rotate([99.5, 0]).fitExtent([[12, 12], [W - 12, H - 12]], tx);
  const path = d3.geoPath(proj);
  const body = `<path class="land state-hl" d="${r1(path(tx))}"/>` +
    marker(proj([-96.334, 30.628]), "College Station", { dx: -10, dy: -9, anchor: "end" });
  fs.writeFileSync(`${OUT}/texas.svg`, wrap(W, H, "Texas, with College Station marked", "Site of the Rural Heritage Resilience Workshop at Texas A&M University.", body));
}

// ---------------------------------------------------------------- 4b. upper Indus and Karakoram glaciers (no boundaries)
{
  const W = 340, H = 330;
  const bbox = [72.6, 34.55, 77.3, 37.25];
  const gl = clipSimplify("ne/ne_10m_glaciated_areas.geojson", bbox, 16);
  const riv = clipSimplify("ne/ne_10m_rivers_lake_centerlines.geojson", bbox, 60, ["-filter", `name=='Indus'`]);
  const ext = { type: "Polygon", coordinates: [[[bbox[0], bbox[1]], [bbox[0], bbox[3]], [bbox[2], bbox[3]], [bbox[2], bbox[1]], [bbox[0], bbox[1]]]] };
  const proj = d3.geoConicConformal().parallels([35, 37]).rotate([-74.95, 0]).fitExtent([[0, 0], [W, H]], ext).clipExtent([[0, 0], [W, H]]);
  const path = d3.geoPath(proj);
  const P = (lon, lat) => proj([lon, lat]);
  const lb = (cls, lonlat, text, rot = 0) => { const [x, y] = P(...lonlat); return `<text class="${cls}" x="${x.toFixed(1)}" y="${y.toFixed(1)}"${rot ? ` transform="rotate(${rot} ${x.toFixed(1)} ${y.toFixed(1)})"` : ""}>${text}</text>`; };
  const body =
    `<rect class="land" width="${W}" height="${H}"/>` +
    `<path class="ice" d="${r1(path(gl))}"/>` +
    `<path class="river river-main" d="${r1(path(riv))}"/>` +
    lb("lb-river", [75.95, 35.02], "Indus", -24) + lb("lb-ice", [75.55, 36.02], "Karakoram glaciers") +
    marker(P(74.62, 36.31), "Hunza", { dx: -10, dy: -8, anchor: "end" }) +
    marker(P(74.31, 35.92), "Gilgit", { dx: -10, dy: 14, anchor: "end" }) +
    marker(P(75.63, 35.30), "Skardu", { dx: 10, dy: 15 }) +
    frame(W, H);
  fs.writeFileSync(`${OUT}/karakoram.svg`, wrap(W, H, "The upper Indus and the Karakoram glaciers, with Hunza, Gilgit and Skardu marked",
    "Glaciers and the Indus only. No boundaries are drawn.", body));
}

for (const f of fs.readdirSync(OUT)) if (f.startsWith("_")) fs.unlinkSync(`${OUT}/${f}`);
for (const f of fs.readdirSync(OUT)) console.log(f, fs.statSync(`${OUT}/${f}`).size);
```

### C.5 tools/shot.mjs (Playwright screenshot helper)
```javascript
import { chromium } from "/opt/npm-tools/node_modules/playwright/index.mjs";
const [,, url, out, w = "1440", h = "900", full = "1"] = process.argv;
const browser = await chromium.launch({ executablePath: "/usr/bin/google-chrome", args: ["--no-sandbox", "--allow-file-access-from-files"] });
const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
const errs = [];
page.on("console", (m) => { if (m.type() === "error") errs.push(m.text()); });
page.on("pageerror", (e) => errs.push("PAGEERROR " + e.message));
await page.goto(url, { waitUntil: "load" });
await page.waitForTimeout(700);
await page.screenshot({ path: out, fullPage: full === "1" });
if (errs.length) console.log("ERRORS:\n" + errs.join("\n"));
await browser.close();
console.log("shot", out);
```

### C.6 Map stylesheet used for the check page (maps_check.html head; reuse in site.css)
```html
<!doctype html><meta charset="utf-8"><style>
body{margin:0;background:#FAF7F2;font-family:sans-serif;display:grid;grid-template-columns:1fr 1fr;gap:14px;padding:14px}
.map{width:100%;height:auto;display:block}
.sphere{fill:#F2ECE1;stroke:rgba(24,24,27,.25);stroke-width:.8}.grat{fill:none;stroke:rgba(24,24,27,.10);stroke-width:.5}
.land{fill:#E9E1D2;stroke:rgba(24,24,27,.45);stroke-width:.6}.sea{fill:#F2ECE1}
.extent{fill:none;stroke:#B45309;stroke-width:1}.neat{fill:none;stroke:rgba(24,24,27,.3)}
.ice{fill:rgba(15,118,110,.22);stroke:#0F766E;stroke-width:.3}.river{fill:none;stroke:#0F766E;stroke-linecap:round;stroke-linejoin:round}
.river-main{stroke-width:1.8}.river-minor{stroke-width:.9}
.state-lines{fill:none;stroke:rgba(24,24,27,.3);stroke-width:.5}.state-hl{fill:#EADBC4}.hatch-line{stroke:#B45309;stroke-width:1.1}
.mk-ring{fill:none;stroke:#B45309;stroke-width:1}.mk-dot{fill:#B45309}.mk-label{font:600 13px sans-serif;fill:#18181B}
.lb-region{font:12px sans-serif;fill:#57534E;text-anchor:middle}.lb-water,.lb-river,.lb-ice{font:italic 12px serif;fill:#0F766E}
.locator{width:300px}.loc-dot{fill:#B45309}
</style>
```

### C.7 Commands
```bash
npm install
mkdir -p ne && for f in ne_10m_rivers_lake_centerlines ne_10m_glaciated_areas; do curl -sSL -o ne/$f.geojson "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/$f.geojson"; done
python3 terrain.py tout            # -> tout/terrain.js (copy to site/assets/js/)
python3 terrain_preview.py tout/terrain.js terrain_preview.png 4
node maps.mjs                      # -> maps/*.svg (copy to site/assets/maps/)
node shot.mjs file:///abs/path/index.html shot.png 1440 900 1
```

_End of handoff._
