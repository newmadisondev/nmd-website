/* Project map — OpenStreetMap street map (via Leaflet), shown in the dark map section.
 *
 * Pins are placed from each project's geocoded street address.
 * TO MOVE A PIN: open Google Maps, right-click the building, click the coordinates
 * at the top of the menu to copy them (e.g. 43.0812, -89.3733), and paste them below.
 * The numbers must stay in the same order as the list next to the map.
 */
var NMD_PROJECTS = [
  // Coordinates are the geocoded street addresses (sources in notes/sources.md).
  { num: 1, slug: 'starkweather-place', name: 'Starkweather Place',     lat: 43.10188, lng: -89.33048 }, // 215 N Fair Oaks Ave
  { num: 2, slug: 'traders-way',        name: 'Trader\u2019s Way',      lat: 43.07522, lng: -89.49456 }, // 6624 Old Sauk Rd
  { num: 3, slug: 'the-tinsmith',       name: 'The Tinsmith',           lat: 43.08116, lng: -89.37333 }, // 828 E Main St
  { num: 4, slug: 'dickinson-street',   name: '210 S Dickinson Street', lat: 43.08645, lng: -89.36203 }, // 210 S Dickinson St
  { num: 5, slug: 'northern-court',     name: 'Northern Court',         lat: 43.08743, lng: -89.36233 }  // between 1401 and 1413 Northern Ct
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
  // Keep neighbouring pins readable when zoomed out: pins closer than one pin-width are
  // nudged apart on screen only. Their map positions stay exact, and the nudge disappears as you zoom in.
  var PIN = 32;
  function declutter() {
    var pts = markers.map(function (x) { return map.latLngToContainerPoint(x.marker.getLatLng()); });
    var off = markers.map(function () { return { x: 0, y: 0 }; });
    for (var i = 0; i < pts.length; i++) {
      for (var j = i + 1; j < pts.length; j++) {
        var dx = pts[j].x - pts[i].x, dy = pts[j].y - pts[i].y, d = Math.sqrt(dx * dx + dy * dy);
        if (d >= PIN) continue;
        var ux = d ? dx / d : 0, uy = d ? dy / d : 1, push = (PIN - d) / 2;
        off[i].x -= ux * push; off[i].y -= uy * push;
        off[j].x += ux * push; off[j].y += uy * push;
      }
    }
    markers.forEach(function (x, k) {
      var span = x.marker.getElement() && x.marker.getElement().querySelector('span');
      if (span) span.style.translate = Math.round(off[k].x) + 'px ' + Math.round(off[k].y) + 'px';
    });
  }
  map.on('zoomend', declutter);
  map.fitBounds(L.featureGroup(markers.map(function (x) { return x.marker; })).getBounds(), { padding: [48, 48] });
  declutter();

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
