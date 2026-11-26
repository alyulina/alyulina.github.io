PhD defense page (`phd-defense/`), before sending invitations:

The page is locked: its text lives in `_drafts/phd-defense/content.html`, which is never committed (`_drafts/` is in `.gitignore`). After every edit there, run `python3 _scripts/lock_defense.py` (it asks for the page password) and commit `phd-defense/index.html`.

The page is in English and Russian: the draft has an English part and a Russian part, and a calendar block for each. Every change of date, time, room or Zoom details goes in both.

- [ ] Fill in the placeholders in `_drafts/phd-defense/content.html`, in both parts and both calendar blocks: intro, thesis title, abstract and chapters, date, time, room, the chair's name, and the Zoom link and passcode (link in `href`, passcode in `data-pw`); then relock. Check the St Petersburg time against the date (it is 11 hours ahead of Stanford in winter, 10 in summer). Check "add to calendar" on an iPhone and an Android phone.
- [ ] Russian part: think about how to talk about the science in Russian (the thesis title and the scientific terms).
- [ ] Remove the draft highlights: delete the two `.ph` rules at the top of `phd-defense/index.html`.
- [x] Move the folder to `/phd-defense/` at the top level, so the emailed link never changes.

After the defense:

- [ ] Make the page public again: put the text from `_drafts/phd-defense/content.html` back into `phd-defense/index.html` and remove the lock (the unlock lines, the `LOCKED` block and its code). `_scripts/lock_defense.py` can then be deleted.
- [ ] When the thesis is published: replace "full text to follow" with a link to it.
- [ ] Maybe also add a PDF of the introduction next to the page (for example `phd-defense/introduction.pdf`), linked from the same row.

Publications page, once there are more papers:

- [ ] Change the order of the sections to: manuscripts in preparation, then submitted, then published.
- [ ] Maybe highlight a few selected papers.
- [ ] Maybe group the papers by year.

Research page, when the postdoc starts:

- [ ] Rewrite the Research page text around the postdoc focus.
- [ ] Add one figure per section.

Code improvement and other ideas for when I have nothing else to do:

- [x] Extract `<nav>` into `_includes/nav.html` and use Liquid `page.url` for active link highlighting, replacing the per-page `id`-based approach.
- [x] Author collapse edge case: co-second and other middle `*` markers — the marked author is shown correctly with their `*` in the collapsed view, but co-authors sharing that mark are not shown. This is acceptable behavior; the `*` footnote still signals equal contribution. _No action needed unless this becomes confusing in practice._
- [ ] Auto-generate notes index: if the notes section grows, consider moving notes to `_posts/` as HTML files with proper front matter (`title`, `date`), which would allow `notes/index.html` to loop over `site.posts` automatically instead of manually adding links. _Low priority while notes are infrequent._
- [x] Clean up CSS. The spacing feels off in a few places.
- [ ] Add a teaching and mentoring section (or page) if applying for teaching-focused positions; until then, teaching is covered in the CV.
- [ ] Think if I want to add a separate page for misc stuff, e.g. CA backpacking notes and routes, or art that I make, including ceramics. I feel like I should not have that on my professional page, but realistically I will also not make another page for that; so it is either here or nowhere.
