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
