This repository contains the source code for my personal academic website. It is built using [Jekyll](https://jekyllrb.com), hosted on [GitHub Pages](https://pages.github.com), and automatically deployed from the `main` branch. I tried keeping it simple so that it could be maintained without much effort.

## Basic maintenance and updates

**Publications**. Publications are managed through the bibliography file `publications/publications.json`. See [`publications/README.md`](publications/README.md) for detailed instructions.

**Notes**. Notes are standalone files in the `notes/` folder, named `YYYY-MM-DD-note.html`. They must also be manually linked from `notes/index.html`. See [`notes/README.md`](notes/README.md) for detailed instructions.

**Other content**. Each page (`index.html`, `research/index.html`, `contact/index.html`, etc.) is a standalone file; edit them directly. Updating the **CV** requires uploading a new `assets/cv.pdf` file. Note that adding a new page (e.g. `teaching/index.html`) will require changing the navigation menu across _all other pages_.


## If you are forking this

You are welcome to use this as a template for your own site as per `LICENSE.md`. A few things to take care of:

- **Replace my personal information** by editing:
  - `_config.yml` — update the `name` field
  - `index.html` — replace the about text and photo
  - `research/index.html` — replace the research description
  - `publications/publications.json` — replace with your publications
  - `publications/index.html` — update `MY_NAME` to your name in author list format (e.g. `'Smith J'`)
  - `notes/index.html` — do not include my notes without authorship attribution
  - `assets/cv.pdf` — replace with your CV
  - `contact/index.html` — replace the contact details

- Update **third-party account verification**:
  - the file `google389ca975a7ef614c.html` in the root is an ownership verification file for Google Search Console – delete it or replace it with your own
  - the `.well-known/` folder contains an `atproto-did` file used to verify my Bluesky account – delete it or replace it with your own.

- **Attribution.** I would appreciate a note on your website, e.g.
  >Adapted from Anastasia Lyulina

If you do use this as a template, I would love to know — feel free to drop me a line!
