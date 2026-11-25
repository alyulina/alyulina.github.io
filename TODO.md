PhD defense page (`phd-defense/`), before sending invitations:

The page is locked: its text lives in `_drafts/phd-defense/content.html`, which is never committed (`_drafts/` is in `.gitignore`). After every edit there, run `python3 _scripts/lock_defense.py` (it asks for the page password) and commit `phd-defense/index.html`.

The page is in English and Russian (the по-русски button): the draft has an English part and a Russian part, and a calendar block for each. Every change of date, time, room or Zoom details goes in both. Show any new Russian wording to me before it goes live.

- [ ] Fill in the placeholders in `_drafts/phd-defense/content.html`, in both the English and the Russian part: intro, thesis title, abstract and chapters, date, room, and the chair's name. In Russian, write the date like «1 марта 2027».
- [ ] Russian part: think about how to talk about the science in Russian (the thesis title and the scientific terms). The usual Russian terms don't sound right, so it may be best to keep the title in English.
- [ ] Russian part: update the St Petersburg time by hand once the date is set (in «Когда»). St Petersburg is 11 hours ahead of Stanford in winter, 10 in summer (US clocks change in March and November).
- [ ] Remove the draft highlights: delete the two `.ph` rules at the top of `phd-defense/index.html`.
- [ ] Zoom: put the meeting link and passcode in the "Join online" row and the «Удалённо» row of `_drafts/phd-defense/content.html` (link in `href`, passcode in `data-pw`), then relock. Ask whoever hosts to turn on the waiting room, or make a friend a co-host to let guests in.
- [ ] Calendar: put the real date, time and place in both calendar blocks at the end of `_drafts/phd-defense/content.html` (English and Russian; placeholder values for now), then relock. Check "add to calendar" / «в календарь» on an iPhone (adds the calendar file) and on an Android phone (opens Google Calendar with the event filled in).
- [ ] Pick the final page password before the invitations go out (changing it later locks out guests who have the old one).
- [x] Move the folder to `/phd-defense/` at the top level, so the emailed link never changes.
- [ ] If the page should show up in search: delete the `noindex` line in `index.html` and `beads.html`.

After the defense:

- [ ] Make the page public again: paste the contents of `_drafts/phd-defense/content.html` back into the empty `<div class="content">` in `phd-defense/index.html` (without the note at the top), then remove the lock: the two "unlock page" / "email" lines, the `LOCKED` block and the unlock code in the script, and the email line in the `<noscript>` part (keep the still row of beads). Turn the calendar block back into a separate `lyulina-phd-defense.ics` file next to the page. Take the Zoom row out, since the meeting is over. `_scripts/lock_defense.py` can then be deleted.
- [ ] When the thesis is published: replace "full text to follow" with a link to it (in `_drafts/phd-defense/content.html` and relock, if the page is still locked then).
- [ ] Maybe also add a PDF of the introduction next to the page (for example `phd-defense/introduction.pdf`), linked from the same row.

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
