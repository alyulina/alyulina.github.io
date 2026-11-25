# Adding a note

Notes live in the `notes/` folder as standalone files. There is no automatic indexing yet, so each note needs to be added manually after it is created.

## Step 0: draft in `_drafts/`

Write and revise the note in `_drafts/`. That folder is in `.gitignore`, so drafts are never committed (the repository is public), and Jekyll never builds folders starting with `_`, so a draft can't become a page. To preview drafts locally, add `--drafts` to the preview command (`bundle exec jekyll serve --drafts`); each draft then appears at a dated address, e.g. `_drafts/2026-11-11-laplace-transforms.html` at http://localhost:4000/notes/2026/11/11/laplace-transforms.html. When it is ready, move it from `_drafts/` to `notes/` and continue below.

## Step 1: create the note file

Create a new file in `notes/` named `YYYY-MM-DD-note.html`, where the date is the publication date and the slug is a short descriptive identifier, e.g. `2025-02-05-heterozygosity.html`. The file should start with a front matter block:

```yaml
---
layout: default
title: On something
---
```

Set `title` to the note's name. The browser tab then shows "Anastasia Lyulina | On something", and link previews show just the name.

Then write the note content inside a `<div>` with the nav block at the top. Use the existing notes as a template – they all follow the same structure.

## Step 2: add it to the notes index

Open `notes/index.html` and add a link to the new note inside the `<div class="notes">` block:

```html
<p><a href="YYYY-MM-DD-note" class="note-title" style="font-family:'Albra', 'Tiempos', 'Times New Roman', 'Serif'; font-size: 20px;">Note title</a> <span class="note-date"><span class="note-sep">· </span>Month D, YYYY</span></p>
```


## Formatting

**Equations.** MathJax 4 is loaded in `_layouts/default.html` and works out of the box. Use `$ ... $` for inline math and `$ \displaystyle{ ... } $` for display equations, wrapped in a centered paragraph that contains only the equation (and any trailing punctuation):

```html
<p style="text-align: center; display: block;">$ \displaystyle{ f(x) = \frac{1}{x} } $,</p>
```

A few things happen automatically when the page loads, so there is nothing extra to write:

- A centered paragraph holding a single `$...$` is typeset as a display equation, and `\displaystyle{ }` braces are dropped, so that equations too wide for the screen (in practice, on phones) break across lines at `=`, `≈`, `∼` and similar.
- Punctuation right after an equation (`$x$,` or `$x$.`) is moved inside it, so it never wraps onto a line by itself.

To keep this working, don't put anything else (text, `<br>`, a second equation) in the centered paragraph.

**Links between notes.** Link to other notes with an absolute path, e.g. `<a href="/notes/2025-02-05-heterozygosity">`, so the link also works while the note is still in `_drafts/`. Don't link to a note that isn't published yet.

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
