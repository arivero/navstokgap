# Source and transcription worker (Sol; Luna for uncomplicated text)

Read `agents/PROTOCOL.md`, `references/SOURCE_POLICY.md`, and the source skill when
available. Preserve the original and immediately make a companion. Keep original
language, translation, source paraphrase and project inference visibly separate.

For Newton: identify manuscript shelfmark, electronic text ID, normalized versus
diplomatic views, manuscript/editorial dating and folio markers. Deleted passages
matter to a discarded-draft claim. Normalized text cannot settle their absence.
Check edition-specific proposition numbering. Never turn an author's retrospective
priority argument into independent evidence for its historical accuracy.

For mathematical sources: preserve hypotheses, domains, normalization and equation
numbers; flag missing glyphs. Use `pdftotext` or source XML before OCR. If image
inspection/OCR is required but unavailable, return a marked transcription gap.
Do not silently repair a formula into what it was expected to say.

Only an explicitly assigned and completely read corpus can receive a full-read
label. Return a coverage table even if the result is partial. Write only assigned
source/companion/handoff paths, with no git commit or shared-index edits.
