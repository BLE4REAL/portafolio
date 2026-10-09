# BLE Portfolio

Portfolio of Juan Esteban Araujo Ortiz (BLE), built from the supplied 21-slide presentation. English content, 12 project pages, 39 optimized images, six videos and three interactive GLB models.

## Run locally

In the GitHub checkout, serve the docs folder using a static server, for example `python -m http.server 4174 --directory docs`, then open http://localhost:4174. A server is needed for the interactive models.

## Publish

GitHub Pages: repository Settings → Pages → Deploy from a branch → main → /docs → Save. The deployed website files are in docs/. No build service or account is required.

## Content

All portfolio assets originate in BLE_Portfolio_Interactive_Final_v2.pptx. Credits are retained on each project page. Vapo's supplied model has no textures. Acting-scene assets and Mixamo base models are attributed as provided. Do not infer a license granting reuse of portfolio artwork.

## Dependencies

The local model-viewer 4.3.1 bundle is from @google/model-viewer (Apache-2.0). Fonts: Barlow Condensed and Manrope, from Google Fonts, redistributed under their original Open Font License. Fonts and scripts are hosted locally; no analytics, tracking or external font requests.


## Current local review

Character-focused revision on `review/character-focus`. This revision has not been published.

Edit project content in `content/projects.json`, then run `python tools/build.py`. The generator rebuilds the homepage and 12 project pages in `docs/`; CSS and interaction code remain in `docs/styles.css` and `docs/app.js`. Run `python tools/validate.py` to check routes, anchors and media preservation. Serve `docs/` for browser review. Do not run the older generator outside this repository.

Selected work: VERT, Cheni, Weathered Treasure Chest and Corner Café. Eight further projects remain accessible under Studies & exploration. Cheni distinguishes the original concept from the current 3D version; new-version imagery must only be added when supplied.
