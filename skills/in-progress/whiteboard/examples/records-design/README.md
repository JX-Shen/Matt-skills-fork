# Example: records tool, one mechanism, two postures

The first diagram made this way, 2026-10-28, for the AgentOS code-boundary refactor after a second repository (OliviaMIDI) joined the design and the user's model stopped keeping up.

- Thesis (title): 「工作记录工具：一个机制，两种姿态」.
- Left panel, the invariant: users → the CLI as the single write entry → `main` and `records` lanes in one `.git` → the single `.records/` checkout every worktree shares.
- Right panel, the variables: eight dimensions × one column per repository.
- Callout: the ten fields the tool knows. Footer: the splitting rule and the open naming question.
- Every figure on it (zero mixed commits, the ten core fields) came from the refactor record; nothing was added.

The first render had three defects, fixed in the second: body text overflowing a box, a many-to-one arrow drawn across a box (now a bus), and a footer line running past the canvas.

Source record: `docs/Refactor/20261028-01-code-boundary-restructure.md` in AgentOS (private). The two files here are a verbatim copy of what was served, on the single-screen path. [`../records-design-page/`](../records-design-page/) is the same content rebuilt on the page path and kept as its skeleton: the mechanism panel verbatim as inline SVG, the table, callout, and footer as HTML with the same text.
