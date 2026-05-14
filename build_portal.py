#!/usr/bin/env python3
"""Rebuilds portal_bbdd.html with all modules base64-encoded."""
import base64, re

MODULES = [
    ("relaciones_tablas.html",    "🔗", "01", "Relaciones entre Tablas",     "Teoría y ejercicios sobre relaciones 1:1, 1:N y N:M",          "#00e5ff"),
    ("practica_campos_bbdd.html", "🎮", "02", "DataQuest: Campos BD",         "Aprende el porqué de cada campo con videojuegos",              "#ff4d8f"),
    ("reto_diseno_bbdd.html",     "🏁", "03", "NeonRace: Reto de Diseño",     "Diseña desde cero la BD de un videojuego",                     "#ffe44d"),
    ("consultas_access.html",     "🔍", "04", "Consultas SQL",                "Aprende SELECT, WHERE, JOIN y más desde cero",                  "#3dffa0"),
    ("formularios_informes.html", "📋", "05", "Formularios e Informes",       "Crea formularios e informes profesionales en Access",           "#c084fc"),
    ("ejercicios_sql.html",       "💻", "06", "Ejercicios SQL",               "Practica SELECT, WHERE, ORDER BY y GROUP BY con ejercicios",    "#ffa940"),
    ("examen_modelo_c.html",      "📋", "07", "Examen Final — Modelo C",      "Enunciado completo y soluciones del examen final GGZone",        "#b048f5"),
]

def encode(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

def chunk(s, n=120):
    return "+\n    \"".join('"' + s[i:i+n] + '"' for i in range(0, len(s), n))

# Build color CSS for cards + tabs
color_css = ""
for i, (_, _, _, _, _, color) in enumerate(MODULES):
    n = i + 1
    color_css += f"""
.card:nth-child({n})::before{{background:{color};}}
.card:nth-child({n}):hover{{border-color:{color};box-shadow:0 12px 50px {color}22;}}
.card:nth-child({n}) .c-cta{{color:{color};}}
.nt:nth-child({n}).active{{border-bottom-color:{color};background:{color}18;}}
.nt:nth-child({n}).active .ni{{background:{color}22;color:{color};}}"""

# Build tabs HTML
tabs_html = ""
for i, (_, icon, num, title, _, _) in enumerate(MODULES):
    tabs_html += f'    <button class="nt" id="tab-{i}" onclick="openApp({i})"><span class="ni">{num}</span><span style="font-size:1.05rem">{icon}</span>{title}</button>\n'

# Build cards HTML
cards_html = ""
for i, (_, icon, num, title, desc, _) in enumerate(MODULES):
    cards_html += f"""  <div class="card" onclick="openApp({i})">
    <div class="c-icon">{icon}</div>
    <div class="c-num">Módulo {num}</div>
    <div class="c-title">{title}</div>
    <div class="c-desc">{desc}</div>
    <div class="c-cta">Abrir →</div>
  </div>\n"""

# Build frames HTML
frames_html = ""
for i, (_, _, _, title, _, _) in enumerate(MODULES):
    frames_html += f'  <iframe class="frame" id="frame-{i}" title="Módulo {i+1} — {title}"></iframe>\n'

# Build APPS JS array
apps_js_parts = []
for path, _, _, title, _, _ in MODULES:
    b64 = encode(path)
    lines = [b64[j:j+100] for j in range(0, len(b64), 100)]
    b64_js = ('"+\n    "').join(lines)
    apps_js_parts.append(f'  {{title:"{title}",b64:"{b64_js}"}}')

apps_js = "const APPS=[\n" + ",\n".join(apps_js_parts) + "\n];"

module_count = len(MODULES)

portal_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bases de Datos — Centro de Recursos</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Syne+Mono&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#08090f;--s1:#0d0f1c;--s2:#12152a;
  --border:#1b2040;--border2:#252d52;
  --text:#e0e6ff;--muted:#4a5580;--muted2:#7a85b8;
  --sans:'Syne',sans-serif;--mono:'Syne Mono',monospace;
}}
html,body{{height:100%;overflow:hidden}}
body{{background:var(--bg);color:var(--text);font-family:var(--sans);display:flex;flex-direction:column;}}

#topbar{{
  display:flex;align-items:center;height:54px;flex-shrink:0;
  background:var(--s1);border-bottom:2px solid var(--border2);z-index:200;
}}
.tb-logo{{
  padding:0 1.4rem;font-family:var(--mono);font-size:0.72rem;letter-spacing:0.14em;
  text-transform:uppercase;color:#00e5ff;border-right:1px solid var(--border2);
  height:100%;display:flex;align-items:center;gap:0.55rem;white-space:nowrap;flex-shrink:0;
}}
.logo-dot{{width:7px;height:7px;border-radius:50%;background:#00e5ff;animation:blink 2s infinite;}}
@keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:0.2}}}}

.nav-tabs{{display:flex;height:100%;flex:1;overflow-x:auto;scrollbar-width:none;}}
.nav-tabs::-webkit-scrollbar{{display:none;}}
.nt{{
  display:flex;align-items:center;gap:0.5rem;padding:0 1.25rem;height:100%;
  font-size:0.83rem;font-weight:700;color:var(--muted2);cursor:pointer;
  border-right:1px solid var(--border);border-bottom:3px solid transparent;
  border-top:none;border-left:none;background:none;
  transition:all 0.18s;white-space:nowrap;flex-shrink:0;
}}
.nt:hover{{color:var(--text);background:rgba(255,255,255,0.03);}}
.nt.active{{color:var(--text);}}
.nt .ni{{font-family:var(--mono);font-size:0.56rem;background:var(--border2);padding:0.15rem 0.4rem;border-radius:2px;color:var(--muted);}}

.tb-end{{padding:0 1.1rem;height:100%;display:flex;align-items:center;border-left:1px solid var(--border2);flex-shrink:0;}}
.home-btn{{
  background:none;border:1px solid var(--border2);font-family:var(--mono);font-size:0.62rem;
  letter-spacing:0.08em;text-transform:uppercase;color:var(--muted2);
  padding:0.4rem 0.85rem;cursor:pointer;border-radius:3px;transition:all 0.15s;
}}
.home-btn:hover{{border-color:#ff4d8f;color:#ff4d8f;}}

#hub{{
  flex:1;display:flex;flex-direction:column;align-items:center;
  justify-content:center;gap:2.5rem;padding:2rem;overflow-y:auto;
  background:radial-gradient(ellipse 70% 50% at 50% 55%,#00e5ff07 0%,transparent 70%);
}}
.hub-label{{font-family:var(--mono);font-size:0.68rem;letter-spacing:0.18em;text-transform:uppercase;color:#00e5ff;text-align:center;margin-bottom:0.5rem;}}
.hub-title{{text-align:center;font-size:clamp(2rem,5vw,4rem);font-weight:800;line-height:1;}}
.hub-title em{{color:#00e5ff;font-style:normal;}}
.hub-sub{{color:var(--muted2);font-size:0.9rem;text-align:center;max-width:500px;margin-top:0.65rem;}}

.cards{{display:flex;gap:1.25rem;flex-wrap:wrap;justify-content:center;max-width:1100px;}}
.card{{
  background:var(--s1);border:1px solid var(--border2);border-radius:8px;
  padding:1.9rem 1.55rem;width:200px;cursor:pointer;
  transition:transform 0.2s,border-color 0.2s,box-shadow 0.2s;
  display:flex;flex-direction:column;gap:0.5rem;
  position:relative;overflow:hidden;
}}
.card::before{{content:'';position:absolute;top:0;left:0;right:0;height:3px;opacity:0.3;transition:opacity 0.2s;}}
.card:hover{{transform:translateY(-5px);}}
.card:hover::before{{opacity:1;}}
.c-icon{{font-size:2rem;}}
.c-num{{font-family:var(--mono);font-size:0.57rem;color:var(--muted);letter-spacing:0.14em;text-transform:uppercase;}}
.c-title{{font-size:1rem;font-weight:700;color:var(--text);}}
.c-desc{{font-size:0.8rem;color:var(--muted2);line-height:1.5;}}
.c-cta{{margin-top:0.3rem;font-family:var(--mono);font-size:0.65rem;letter-spacing:0.1em;text-transform:uppercase;opacity:0;transform:translateX(-5px);transition:all 0.2s;}}
.card:hover .c-cta{{opacity:1;transform:translateX(0);}}

#frames{{flex:1;position:relative;display:none;}}
#frames.on{{display:block;}}
.frame{{position:absolute;inset:0;width:100%;height:100%;border:none;display:none;}}
.frame.on{{display:block;}}

#loader{{display:none;position:absolute;inset:0;background:var(--bg);z-index:100;align-items:center;justify-content:center;flex-direction:column;gap:1.25rem;}}
#loader.on{{display:flex;}}
.ld-spin{{width:34px;height:34px;border:3px solid var(--border2);border-top-color:#00e5ff;border-radius:50%;animation:spin 0.8s linear infinite;}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.ld-txt{{font-family:var(--mono);font-size:0.68rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--muted2);}}
.ld-bar{{width:220px;height:3px;background:var(--border2);border-radius:3px;overflow:hidden;margin-top:0.1rem;}}
.ld-prog{{height:100%;background:linear-gradient(90deg,#00e5ff,#4dd9ff);width:0%;transition:width 0.4s ease;}}
</style>
</head>
<body>

<style>{color_css}
</style>

<div id="topbar">
  <div class="tb-logo"><span class="logo-dot"></span>BD · Access</div>
  <div class="nav-tabs">
{tabs_html}  </div>
  <div class="tb-end"><button class="home-btn" onclick="goHome()">&#8962; Inicio</button></div>
</div>
<div id="hub">
  <div>
    <div class="hub-label">Aplicaciones Ofimáticas · Access</div>
    <div class="hub-title">Centro de<br><em>Recursos BD</em></div>
    <p class="hub-sub">{module_count} módulos interactivos para aprender bases de datos con Microsoft Access desde cero.</p>
  </div>
  <div class="cards">
{cards_html}  </div>
</div>
<div id="frames">
{frames_html}  <div id="loader">
    <div class="ld-spin"></div>
    <div class="ld-txt" id="ldTxt">Cargando...</div>
    <div class="ld-bar"><div class="ld-prog" id="ldProg"></div></div>
  </div>
</div>

<script>
{apps_js}

function b64ToBlob(b64){{
  const bin=atob(b64),bytes=new Uint8Array(bin.length);
  for(let i=0;i<bin.length;i++) bytes[i]=bin.charCodeAt(i);
  return new Blob([bytes],{{type:"text/html;charset=utf-8"}});
}}

const blobUrls=new Array({module_count}).fill(null);
let current=-1;

function showLoader(title){{
  const ld=document.getElementById("loader");
  document.getElementById("ldTxt").textContent="Cargando "+title+"...";
  document.getElementById("ldProg").style.width="0%";
  ld.classList.add("on");
  let p=0;
  const iv=setInterval(()=>{{p=Math.min(p+Math.random()*18,90);document.getElementById("ldProg").style.width=p+"%";}},120);
  return iv;
}}
function hideLoader(iv){{
  document.getElementById("ldProg").style.width="100%";
  clearInterval(iv);
  setTimeout(()=>document.getElementById("loader").classList.remove("on"),350);
}}

function openApp(n){{
  if(current===n) return;
  if(current>=0){{
    document.getElementById("frame-"+current).classList.remove("on");
    document.getElementById("tab-"+current).classList.remove("active");
  }}
  document.getElementById("hub").style.display="none";
  document.getElementById("frames").classList.add("on");
  document.getElementById("tab-"+n).classList.add("active");
  current=n;

  const frame=document.getElementById("frame-"+n);
  if(!blobUrls[n]){{
    const iv=showLoader(APPS[n].title);
    frame.onload=()=>hideLoader(iv);
    const url=URL.createObjectURL(b64ToBlob(APPS[n].b64));
    blobUrls[n]=url;
    frame.src=url;
  }} else {{
    frame.classList.add("on");
  }}
  frame.classList.add("on");
}}

function goHome(){{
  if(current>=0){{
    document.getElementById("frame-"+current).classList.remove("on");
    document.getElementById("tab-"+current).classList.remove("active");
    current=-1;
  }}
  document.getElementById("frames").classList.remove("on");
  document.getElementById("hub").style.display="";
}}
</script>
</body>
</html>"""

with open("portal_bbdd.html","w",encoding="utf-8") as f:
    f.write(portal_html)

import os
size = os.path.getsize("portal_bbdd.html")
print(f"portal_bbdd.html generado: {size/1024:.0f} KB con {module_count} módulos")
