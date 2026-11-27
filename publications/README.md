# Adding a paper to the publications page

All papers are stored in `_data/publications.json`. To add a new paper, simply add a new entry.

The file is embedded in `publications/index.html` when the site is built (via `{{ site.data.publications | jsonify }}` near the bottom of the file).

## Fields

| Field | Description |
|---|---|
| `authors` | Author list, comma-separated. Use `*` for co-first/co-last, `**` for co-last when both symbols are needed. |
| `title` | Paper title. |
| `journal` | Journal name, written out in full (e.g. `"Nature Ecology & Evolution"`). For a preprint, `"bioRxiv"` or `"arXiv"`. Leave empty if not yet published. |
| `volume` | Volume number. Leave empty if unavailable. |
| `pages` | Page range or article number (e.g. `"2145–2160"` or `"iyae145"`). Leave empty if unavailable. |
| `year` | Publication year (e.g. `"2025"`). Leave empty (`""`) if not yet published. |
| `status` | Not shown on the page; decides where the paper goes. One of `"published"` (published papers and preprints), `"submitted"` (submitted, not public, so no `paper` link: once it is posted as a preprint, it counts as `"published"`) or `"preparation"`. A paper with any other value is not shown at all, so check the spelling. |
| `paper` | Journal or preprint link. Leave empty if unavailable. |
| `code` | Code repository link. Leave empty if unavailable. |
| `thread` | Social media thread link. Leave empty if unavailable. Currently not displayed (commented out in `publications/index.html`). |
| `cover` | Journal cover link. Leave empty if unavailable. |
| `commentary` | Commentary or editorial link. Leave empty if unavailable. |
| `news` | News article link. Leave empty if unavailable. |
| `note` | Link to an accompanying note on this site (e.g. `"/notes/2025-02-05-heterozygosity"`). Leave empty if there is none. |

## How papers are displayed

- Papers are split into two sections by `status`:
  - **Published** (`"published"`): published papers and preprints, sorted by year (newest first).
  - **Submitted and in preparation**: first the `"submitted"` papers, then the `"preparation"` ones, each in the same order as in `_data/publications.json`.
- Each section is numbered in reverse and is hidden if empty.
- Some papers get a short light-grey note on its own line under the citation and buttons:
  - a preprint (`"published"`, with `journal` set to `"bioRxiv"` or `"arXiv"`): *not peer reviewed*;
  - a submitted paper (`"submitted"`): *text available upon request*.
- The "These authors contributed equally" footnote sits at the end of the page.
- Author lists longer than 12 are collapsed automatically, with an "all authors" toggle button.
- `Lyulina AS` is always bolded automatically — no need to add `<strong>` tags manually. Name can be changed via `publication_name` in `_config.yml`.

## Quick reference

| Case | `status` | `journal` | `year` | `paper` | Section | Note |
|---|---|---|---|---|---|---|
| Published | `"published"` | journal name in full | year | DOI link | Published | none |
| Preprint | `"published"` | `"bioRxiv"` or `"arXiv"` | year | DOI link | Published | *not peer reviewed* |
| Submitted | `"submitted"` | `""` | `""` | `""` | Submitted and in preparation | *text available upon request* |
| In preparation | `"preparation"` | `""` | `""` | `""` | Submitted and in preparation | none |

## Example entry

```json
{
  "authors": "Lyulina AS*, Doe J*",
  "title": "A new paper about something interesting",
  "journal": "Genetics",
  "volume": "231",
  "pages": "iyae001",
  "year": "2026",
  "status": "published",
  "paper": "https://doi.org/10.xxxx/xxxxxx",
  "code": "https://github.com/alyulina/new-paper",
  "thread": "",
  "cover": "",
  "commentary": "",
  "news": "",
  "note": ""
}
```

## Adding a preprint

A preprint is listed with the published papers, marked as not peer reviewed:

1. Set `status` to `"published"`.
2. Set `journal` to `"bioRxiv"` or `"arXiv"`, fill in `year`, and leave `volume` and `pages` empty.
3. Add the preprint's DOI link to `paper` (bioRxiv: `https://doi.org/10.1101/…`; arXiv: `https://doi.org/10.48550/arXiv.…`).

## Moving a paper from in preparation to published

1. Set `status` to `"published"`.
2. Fill in `journal`, `volume`, `pages` and `year`.
3. Add the DOI to `paper`.

When a preprint comes out in a journal, do steps 2 and 3 the same way; the "not peer reviewed" note then disappears.
