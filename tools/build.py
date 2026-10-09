"""Rebuild the existing static portfolio. Run from any directory; no dependencies."""
from pathlib import Path
import json
from html import escape as esc

repo=Path(__file__).resolve().parents[1]
root=repo/'docs'
projects=json.loads((repo/'content/projects.json').read_text(encoding='utf-8'))

def image(n,prefix=''):return f'{prefix}assets/image{n}.webp'
def head(title,description,prefix='',cover=4):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#191c1e">
<title>{esc(title)} · BLE</title><meta name="description" content="{esc(description)}"><meta property="og:title" content="{esc(title)} · BLE"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:image" content="https://ble4real.github.io/portafolio/assets/image{cover}.webp"><link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/fonts/fonts.css"><link rel="stylesheet" href="{prefix}styles.css"><script defer src="{prefix}app.js"></script></head>
<body><a class="skip" href="#main">Skip to content</a>'''
def header(prefix=''):
    return f'''<header class="site-header"><a class="brand" href="{prefix}index.html" aria-label="BLE home">BLE<span>3D Artist &amp; Modeler</span></a><nav aria-label="Main navigation"><a href="{prefix}index.html#work">Work</a><a href="{prefix}index.html#studies">Studies</a><a href="{prefix}index.html#about">Profile</a><a href="{prefix}index.html#contact">Contact</a></nav></header>'''
def footer(prefix=''):
    return f'''<footer><a class="brand" href="{prefix}index.html">BLE</a><p>Juan Esteban Araujo Ortiz<br>Medellín, Colombia</p><a href="https://www.artstation.com/ble4real" target="_blank" rel="noopener noreferrer">ArtStation</a><a href="mailto:arajuanes405@gmail.com">Email BLE</a></footer>
<dialog class="lightbox" aria-label="Enlarged artwork"><button type="button" class="close-lightbox">Close image</button><img src="{prefix}assets/image4.webp" alt=""><p></p></dialog></body></html>'''
def card(p):
    caption=next(c for n,c in p['images'] if n==p['cover'])
    label='Original concept · 3D in development' if p['slug']=='cheni' else p['kind']
    return f'''<a class="project-item" href="projects/{p['slug']}.html" data-category="{p['group']}"><div class="project-image {'portrait' if p['cover'] in (1,24) else ''}"><img src="{image(p['cover'])}" alt="{esc(caption)}" loading="lazy" width="900" height="600"></div><div class="project-label"><h3>{esc(p['title'])}</h3><span>{esc(label)}</span></div></a>'''
filters=''.join(f'<button type="button" aria-pressed="{str(c=="All").lower()}" class="{"active" if c=="All" else ""}" data-filter="{c}">{c}</button>' for c in ['All','Characters','Props','Environments','Motion','Studies'])
index=head('Stylized characters & 3D modeling','Juan Esteban Araujo Ortiz (BLE). Stylized characters and 3D modeling, with selected props, environments and studies.')+header()+f'''
<main id="main"><section class="exhibition" aria-labelledby="hero-title"><div class="exhibition-art"><img id="featured-image" src="assets/image4.webp" alt="VERT — stylized character render by BLE" width="1600" height="900" fetchpriority="high"></div><div class="exhibition-copy"><h1 id="hero-title">Stylized characters.<br>3D modeling.</h1><p>Juan Esteban Araujo Ortiz · BLE<br>Character design, models and textured renders.</p><a id="featured-link" class="button primary" href="projects/vert.html">Explore VERT</a></div><div class="stage-controls" aria-label="Featured work"><span>On display</span><button type="button" class="active" aria-pressed="true" data-feature="vert">VERT</button><button type="button" aria-pressed="false" data-feature="cheni">CHENI</button><button type="button" aria-pressed="false" data-feature="chest">CHEST</button></div></section>
<section id="work" class="work-section" aria-labelledby="work-title"><div class="section-heading"><h2 id="work-title">Selected work.</h2><p>Character work first, with a stylized prop and an environment.</p></div><div class="filters" role="group" aria-label="Filter all projects">{filters}</div><p id="filter-status" class="sr-only" aria-live="polite">12 projects shown</p><div class="project-grid selected-grid">{''.join(card(p) for p in projects if p['featured'])}</div><p class="selected-empty" hidden>No selected projects in this category. See Studies &amp; exploration below.</p></section>
<section id="studies" class="work-section studies-section" aria-labelledby="studies-title"><div class="section-heading"><h2 id="studies-title">Studies &amp; exploration</h2><p>Further modeling work, plus exercises in rigging, animation and real-time effects.</p></div><div class="project-grid studies-grid">{''.join(card(p) for p in projects if not p['featured'])}</div><p class="studies-empty" hidden>No studies in this category.</p></section>
<section id="about" class="profile"><div class="profile-title"><h2>From character design<br>to <span>3D form.</span></h2></div><div class="profile-body"><p class="intro">I’m Juan Esteban Araujo Ortiz, a 3D artist focused on stylized characters and modeling. My portfolio brings together original character design, 3D models and textured renders, alongside prop and environment work.</p><h3>Main focus</h3><ul class="focus-list"><li>Stylized characters</li><li>3D modeling</li><li>UVs &amp; texturing</li></ul><h3>Further exploration</h3><p class="tools">Rigging, animation and real-time effects appear in the studies section. Project credits identify autorig assistance and assets made by others.</p><h3>Tools used in this portfolio</h3><p class="tools">Blender · Maya · Substance 3D Painter · Procreate · Unity</p><p class="profile-name">Juan Esteban Araujo Ortiz<br>3D Artist &amp; Modeler · Medellín, Colombia</p></div></section>
<section id="contact" class="contact"><h2>Get in touch.</h2><a class="contact-email" href="mailto:arajuanes405@gmail.com">arajuanes405@gmail.com</a><p>More work on <a href="https://www.artstation.com/ble4real" target="_blank" rel="noopener noreferrer">ArtStation</a>.</p></section></main>'''+footer()
(root/'index.html').write_text(index,encoding='utf-8')

def figure(im,eager=False):
    n,caption=im
    return f'''<figure class="gallery-item"><button type="button" class="artwork-open" data-image="{image(n,'../')}" data-caption="{esc(caption)}" aria-label="Enlarge: {esc(caption)}"><img src="{image(n,'../')}" alt="{esc(caption)}" loading="{'eager' if eager else 'lazy'}" width="1600" height="900"></button><figcaption>{esc(caption)}</figcaption></figure>'''
for i,p in enumerate(projects):
    cheni=p['slug']=='cheni'
    body=head(p['title'],p['intro'],'../',p['cover'])+header('../')
    body+=f'''<main id="main" class="project-page"><a class="back-link" href="../index.html#{'work' if p['featured'] else 'studies'}">Back to {'selected work' if p['featured'] else 'studies'}</a><div class="project-heading"><h1>{esc(p['title'])}</h1><p class="project-kind">{esc(p['kind'])}</p><p class="project-intro">{esc(p['intro'])}</p></div>'''
    if cheni:body+='<h2 class="case-section-title">Original concept</h2>'
    body+='<section class="project-gallery lead-gallery" aria-label="Main artwork">'+figure(p['images'][0],True)+'</section>'
    body+=f'''<section class="case-overview" aria-label="Project context"><div><h2>Project objective</h2><p>{esc(p['objective'])}</p></div><div><h2>My contribution</h2><p>{esc(p['contribution'])}</p><p class="tools">{' · '.join(esc(t) for t in p['tools'])}</p></div></section>'''
    rest=p['images'][1:]
    if cheni:
        body+='<section class="case-process" aria-labelledby="concept-title"><h2 class="case-section-title" id="concept-title">Concept — back view</h2><div class="project-gallery">'+''.join(figure(im) for im in rest if im[0]==21)+'</div></section>'
        body+='<section class="case-process" aria-labelledby="current-title"><h2 class="case-section-title" id="current-title">Current 3D version</h2><p class="section-intro">The existing model, shown in Blender. A new 3D version is in development; no images of that version are shown here.</p><div class="project-gallery">'+''.join(figure(im) for im in rest if im[0]!=21)+'</div></section>'
    elif rest:
        body+='<section class="case-process" aria-labelledby="process-title"><h2 class="case-section-title" id="process-title">Selected views &amp; process</h2><div class="project-gallery">'+''.join(figure(im) for im in rest)+'</div></section>'
    for file,poster,title,desc in p.get('videos',[]):
        body+=f'''<section class="film"><h2>{esc(title)}</h2><video controls playsinline preload="none" poster="{image(poster,'../')}" aria-label="{esc(title)}"><source src="../assets/{file}" type="video/mp4"><p>Your browser does not support this video. <a href="../assets/{file}">Download the video</a>.</p></video><p>{esc(desc)}</p><a class="subtle-link" href="../assets/{file}" download>Download video</a></section>'''
    for file,poster,title,desc in p.get('models',[]):
        body+=f'''<section class="model-section"><h2>{esc(title)} in 3D</h2><div class="model-shell"><model-viewer src="../assets/{file}" poster="{image(poster,'../')}" alt="Interactive 3D model of {esc(title)}" camera-controls touch-action="pan-y" shadow-intensity="1" exposure="1" loading="lazy" reveal="interaction"><button type="button" slot="poster" class="model-poster" style="background-image:url('{image(poster,'../')}')"><span>Load interactive 3D model</span></button><div slot="progress-bar" class="model-progress">Loading 3D model…</div></model-viewer><p class="model-error" hidden>The 3D preview could not load. You can download the original model below.</p></div><p>{esc(desc)} Drag to rotate, pinch or scroll to zoom. Keyboard arrow keys rotate the model after loading.</p><a class="subtle-link" href="../assets/{file}" download>Download original GLB</a></section>'''
    previous=projects[(i-1)%len(projects)];nxt=projects[(i+1)%len(projects)]
    body+=f'''<section class="credits"><h2>Credits &amp; project status</h2><p>{esc(p['credits'])}</p><p class="project-status"><strong>Status.</strong> {esc(p['status'])}</p></section><nav class="project-pagination" aria-label="More projects"><a href="{previous['slug']}.html"><span>Previous project</span>{esc(previous['title'])}</a><a href="{nxt['slug']}.html"><span>Next project</span>{esc(nxt['title'])}</a></nav></main>'''
    if p.get('models'):body+='<script type="module" src="../assets/vendor/model-viewer.min.js"></script>'
    (root/'projects'/f"{p['slug']}.html").write_text(body+footer('../'),encoding='utf-8')
print('Updated homepage and all 12 existing project routes. No assets removed.')
