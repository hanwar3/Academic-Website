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
