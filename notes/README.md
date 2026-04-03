# Adding a note

Notes live in the `notes/` folder as standalone files. There is no automatic indexing yet, so each note needs to be added manually after it is created.

## Step 1: create the note file

Create a new file in `notes/` named `YYYY-MM-DD-note.html`, where the date is the publication date and the slug is a short descriptive identifier, e.g. `2025-02-05-h-of-s.html`. The file should start with a front matter block:

```yaml
---
layout: default
title: Anastasia Lyulina | Notes
---
```

Then write the note content inside a `<div>` with the nav block at the top. Use the existing notes as a template – they all follow the same structure.

## Step 2: add it to the notes index

Open `notes/index.html` and add a link to the new note inside the `<div class="notes">` block:

```html
<p><a href="YYYY-MM-DD-note" style="font-family:'Albra', 'Tiempos', 'Times New Roman', 'Serif'; font-size: 20px;">Note title</a></p>
```


## Formatting

**Equations.** MathJax is loaded in `_layouts/default.html` and works out of the box. Use `$ ... $` for inline math and `$ \displaystyle{ ... } $` for display equations, wrapped in a centered paragraph:

```html
<p style="text-align: center; display: block;">
  $ \displaystyle{ f(x) = \frac{1}{x} } $
</p>
```

**Figures.** Use the `.figure-container` class defined in `css/main.css` for figures with captions:

```html
<div class="figure-container">
  <div class="figure">
    <img src="/img/your-figure.png" alt="Figure description">
  </div>
  <div class="legend">
    Caption text goes here.
  </div>
</div>
```

**Section headings.** Use `<h2>` with an inline font size override to match the existing style:

```html
<h2>Section title</h2>
```

**Footnotes.** Add footnote markers inline with `<sup>1</sup>` and collect the footnote text at the bottom of the note after an `<hr>`, using the `.footnote` class:

```html
<hr style="width:25%" align="left">
<p class="footnote"><sup>1</sup> Footnote text here.</p>
```

**Acknowledgments.** If you want to thank people, add a serif italic paragraph just above the footnotes:

```html
<p style="font-family:'Albra', 'Tiempos', 'Times New Roman', 'Serif';">
  <em>Thanks to ...</em>
</p>
```
