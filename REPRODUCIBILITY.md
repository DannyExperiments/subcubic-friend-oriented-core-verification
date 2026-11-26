# Reproducibility

Run these commands from the candidate root with Python 3.11 or later. The workflows select Python 3.11.

| Check | Command | Evidence |
| --- | --- | --- |
| Inventory and integrity | `python3 -I scripts/verify_repository.py` | Manifest and SHA-256 ledger match the candidate tree. Known private markers are checked in text files. |
| Verification replay | `python3 verification/src/replay.py` | Review the output against `verification/logs/replay.txt` and the scope described in the manuscript. |
| Manuscript PDF | Follow `paper/BUILD.md`. | Rebuild from the TeX and bibliography and inspect the output. |

The replay checks the cases stated in its source and report. Those finite checks corroborate the manuscript. The proof is in the manuscript and proof note. The PDF recorded in the SHA-256 ledger is the distributed artifact. PDF metadata and toolchain versions can affect byte-for-byte rebuilds.
