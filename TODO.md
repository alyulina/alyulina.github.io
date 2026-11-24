PhD defense page (`assets/phd-defense/`), before sending invitations:

- [ ] Fill in the placeholders: intro, thesis title, abstract and chapters, date, room, and the chair's name.
- [ ] Remove the pink draft highlights: delete the two `.ph` rules at the top of `assets/phd-defense/index.html`.
- [ ] Zoom: put the link and password in the invitation email, not on the page; ask whoever hosts to turn on the waiting room.
- [ ] Calendar: if the time or place changes (now March 1, 2027, 9 am to 12 pm, Room 122), edit `assets/phd-defense/lyulina-phd-defense.ics`.
- [ ] Move the folder to `/phd-defense/` at the top level before the invitations go out, so the emailed link never changes (and update the link in the `.ics` file).
- [ ] If the page should show up in search: delete the `noindex` line in `index.html` and `beads.html`.

Code improvement and other ideas for when I have nothing else to do:

- [x] Extract `<nav>` into `_includes/nav.html` and use Liquid `page.url` for active link highlighting, replacing the per-page `id`-based approach.
- [x] Author collapse edge case: co-second and other middle `*` markers — the marked author is shown correctly with their `*` in the collapsed view, but co-authors sharing that mark are not shown. This is acceptable behavior; the `*` footnote still signals equal contribution. _No action needed unless this becomes confusing in practice._
- [ ] Auto-generate notes index: if the notes section grows, consider moving notes to `_posts/` as HTML files with proper front matter (`title`, `date`), which would allow `notes/index.html` to loop over `site.posts` automatically instead of manually adding links. _Low priority while notes are infrequent._
- [ ] Clean up CSS. The spacing feels off in a few places.
- [ ] If `MY_NAME` is not found in the author list of a paper (e.g. due to a typo in `_data/publications.json`), skip the entry and log a console warning. Do not attempt to render it.
```
pubs.forEach(p => {
  if (!p.authors.includes(MY_NAME)) {
    console.warn(`Skipping entry — "${MY_NAME}" not found in authors: "${p.title}"`);
    return;
  }
  // ... rest of the existing code
});
```
- [ ] Do I want to add a page dedicated to teaching?
- [ ] Think if I want to add a separate page for misc stuff, e.g. CA backpacking notes and routes, or art that I make, including ceramics. I feel like I should not have that on my professional page, but realistically I will also not make another page for that; so it is either here or nowhere.
