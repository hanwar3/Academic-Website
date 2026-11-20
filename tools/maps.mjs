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
