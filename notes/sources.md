# Sources

## Used on the site
- `content/content-v3.md` (William's content, merged from `main`). Every fact on the site comes from this file. It replaces `content.md` and `content-v2.md`.
- William's headshot: Principal Madison About page, page 8 of "998_E_Main_Sun_Prairie_-_Listing_Proposal_v21_-_About_from_website.pdf" in William's Google Drive.
- Trader's Way site plan and floor plan: "Traders_Way_Units_209_215_251_V8_10_13_26_-_253_removed.pdf" in William's Google Drive (images only; no text or figures from it are used).
- Photos: `content/photos/` (William's files, including `starkweather-drone.jpg` and `starkweather-photo-2.jpg`). Logos: `content/logo/`.
- Map: street map tiles © OpenStreetMap contributors (https://www.openstreetmap.org/copyright), displayed with Leaflet 1.9.4 (https://leafletjs.com, BSD 2-Clause, `assets/vendor/leaflet/LICENSE.txt`).
- Map pin coordinates, from the geocoded street address in published listings. At least two sources agree within about 10 m for each. Nominatim and the City/County address services were blocked from the build environment, so these were used instead:
  - 215 N Fair Oaks Ave: 43.10188, -89.33048 (Rent.com and ApartmentGuide listing data; Apartments.com and starkweatherplace.com agree within ~10 m).
  - 6624 Old Sauk Rd: 43.07522, -89.49456 (ApartmentGuide listing data for Trader's Way, https://www.apartmentguide.com/a/Traders-Way-Madison-WI-6755989/).
  - 828 E Main St: 43.08116, -89.37333 (Isthmus and Visit Madison listing data for The Tinsmith; MapQuest, Poyst and Green Bowtie agree within ~1 m).
  - 210 S Dickinson St: 43.08645, -89.36203 (MapQuest, https://www.mapquest.com/us/wisconsin/madison-window-cleaning-410781938; Yellow Pages and Nextdoor agree within ~10 m).
  - Northern Court: 43.08743, -89.36233, the midpoint of 1413 Northern Ct (43.08752, -89.36219, Visit Madison and MapQuest listings for State Line Distillery) and 1401 Northern Ct (43.08735, -89.36247, business directory for Northern Plating).
  The no-JavaScript fallback drawing uses the same coordinates; its lake shapes are hand-drawn approximations.
- Fonts: Hanken Grotesk and Instrument Serif, Google Fonts (https://fonts.google.com), SIL Open Font License (`assets/fonts/OFL-*.txt`).

## Looked at early, not used
Before William's content files arrived, a few public web searches were run. None of it is used on the site.
- https://statelinedistillery.com/visit
- https://greenbowtie.com/venues/wisconsin/the-tinsmith-madison
- https://www.ibmadison.com/industries/construction-real-estate/madison-window-cleaning-to-build-expand/article_8ad5a921-d3cd-58ef-87d6-d00e8c529d13.html
- https://hotpads.com/traders-way-madison-wi-53705-25dcb88/pad
