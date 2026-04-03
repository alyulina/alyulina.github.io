# alyulina.github.io

Source code for my personal academic website at [alyulina.github.io](https://alyulina.github.io). I tried keeping it simple so that it could be maintained without much effort.

## Editing the site

### Content pages
Each page (`index.html`, `research/index.html`, `contact/index.html`, etc.) is a standalone file; edit them directly. Not that – at least at the moment – adding a new page requires changing the navigation menu across _all other pages_.

### Publications
Publications are managed through the bibliography file `publications/publications.json`. See [`publications/README.md`](publications/README.md) for detailed instructions.

### CV
Upload a new `assets/cv.pdf` file.

### Notes
Notes are standalone files in the `notes/` folder, named `YYYY-MM-DD-slug.html`. They must also be manually linked from `notes/index.html`. See [`notes/README.md`](notes/README.md) for detailed instructions.

### Deployment
This site is hosted using GitHub Pages and is automatically deployed from the `main` branch.

## If you are forking this

You are welcome to use this as a template for your own site as per `LICENSE.md`. A few things to take care of:

**Replace my personal information** by editing:
- `_config.yml` — update the `name` field
- `index.html` — replace the about text and photo
- `research/index.html` — replace the research description
- `publications/publications.json` — replace with your publications
- `publications/index.html` — update `MY_NAME` to your name in author list format (e.g. `'Smith J'`)
- `notes/index.html` — do not include my notes without authorship attribution
- `assets/cv.pdf` — replace with your CV
- `contact/index.html` — replace the contact details

Update **third-party account verification**.
- The file `google389ca975a7ef614c.html` in the root is an ownership verification file for Google Search Console. Delete it or replace it with your own.
- The `.well-known/` folder contains an `atproto-did` file used to verify my Bluesky account. Delete it or replace it with your own.

**Attribution.** I would appreciate a note on your website, e.g. “Adapted from Anastasia Lyulina”.

If you do use this as a template, I'd love to know — feel free to drop me a line!
