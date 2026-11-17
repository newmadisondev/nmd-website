import datetime
import json
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

COMPANY = ("New Madison Development is a Madison, Wisconsin development company led by partners "
           "William Butcher and Eric Welch. NMD builds new housing and gives older buildings with historic character new uses.")

STATS = [("5", "projects"), ("256", "new apartments"), ("27,000", "square feet of industrial buildings reused (about)")]

# lat/lon from OpenStreetMap address lookup; nudge separates pins that sit on top of each other
PROJECTS = [
    dict(slug="starkweather-place", name="Starkweather Place", short="Starkweather Place",
         address="215 N Fair Oaks Avenue, Madison", area="East side", kind="Multifamily, new construction",
         partner="", status="Completed", year="2024", units="112 apartments",
         card_img="sw-courtyard.jpg", card_hover="sw-entrance.jpg", hero_img="sw-courtyard.jpg", slideshow=True, keep_gallery=True, lat=43.1019, lon=-89.3307,
         lede="112 apartments on Starkweather Creek, with 2.5 acres of creek frontage.",
         facts=["112 apartments, four stories, on 4.33 acres.",
                "Site put under contract in 2020 in the Town of Blooming Grove, annexed into Madison, rezoned November 2022.",
                "Underground parking, rooftop solar, dog park, canoe and kayak storage, and 2.5 acres of Starkweather Creek frontage.",
                "Designed by Potter Lawson. Built by McGann Construction.",
                "Opened November 1, 2024. Full occupancy achieved spring 2026."],
         rows=[("Address", "215 N Fair Oaks Avenue, Madison"), ("Type", "Multifamily, new construction"),
               ("Apartments", "112"), ("Site", "4.33 acres"), ("Partners", "New Madison Development with Stone House Development"),
               ("Architect", "Potter Lawson"), ("Builder", "McGann Construction"), ("Opened", "November 1, 2024")],
         link=("starkweatherplace.com", "https://starkweatherplace.com"),
         gallery=[("sw-exterior.jpg", "Rear courtyard", True),
                  ("sw-courtyard.jpg", "Courtyard above Starkweather Creek", False), ("sw-patio.jpg", "Pergola and patio", False),
                  ("sw-entrance.jpg", "Main entrance", False), ("sw-fire-ring.jpg", "Fire ring by the creek", False),
                  ("sw-creek-bank.jpg", "Starkweather Creek", False), ("starkweather-creek.jpg", "Creek frontage", False), ("starkweather-drone.jpg", "Aerial, Starkweather Creek", True),
                  ("sw-clubroom.jpg", "Clubroom", False), ("sw-clubroom-2.jpg", "Clubroom", False),
                  ("sw-bar.jpg", "Clubroom bar", False), ("sw-bar-2.jpg", "Clubroom bar", False),
                  ("sw-fireplace.jpg", "Clubroom lounge", False), ("sw-booths.jpg", "Clubroom booths", False),
                  ("sw-fitness.jpg", "Fitness center", True)]),
    dict(slug="traders-way", name="Trader’s Way", short="Trader’s Way",
         address="6624 Old Sauk Road, Madison", area="West side", kind="Multifamily, new construction",
         partner="", status="Completed", year="2026", units="144 apartments",
         card_img="tw-pool-building.jpg", card_hover="tw-street.jpg", hero_img="tw-street.jpg", slideshow=True, keep_gallery=True,
         slide_order=["tw-street.jpg", "tw-pool-building.jpg", "tw-lobby.jpg", "tw-clubroom.jpg", "tw-bar.jpg", "tw-fireplace.jpg",
                      "tw-game-room.jpg", "tw-mail.jpg", "tw-coworking.jpg", "tw-conference.jpg", "tw-yoga.jpg", "tw-sauna-interior.jpg",
                      "tw-fire-pit.jpg", "tw-hot-tub.jpg", "tw-clubhouse-patio.jpg", "tw-sauna.jpg", "tw-grills.jpg"], lat=43.0753, lon=-89.4946,
         lede="144 apartments on a four-acre wooded site; a vestigial portion of an original land grant farm on the near west side.",
         facts=["144 apartments in three stories on a four-acre site.",
                "Outdoor pool, hot tub, sauna, coworking space, green roofs, underground parking with EV charging.",
                "Designed by Potter Lawson. Built by Stevens Construction.",
                "Opened September 15, 2026."],
         rows=[("Address", "6624 Old Sauk Road, Madison"), ("Type", "Multifamily, new construction"),
               ("Apartments", "144"), ("Site", "About four acres"), ("Partners", "New Madison Development with Stone House Development"),
               ("Architect", "Potter Lawson"), ("Builder", "Stevens Construction"), ("Opened", "September 15, 2026")],
         link=("traderswayapts.com", "https://www.traderswayapts.com/"),
         gallery=[("tw-street.jpg", "Old Sauk Road", True), ("tw-fire-pit.jpg", "Courtyard fire pit", False), ("tw-pool-building.jpg", "Pool and courtyard", False),
                  ("tw-hot-tub.jpg", "Hot tub and pergola", False), ("tw-clubhouse-patio.jpg", "Clubhouse patio", False),
                  ("tw-sauna.jpg", "Sauna", False), ("tw-sauna-interior.jpg", "Sauna", False),
                  ("tw-clubroom.jpg", "Clubroom", False), ("tw-bar.jpg", "Clubroom bar", False),
                  ("tw-fireplace.jpg", "Clubroom lounge", False), ("tw-lobby.jpg", "Lobby", False),
                  ("tw-game-room.jpg", "Game room", False), ("tw-mail.jpg", "Mail room", False),
                  ("tw-coworking.jpg", "Coworking", False), ("tw-conference.jpg", "Conference room", False),
                  ("tw-fitness.jpg", "Fitness center", False), ("tw-yoga.jpg", "Yoga studio", False),
                  ("tw-grills.jpg", "Grills under the pergola", True),
                  ("traders-way-rendering.jpg", "Rendering: Potter Lawson", True)]),
    dict(slug="the-tinsmith", name="The Tinsmith", short="The Tinsmith",
         address="828 E Main Street, Madison", area="East Main Street", kind="Adaptive reuse",
         partner="NMD project", status="Completed", year="2020", units="About 9,000 SF",
         card_img="tinsmith-exterior.jpg", card_pos="12% 50%", card_hover="tinsmith-solarium.jpg", hero_img="tinsmith-exterior.jpg", slideshow=True, keep_gallery=True, lat=43.0812, lon=-89.3733,
         lede="Two Trachte steel warehouses, kept instead of demolished, now a wedding and event venue.",
         facts=["Two joined Trachte steel warehouses, about 9,000 SF under barrel-vaulted roofs. Trachte was the Madison company that patented the prefabricated steel building.",
                "Acquired in 2018 after a seven-year pursuit.",
                "Converted, instead of demolished, into The Tinsmith, a wedding and event venue with a glass solarium courtyard. Opened 2020."],
         recog=[("Adaptive Reuse Project of the Year 2021", "Madison Trust for Historic Preservation"),
                ("Best venue in Wisconsin, four years running", "Wisconsin Bride")],
         rows=[("Address", "828 E Main Street, Madison"), ("Type", "Adaptive reuse"), ("Size", "About 9,000 SF"),
               ("Acquired", "2018"), ("Opened", "2020")],
         link=None,
         gallery=[("tinsmith-exterior.jpg", "East Main Street", True), ("tinsmith-before.jpg", "Before: the Kleenaire Corp. building", False), ("tinsmith-solarium.jpg", "The solarium courtyard", False), 
                  ("tinsmith-main-hall.jpg", "The main hall. Photo: Anya Kubilus Photography", False), ("tinsmith-evening.jpg", "The solarium in the evening", False),
                  ("tinsmith-tables.jpg", "Reception in the main hall. Photo: Anya Kubilus Photography", False)]),
    dict(slug="210-s-dickinson", name="210 S Dickinson", short="210 S Dickinson",
         address="210 S Dickinson Street, Madison", area="Marquette neighborhood", kind="Adaptive reuse, build-to-suit office",
         partner="NMD project", status="Completed", year="2020", units="6,158 SF",
         card_img="dickinson-after-night.jpg", card_hover="dickinson-after-deck.jpg", hero_img="dickinson-after-night.jpg", keep_gallery=True, lat=43.0869, lon=-89.3624, nudge=(-13, 10),
         lede="A 1967 ice house and window-cleaning shop, rebuilt as creative office for Stephan & Brady.",
         facts=["A 1967 metal building, built as an ice house and for decades the shop of Madison Window Cleaning.",
                "Acquired in 2019.",
                "Gutted and rebuilt as a 6,158 SF single-tenant creative office, build-to-suit for Stephan & Brady, the marketing agency, on a long-term lease. Delivered 2020.",
                "Stephan & Brady remains the tenant."],
         rows=[("Address", "210 S Dickinson Street, Madison"), ("Neighborhood", "Marquette"),
               ("Type", "Adaptive reuse, build-to-suit office"), ("Size", "6,158 SF"), ("Built", "1967"),
               ("Acquired", "2019"), ("Delivered", "2020"), ("Tenant", "Stephan & Brady")],
         link=None,
         gallery=[("dickinson-before-corner.jpg", "Before", False), ("dickinson-after-night.jpg", "After", False),
                  ("dickinson-before-lot.jpg", "Before", False), ("dickinson-after-deck.jpg", "After", False)]),
    dict(slug="northern-court", name="Northern Court", short="Northern Court",
         address="1401 and 1413 Northern Court, Madison", area="1 block off Williamson St", kind="Industrial reuse",
         partner="NMD project", status="Completed", year="2017", units="About 12,000 SF",
         card_img="state-line-lounge.jpg", card_hover="state-line-patio-1413.jpg", hero_img="state-line-patio-1413.jpg", lat=43.0875, lon=-89.3622, nudge=(13, -10),
         lede="Two industrial buildings that turned a short street into one of Madison’s craft-beverage blocks.",
         facts=["Two industrial buildings, about 12,000 SF of leasable space, converted in 2016–2017.",
                "Tenants: State Line Distillery (opened 2017); Imaginary Factory, a liqueur and bitters maker with a cocktail bar (about 2,500 SF; its founder was a 2026 James Beard Award finalist); Creative Energy Designs (about 3,600 SF).",
                "The buildings turned a short industrial street into one of Madison’s craft-beverage blocks."],
         rows=[("Address", "1401 and 1413 Northern Court, Madison"), ("Type", "Industrial reuse"),
               ("Leasable space", "About 12,000 SF"), ("Converted", "2016–2017"),
               ("Tenants", "State Line Distillery, Imaginary Factory, Creative Energy Designs")],
         link=None,
         gallery=[("state-line-lounge.jpg", "State Line Distillery cocktail lounge", False),
                  ("state-line-bar.jpg", "State Line Distillery", False),
                  ("northern-court-interior.jpg", "Imaginary Factory", False),
                  ("northern-court-imaginary-factory-2.jpg", "Imaginary Factory", False)]),
]

RECOGNITION = [("Adaptive Reuse Project of the Year 2021", "The Tinsmith · Madison Trust for Historic Preservation"),
               ("Best venue in Wisconsin, four years running", "The Tinsmith · Wisconsin Bride")]

PEOPLE = [("William Butcher", "Owner", '25+ years in Madison commercial real estate, development, and brokerage. Owner <a href="https://principalmadison.com" target="_blank" rel="noopener">Principal Madison</a>'),
          ("Eric Welch", "Owner", "20+ years investing, building, and developing in Madison.")]

e = html.escape
import hashlib
CSS_V = hashlib.md5((ROOT / "assets/site.css").read_bytes()).hexdigest()[:8]
BIG = {"starkweather-drone.jpg", "starkweather-creek.jpg", "tinsmith-solarium.jpg"}
def srcset(img, up=""):
    if img in BIG:
        stem = img[:-4]
        return f' srcset="{up}img/{stem}-1000.jpg 1000w, {up}img/{img} 2000w" sizes="100vw"'
    return ""

SITE = "https://newmadisondevelopment.com"
ORG_LD = json.dumps({
    "@context": "https://schema.org", "@type": "Organization",
    "name": "New Madison Development", "alternateName": "NMD", "url": SITE + "/",
    "logo": SITE + "/img/nmd-logo-circle-ink.png", "foundingDate": "2017",
    "description": "Real estate development company in Madison, Wisconsin. Apartment communities and adaptive reuse of older buildings.",
    "address": {"@type": "PostalAddress", "streetAddress": "902 Williamson St", "addressLocality": "Madison",
                "addressRegion": "WI", "postalCode": "53703", "addressCountry": "US"},
    "telephone": "+1-608-301-5008", "areaServed": "Madison, Wisconsin",
    "founder": [{"@type": "Person", "name": "William Butcher"}, {"@type": "Person", "name": "Eric Welch"}],
})

def head(title, desc, depth=0, share="share-home.jpg", path=""):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="New Madison Development">
<meta property="og:url" content="{SITE}/{path}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="https://newmadisondevelopment.com/img/{share}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{ORG_LD}</script>
<link rel="icon" href="{up}img/nmd-logo-circle-ink.png">
{FONTS}
<link rel="stylesheet" href="{up}assets/site.css?v={CSS_V}">
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
<nav aria-label="Main"><a href="{home}#projects">Projects</a><a href="{home}#map">Map</a><a href="{up}about.html">About</a><a href="{home}#contact">Contact</a></nav>
</div></header>
"""

def footer(depth=0):
    up = "../" * depth
    return f"""<footer class="site-foot"><div class="wrap">
<img src="{up}img/nmd-logo-circle-white.png" alt="New Madison Development">
<span>902 Williamson Street, Madison, WI 53703</span>
<span>© 2026 New Madison Development · Map data © OpenStreetMap contributors</span>
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
        x, y = x + p.get("nudge", (0, 0))[0], y + p.get("nudge", (0, 0))[1]
        pins.append(f'<a href="projects/{p["slug"]}.html" class="pin" data-n="{i}" aria-label="{e(p["name"])}">'
                    f'<circle cx="{x}" cy="{y}" r="17"/><text x="{x}" y="{y + 5}" text-anchor="middle">{i}</text></a>')
    m = xy(43.118, -89.425)
    n = xy(43.055, -89.356)
    ex = xy(43.0830, -89.5200); ey = xy(43.0990, -89.3050)
    return f"""<svg class="map" viewBox="0 0 {W} {H}" role="img" aria-label="Map of Madison with the five NMD projects">
<image href="assets/map-base.svg" x="0" y="0" width="{W}" height="{H}"/>
<text class="lake-label" x="{m[0]}" y="{m[1]}" text-anchor="middle">Lake Mendota</text>
<text class="lake-label" x="{n[0]}" y="{n[1]}" text-anchor="middle">Lake Monona</text>
<path class="cap-mark" d="M{cx},{cy - 9} L{cx + 9},{cy} L{cx},{cy + 9} L{cx - 9},{cy} Z"/>
<text class="cap-label" x="{cx - 14}" y="{cy + 28}" text-anchor="end">CAPITOL</text>
{''.join(pins)}
</svg>"""

# ---------- hero slideshow ----------
HERO_SLIDES = [("starkweather-place", "sw-courtyard.jpg"), ("the-tinsmith", "tinsmith-exterior.jpg"),
               ("traders-way", "tw-street.jpg"), ("northern-court", "state-line-lounge.jpg"),
               ("starkweather-place", "starkweather-drone.jpg"), ("the-tinsmith", "tinsmith-solarium.jpg"),
               ("traders-way", "tw-pool-building.jpg"), ("210-s-dickinson", "dickinson-after-night.jpg"),
               ("starkweather-place", "sw-bar.jpg"), ("northern-court", "state-line-patio-1413.jpg"),
               ("traders-way", "tw-bar.jpg")]

def slides():
    by = {p["slug"]: p for p in PROJECTS}
    out = []
    for i, (slug, img) in enumerate(HERO_SLIDES):
        p = by[slug]
        extra = ' fetchpriority="high"' if i == 0 else ' loading="lazy"'
        out.append(f'<img class="slide{" on" if i == 0 else ""}" src="img/{img}"{srcset(img)} alt="{e(p["name"])}" '
                   f'data-name="{e(p["name"])}" data-href="projects/{p["slug"]}.html"{extra}>')
    return "\n".join(out)

# ---------- pages ----------
def index():
    cards = "".join(f"""<a class="card" href="projects/{p['slug']}.html">
<div class="ph"><img src="img/{p['card_img']}"{f' style="object-position:{p["card_pos"]}"' if p.get("card_pos") else ""}{srcset(p['card_img']).replace('sizes="100vw"','sizes="(max-width:1100px) 80vw, 20vw"')} alt="{e(p['name'])}" loading="lazy"><img class="alt" src="img/{p['card_hover']}" alt="" loading="lazy"><span class="num">{i:02d}</span></div>
<h3>{e(p['name'])}</h3>
<div class="meta">{e(p['area'])}<br>{e(p['units'])} · {e(p['year'])}</div>
<span class="go">View project</span></a>""" for i, p in enumerate(PROJECTS, 1))
    key = "".join(f"""<li><a href="projects/{p['slug']}.html" data-n="{i}"><span class="n">{i:02d}</span><span><b>{e(p['name'])}</b><small>{e(p['area'])} · {e(p['units'])} · {e(p['status'])}</small></span></a></li>"""
                  for i, p in enumerate(PROJECTS, 1))
    stats = "".join(f'<div class="stat"><b>{e(n)}</b><span>{e(l)}</span></div>' for n, l in STATS)
    people = "".join(f'<div class="person"><b>{e(n)}</b><span>{e(r)}</span>{f"<p>{t}</p>" if t else ""}</div>' for n, r, t in PEOPLE)
    return (head("New Madison Development | Creative Real Estate Development in Madison, WI", "Madison, Wisconsin real estate development company led by William Butcher and Eric Welch. New apartment communities and new uses for older buildings with historic character.")
            + header() + f"""<main>
<section class="hero">
{slides()}
<div class="wrap">
<h1>Ground Up. <em>Adaptive Reuse.</em></h1>
<div class="cap"><span>Madison, Wisconsin</span><a class="slide-cap" href="projects/{PROJECTS[0]['slug']}.html">{e(PROJECTS[0]['name'])}</a></div>
</div>
</section>

<section class="intro"><div class="wrap"><div class="grid">
<h2 class="h-section">Built in Madison.</h2>
<p class="lede">{e(COMPANY)}</p>
</div></div></section>

<section class="stats" aria-label="By the numbers"><div class="wrap">{stats}</div></section>

<section class="projects" id="projects"><div class="wrap">
<div class="projects-head"><div><p class="eyebrow">Completed work</p><h2 class="h-section">Projects.</h2></div>
<p>Two apartment communities with Stone House Development, and three historic industrial buildings reinvented as office and hospitality spaces.</p></div>
<div class="cards">{cards}</div>
</div></section>

<section class="night" id="map"><div class="wrap">
<h2 class="h-section">Madison.</h2>
<div class="night-grid">
<div>{map_svg()}</div>
<ol class="key">{key}</ol>
</div>
</div></section>

<section class="people" id="people"><div class="wrap">
<h2 class="h-section">Partners.</h2>
<div class="people-grid">{people}</div>
</div></section>

<section class="contact" id="contact"><div class="wrap"><div class="contact-grid">
<div><h2 class="h-section">Contact.</h2></div>
<dl>
<dt>William</dt><dd>William Butcher</dd>
<dt>Phone</dt><dd><a href="tel:+16083015008">608.301.5008</a></dd>
<dt>Email</dt><dd><a href="mailto:william@newmadisondevelopment.com">william@newmadisondevelopment.com</a></dd>
<dt>Eric</dt><dd>Eric Welch<br><a href="mailto:eric@newmadisondevelopment.com">eric@newmadisondevelopment.com</a></dd>
<dt>Office</dt><dd>902 Williamson Street<br>Madison, WI 53703</dd>
</dl>
</div></div></section>
</main>
<script>
(function(){{var s=document.querySelectorAll('.hero .slide'),c=document.querySelector('.slide-cap'),i=0;
if(s.length<2||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
setInterval(function(){{s[i].classList.remove('on');i=(i+1)%s.length;s[i].classList.add('on');c.textContent=s[i].dataset.name;c.href=s[i].dataset.href}},5500);}})();
(function(){{var pins=document.querySelectorAll('.map .pin'),keys=document.querySelectorAll('.key a');
function set(n,on){{pins.forEach(function(p){{p.classList.toggle('active',on&&p.dataset.n==n)}});keys.forEach(function(k){{k.classList.toggle('active',on&&k.dataset.n==n)}})}}
[].forEach.call(pins,function(el){{el.addEventListener('mouseenter',function(){{set(el.dataset.n,true)}});el.addEventListener('mouseleave',function(){{set(0,false)}})}});
[].forEach.call(keys,function(el){{el.addEventListener('mouseenter',function(){{set(el.dataset.n,true)}});el.addEventListener('mouseleave',function(){{set(0,false)}});el.addEventListener('focus',function(){{set(el.dataset.n,true)}});el.addEventListener('blur',function(){{set(0,false)}})}});}})();
</script>
""" + footer())

def recog_block(p):
    if not p.get("recog"):
        return ""
    items = "".join(f"<li><b>{e(a)}</b><span>{e(b)}</span></li>" for a, b in p["recog"])
    return f"""<section class="recog"><div class="wrap"><div class="recog-grid">
<div><p class="eyebrow">Recognition</p><h2 class="h-2">Awards.</h2></div>
<ul>{items}</ul>
</div></div></section>"""

def project_page(i, p):
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    rows = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b).replace(" with Stone House Development", "<br>with Stone House Development")}</dd></div>" for a, b in p["rows"])
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
        if p.get("slideshow"):
            imgs = p.get("slide_order") or [p["hero_img"]] + [g[0] for g in p["gallery"] if g[0] != p["hero_img"]
                                      and "fitness" not in g[0] and "rendering" not in g[0]]
            pics = "".join(f'<img class="slide{" on" if k == 0 else ""}" src="../img/{im}"{srcset(im, "../")} alt="{e(p["name"])}"{"" if k == 0 else " loading=\"lazy\""}>'
                           for k, im in enumerate(imgs))
        else:
            pics = f'<img src="../img/{p["hero_img"]}"{srcset(p["hero_img"], "../")} alt="{e(p["name"])}">'
        top = f"""<section class="p-hero">
{pics}
<div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{e(p['name'])}</h1></div>
</section>"""
    return (head(f"{p['name']}, Madison, WI · New Madison Development", f"{p['name']}, {p['address']}, WI. {p['lede']}", 1, f"share-{p['slug']}.jpg", f"projects/{p['slug']}.html") + header(1, bool(p.get("framed"))) + f"""<main>
{top}
<section class="p-body"><div class="wrap"><div class="p-grid">
<dl class="p-facts">{rows}</dl>
<div class="p-text">{f'<p class="eyebrow">{e(p["partner"])}</p>' if p["partner"] else ""}<p class="lede" style="margin-top:{14 if p["partner"] else 0}px">{e(p['lede'])}</p><ul>{facts}</ul></div>
</div></div></section>
{recog_block(p)}
{f'<section><div class="wrap"><div class="gallery">{gal}</div></div></section>' if gal else '<div style="height:clamp(24px,4vw,60px)"></div>'}
<section class="next"><div class="wrap"><a href="{nxt['slug']}.html"><span>Next project</span><b>{e(nxt['name'])}</b></a></div></section>
</main>
<script>
(function(){{var s=document.querySelectorAll('.p-hero .slide'),i=0;
if(s.length<2||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
setInterval(function(){{s[i].classList.remove('on');i=(i+1)%s.length;s[i].classList.add('on')}},5000);}})();
</script>
""" + footer(1))

ABOUT_INTRO = [
    "William Butcher and Eric Welch founded New Madison Development in 2017. Together we seek out and find unique development sites, both in the downtown core and in outlying areas, specializing in finding promising sites that have been overlooked or are hiding in plain sight.",
    "Our work includes two apartment communities, Starkweather Place and Trader's Way, totaling 256 units, and three industrial buildings reinvented as office and hospitality spaces.",
]
ABOUT_PEOPLE = [
    ("William Butcher", "Owner", 'William has worked in Madison real estate since 2002 as an agent, broker, investor, and developer. As a broker he has represented clients on more than $250 million in closed transactions, many of them development acquisitions that became more than $1 billion in built assets. He represents buyers and sellers of development sites, office, retail, land and investment property, and landlords and tenants. He owns <a href="https://principalmadison.com" target="_blank" rel="noopener">Principal Madison</a>.'),
    ("Eric Welch", "Owner", "Born and raised in Monona, Eric's career has spanned construction, investing, and developing multifamily and retail real estate in Madison, Milwaukee, and satellite communities. He continues to operate his own painting and contracting company, established in 2004."),
]

def about_page():
    intro = "".join(f"<p>{e(t)}</p>" for t in ABOUT_INTRO)
    people = "".join(f'<div class="person"><b>{e(n)}</b><span>{e(r)}</span><p>{t}</p></div>' for n, r, t in ABOUT_PEOPLE)
    return (head("About William Butcher and Eric Welch · New Madison Development", "New Madison Development was founded in 2017 by William Butcher and Eric Welch. Apartment communities and adaptive reuse projects in Madison, Wisconsin.", path="about.html") + header(0, True) + f"""<main class="about">
<section class="about-top"><div class="wrap">
<h1 class="h-section">About.</h1>
<div class="about-text">{intro}</div>
</div></section>
<section class="about-photo"><div class="wrap"><img src="img/about-partners-3.jpg" alt="William Butcher and Eric Welch"></div></section>
<section class="people"><div class="wrap"><div class="people-grid two">{people}</div></div></section>
</main>
""" + footer(0))

def main():
    (ROOT / "about.html").write_text(about_page(), encoding="utf-8")
    (ROOT / "index.html").write_text(index(), encoding="utf-8")
    (ROOT / "projects").mkdir(exist_ok=True)
    for i, p in enumerate(PROJECTS):
        (ROOT / "projects" / f"{p['slug']}.html").write_text(project_page(i, p), encoding="utf-8")
    urls = ["", "about.html"] + [f"projects/{p['slug']}.html" for p in PROJECTS]
    today = datetime.date.today().isoformat()
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{SITE}/{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print("built", 1 + len(PROJECTS), "pages")

if __name__ == "__main__":
    main()
