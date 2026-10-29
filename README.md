# New Madison Development — website

A plain HTML/CSS website. There is no build step: what you see in these files is exactly what gets published.

## What's where

| File or folder | What it is |
|---|---|
| `index.html` | Home page |
| `projects/index.html` | Projects grid |
| `projects/*.html` | One page per project |
| `about.html`, `contact.html` | About and Contact |
| `brand/index.html` | One-page brand sheet (logo, colors, type). Not linked from the menu. |
| `assets/css/site.css` | All the styling. Colors and fonts are set at the top. |
| `assets/js/site.js` | Small script for the mobile menu and scroll animations. |
| `assets/img/projects/` | Photos used on the site (web-sized copies) |
| `assets/img/logo/` | Logo files used on the site |
| `content/` | William's source material (`content-v3.md`, original full-size photos and logos). Not published. |
| `notes/` | Decisions, sources and next steps. Not published. |

## Preview it on your computer

Double-click `index.html` to open it in a browser. Everything works that way.

## Change text

1. Open the page's `.html` file in any text editor (or click the pencil icon on GitHub).
2. Find the sentence you want to change (Ctrl/Cmd + F) and type over it. Only change words between the `>` and `<` marks; leave the tags alone.
3. Save (or "Commit changes" on GitHub).

Things that appear on every page, like the menu, phone number, email and footer, are repeated in every `.html` file. If you change one, use search-and-replace across all files (on GitHub, edit each file; in an editor like VS Code, use "Replace in files"). Every page has comments marking the `HEADER` and `FOOTER` sections.

Project facts must match `content/content-v3.md`. **No construction costs, acquisition prices, financing, sale prices, valuations, rents or loan information anywhere.**

## Swap or add a photo

1. Resize the photo to about **2400 px wide** at most and save it as a JPG (quality about 80). Aim for under 700 KB. Keep the full-size original in `content/photos/` (not published).
2. Put it in `assets/img/projects/`, with a simple lowercase name, e.g. `traders-way-courtyard.jpg`.
3. In the HTML, find the `<img ...>` you want to replace and change:
   - `src="..."` to the new file path,
   - `width="..."` and `height="..."` to the new photo's pixel size,
   - `alt="..."` to a one-sentence description of the photo (for screen readers and search engines).
4. If that `<img>` also has a `srcset="..."` part (a list of the same photo at two sizes for phones and desktops), either delete the whole `srcset="..."` and `sizes="..."` attributes, or also save a smaller copy (1000–1200 px wide) and update both paths and widths.

Photo frames crop automatically to fit, so any reasonably sized landscape photo works.

## The project map

The map on Home and Projects is a real street map from **OpenStreetMap**, shown with the free Leaflet map library (bundled in `assets/vendor/leaflet/`, no account or key needed). It is toned dark to match the site.

**To move a pin:** open `assets/js/projects-map.js`. Each project has a line with `lat` and `lng`. In Google Maps, right-click the building, click the coordinates at the top of the menu to copy them, and paste the two numbers in. Save; that's it.

If JavaScript is off, a simple drawn map shows instead.

## Change colors or fonts

Open `assets/css/site.css`. The brand colors are listed at the top under `:root` (e.g. `--bg: #F5F4F0;`). Change a value there and it changes everywhere.

## The logo

The logo is used exactly as drawn. The transparent PNGs in `assets/img/logo/` and `brand/downloads/` were made from `content/logo/` by removing the white background only. Don't redraw or edit it.

## Publishing

The site is ready for GitHub Pages (Settings → Pages → Deploy from branch → `main`, folder `/ (root)`). That has **not** been turned on. See `notes/next-steps.md` before going live.
