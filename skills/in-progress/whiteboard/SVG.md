# SVG and page reference

What made the two examples render cleanly: [`examples/records-design/`](examples/records-design/) (single screen) and [`examples/records-design-page/`](examples/records-design-page/) (page). Copy a skeleton; adjust the numbers here.

## Single-screen skeleton

- `viewBox="0 0 1440 1100"` with matching `width`/`height`, and a white background `<rect>` first.
- Title and lede as SVG text at the top, invariant panel left, warm variables panel right, footer lines at the bottom.
- `index.html`: the `<img>`, one line of guidance, a link to the raw SVG. Constrain the wrapper to `max-width: 1440px` and let the image take `width: 100%`.

## Page skeleton

- `<h1>` thesis, one `.lede` line, then the inline `<svg>` (invariant) and a warm `<section>` (variables table, contract callout). Footer below: splitting rule, open questions.
- The example puts SVG and section in a two-column grid that stacks under about 1100px. If you keep that, write the lede without 左/右. Stacking always is the simpler choice and is fine.
- The SVG takes `width: 100%; height: auto`, no `width`/`height` attributes, and a `viewBox` sized to the diagram alone (example: `viewBox="30 92 880 930"`). The page supplies the background.

## Type

- Body font: `PingFang SC, Hiragino Sans GB, Helvetica Neue, Arial, sans-serif`. Identifiers, commands, field names: `SF Mono, Menlo, monospace`, one or two px smaller than the text around them.
- Sizes: title 26 bold, panel heading 17 bold, box heading 15 bold, box body 13, annotations 12.

## Colour

Colour carries meaning, one meaning per hue, held for the whole diagram:

- Neutral grey frames (`#d0d7de` stroke, `#f6f8fa` panel fill) for structure that carries no category.
- One hue per lane or concept the argument names (in the example: blue for `main` and the CLI, green for `records`).
- A warm panel (`#fffbf2` fill, `#e8d9b5` stroke) for the variables, so invariant and variables read apart before a word is read.
- Text `#1f2328`, secondary `#424a53`, annotation `#57606a`.

## Layout arithmetic

Measure before placing, so nothing overflows:

- A CJK glyph is about one font-size wide (13px text: about 13px per character). A Latin glyph is about 0.55 of the font-size.
- Box width ≥ longest line + 2 × 14px padding. When a line will not fit, break it with `<tspan x="…" dy="…">`, never by shrinking the font.
- Line pitch: 18 to 19px at 13px text. A table row of 87px holds three lines.
- Escape `<`, `>`, `&` in text as `&lt;`, `&gt;`, `&amp;`.

## Connectors

- Arrows: a `<marker>` in `<defs>` with `orient="auto-start-reverse"`, applied with `marker-end`. A dashed grey marker for references (pointers, IDs), a solid one for flow.
- Many-to-one: draw a **bus**. Short drops from each source into one horizontal line, then a single arrow to the target. A straight line from each source to the target crosses boxes.
- End arrows a couple of px short of the target edge so the head is visible.

## Self-check render (macOS)

QuickLook writes a square thumbnail.

**Single screen.** Render the SVG. The square crops a wide canvas on the right, so render the right half from a copy with a shifted viewBox:

```bash
qlmanage -t -s 2200 -o <dir> <dir>/design.svg
sed 's/viewBox="0 0 1440 1100"/viewBox="690 0 750 1100"/' <dir>/design.svg > <dir>/right.svg
qlmanage -t -s 2200 -o <dir> <dir>/right.svg
```

**Page.** QuickLook renders HTML through WebKit, inline SVG included, at roughly a phone-width viewport, and crops a long page at the bottom:

```bash
qlmanage -t -s 1600 -o <dir> <dir>/index.html
```

To see what falls below the crop, render a copy with the `<svg>` element stripped out. A wide multi-column layout never shows in QuickLook; check it with a browser screenshot when one runs, or say it is unverified.

Open each PNG as an image and read it. Remove the copies and every PNG afterwards.
