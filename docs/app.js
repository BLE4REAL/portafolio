(() => {
  const filters = document.querySelectorAll('[data-filter]');
  const projects = document.querySelectorAll('[data-category]');
  filters.forEach(button => button.addEventListener('click', () => {
    const category = button.dataset.filter;
    filters.forEach(item => { const active = item === button; item.classList.toggle('active', active); item.setAttribute('aria-pressed', String(active)); });
    let visible = 0;
    projects.forEach(project => {
      const match = category === 'All' || (category === 'Studies' ? project.closest('.studies-grid') : project.dataset.category === category);
      project.hidden = !match;
      if (!project.hidden) visible++;
    });
    document.querySelectorAll('.project-grid').forEach(grid => grid.classList.toggle('filtered', category !== 'All'));
    document.querySelector('#filter-status').textContent = `${visible} ${visible === 1 ? 'project' : 'projects'} shown`;
    document.querySelector('.selected-empty').hidden = !!document.querySelector('.selected-grid .project-item:not([hidden])');
    document.querySelector('.studies-empty').hidden = !!document.querySelector('.studies-grid .project-item:not([hidden])');
  }));
  const features = {
    vert: { image: 'assets/image4.webp', alt: 'VERT — stylized character render by BLE', href: 'projects/vert.html', label: 'Explore VERT' },
    cheni: { image: 'assets/image1.webp', alt: 'Cheni — original character concept; 3D version in development', href: 'projects/cheni.html', label: 'Explore Cheni’s concept' },
    chest: { image: 'assets/image5.webp', alt: 'Weathered Treasure Chest — stylized prop render by BLE', href: 'projects/treasure-chest.html', label: 'Explore the chest' }
  };
  let featureRequest = 0;
  let outgoingArt;
  document.querySelectorAll('[data-feature]').forEach(button => button.addEventListener('click', async event => {
    const request = ++featureRequest;
    const feature = features[button.dataset.feature];
    const image = document.querySelector('#featured-image');
    const preload = new Image(); preload.src = feature.image;
    try { await preload.decode(); } catch { return; }
    if (request !== featureRequest) return;
    outgoingArt?.remove();
    const reduce = event.detail === 0 || matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!reduce) {
      outgoingArt = image.cloneNode(); outgoingArt.removeAttribute('id');
      outgoingArt.alt = ''; outgoingArt.setAttribute('aria-hidden', 'true');
      Object.assign(outgoingArt.style, {position:'absolute', inset:'0', pointerEvents:'none'});
      image.after(outgoingArt);
    }
    image.src = feature.image; image.alt = feature.alt;
    image.style.objectFit = button.dataset.feature === 'cheni' ? 'contain' : 'cover';
    image.style.objectPosition = button.dataset.feature === 'cheni' ? '85% center' : '70% center';
    const link = document.querySelector('#featured-link'); link.href = feature.href; link.textContent = feature.label;
    document.querySelectorAll('[data-feature]').forEach(item => { const active = item === button; item.classList.toggle('active', active); item.setAttribute('aria-pressed', String(active)); });
    if (!reduce) {
      const layer = outgoingArt;
      layer.animate([{opacity:1},{opacity:0}], {duration:180, easing:'ease-out'}).onfinish = () => layer.remove();
    }
  }));
  const dialog = document.querySelector('.lightbox');
  let imageTrigger;
  document.querySelectorAll('.artwork-open').forEach(button => button.addEventListener('click', () => {
    if (!dialog || !dialog.showModal) { window.location.href = button.dataset.image; return; }
    imageTrigger = button;
    const img = dialog.querySelector('img'); img.src = button.dataset.image; img.alt = button.dataset.caption;
    dialog.querySelector('p').textContent = button.dataset.caption;
    dialog.showModal();
  }));
  dialog?.querySelector('.close-lightbox').addEventListener('click', () => dialog.close());
  dialog?.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  dialog?.addEventListener('close', () => imageTrigger?.focus());
  document.querySelectorAll('model-viewer').forEach(viewer => {
    const progress = viewer.querySelector('.model-progress');
    progress.hidden = true;
    viewer.querySelector('.model-poster').addEventListener('click', async () => {
      progress.hidden = false;
      await customElements.whenDefined('model-viewer');
      viewer.dismissPoster();
    });
    viewer.addEventListener('progress', event => { progress.hidden = event.detail.totalProgress >= 1; });
    viewer.addEventListener('error', () => { const error = viewer.parentElement.querySelector('.model-error'); error.hidden = false; });
    viewer.addEventListener('load', () => { const error = viewer.parentElement.querySelector('.model-error'); error.hidden = true; });
  });
})();
