---
name: whiteboard
description: "Whiteboard a design for the user as one hand-written SVG diagram (or, when it outgrows one screen, an HTML page with the diagram inline), plus a short reading guide, built from an existing design record, so their mental model catches up. Use when the user says 白板一下, whiteboard this, 讲一下这个设计, 画张图, 心智模型跟不上, 我没跟上, walk me through the design, or when a design grew a second case and the mechanism and its variations are now explained together."
---

<what-to-do>

A whiteboard session **separates**. The user already has the facts; what they lack is the layering. The diagram's job is to split the **invariant** (what every case shares) from the **variables** (what each case decides), not to draw everything. Every step below serves that.

## 1. Name the sticking point and the source

You need two things: the design record the facts come from (a decision record, spec, ADR, refactor log), and the point where the user's model stalls. When the user has not said where they are stuck, ask one question. Typical stall: a second case was added and mechanism and posture got explained in one breath.

**Done when** you can name the source file and say in one line what the user cannot yet hold.

## 2. Find the thesis before drawing

Write one organising sentence; it becomes the title. Example: 「一个机制，两种姿态」. A title that only names the topic ("Records tool design") is not a thesis: keep looking. Draw nothing before this sentence exists.

**Done when** the title states an argument that the two panels will prove.

## 3. Let the content pick the form

- **Invariant** → a layered flow: who uses it → the single entry point → the storage underneath → what is shared.
- **Variables** → a table: one row per dimension, one column per case. A third case is one more column, nothing else moves.
- **Contract** (the few fields or calls the mechanism actually knows) → a small callout box.
- **Footer** → the splitting rule in one line, open questions in one line.

Zero new claims: every number and sentence on the diagram must be findable in the source record. The diagram compresses the argument; it is not a new document. A claim you cannot trace gets cut, not softened.

## 4. Pick the path, then write the SVG by hand

Two paths. The content decides, not taste.

- **Single screen (default).** One `design.svg` holds everything, and a two-line `index.html` embeds it with `<img>`. Take it when the whole argument fits about 1440 × 1100: two or three cases, a variables table of up to about eight rows with no cell over three lines, one diagram. One file, so what you checked is exactly what the user sees.
- **Page.** One `index.html`: inline SVG only for what carries meaning by position and connection (layers, lanes, arrows, buses, the boxes they join), HTML for everything that is mostly text (the thesis as `<h1>`, the variables as a `<table>`, the contract callout, the footer, any paragraph). Take it when any one of these holds: a fourth case or more, table cells that need paragraphs, more than one diagram (a mechanism plus a migration sequence, say), or prose that must sit beside the figure.

Signal you picked wrong: on the single-screen path you are doing line-break arithmetic for something with no arrows, or shrinking the canvas to fit. Switch to the page.

Hand-write the SVG on both paths. A model-generated image cannot draw structure accurately, and a chart library is for data, not design. SVG stays sharp at any zoom, diffs as text, and can be edited on the next round.

Read [`SVG.md`](SVG.md) for type, colour, layout arithmetic, and each path's skeleton. Copy from [`examples/records-design/`](examples/records-design/) (single screen) or [`examples/records-design-page/`](examples/records-design-page/) (the same content as a page, kept as the page skeleton) rather than starting blank.

Put the files in a scratch directory of their own, outside any tracked tree unless the user wants it kept.

## 5. Look at your own diagram before anyone else does

Render to PNG, open the image, list every defect, fix, re-render. Text overflowing a box, an arrow crossing a box, a line running past the canvas: these live in the pixels, not in the source. [`SVG.md`](SVG.md) has the render commands for each path.

**Done when** a render of every region shows no overflow, no arrow through a box, no clipped line, and you have read the whole thing as an image at least once after the last edit. On the page path, the text parts also read cleanly at a narrow width. Then delete the render artefacts: the directory holds only what you will serve.

## 6. Serve, then hand over with a reading guide

Serve the directory through whatever the host offers for showing local files to the user (a preview server, a tunnel), and confirm the URL actually loads before sending it. A file path is the fallback when nothing can serve.

The reply carries, in this order:

- the URL;
- a reading guide of at most eight lines: which panel first, what each panel answers;
- **one-line compression** of the whole diagram (「机制是工具的，姿态是仓库的」);
- open questions, listed separately so they are not mistaken for settled design.

**Done when** the URL is live, every claim on the diagram traces to the source record, and the user can read it in about two minutes.

</what-to-do>

<supporting-info>

## Where this fits

- `briefing` writes for a named non-technical decider who must ratify. `whiteboard` draws for the user's own understanding. Briefing's reader model maps to the sticking point here; briefing's cost sentence maps to the thesis. When a briefing needs a structural figure, call the Skill tool with "whiteboard" to draw it.
- `dataviz` owns charts of data. A figure of quantities over time or categories goes there.

</supporting-info>
