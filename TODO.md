Code improvement and other ideas for when I have nothing else to do:

- [x] Extract `<nav>` into `_includes/nav.html` and use Liquid `page.url` for active link highlighting, replacing the per-page `id`-based approach.
- [x] Author collapse edge case: co-second and other middle `*` markers — the marked author is shown correctly with their `*` in the collapsed view, but co-authors sharing that mark are not shown. This is acceptable behavior; the `*` footnote still signals equal contribution. _No action needed unless this becomes confusing in practice._
- [ ] Auto-generate notes index: if the notes section grows, consider moving notes to `_posts/` as HTML files with proper front matter (`title`, `date`), which would allow `notes/index.html` to loop over `site.posts` automatically instead of manually adding links. _Low priority while notes are infrequent._
- [ ] Clean up CSS. The spacing feels off in a few places.
- [ ] If `MY_NAME` is not found in the author list of a paper (e.g. due to a typo in `publications.json`), skip the entry and log a console warning. Do not attempt to render it.
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
