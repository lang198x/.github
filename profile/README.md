# Lang198x

Language tools for understanding and working with vintage programming languages.
We are starting with AMOS: its source syntax, releases and extensions. Blitz
follows, with other languages considered through the same evidence-led process.

The scope includes parsers, analysis, diagnostics and language services, including
LSP tools for editors. Interpreters and compilers are possible later capabilities.

**The first [AMOS language kit](https://github.com/lang198x/amos) is available.**
It provides a small Rust parser/checker and reusable TextMate highlighting for
Shiki and VS Code. Coverage is deliberately bounded and explicit; native-file
output, LSP and compilation remain future work. The
[hub](https://github.com/lang198x/lang198x) holds cross-language research and
coordination. Each language family has its own repository and AST, built on
a [shared lossless syntax tree](https://github.com/lang198x/syntax).

**Assembly is moving here too.** The [Z80 family](https://github.com/lang198x/z80-asm)
has started: one parser for Z80 assemblers that share a structure, with a
profile per dialect, beginning with PasmoNext. It feeds the
[Asm198x](https://github.com/asm198x) assembler, and a dialect counts as
supported once the result matches the real assembler byte for byte.

## Work with us

Useful contributions include release notes, small reproducible language cases,
extension documentation and comparisons with named original versions. Separate
what a manual says from what an original runtime accepts or executes.

## The 198x family

Lang198x is a peer of [Code198x](https://github.com/code198x) (curriculum),
[Asm198x](https://github.com/asm198x) (assembly tooling),
[Build198x](https://github.com/build198x) (asset/media builds),
[Format198x](https://github.com/format198x) (historical formats), and
[Emu198x](https://github.com/emu198x) (machine emulation). The future Forge198x
workbench can consume language services alongside other editors.

We share [our purpose](https://github.com/lang198x/.github/blob/main/MANIFESTO.md),
[principles](https://github.com/lang198x/.github/blob/main/PRINCIPLES.md) and
[practice](https://github.com/lang198x/.github/blob/main/PRACTICE.md).
