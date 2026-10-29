# Next steps

There are **no placeholders on the site**. Everything visible comes from `content/content-v3.md` and William's photos.

## Please check before launch
1. **Headlines and framing lines** (not facts, edit freely): "Madison, built forward.", "Featured projects.", "Across Madison.", "Where we build.", "Five projects. All completed.", "Two partners. One city.", "Let's talk.", "Talk with William."
2. **Map:** pins are placed from the geocoded addresses. Give the map one look in a browser; the street map couldn't be viewed from the build environment.
3. **Starkweather Place:** "95% leased by mid-2026" is shown (it is in the content file). Remove it if you'd rather not.
4. **Northern Court tenants** and the Imaginary Factory founder's James Beard finalist line.
5. **210 S Dickinson photo crops** (four images cut from one sheet).
6. **Eric Welch's email** (eric@newmadisondevelopment.com) is public on About and Contact.

## Content that would make it better
- **Finished-building photos** of Starkweather Place and Trader's Way (exterior and amenity shots). Both cards and the Trader's Way hero use renderings, which are low resolution (1400 px and 1200 px wide). Trader's Way's full-bleed hero will look soft on large screens until a real photo replaces it.
- **Higher-resolution Dickinson before/after photos** (current ones are 650 px wide each). With a large "after" photo, that page could get a full-bleed hero like the others.
- **More Tinsmith and Northern Court photos** (exteriors, roofs).
- **A photo of Eric** (about 700×875 px, portrait). Save it as `assets/img/people/eric-welch.jpg` and, in `about.html`, replace the `EW` tile with an `<img>` like William's. A one-line bio for Eric would help too.

## Before going live (not done, per instructions)
- Turn on GitHub Pages (Settings → Pages → `main`, `/ (root)`) and connect newmadisondevelopment.com.
- Then add a full-URL share image to each page's `<head>`: `<meta property="og:image" content="https://newmadisondevelopment.com/assets/img/share.jpg">` (the image, from the drone shot, is already in `assets/img/share.jpg`).
- Optionally add `sitemap.xml` once the domain is known.
