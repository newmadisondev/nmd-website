/* Project map — OpenStreetMap street map (via Leaflet), shown in the dark map section.
 *
 * TO MOVE A PIN: open Google Maps, right-click the building, click the coordinates
 * at the top of the menu to copy them (e.g. 43.0802, -89.3727), and paste them below.
 * The numbers must stay in the same order as the list next to the map.
 */
var NMD_PROJECTS = [
  { num: 1, slug: 'starkweather-place', name: 'Starkweather Place',     lat: 43.0985, lng: -89.3315 },
  { num: 2, slug: 'traders-way',        name: 'Trader’s Way',      lat: 43.0750, lng: -89.4962 },
  { num: 3, slug: 'the-tinsmith',       name: 'The Tinsmith',           lat: 43.0802, lng: -89.3727 },
  { num: 4, slug: 'dickinson-street',   name: '210 S Dickinson Street', lat: 43.0857, lng: -89.3667 },
  { num: 5, slug: 'northern-court',     name: 'Northern Court',         lat: 43.0893, lng: -89.3645 }
];

(function () {
  var el = document.getElementById('project-map');
  if (!el || !window.L) return; // without JavaScript the simple drawn map stays in place

  var base = el.getAttribute('data-base') || '';
  el.innerHTML = '';
  el.classList.add('is-live');

  var map = L.map(el, {
    scrollWheelZoom: false,          // don't trap the page scroll
    dragging: !L.Browser.mobile,     // on phones, one finger scrolls the page
    tap: false,
    zoomControl: true,
    attributionControl: true
  });
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    subdomains: 'abc',
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" rel="noopener">OpenStreetMap</a> contributors'
  }).addTo(map);
  map.attributionControl.setPrefix('<a href="https://leafletjs.com" rel="noopener">Leaflet</a>');

  var markers = [];
  NMD_PROJECTS.forEach(function (p) {
    var icon = L.divIcon({ className: 'nmd-pin', html: '<span>' + p.num + '</span>', iconSize: [30, 30], iconAnchor: [15, 15] });
    var m = L.marker([p.lat, p.lng], { icon: icon, title: p.name, keyboard: true })
      .bindPopup('<a href="' + base + 'projects/' + p.slug + '.html">' + p.name + '</a>', { closeButton: false, offset: [0, -10] })
      .addTo(map);
    m.on('mouseover', function () { highlight(p.slug, true); });
    m.on('mouseout', function () { highlight(p.slug, false); });
    m.on('click', function () { m.openPopup(); });
    markers.push({ slug: p.slug, marker: m });
  });
  map.fitBounds(L.featureGroup(markers.map(function (x) { return x.marker; })).getBounds(), { padding: [48, 48] });

  function highlight(slug, on) {
    document.querySelectorAll('.map-list [data-pin="' + slug + '"]').forEach(function (a) { a.classList.toggle('is-active', on); });
    markers.forEach(function (x) {
      var node = x.marker.getElement();
      if (node && x.slug === slug) node.classList.toggle('is-active', on);
    });
  }
  // Hovering a row in the list lights up its pin and opens its label.
  document.querySelectorAll('.map-list [data-pin]').forEach(function (a) {
    var slug = a.getAttribute('data-pin');
    var hit = markers.filter(function (x) { return x.slug === slug; })[0];
    if (!hit) return;
    a.addEventListener('mouseenter', function () { highlight(slug, true); hit.marker.openPopup(); });
    a.addEventListener('mouseleave', function () { highlight(slug, false); hit.marker.closePopup(); });
  });
})();
