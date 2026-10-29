# New Madison Development website

Static site for New Madison Development. No build tools needed to view it: open `index.html`.

- `tools/build.py` holds every fact on the site (taken from `content/content-v3.md`) and writes `index.html` and `projects/*.html`. Edit it, then run `python3 tools/build.py`.
- `assets/site.css` is the design.
- `img/` holds web-sized photos and the logo (transparent ink and white versions made from Maryrose's originals in `content/logo/`).
- Hosted with GitHub Pages from the `main` branch, root folder.
