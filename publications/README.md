# Adding a paper to the publications page

All papers are stored in `publications.json`. To add a new paper, add an entry anywhere in the array — published papers are sorted automatically by year (newest first), and preparation papers are displayed in the order they appear in the file.

## Fields

| Field | Description |
|---|---|
| `authors` | Author list, comma-separated. Use `*` for co-first/co-last, `**` for co-last when both symbols are needed. |
| `title` | Paper title. |
| `year` | Publication year (e.g. `"2025"`). Leave empty (`""`) if unpublished. |
| `status` | One of `"published"`, `"review"`, or `"preparation"`. |
| `paper` | DOI or journal URL. Leave empty if unavailable. |
| `code` | GitHub or other code repository URL. Leave empty if unavailable. |
| `thread` | Bluesky/Twitter thread URL. Leave empty if unavailable. |
| `cover` | Journal cover URL. Leave empty if unavailable. |
| `commentary` | Commentary or editorial URL. Leave empty if unavailable. |
| `news` | News article URL. Leave empty if unavailable. |

## How papers are displayed

- **Published manuscripts**: any paper with a non-empty `year`, sorted by year (newest first), numbered in reverse order.
- **Manuscripts in preparation**: any paper with an empty `year`, displayed in JSON order, numbered separately in reverse order.
- Papers with `status: "review"` appear in the preparation section with an *under review* label and a `preprint` button instead of `paper`.
- Author lists longer than 12 are collapsed automatically, with an "all authors" toggle button.
- `Lyulina AS` is always bolded automatically — no need to add `<strong>` tags manually.

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

The paper will automatically appear in the correct position in the published list — no reordering needed.
