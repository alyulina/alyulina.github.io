This repository contains the source code for my personal academic website. It is built using [Jekyll](https://jekyllrb.com), hosted on [GitHub Pages](https://pages.github.com), and automatically deployed from the `master` branch. I tried keeping it simple so that it could be maintained without much effort.

## Basic maintenance and updates

**Publications**. Publications are managed through the bibliography file `publications/publications.json`. See [`publications/README.md`](publications/README.md) for detailed instructions.

**Updates**. The short dated list next to the photo on the About page lives in `index.html` (the `<div class="news">` block). Add new items at the top and drop the oldest; three to five lines fit beside the photo on desktop.

**Notes**. Notes are standalone files in the `notes/` folder, named `YYYY-MM-DD-note.html`. They must also be manually linked from `notes/index.html`. Work on drafts in `_drafts/` — that folder is in `.gitignore` and is never committed (the repository is public), and Jekyll does not build folders starting with `_`. Preview drafts locally with `bundle exec jekyll serve --drafts`. Move a note to `notes/` only when it is ready to publish. See [`notes/README.md`](notes/README.md) for detailed instructions.

**CV**. Replace `assets/cv.pdf` with an updated file.

**Other content**. Each page (`index.html`, `research/index.html`, `contact/index.html`, etc.) is a standalone file; edit them directly. To add a new page, create a new folder with an `index.html` inside (e.g. `teaching/index.html`) following the structure of existing pages, and add it to `_includes/nav.html` to include it in the navigation bar. For better search engine results, add a `description` field to the front matter of any page you want indexed.

**Link previews**. When a page is shared (e.g. on Bluesky), the preview image comes from the `defaults` block in `_config.yml` (currently the portrait, `img/nastia_small.jpg`). To use a different image for one page, add `image: /img/your-image.png` to that page's front matter.

**Phone layout**. Screens 1024 px wide or narrower get the phone styles in the `@media (max-width: 1024px)` rules in `css/main.css` (and in a few pages' own `<style>` blocks). The layout is fluid, not scaled, so check new pages at phone width before pushing.

### Local preview

To preview the site locally before pushing, run the commands below _from the repository root_ and open http://localhost:4000 in your browser. Make sure Ruby and Jekyll are [installed](https://jekyllrb.com/docs/installation/).

```bash
bundle install   # first time only
bundle exec jekyll serve
```

If `bundle exec` fails with missing gems (e.g. after a Ruby update), building without Bundler also works for a quick look: `JEKYLL_NO_BUNDLER_REQUIRE=true jekyll serve`. GitHub Pages builds with its own Jekyll version, so minor differences are possible.

## If you are forking this

You are welcome to use this as a template for your own site as per [`LICENSE.md`](LICENSE.md). A few things to take care of:

- **Replace my personal information** by editing:
  - `_config.yml` — update the `name`, `title`, `description`, `url`, `social` links and the default preview `image`.
  - `index.html` — replace the about text, the updates list and the photo.
  - `research/index.html` — replace my research description.
  - `publications/publications.json` — replace with your publications.
  - `publications/index.html` — update the `MY_NAME` variable to your name (e.g. `'Smith J'`) for publication formatting.
  - `notes/index.html` — please do not include my notes without proper acknowledgments.
  - `assets/cv.pdf` — replace with your own.
  - `contact/index.html` — replace the contact details.

- Update **third-party account verification**:
  - The file `google389ca975a7ef614c.html` in the root is an ownership verification file for [Google Search Console](https://search.google.com/search-console/about). Delete it or replace it with your own.
  - The `.well-known/` folder contains an `atproto-did` file used to verify my [Bluesky account](https://bsky.app/profile/alyulina.github.io). Delete it or replace it with your own.

- Provide **attribution**. I would appreciate a note on your website, e.g.
  >Adapted from Anastasia Lyulina

If you do use this as a template, I would love to know — feel free to drop me a line!
