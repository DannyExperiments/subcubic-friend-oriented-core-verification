# Core verification with at most three mutual friends

Can one efficiently verify core stability or strict core stability when everyone has at most three mutual friends? The original question appears in [Simola, dissertation, §5.5](https://doi.org/10.34726/hss.2026.138201).

**Result.** Both partition verification problems are coNP-complete for symmetric friend-oriented hedonic games without neutrals and with at most three mutual friends. With at most two they are polynomial-time decidable.

[Read the paper (PDF)](paper/manuscript.pdf) · [Proof guide](proof/PROBLEM_AND_PROOF.md) · [Reproduce the checks](REPRODUCIBILITY.md)

One cubic Vertex Cover reduction ensures all-strict blocking in yes instances and excludes every weak block in no instances.

Internally reviewed, not peer reviewed. [Mathematical audit](audits/public_safe_reports/MATHEMATICAL_AUDIT.md) · [Literature and priority](audits/public_safe_reports/LITERATURE_AUDIT.md) · [Citation](CITATION.cff)
