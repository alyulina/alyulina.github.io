# Adding a paper to the publications page

All papers are stored in `publications.json`. To add a new paper, simply add a new entry.

## Fields

| Field | Description |
|---|---|
| `authors` | Author list, comma-separated. Use `*` for co-first/co-last, `**` for co-last when both symbols are needed. |
| `title` | Paper title. |
| `journal` | Journal name, written out in full (e.g. `"Nature Ecology & Evolution"`). Leave empty if not yet published. |
| `volume` | Volume number. Leave empty if unavailable. |
| `pages` | Page range or article number (e.g. `"2145–2160"` or `"iyae145"`). Leave empty if unavailable. |
| `year` | Publication year (e.g. `"2025"`). Leave empty (`""`) if not yet published. |
| `status` | One of `"published"`, `"review"`, or `"preparation"`. |
| `paper` | Journal link. Leave empty if unavailable. |
| `code` | Code repository link. Leave empty if unavailable. |
| `thread` | Social media thread link. Leave empty if unavailable. Currently not displayed (commented out in `index.html`). |
| `cover` | Journal cover link. Leave empty if unavailable. |
| `commentary` | Commentary or editorial link. Leave empty if unavailable. |
| `news` | News article link. Leave empty if unavailable. |

## How papers are displayed

- Papers are split into three sections by `status`:
  - **Published manuscripts** (`"published"`): sorted by year (newest first).
  - **Submitted manuscripts** (`"review"`): in the same order as in `publications.json`.
  - **Manuscripts in preparation** (`"preparation"`): in the same order as in `publications.json`.
- Each section is numbered in reverse and is hidden if empty.
- Each entry reads: *Authors. Title. Journal Volume, Pages (Year).* The title is italic, and the journal name is in the serif italic (`.pub-journal` in `index.html`). Journal, volume, pages and year are each skipped when empty.
- Buttons (`paper`, `code`, `cover`, …) appear on the same line as the citation and wrap to the next line together.
- For `status: "review"`, the `paper` link appears as a `preprint` button.
- Author lists longer than 12 are collapsed automatically, with an "all authors" toggle button.
- `Lyulina AS` is always bolded automatically — no need to add `<strong>` tags manually. Name can be changed in `index.html`.

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
  "news": ""
}
```

## Moving a paper from in preparation to published

1. Set `status` to `"published"`.
2. Fill in `journal`, `volume`, `pages` and `year`.
3. Add the DOI to `paper`.
