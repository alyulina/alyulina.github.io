# Adding a paper to the publications page

All papers are stored in `publications.json`. To add a new paper, simply add a new entry.

## Fields

| Field | Description |
|---|---|
| `authors` | Author list, comma-separated. Use `*` for co-first/co-last, `**` for co-last when both symbols are needed. |
| `title` | Paper title. |
| `year` | Publication year (e.g. `"2025"`). Leave empty (`""`) if not yet published. |
| `status` | One of `"published"`, `"review"`, or `"preparation"`. |
| `paper` | Journal link. Leave empty if unavailable. |
| `code` | Code repository link. Leave empty if unavailable. |
| `thread` | Social media thread link. Leave empty if unavailable. |
| `cover` | Journal cover link. Leave empty if unavailable. |
| `commentary` | Commentary or editorial link. Leave empty if unavailable. |
| `news` | News article link. Leave empty if unavailable. |

## How papers are displayed

- **Published manuscripts**: any paper with a non-empty `year`, sorted by year (newest first), numbered in reverse order. A manuscript that was preprinted (and hence has a publication year) will be listed here.
- **Manuscripts in preparation**: any paper with an empty `year`, displayed in the same order as in `publications.json`, numbered in reverse. A manuscript that was not preprinted will appear here, even if it was sent out for review.
- Papers with `status: "review"` appear with an *under review* label and a `preprint` button instead of `paper`, if a preprint is available.
- Author lists longer than 12 are collapsed automatically, with an "all authors" toggle button.
- `Lyulina AS` is always bolded automatically — no need to add `<strong>` tags manually. Name can be changed in `index.html`.

## Example entry

```json
{
  "authors": "Lyulina AS*, Doe J*",
  "title": "A new paper about something interesting",
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

1. Set `year` to the publication year.
2. Set `status` to `"published"`.
3. Add the DOI to `paper`.
