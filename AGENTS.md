# Lang198x — org container

Read [PRINCIPLES.md](PRINCIPLES.md) first; MANIFESTO.md explains why and
PRACTICE.md explains the shared method. The
[umbrella ownership decision](https://github.com/stevehill1981/198x/blob/dd9bdfa0cf272fb87763c15afa45f6b35e0978e2/decisions/lang198x-language-tools.md)
binds sibling boundaries.

Lang198x owns language frontends, source analysis, release/extension profiles
and language services including LSP tools. The curriculum is a first consumer,
not the limit on correctness.

- `.github/`: org profile, foundation documents and this canonical context.
- `lang198x/`: cross-language coordination/research hub; retained foundation records.
- `amos/`: AMOS frontend, current corpus and reusable highlighting packages.
- `syntax/`: `lang198x-syntax`, the shared lossless tree every front end builds on.

Keep implementation files small; AMOS uses one supported instruction per Rust
module. Each language owns its grammar, AST and meaning; front ends share only
the building blocks in `syntax/`, under the
[shared syntax layer decision](https://github.com/lang198x/lang198x/blob/main/decisions/shared-syntax-layer.md).
Dialects that share a parser form a family with one repository.

Child folders are independent Git repos. Commit in the owning repo. Org-container
AGENTS.md points here; CLAUDE.md points to AGENTS.md. Cross-project decisions
belong in the umbrella, project-only choices in the flagship's decisions folder.

AMOS comes first, with versions and extensions explicit; Blitz follows. The first kit
implements only the documented opening-program surface. No universal grammar,
interpreter, compiler or migration is commissioned. Agree a bounded design
before adding new parser behaviour;
ask before dependencies or breaking APIs.

Keep source analysis, static checks and original execution distinct. Reuse
original-runtime evidence only for its exact source/profile/configuration.
Use public sources; never commit ROMs, runtime disks, tokenised programs, private
media locators or emulator snapshots. Published crate names carry `lang198x-`.

Format codecs remain with Format198x, media builds with Build198x, and canonical
assembly semantics with Asm198x. Review existing analysis for migration before
duplicating it; preserve callers and reference tests. Forge consumes language
services and remains deferred under its own decision.
