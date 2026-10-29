# Design decisions

Each one is easy to change. Later instructions from William replaced earlier ones; this file reflects the final state.

## Identity
- **Logo: the existing NMD logo, used exactly as drawn.** Transparent versions were made only by turning the white background transparent (black line art kept exactly), plus the same artwork in white for photos and dark backgrounds. Web sizes in `assets/img/logo/`, full size in `brand/downloads/`. An early draft wordmark from before William's correction was discarded; none of it is in the repo.
- **Square logo top left in the header; white circle logo centered over the home hero** (Alta-style). On the home page the header logo stays hidden until you scroll, so the logo never appears twice on screen.
- **Palette (Haussmann-led):** warm off-white `#F5F4F0`, ink `#1A1A1A`, charcoal `#1E1E1E` for the map section and dark tiles, stone `#E6E3DB`, and copper `#9A5527` as the one restrained accent. No reds or navy, so it stays clearly apart from Principal Madison.
- **Type:** Hanken Grotesk for everything (Light 300 headlines in sentence case ending with a period; small uppercase letter-spaced labels and nav), plus Instrument Serif for the single "statement" moment (Extell-style). Fonts are self-hosted. Not League Gothic or Montserrat.

## Layout (blend of the three reference sites)
- **Home:** full-bleed aerial hero (William's Starkweather drone shot) with the white logo, "Madison, built forward." and a SCROLL chevron → short intro → four solid-color stat tiles (256 / 5 / 27,000 SF / 2) → "Featured projects." row of tall portrait cards that scrolls sideways, with an underlined VIEW ALL PROJECTS link → centered serif statement over The Tinsmith photo → dark charcoal map with numbered white pins and a numbered list → Recognition list → contact.
- **Project cards:** category tag + "Completed" tag on the photo, small uppercase neighborhood line above the name; on the Projects page each card also shows three key numbers as large numerals.
- **Project pages:** full-bleed photo hero with the title over it (except 210 S Dickinson, whose photos are too small for full-bleed and are shown as before/after pairs instead), four number tiles, then overview, features/tenants/recognition, timeline and an "At a glance" table.
- **Motion:** subtle fade-up reveals on scroll, a gentle zoom on the hero photo as you scroll, header hides on scroll down. All motion is off for visitors who ask their device to reduce motion.

## Content handling
- **Facts come only from `content/content-v3.md`.** No construction costs, acquisition prices, financing, sale prices, valuations, rents or loan information. (The earlier v2 figures are not used anywhere.)
- **Starkweather photos:** the drone shot is the home hero and the Starkweather Place page hero; the rendering stays as the building image on its card and page gallery; photo 2 is in the page gallery. Captions say they show the setting.
- **"Then" in timelines** marks events `content-v3.md` gives without a year (e.g. annexation, the Trader's Way votes).
- **210 S Dickinson:** the single before/after sheet was cut into two before/after pairs; burned-in labels were cropped off and replaced with the site's own tags. The second pair is captioned "Dewey Court side", as printed on the original sheet.
- **Northern Court patio photo:** thin blue/dark frame lines on its edges were trimmed.
- **Neighborhood lines** use what the content gives: East side, West side, E Main Street, Marquette, Off E Washington Ave.
- **Stats:** "27,000 SF" is labeled "about", matching the content (9,000 + 6,158 + 12,000).
- **Contact:** email and phone links, no form. Eric Welch shown with title and email.
- **Partner portraits (About):** William's photo is the headshot from the Principal Madison About page, taken from his own document in Google Drive (998 E Main listing proposal, page 8, printed beside his name). No photo of Eric was found in Drive. A portrait taken from the internet could easily show a different Eric Welch, so his spot is a quiet "EW" tile in the same frame. Portraits show in black and white and turn to color on hover, so the two match.
- **Trader's Way plans:** the site plan and a one-bedroom floor plan come from William's Trader's Way leasing brochure in Drive. The brochure outlined three available units in red. Only those outlines were recolored to neutral gray, since leasing callouts don't belong on the company site.
- **Concise copy:** each project page says things once. Numbers sit in the tiles, dates in the timeline, and names and addresses in "At a glance". The overview is one or two short sentences.

## Map
- **OpenStreetMap street map, as on the Principal Madison site** (William's request). It is shown with Leaflet, which is bundled in `assets/vendor/leaflet/` (BSD license), so it doesn't depend on a CDN. Standard OpenStreetMap tiles are toned to dark charcoal with a CSS filter, so the map matches the Haussmann-style dark map section. White numbered pins match the numbered list; hovering a list row lights its pin.
- Scroll-wheel zoom is off so the map doesn't trap page scrolling, and on phones one finger scrolls the page (zoom with the +/- buttons).
- Attribution "© OpenStreetMap contributors" is shown as OpenStreetMap requires. OpenStreetMap's free tile server is fine for a small company site. If traffic ever grows a lot, switch the tile address in `projects-map.js` to a paid tile provider.
- **Pin positions are estimates.** Address lookup services were blocked from the build environment, so only Trader's Way has a published nearby coordinate (6614 Old Sauk Rd). The other four were placed by hand and must be checked (see next-steps).
- Without JavaScript, the earlier simple drawn map shows instead.

## Technical
- Plain HTML/CSS/JS, no build step, relative links (works on a custom domain, at a `github.io/nmd-website/` address, or opened from disk).
- **Photos resized for the web** (max 2400 px, JPG quality ~76–80) with a smaller copy for phones via `srcset`. Originals stay in `content/photos/` and are **not published**: `_config.yml` excludes `content/`, `notes/` and `README.md` from GitHub Pages.
- `404.html` uses root-relative links, which is correct once the custom domain is set.
- `/brand` is published but not linked from the menu, and is marked `noindex`.
