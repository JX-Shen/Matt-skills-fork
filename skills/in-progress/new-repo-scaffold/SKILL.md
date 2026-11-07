---
name: new-repo-scaffold
description: Scaffold a brand-new ZentosaLabs repo end-to-end — point gh at the company account, configure engineering-skill docs, stamp the Working Philosophy header, run a real charter-grilling interview, then git init and push to GitHub. User-invoked — run once per new repo, right after creating its folder.
disable-model-invocation: true
argument-hint: "repo name, and a one-line description of what the project actually is"
---

# New Repo Scaffold

Standing personal convention for standing up a new ZentosaLabs project repo with shared vocabulary and decision-record discipline from day one. Confirmed in DataLake, private-ETF, and AgenticFutureQuant.

Run the five steps below **in order**, in the current directory. Steps 4 and 5 are the point of this skill, not optional cleanup after steps 1–3 — don't stop early unless the user explicitly says to defer a step.

## 0. Explore first

Don't assume a clean slate:

- `git status` / `git log` if `.git` already exists — never re-init over history.
- Check whether `AGENTS.md`, `docs/agents/`, `CHARTER.md`, `GLOSSARY.md` already exist. If this repo is partway through the pattern, resume from the first missing piece instead of redoing finished steps.

## 1. Point `gh` at the company account

Add to `.claude/settings.local.json` (create the file, or its `permissions` block, if absent — mirror an existing project such as DataLake or private-ETF for the exact shape):

```json
"env": { "GH_CONFIG_DIR": "$HOME/.config/gh-company" }
```

Every ZentosaLabs repo lives under `~/ZentosaLabs/`, and `~/ZentosaLabs/.envrc` already points the real terminal's `gh` at the company account (`Jason-Shen-Zen`) for anything under that directory via direnv's normal parent-directory lookup — no per-repo `.envrc` needed, and don't add one. But Claude Code's own settings don't inherit from a parent directory the way direnv does, so each repo's `.claude/settings.local.json` needs this `env` block for Claude Code itself (this skill's own session included) to use the company account rather than whatever `gh`'s global active account happens to be.

No plugin flag is needed: the JFork skill suite (the personal fork at `~/.claude/jfork`) is available globally via symlinks in `~/.claude/skills/`, not enabled per repo.

Done when: `settings.local.json` carries the `env` block.

## 2. Run `/setup-matt-pocock-skills`

Let it explore the repo and ask its own questions (issue tracker, domain-doc layout). Default to GitHub issues via `gh` and single-context domain docs unless the repo's shape clearly says otherwise.

Done when: `AGENTS.md`'s `## Agent skills` block plus `docs/agents/issue-tracker.md` and `docs/agents/domain.md` exist.

## 3. Stamp the Working Philosophy header

Prepend this fixed text to the very top of `AGENTS.md`, above `## Agent skills`. Verbatim, do not paraphrase.

```markdown
## Working Philosophy: Reduce entropy

Optimize for long-term coherence with minimal machinery.

Work from evidence, not assumption.
Keep state aligned with reality.
Make decisions explicit, not ceremonial.
Prefer compactness: fewer concepts, fewer states, fewer moving parts, fewer open loops.
Make every addition earn its entropy.
Prefer extra information over stacking context.
Keep rigor proportionate; excess constraint is abdication.
Name the threat each gate stops; remove the gate that cannot.
Give every refusal its reason and path forward.
Describe the desired state and the action.
Reserve prohibitions for hard boundaries.
Flag issues, inherited ones included.
Respect coherence, not precedent.
Before changing assumptions, rules, or structure: revisit the charter, name the alternative, record the rationale.
When authorities contradict, VERIFY WITH HUMAN.

Align.
Reproduce.
Slice.
Verify.
Record only what must survive.
```

Done when: `AGENTS.md` opens with this header before anything else.

## 4. Run `/grill-with-docs`

This is a real interview, not boilerplate. Genuinely interrogate the user about what the project actually is — round by round, per that skill's own discipline — until `CHARTER.md`, `GLOSSARY.md`, and at least one `docs/adr/000N-*.md` reflect the real concept rather than a template. Steps 1–3 feeling like "the setup" is not a reason to shortcut this.

Done when: `CHARTER.md`, `GLOSSARY.md`, and a first ADR exist, and the user has confirmed they capture the actual project.

## 5. Git init and push

```bash
git init
git add -A
git commit -m "Initial project scaffolding: <one-line summary>"
GH_CONFIG_DIR="$HOME/.config/gh-company" gh repo create Zentosa-Labs/<repo-name> --private --source=. --remote=origin --push
```

One commit bundling all the scaffolding and charter docs together. Default target is the `Zentosa-Labs` GitHub org, private visibility — only ask if the user has said otherwise for this repo.

The `gh repo create` call needs the `GH_CONFIG_DIR` prefix explicitly, even though step 1 already wrote it into `settings.local.json`: a settings change doesn't retroactively apply to Bash calls already running in *this* scaffold session, only to sessions started after it.

Done when: `gh repo view Zentosa-Labs/<repo-name>` succeeds and `git log` shows the pushed commit tracking `origin/main`.
