## Code improvement

- [ ] Extract `<nav>` into `_includes/nav.html` and use Liquid `page.url` for active link highlighting, replacing the per-page `id`-based approach (see README for details)
- [ ] Use `_layouts/post.html` for notes instead of fully self-contained HTML files, so shared changes (scripts, styles) only need to be made once
- [ ] Delete `tmp.html` from repo root
- [ ] Remove dead `process()` function from `publications/index.html` (now only used for titles, could be inlined)
