# Custom research skills consolidated

The custom skill set now has two distinct responsibilities:

- `principia-action` owns research routing and source-context recovery. The
  separate `navstokgap-bibliography` skill was merged into it and removed,
  including its installation symlink. AGENTS.md now points to the merged
  source-recovery section. Historical handoffs retain their original inputs.
- The installed `physics-source-downloads` skill retains original retrieval
  and Markdown companions. It now follows the active workspace's source policy,
  removes hard-coded kkorchestra indexes, permits document/source Python under
  navstokgap's actual rule, checks downloaded file identity, and tries lawful
  alternatives inside the existing budget without a routine permission gate.

The download skill is user-local, outside this Git repository. Its original
folder is backed up at
`/home/codexssh/.codex/skill-backups/2026-09-13-navstokgap-cleanup/physics-source-downloads/`.
System and plugin-managed skills were left intact. No memory files were edited.

Both retained skills pass skill-creator's quick_validate.py. Repository
`make check` passes 1472 local links, source companions, citations and hashes;
`git diff --check` passes. Written routing review covers context recovery,
explicit historical tasks, gap/action normalization, and failed source access.
No manuscript changed, so paper rebuilds and a mathematical librarian audit
were unnecessary. Research priorities were unchanged by this tooling cleanup.
