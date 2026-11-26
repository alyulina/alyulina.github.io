This repository contains the source code for my personal academic website. It is built using [Jekyll](https://jekyllrb.com), hosted on [GitHub Pages](https://pages.github.com), and automatically deployed from the `master` branch. I tried keeping it simple so that it could be maintained without much effort.

## Basic maintenance and updates

**Publications**. Publications are managed through the bibliography file `_data/publications.json`. See [`publications/README.md`](publications/README.md) for detailed instructions.

**Updates**. Edit the list next to the photo in `index.html`; newest first, three to five items.

**Notes**. Notes are standalone files in the `notes/` folder, named `YYYY-MM-DD-note.html`. They must also be manually linked from `notes/index.html`. Drafts go in `_drafts/`, which is never committed. See [`notes/README.md`](notes/README.md) for detailed instructions.

**CV**. Replace `assets/lyulina_cv.pdf` with an updated file.

**Other content**. Each page (`index.html`, `research/index.html`, `contact/index.html`, etc.) is a standalone file; edit them directly. To add a new page, create a new folder with an `index.html` inside (e.g. `teaching/index.html`) following the structure of existing pages, and add it to `_includes/nav.html` to include it in the navigation bar. For better search engine results, add a `description` field to the front matter of any page you want indexed.

**MathJax**. Equations are rendered with [MathJax](https://www.mathjax.org) 4.1.3, which is stored in `mathjax/` and served from this site, so visitors' browsers don't contact any outside server and their IP addresses are not shared with third parties (a concern under the EU's GDPR; see e.g. [Regional Court of Munich I, 3 O 17493/20](https://www.gesetze-bayern.de/Content/Document/Y-300-Z-GRURRS-B-2022-N-612)). To update, replace the folder with the same files from the new versions of the `mathjax` and `@mathjax/mathjax-newcm-font` npm packages, and check in a local preview that the notes render and that the browser's network tab shows no requests to other sites.

### Local preview

To preview the site locally before pushing, run the commands below _from the repository root_ and open http://localhost:4000 in your browser. Make sure Ruby and Jekyll are [installed](https://jekyllrb.com/docs/installation/).

```bash
bundle install   # first time only
bundle exec jekyll serve
```

Add `--drafts` to include drafts. If gems are missing, `JEKYLL_NO_BUNDLER_REQUIRE=true jekyll serve` also works.

## On using Claude

Many recent changes were made with [Claude Code](https://claude.com/claude-code), under my review. It works well for a site like this – worth a try if you adapt it.

## If you are forking this

You are welcome to use this as a template for your own site as per [`LICENSE.md`](LICENSE.md). A few things to take care of:

- **Replace my personal information** by editing:
  - `_config.yml` — update the `name`, `description`, `url`, `social` links and `publication_name` (your name as it appears in author lists, e.g. `Smith J`). Most other pages read your name and address from here.
  - `index.html` — replace the about text, updates and photo, and the `description` at the top of the file.
  - `research/index.html` — replace my research description and the `description` at the top of the file.
  - `_data/publications.json` — replace with your publications.
  - `notes/` — please do not include my notes without proper acknowledgments. This also applies to the files they use, such as figures and notebooks.
  - `phd-defense/` — my PhD defense page; delete it.
  - `assets/lyulina_cv.pdf` — replace with your own.
  - `contact/index.html` — replace the contact details and the link to this repository at the bottom.

- Update **third-party account verification**:
  - The file `google389ca975a7ef614c.html` in the root and the `webmaster_verifications` entry in `_config.yml` verify ownership for [Google Search Console](https://search.google.com/search-console/about). Delete both or replace them with your own.
  - The `.well-known/` folder contains an `atproto-did` file used to verify my [Bluesky account](https://bsky.app/profile/alyulina.github.io). Delete it or replace it with your own.

- Provide **attribution**. I would appreciate a note on your website, e.g.
  >Adapted from Anastasia Lyulina

If you do use this as a template, I would love to know — feel free to drop me a line!
