# NATP00385 TEI/XML source companion

> Work: *Unarranged fragments, mostly relating to the dispute with Leibniz*
>
> Author/catalogue attribution: Isaac Newton
>
> Manuscript: Cambridge University Library, Portsmouth Collection,
> MS Add. 3968, ff. 594r-619v
>
> Newton Project text ID: NATP00385
>
> Electronic editor: Robert Ralley (2019-2020 revision history)
>
> XML publication statement: Newton Project, University of Oxford, 2020
>
> Source URL: <https://www.newtonproject.ox.ac.uk/view/texts/xml/NATP00385>
>
> Schema URL: <https://www.newtonproject.ox.ac.uk/resources/misc/np-schema.zip>
>
> Retrieved: 2026-09-05
>
> Local original: `docs/Newton_NATP00385.xml`
>
> SHA-256: `4605d27b1853898010d771387c4267573916ac50014011f971d7f07fb7cdfd37`

## Format and validation

The file is UTF-8 TEI XML with embedded MathML and Newton Project extensions.
Python's standard `xml.etree.ElementTree.parse` accepted it as well-formed on
2026-09-05. No schema validation was performed.

Mechanical counts in the downloaded XML found 7,123 `<del>` elements and 4,904
addition-like starts (4,886 `<add>` plus 18 `<addSpan>`), agreeing with the view's
reported deletion/addition totals. The XML has 285 page-break elements, 1,100
paragraph IDs, and 7,437 line-break IDs. The rendered HTML shows 195 standalone
page-number spans; other page breaks can occur inside paragraphs. A paragraph's
opening page label is therefore not always its complete leaf coverage.

The XML header reports approximately 113,053 words and “16 ff.” while identifying
the source as ff. 594r-619v. The transcription itself has numerous internal labels
from `<1r>` through `<158v>`, with gaps and repeats. This companion does not infer
a mapping between those internal labels and the CUL foliation.

## Rights and source status

The TEI `<availability>` element marks the text “restricted” and links CC
BY-NC-ND 3.0. The XML is stored for noncommercial source verification; no claim
is made that the transcription or a transformed full text may be redistributed.

- Retrieval: official XML endpoint downloaded successfully.
- Validation: well-formedness checked; schema not checked.
- Extraction: XML is the authority for deletion/addition status and line IDs.
- Reading: only the header and selected audit passages were inspected.
- Facsimile: the XML contains facsimile references, but image witnesses were not
  downloaded or visually checked in H01.
