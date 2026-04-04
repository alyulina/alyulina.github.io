This repository contains the source code for my personal academic website. It is built using [Jekyll](https://jekyllrb.com), hosted on [GitHub Pages](https://pages.github.com), and automatically deployed from the `main` branch. I tried keeping it simple so that it could be maintained without much effort.

## Basic maintenance and updates

**Publications**. Publications are managed through the bibliography file `publications/publications.json`. See [`publications/README.md`](publications/README.md) for detailed instructions.

**Notes**. Notes are standalone files in the `notes/` folder, named `YYYY-MM-DD-note.html`. They must also be manually linked from `notes/index.html`. See [`notes/README.md`](notes/README.md) for detailed instructions.

**CV**. Replace `assets/cv.pdf` with an updated file.

**Other content**. Each page (`index.html`, `research/index.html`, `contact/index.html`, etc.) is a standalone file; edit them directly. To add a new page, create a new folder with an `index.html` inside (e.g. `teaching/index.html`) following the structure of existing pages, and add it to `_includes/nav.html` to include it in the navigation bar. For better search engine results, add a `description` field to the front matter of any page you want indexed.


## If you are forking this

You are welcome to use this as a template for your own site as per [`LICENSE.md`](LICENSE.md). A few things to take care of:

- **Replace my personal information** by editing:
  - `_config.yml` — update the `name` field.
  - `index.html` — replace the about text and photo.
  - `research/index.html` — replace my research description.
  - `publications/publications.json` — replace with your publications.
  - `publications/index.html` — update the `MY_NAME` variable to your name (e.g. `'Smith J'`) for publication formatting.
  - `notes/index.html` — please do not include my notes without proper acknowledgments.
  - `assets/cv.pdf` — replace with your own.
  - `contact/index.html` — replace the contact details.

- Update **third-party account verification**:
  - The file `google389ca975a7ef614c.html` in the root is an ownership verification file for [Google Search Console](https://search.google.com/search-console/about). Delete it or replace it with your own.
  - The `.well-known/` folder contains an `atproto-did` file used to verify my [Bluesky account](https://bsky.app/profile/alyulina.github.io). Delete it or replace it with your own.

- Provide **attribution.** I would appreciate a note on your website, e.g.
  >Adapted from Anastasia Lyulina

If you do use this as a template, I would love to know — feel free to drop me a line!
