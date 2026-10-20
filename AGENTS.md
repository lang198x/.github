# Lang198x — org container

Read [PRINCIPLES.md](PRINCIPLES.md) first; MANIFESTO.md explains why and
PRACTICE.md explains the shared method. The
[umbrella ownership decision](https://github.com/stevehill1981/198x/blob/dd9bdfa0cf272fb87763c15afa45f6b35e0978e2/decisions/lang198x-language-tools.md)
binds sibling boundaries.

Lang198x owns language frontends, source analysis, release/extension profiles
and language services including LSP tools. The curriculum is a first consumer,
not the limit on correctness.

- `.github/`: org profile, foundation documents and this canonical context.
- `lang198x/`: flagship source/design repository; foundation stage, no parser yet.

Child folders are independent Git repos. Commit in the owning repo. Org-container
AGENTS.md points here; CLAUDE.md points to AGENTS.md. Cross-project decisions
belong in the umbrella, project-only choices in the flagship's decisions folder.

AMOS comes first, with versions and extensions explicit; Blitz follows. No
universal grammar, interpreter, compiler or migration is commissioned by the
foundation. Agree a bounded implementation design before adding parser code;
ask before dependencies or breaking APIs.

Keep source analysis, static checks and original execution distinct. Reuse
original-runtime evidence only for its exact source/profile/configuration.
Use public sources; never commit ROMs, runtime disks, tokenised programs, private
media locators or emulator snapshots. Published crate names carry `lang198x-`.

Format codecs remain with Format198x, media builds with Build198x, and canonical
assembly semantics with Asm198x. Review existing analysis for migration before
duplicating it; preserve callers and reference tests. Forge consumes language
services and remains deferred under its own decision.
