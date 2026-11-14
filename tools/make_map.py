"""Turns content/madison-osm.json (OpenStreetMap data) into tools/map-paths.json:
simplified SVG paths for streets, water and creeks, in the site map's coordinates."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
LON0, LON1, LAT0, LAT1 = -89.525, -89.318, 43.032, 43.153
W = 1000; KX = W / (LON1 - LON0); KY = KX / 0.7314; H = round((LAT1 - LAT0) * KY)
def xy(p): return ((p[0] - LON0) * KX, (LAT1 - p[1]) * KY)
def rdp(pts, eps):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; L = (dx*dx + dy*dy) ** .5 or 1e-9
    i, dm = 0, -1
    for k in range(1, len(pts) - 1):
        d = abs(dy*pts[k][0] - dx*pts[k][1] + x2*y1 - y2*x1) / L
        if d > dm: i, dm = k, d
    if dm > eps: return rdp(pts[:i+1], eps)[:-1] + rdp(pts[i:], eps)
    return [pts[0], pts[-1]]
def inview(pts, m=40): return any(-m <= x <= W+m and -m <= y <= H+m for x, y in pts)
def path(pts, close=False):
    s = "M" + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return s + ("Z" if close else "")
def join(rings):
    rings = [r[:] for r in rings]; out = []
    while rings:
        cur = rings.pop(0)
        changed = True
        while changed and cur[0] != cur[-1]:
            changed = False
            for i, r in enumerate(rings):
                if r[0] == cur[-1]: cur += r[1:]
                elif r[-1] == cur[-1]: cur += r[::-1][1:]
                elif r[-1] == cur[0]: cur = r + cur[1:]
                elif r[0] == cur[0]: cur = r[::-1] + cur[1:]
                else: continue
                rings.pop(i); changed = True; break
        out.append(cur)
    return out
d = json.load(open(ROOT / "content/madison-osm.json"))
res = {}
for cls, eps in (("r", .8), ("t", .6), ("p", .5), ("m", .5)):
    segs = []
    for way in d["roads"].get(cls, []):
        pts = [xy(p) for p in way]
        if inview(pts): segs.append(path(rdp(pts, eps)))
    res[cls] = "".join(segs)
water = []
for w in d["water"]:
    for ring in join(w["r"]):
        pts = [xy(p) for p in ring]
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        if not inview(pts) or (max(xs)-min(xs))*(max(ys)-min(ys)) < 60: continue
        h = len(pts) // 2
        water.append(path(rdp(pts[:h+1], .6)[:-1] + rdp(pts[h:], .6), True))
res["water"] = "".join(water)
res["rivers"] = "".join(path(rdp([xy(p) for p in r], .6)) for r in d["rivers"] if inview([xy(p) for p in r]))
json.dump(res, open(ROOT / "tools/map-paths.json", "w"))
print({k: len(v) for k, v in res.items()})

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<path d="{res['water']}" fill="#22302C"/>
<path d="{res['rivers']}" fill="none" stroke="#22302C" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="{res['r']}" fill="none" stroke="#2A2E2C" stroke-width=".7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="{res['t']}" fill="none" stroke="#353A37" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"/>
<path d="{res['p']}" fill="none" stroke="#434845" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="{res['m']}" fill="none" stroke="#525754" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
(ROOT / "assets/map-base.svg").write_text(svg)
print("map-base.svg", len(svg))
