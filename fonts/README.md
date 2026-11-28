# Fonts

`texgyretermes-*.otf`: TeX Gyre Termes (regular, bold, italic, bold italic), a free font drawn after Times. The site's serif ('Site Serif' in the CSS) is the Times New Roman installed on a visitor's device; these files are only downloaded where there is none (mostly Android and Linux), so that those visitors see the same letter shapes instead of their own default serif.

Source: CTAN, https://mirrors.ctan.org/fonts/tex-gyre/opentype/ (downloaded November 2026). Unmodified, under the GUST Font License (`GUST-FONT-LICENSE.txt`), which asks that changed versions be renamed, so keep them as they are.

The `@font-face` rules that load them are at the top of `css/main.css`.
