# Core verification with at most three mutual friends

[![Repository verification](https://github.com/DannyExperiments/subcubic-friend-oriented-core-verification/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/subcubic-friend-oriented-core-verification/actions/workflows/verify.yml) [![Verifier replay](https://github.com/DannyExperiments/subcubic-friend-oriented-core-verification/actions/workflows/replay.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/subcubic-friend-oriented-core-verification/actions/workflows/replay.yml) [![PDF build](https://github.com/DannyExperiments/subcubic-friend-oriented-core-verification/actions/workflows/pdf.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/subcubic-friend-oriented-core-verification/actions/workflows/pdf.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24564936.svg)](https://doi.org/10.5281/zenodo.24564936)

Can one efficiently verify core stability or strict core stability when everyone has at most three mutual friends? The original question appears in [Simola, dissertation, §5.5](https://doi.org/10.34726/hss.2026.138201).

**Result.** Both partition verification problems are coNP-complete for symmetric friend-oriented hedonic games without neutrals and with at most three mutual friends. With at most two they are polynomial-time decidable.

[Read the paper (PDF)](paper/manuscript.pdf) · [LaTeX source](paper/manuscript.tex) · [Proof guide](proof/PROBLEM_AND_PROOF.md) · [Reproduce the checks](REPRODUCIBILITY.md)

One cubic Vertex Cover reduction ensures all-strict blocking in yes instances and excludes every weak block in no instances.

Internally reviewed, not peer reviewed. [Mathematical audit](audits/public_safe_reports/MATHEMATICAL_AUDIT.md) · [Literature and priority](audits/public_safe_reports/LITERATURE_AUDIT.md) · [Citation](CITATION.cff)
