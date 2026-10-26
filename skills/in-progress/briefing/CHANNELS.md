# Channels

A **channel** is where the document lands: a GitHub issue thread, a report the reader opens in a browser, a PDF they file, a Word file they edit, a chat post. The host decides what the reader sees around the document and how it is drawn, so each channel has its own render target and its own way to look at the result. The rules here hold for every reader. What one reader wants (voice, register, silences) lives in their reader model (see [`MECHANICS.md`](MECHANICS.md)), whatever the channel.

## GitHub issue or pull request comment

- Medium: Markdown. Front matter `cover: title` (the comment header already shows author and date) and `repo: owner/name`.
- Review with `build.py brief.md --to gh`, then screenshot `out/work.gh.html`: that is GitHub's own rendering, so autolinks, issue references, commit SHAs and tables look as they will on the page. Use `scripts/briefkit/shoot.py out/work.gh.html` to screenshot and split a tall page into readable slices; it passes `--virtual-time-budget=8000` so Mermaid from the CDN has time to render before capture. Post `out/work.md` verbatim.
- **Mermaid version drift:** `work.gh.html` loads Mermaid from the latest CDN build, which may support diagram types (e.g. `xychart-beta`) that GitHub's own renderer does not draw. Use only `flowchart`, `sequenceDiagram`, `gantt`, and `graph` in briefs bound for a GitHub comment. For any other diagram type, place a table carrying the same numbers beside the Mermaid block so the data survives if the diagram does not render.
- The thread is the record. Earlier comments in the same thread are the first precedent to read, and a link to one of them replaces restating it.
- **Reader-accessible citations.** When the reader sees only GitHub, every citation tag in their text names a GitHub record they can open: a file at a pushed commit, an issue, a pull request, or a comment. Identify a file by a commit permalink or an unambiguous repository, commit and path. Local-only work logs, `evidence/`, `.scratch`, `.local`, and unpushed branches or commits stay in the briefing's local record. Re-source a claim supported only locally to a pushed record that supports it, or drop the claim from the reader's text and retain it locally.
- **Before posting, audit `out/work.md`.** Verify every cited commit exists on the intended remote, using refreshed remote refs and a containment check (for example, `git branch -r --contains <sha>`) or GitHub's commit view. For a cited file, also check the exact path at that commit (`git cat-file -e <sha>:<path>`), and confirm the reader can open the record. `git cat-file -e` alone checks a local object, not whether it was pushed. Record the citation audit in the briefing README; posting waits until every citation meets this rule.
- The issue's own list of items (its parts, its acceptance tests, its asks) is the natural key for any status table.

## HTML report

- Medium: HTML, one self-contained file that opens from an attachment or a share.
- Screenshot at 1000 px wide. The summary fits the first screen; tables sort on header click and nothing overflows the right edge.

## PDF report

- Medium: PDF, for a reader who prints or files.
- Read every page as an image. The summary fits page one; no heading is stranded at a page foot; a split table repeats its header. Record the page count in the README.

## Word document

- Medium: docx, for a reader who edits or comments in Word.
- Open the file (or convert it to PDF) and look at every page; tracked changes from the reader come back as a new version of `brief.md`, never as edits to the docx.

## Chat post

- Medium: Markdown, cut to what the host renders. Discord and Telegram draw no tables: use one bullet per row. Slack's mrkdwn is not GitHub Markdown.
- Post a link to the full report rather than the report itself when the summary alone does not carry the decision.
