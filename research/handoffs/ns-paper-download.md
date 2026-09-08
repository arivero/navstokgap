# NS paper download handoff

Task: retrieve and catalogue the official OpenAI *Finite time blowup for Navier–Stokes* PDF.
Role: bounded librarian retrieval. Requested model/effort: Luna, low. Date: 2026-09-08.

## Inputs and outputs

- Official route: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
- Existing local original verified and reused: `.build/openai-ns/navier-stokes.pdf`.
- Layout extraction: `.build/openai-ns/navier-stokes.layout.txt` (created with `pdftotext -layout`).
- Companion updated: `docs/OpenAI_NavierStokes_2026.md`.
- Original remains in ignored cache because redistribution rights are unestablished.

## Verification and coverage

`pdfinfo` reports 165 pages and 2,955,931 bytes; the PDF is unencrypted and complete.
SHA-256: `8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81`.
The extraction is full-document layout text (673,086 bytes; 8,652 lines). Reading
coverage is limited to PDF pages 1–2: title, abstract, contents, Theorem 1.1 and
the opening historical/physical-description paragraphs. No proof or formula
visual audit was performed.

## Source-to-task suggestion

For the Millennium comparison, use the paper's explicit separation between bounded
global kinetic energy and unbounded local velocity as a diagnostic: any transferred
gap/coercivity claim must name the observable and identify the missing uniform local
estimate. This is a source-grounded suggestion, not an accepted new claim.

## Next bounded task

Coordinator review of the metadata and first-reading anchors; a separate proof/formalization
audit is required before treating the theorem or construction as independently established.

Coordinator verification: recomputed the PDF hash, reviewed the companion and
handoff, and passed repository checks (575 local Markdown links). No fresh
download was needed; the official cached copy matched the earlier retrieval.
