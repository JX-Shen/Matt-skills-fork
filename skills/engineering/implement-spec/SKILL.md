---
name: implement-spec
description: "Implement the result of /to-spec and /to-tickets in code."
disable-model-invocation: true
---

You have been provided a spec. This spec should have tickets associated with it, describing how to implement the spec.

The issue tracker should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

The goal is the entire spec implemented on a single **integration branch**, with every ticket resolved the way the issue tracker closes work.

The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.

Start every subagent with a fresh context window.

Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the spec, tickets, research notes, and previous commits. Don't duplicate information already available via pointers.

**Implementer subagents** should be run in the background where possible for maximum concurrency.

Where the repo has its own git conventions (in `CLAUDE.md`, `AGENTS.md` or local instructions) for branches, merges, PRs or worktree locations, follow them; they take precedence over the git mechanics below.

## Steps

1. Read the spec and tickets to understand the task graph.

2. (optional) Use an **exploration subagent** to conduct any exploration required by the tickets - relevant codebase files or external documentation. Ensure the exploration subagent can save files - it should save its markdown notes in a directory outside the repo, accessible by all future subagents. This lets **implementer subagents** focus on implementation rather than exploration.

3. Create the integration branch. If the issue tracker closes work through PRs, or the user asks for one, open a draft PR after the first merge in step 5 (a branch with no commits ahead of main can't open one), marked as closing the spec and tickets.

4. Use a fresh **implementer subagent** for each ticket, each in its own worktree on its own branch. Each implementer subagent:
   - confirms its worktree is based on the integration branch before starting, and resets onto it if not;
   - calls the Skill tool with `tdd` to build the ticket;
   - merges the integration branch tip into its own branch before reporting done

5. Once an **implementer subagent** completes, merge its work to the integration branch with a **merger subagent**, then reclaim that implementer's worktree (see **Reclaiming worktrees**). Reclaim as each ticket lands, not at the end: every worktree is a full checkout, and a large graph left standing can fill the disk mid-run.

6. If this changes the **frontier** of available tickets, kick off more **implementer subagents** to work on the new tickets. This allows for maximum concurrency.

7. Once all tickets are complete, call the Skill tool with `code-review` on the integration branch. Fix all issues raised by the code review in a single fresh **implementer subagent**.

8. If a draft PR exists, mark it ready for review. Otherwise, resolve each ticket the way the issue tracker closes work, and report the integration branch.

9. Reclaim every **implementer subagent** worktree still standing. Reclaim the integration branch's own worktree once nothing still needs it, typically after its PR merges.

## Reclaiming worktrees

A worktree is reclaimable when all three hold:

- `git -C <worktree> status --porcelain` prints nothing;
- its branch is fully merged: `git merge-base --is-ancestor <branch> <integration-branch>` succeeds;
- no process is running inside it.

Remove it with `git worktree remove <worktree>`, then run `git worktree prune`. Keep the branch: it is the record, and the worktree can be recreated from it.

`git worktree remove` also deletes gitignored files. Dependency installs and caches can go. If the worktree holds anything else ignored (run outputs, evidence, notes), stop and ask before removing it.

A worktree whose branch is ahead of the integration branch holds unfinished work. Leave it.
