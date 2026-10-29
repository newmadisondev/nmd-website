"""Builds the New Madison Development site from the facts below.

Every fact here comes from content/content-v3.md. Edit this file, then run
    python3 tools/build.py
from the repo root to regenerate index.html and projects/*.html.
"""
import html, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;1,300&family=Hanken+Grotesk:wght@200;300;400;500&family=IBM+Plex+Mono:wght@400;600&display=swap">')

COMPANY = ("New Madison Development (NMD) is a Madison, Wisconsin development company led by partners "
           "William Butcher and Eric Welch. NMD builds new housing and gives older industrial buildings new uses. "
           "On its two apartment projects NMD is joint venture partner with Stone House Development.")

STATS = [("5", "projects"), ("256", "new apartments"), ("27,000", "square feet of industrial buildings reused (about)"),
         ("2", "joint ventures with Stone House Development")]

# lat/lon are approximate, for a schematic map only
PROJECTS = [
    dict(slug="starkweather-place", name="Starkweather Place", short="Starkweather Place",
         address="215 N Fair Oaks Avenue, Madison", area="East side", kind="Multifamily, new construction",
         partner="NMD with Stone House Development", status="Completed", year="2024", units="112 apartments",
         card_img="starkweather-rendering.jpg", hero_img="starkweather-drone.jpg", lat=43.0995, lon=-89.3410,
         lede="112 apartments on Starkweather Creek, with 2.5 acres of restored creek frontage.",
         facts=["112 apartments, four stories, on 4.33 acres.",
                "Site put under contract in 2020 in the Town of Blooming Grove, annexed into Madison, rezoned November 2022.",
                "Underground parking, rooftop solar, dog park, canoe and kayak storage, and 2.5 acres of restored Starkweather Creek frontage.",
                "Designed by Potter Lawson. Built by McGann Construction.",
                "Opened November 1, 2024. 95% leased by mid-2026."],
         rows=[("Address", "215 N Fair Oaks Avenue, Madison"), ("Type", "Multifamily, new construction"),
               ("Apartments", "112"), ("Site", "4.33 acres"), ("Partner", "Stone House Development"),
               ("Architect", "Potter Lawson"), ("Builder", "McGann Construction"), ("Opened", "November 1, 2024")],
         link=("starkweatherplace.com", "https://starkweatherplace.com"),
         gallery=[("starkweather-rendering.jpg", "Rendering: Potter Lawson", True),
                  ("starkweather-creek.jpg", "Starkweather Creek frontage", False),
                  ("starkweather-drone.jpg", "Aerial, Starkweather Creek", False)]),
    dict(slug="traders-way", name="Trader’s Way", short="Trader’s Way",
         address="6624 Old Sauk Road, Madison", area="West side", kind="Multifamily, new construction",
         partner="NMD with Stone House Development", status="Completed", year="2026", units="144 apartments",
         card_img="traders-way-rendering.jpg", hero_img="traders-way-rendering.jpg", framed=True, hero_cap="Rendering: Potter Lawson", lat=43.0830, lon=-89.5050,
         lede="144 apartments on a four-acre former farmstead on the west side.",
         facts=["144 apartments in three stories on a four-acre former farmstead, put under contract in 2023.",
                "Rezoning approved unanimously by the Plan Commission, then by the City Council.",
                "Outdoor pool, hot tub, sauna, coworking space, green roofs, underground parking with EV charging.",
                "Designed by Potter Lawson. Built by Stevens Construction.",
                "Opened September 15, 2026."],
         rows=[("Address", "6624 Old Sauk Road, Madison"), ("Type", "Multifamily, new construction"),
               ("Apartments", "144"), ("Site", "About four acres"), ("Partner", "Stone House Development"),
               ("Architect", "Potter Lawson"), ("Builder", "Stevens Construction"), ("Opened", "September 15, 2026")],
         link=None,
         gallery=[("traders-way-rendering.jpg", "Rendering: Potter Lawson", True)]),
    dict(slug="the-tinsmith", name="The Tinsmith", short="The Tinsmith",
         address="828 E Main Street, Madison", area="East Main Street", kind="Adaptive reuse",
         partner="NMD project, William Butcher and Eric Welch", status="Completed", year="2020", units="About 9,000 SF",
         card_img="tinsmith-solarium.jpg", hero_img="tinsmith-solarium.jpg", lat=43.0806, lon=-89.3727,
         lede="Two Trachte steel warehouses, kept instead of demolished, now a wedding and event venue.",
         facts=["Two joined Trachte steel warehouses, about 9,000 SF under barrel-vaulted roofs. Trachte was the Madison company that patented the prefabricated steel building.",
                "Acquired in 2018 after a seven-year pursuit.",
                "Converted, instead of demolished, into The Tinsmith, a wedding and event venue with a glass solarium courtyard. Opened 2020.",
                "Adaptive Reuse Project of the Year 2021, Madison Trust for Historic Preservation. Voted best venue by Wisconsin Bride four years running."],
         rows=[("Address", "828 E Main Street, Madison"), ("Type", "Adaptive reuse"), ("Size", "About 9,000 SF"),
               ("Acquired", "2018"), ("Opened", "2020"), ("Partners", "William Butcher and Eric Welch")],
         link=None,
         gallery=[("tinsmith-solarium.jpg", "The solarium courtyard", True)]),
    dict(slug="210-s-dickinson", name="210 S Dickinson", short="210 S Dickinson",
         address="210 S Dickinson Street, Madison", area="Marquette neighborhood", kind="Adaptive reuse, build-to-suit office",
         partner="NMD project", status="Completed", year="2020", units="6,158 SF",
         card_img="dickinson-after-1.jpg", hero_img="dickinson-after-2.jpg", framed=True, hero_cap="After", keep_gallery=True, lat=43.0843, lon=-89.3637,
         lede="A 1967 ice house and window-cleaning shop, rebuilt as creative office for Stephan & Brady.",
         facts=["A 1967 masonry building, built as an ice house and for decades the shop of Madison Window Cleaning.",
                "Acquired in 2019.",
                "Gutted and rebuilt as a 6,158 SF single-tenant creative office, build-to-suit for Stephan & Brady, the marketing agency, on a long-term lease. Delivered 2020.",
                "Stephan & Brady remains the tenant."],
         rows=[("Address", "210 S Dickinson Street, Madison"), ("Neighborhood", "Marquette"),
               ("Type", "Adaptive reuse, build-to-suit office"), ("Size", "6,158 SF"), ("Built", "1967"),
               ("Acquired", "2019"), ("Delivered", "2020"), ("Tenant", "Stephan & Brady")],
         link=None,
         gallery=[("dickinson-before-1.jpg", "Before, Dewey Court side", False), ("dickinson-after-1.jpg", "After, Dewey Court side", False),
                  ("dickinson-before-2.jpg", "Before", False), ("dickinson-after-2.jpg", "After", False)]),
    dict(slug="northern-court", name="Northern Court", short="Northern Court",
         address="1401 and 1413 Northern Court, Madison", area="Off East Washington Avenue", kind="Industrial reuse",
         partner="NMD project, William Butcher and Eric Welch", status="Completed", year="2017", units="About 12,000 SF",
         card_img="northern-court-patio.jpg", hero_img="northern-court-patio.jpg", lat=43.0905, lon=-89.3575,
         lede="Two industrial buildings that turned a short street into one of Madison’s craft-beverage blocks.",
         facts=["Two industrial buildings, about 12,000 SF of leasable space, converted in 2016–2017.",
                "Tenants: State Line Distillery (opened 2017); Imaginary Factory, a liqueur and bitters maker with a cocktail bar (about 2,500 SF; its founder was a 2026 James Beard Award finalist); Creative Energy Designs (about 3,600 SF).",
                "The buildings turned a short industrial street into one of Madison’s craft-beverage blocks."],
         rows=[("Address", "1401 and 1413 Northern Court, Madison"), ("Type", "Industrial reuse"),
               ("Leasable space", "About 12,000 SF"), ("Converted", "2016–2017"),
               ("Tenants", "State Line Distillery, Imaginary Factory, Creative Energy Designs"),
               ("Partners", "William Butcher and Eric Welch")],
         link=None,
         gallery=[("northern-court-patio.jpg", "State Line Distillery patio", False),
                  ("northern-court-interior.jpg", "Imaginary Factory", False)]),
]

RECOGNITION = [("Adaptive Reuse Project of the Year 2021", "The Tinsmith · Madison Trust for Historic Preservation"),
               ("Best venue, four years running", "The Tinsmith · Wisconsin Bride")]

PEOPLE = [("William Butcher", "Partner", "More than 24 years in Madison commercial real estate."),
          ("Eric Welch", "Partner", ""),
          ("Stone House Development", "Joint venture partner", "Starkweather Place and Trader’s Way.")]

e = html.escape
BIG = {"starkweather-drone.jpg", "starkweather-creek.jpg", "tinsmith-solarium.jpg", "northern-court-patio.jpg"}
def srcset(img, up=""):
    if img in BIG:
        stem = img[:-4]
        return f' srcset="{up}img/{stem}-1000.jpg 1000w, {up}img/{img} 2000w" sizes="100vw"'
    return ""

def head(title, desc, depth=0):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="https://newmadisondev.github.io/nmd-website/img/share.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{up}img/nmd-logo-circle-ink.png">
{FONTS}
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>
"""

def header(depth=0, on_paper=False):
    up = "../" * depth
    cls = "site-head on-paper" if on_paper else "site-head"
    logo = "nmd-logo-circle-ink.png" if on_paper else "nmd-logo-circle-white.png"
    home = f"{up}index.html"
    return f"""<header class="{cls}"><div class="wrap">
<a href="{home}" aria-label="New Madison Development, home"><img src="{up}img/{logo}" alt="New Madison Development"></a>
<nav aria-label="Main"><a href="{home}#projects">Projects</a><a href="{home}#map">Map</a><a href="{home}#contact">Contact</a></nav>
</div></header>
"""

def footer(depth=0):
    up = "../" * depth
    return f"""<footer class="site-foot"><div class="wrap">
<img src="{up}img/nmd-logo-circle-white.png" alt="New Madison Development">
<span>902 Williamson Street, Madison, WI 53703</span>
<span>© 2026 New Madison Development</span>
</div></footer>
</body>
</html>
"""

# ---------- schematic map ----------
LON0, LON1, LAT0, LAT1 = -89.525, -89.318, 43.032, 43.153
W = 1000
KX = W / (LON1 - LON0)
KY = KX / 0.7314  # cos(43.07)
H = round((LAT1 - LAT0) * KY)

def xy(lat, lon):
    return round((lon - LON0) * KX, 1), round((LAT1 - lat) * KY, 1)

def poly(pts):
    p = [xy(a, b) for a, b in pts]
    return "M" + " L".join(f"{x},{y}" for x, y in p) + " Z"

MENDOTA = [(43.0790, -89.3815), (43.0840, -89.3745), (43.0905, -89.3680), (43.0960, -89.3615), (43.1060, -89.3640),
           (43.1150, -89.3720), (43.1260, -89.3850), (43.1390, -89.3930), (43.1480, -89.4080), (43.1500, -89.4250),
           (43.1440, -89.4430), (43.1330, -89.4600), (43.1180, -89.4740), (43.1050, -89.4770), (43.0960, -89.4640),
           (43.0930, -89.4450), (43.0900, -89.4300), (43.0935, -89.4185), (43.0880, -89.4170), (43.0850, -89.4060),
           (43.0800, -89.3950)]
MONONA = [(43.0730, -89.3830), (43.0760, -89.3740), (43.0790, -89.3640), (43.0820, -89.3555), (43.0835, -89.3505),
          (43.0790, -89.3410), (43.0720, -89.3330), (43.0620, -89.3290), (43.0500, -89.3330), (43.0400, -89.3430),
          (43.0350, -89.3580), (43.0400, -89.3740), (43.0470, -89.3830), (43.0560, -89.3860), (43.0650, -89.3870)]
WINGRA = [(43.0580, -89.4120), (43.0590, -89.4220), (43.0550, -89.4320), (43.0510, -89.4300), (43.0510, -89.4180), (43.0545, -89.4110)]

def map_svg():
    cx, cy = xy(43.0747, -89.3842)
    r1 = xy(43.0960, -89.3615); r2 = xy(43.0880, -89.3575); r3 = xy(43.0835, -89.3505)
    pins = []
    for i, p in enumerate(PROJECTS, 1):
        x, y = xy(p["lat"], p["lon"])
        pins.append(f'<a href="projects/{p["slug"]}.html" class="pin" data-n="{i}" aria-label="{e(p["name"])}">'
                    f'<circle cx="{x}" cy="{y}" r="17"/><text x="{x}" y="{y + 5}" text-anchor="middle">{i}</text></a>')
    m = xy(43.118, -89.425)
    n = xy(43.055, -89.356)
    ex = xy(43.0830, -89.5200); ey = xy(43.0990, -89.3050)
    return f"""<svg class="map" viewBox="0 0 {W} {H}" role="img" aria-label="Schematic map of Madison with the five NMD projects">
<path class="road" d="M{ex[0]},{ex[1]} C{xy(43.080,-89.46)[0]},{xy(43.080,-89.46)[1]} {xy(43.072,-89.42)[0]},{xy(43.072,-89.42)[1]} {cx},{cy} L{ey[0]},{ey[1]}"/>
<path class="lake" d="{poly(MENDOTA)}"/>
<path class="lake" d="{poly(MONONA)}"/>
<path class="lake" d="{poly(WINGRA)}"/>
<path class="river" d="M{r1[0]},{r1[1]} Q{r2[0]},{r2[1]} {r3[0]},{r3[1]}"/>
<text class="lake-label" x="{m[0]}" y="{m[1]}" text-anchor="middle">Lake Mendota</text>
<text class="lake-label" x="{n[0]}" y="{n[1]}" text-anchor="middle">Lake Monona</text>
<path class="cap-mark" d="M{cx},{cy - 9} L{cx + 9},{cy} L{cx},{cy + 9} L{cx - 9},{cy} Z"/>
<text class="cap-label" x="{cx - 14}" y="{cy + 28}" text-anchor="end">CAPITOL</text>
{''.join(pins)}
<text class="note" x="{W - 10}" y="{H - 12}" text-anchor="end">SCHEMATIC · NOT TO SCALE</text>
</svg>"""

# ---------- pages ----------
def index():
    cards = "".join(f"""<a class="card" href="projects/{p['slug']}.html">
<div class="ph"><img src="img/{p['card_img']}"{srcset(p['card_img']).replace('sizes="100vw"','sizes="(max-width:1100px) 80vw, 20vw"')} alt="{e(p['name'])}" loading="lazy"><span class="num">{i:02d}</span></div>
<h3>{e(p['name'])}</h3>
<div class="meta">{e(p['area'])}<br>{e(p['units'])} · {e(p['year'])}</div>
<span class="go">View project</span></a>""" for i, p in enumerate(PROJECTS, 1))
    key = "".join(f"""<li><a href="projects/{p['slug']}.html" data-n="{i}"><span class="n">{i:02d}</span><span><b>{e(p['name'])}</b><small>{e(p['area'])} · {e(p['units'])} · {e(p['status'])}</small></span></a></li>"""
                  for i, p in enumerate(PROJECTS, 1))
    stats = "".join(f'<div class="stat"><b>{e(n)}</b><span>{e(l)}</span></div>' for n, l in STATS)
    recog = "".join(f"<li><b>{e(a)}</b><span>{e(b)}</span></li>" for a, b in RECOGNITION)
    people = "".join(f'<div class="person"><b>{e(n)}</b><span>{e(r)}</span>{f"<p>{e(t)}</p>" if t else ""}</div>' for n, r, t in PEOPLE)
    return (head("New Madison Development", "Madison, Wisconsin development company led by William Butcher and Eric Welch. New housing and new uses for older industrial buildings.")
            + header() + f"""<main>
<section class="hero">
<img src="img/starkweather-drone.jpg"{srcset("starkweather-drone.jpg")} alt="Aerial view of Starkweather Creek beside Starkweather Place" fetchpriority="high">
<div class="wrap">
<h1>New housing. <em>Second lives</em> for old buildings.</h1>
<div class="cap"><span>Madison, Wisconsin</span><span>Starkweather Creek, Starkweather Place</span></div>
</div>
</section>

<section class="intro"><div class="wrap"><div class="grid">
<h2 class="h-section">Built in Madison.</h2>
<p class="lede">{e(COMPANY)}</p>
</div></div></section>

<section class="stats" aria-label="By the numbers"><div class="wrap">{stats}</div></section>

<section class="projects" id="projects"><div class="wrap">
<div class="projects-head"><div><p class="eyebrow">Completed work</p><h2 class="h-section">Projects.</h2></div>
<p>Two apartment communities with Stone House Development, and three older industrial buildings put back to work.</p></div>
<div class="cards">{cards}</div>
</div></section>

<section class="night" id="map"><div class="wrap">
<p class="eyebrow">Where</p><h2 class="h-section">Across Madison.</h2>
<div class="night-grid">
<div>{map_svg()}</div>
<ol class="key">{key}</ol>
</div>
</div></section>

<section class="recog"><div class="wrap"><div class="recog-grid">
<div><p class="eyebrow">Recognition</p><h2 class="h-2">The Tinsmith.</h2></div>
<ul>{recog}</ul>
</div></div></section>

<section class="people" id="people"><div class="wrap">
<p class="eyebrow">People</p><h2 class="h-section">Partners.</h2>
<div class="people-grid">{people}</div>
</div></section>

<section class="contact" id="contact"><div class="wrap"><div class="contact-grid">
<div><p class="eyebrow">Contact</p><h2 class="h-section">Talk to us.</h2></div>
<dl>
<dt>William</dt><dd>William Butcher, Partner</dd>
<dt>Phone</dt><dd><a href="tel:+16083451296">608.345.1296</a></dd>
<dt>Email</dt><dd><a href="mailto:william@newmadisondevelopment.com">william@newmadisondevelopment.com</a></dd>
<dt>Eric</dt><dd>Eric Welch, Partner · <a href="mailto:eric@newmadisondevelopment.com">eric@newmadisondevelopment.com</a></dd>
<dt>Office</dt><dd>902 Williamson Street<br>Madison, WI 53703</dd>
</dl>
</div></div></section>
</main>
<script>
(function(){{var pins=document.querySelectorAll('.map .pin'),keys=document.querySelectorAll('.key a');
function set(n,on){{pins.forEach(function(p){{p.classList.toggle('active',on&&p.dataset.n==n)}});keys.forEach(function(k){{k.classList.toggle('active',on&&k.dataset.n==n)}})}}
[].forEach.call(pins,function(el){{el.addEventListener('mouseenter',function(){{set(el.dataset.n,true)}});el.addEventListener('mouseleave',function(){{set(0,false)}})}});
[].forEach.call(keys,function(el){{el.addEventListener('mouseenter',function(){{set(el.dataset.n,true)}});el.addEventListener('mouseleave',function(){{set(0,false)}});el.addEventListener('focus',function(){{set(el.dataset.n,true)}});el.addEventListener('blur',function(){{set(0,false)}})}});}})();
</script>
""" + footer())

def project_page(i, p):
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    rows = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in p["rows"])
    if p["link"]:
        rows += f'<div><dt>Website</dt><dd><a href="{p["link"][1]}" target="_blank" rel="noopener">{e(p["link"][0])}</a></dd></div>'
    facts = "".join(f"<li>{e(f)}</li>" for f in p["facts"])
    items = p["gallery"] if p.get("keep_gallery") else [g for g in p["gallery"] if g[0] != p["hero_img"]]
    gal = "".join(f'<figure class="{"wide" if w else ""}"><img src="../img/{img}" alt="{e(cap)}" loading="lazy"><figcaption>{e(cap)}</figcaption></figure>'
                  for img, cap, w in items)
    eyebrow = f"{i + 1:02d} · {e(p['kind'])} · {e(p['status'])}"
    if p.get("framed"):
        top = f"""<section class="p-framed"><div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{e(p['name'])}</h1>
<figure style="margin:0;max-width:1100px"><img src="../img/{p['hero_img']}" alt="{e(p['name'])}">{f'<figcaption class="mono" style="color:var(--stone);margin-top:8px">{e(p["hero_cap"])}</figcaption>' if p.get("hero_cap") else ""}</figure></div></section>"""
    else:
        top = f"""<section class="p-hero">
<img src="../img/{p['hero_img']}"{srcset(p['hero_img'], "../")} alt="{e(p['name'])}">
<div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{e(p['name'])}</h1></div>
</section>"""
    return (head(f"{p['name']} · New Madison Development", p["lede"], 1) + header(1, bool(p.get("framed"))) + f"""<main>
{top}
<section class="p-body"><div class="wrap"><div class="p-grid">
<dl class="p-facts">{rows}</dl>
<div class="p-text"><p class="eyebrow">{e(p['partner'])}</p><p class="lede" style="margin-top:14px">{e(p['lede'])}</p><ul>{facts}</ul></div>
</div></div></section>
{f'<section><div class="wrap"><div class="gallery">{gal}</div></div></section>' if gal else '<div style="height:clamp(24px,4vw,60px)"></div>'}
<section class="next"><div class="wrap"><a href="{nxt['slug']}.html"><span>Next project</span><b>{e(nxt['name'])}</b></a></div></section>
</main>
""" + footer(1))

def main():
    (ROOT / "index.html").write_text(index(), encoding="utf-8")
    (ROOT / "projects").mkdir(exist_ok=True)
    for i, p in enumerate(PROJECTS):
        (ROOT / "projects" / f"{p['slug']}.html").write_text(project_page(i, p), encoding="utf-8")
    print("built", 1 + len(PROJECTS), "pages")

if __name__ == "__main__":
    main()
