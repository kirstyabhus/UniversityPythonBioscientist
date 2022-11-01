# UniversityPythonBioscientist
Work completed during the python for Bioscientists module.

## Background information for the projects
### Promoter Search
A fundamental first step in gene expression is the recognition of the promoter which initiates transcription by an RNA polymerase. Protein-coding genes in eukaryotic cells are transcribed by RNA polymerase II (pol II). Transcription is initiated at a site called the Transcriptional Start Site (TSS), which is located in the middle of the ~100 base pair (bp) long core promoter. The core promoter contains a number of sequence motifs which various proteins bind to, assembling the pre-initiation complex. This includes pol II and allows transcription to start. In one class of promoter, the TATA-box motif is located 24 to 31 bp upstream of the TSS. The TATA-box binding protein (TBP) recognises the sequence motif TATAA. This type of promoter also contains the Inr motif to mark the TSS. This motif includes CA, where the A is the TSS.
However, there are a number of alternative sequences for the Inr motif. One of these is 'YR' where Y is the ambiguity code for either a C or a T, and R is the ambiguity code for either an A or a G 

The function created in the Promoter Search will search for promoters in a sequence file. It will:
- identify core promoters which contain a TATA-box and Inr motif with the appropriate spacing
- take one argument: the name of the sequence file
- return one variable: the list of potential TSSs
- display (print) the 100 nucleotide core promoter region with a space before the TSS
- be entirely self-contained, so that the function only uses the argument provided and doesn't rely on any other existing variables
