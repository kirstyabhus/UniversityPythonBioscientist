# UniversityPythonBioscientist
Work completed during the python for Bioscientists module.

## Background information for the projects
### Promoter Search
<p align="justify"> A fundamental first step in gene expression is the recognition of the promoter which initiates transcription by an RNA polymerase. Protein-coding genes in eukaryotic cells are transcribed by RNA polymerase II (pol II). Transcription is initiated at a site called the Transcriptional Start Site (TSS), which is located in the middle of the ~100 base pair (bp) long core promoter. The core promoter contains a number of sequence motifs which various proteins bind to, assembling the pre-initiation complex. This includes pol II and allows transcription to start. In one class of promoter, the TATA-box motif is located 24 to 31 bp upstream of the TSS. The TATA-box binding protein (TBP) recognises the sequence motif TATAA. This type of promoter also contains the Inr motif to mark the TSS. This motif includes CA, where the A is the TSS.
However, there are a number of alternative sequences for the Inr motif. One of these is 'YR' where Y is the ambiguity code for either a C or a T, and R is the ambiguity code for either an A or a G. </p> 

The function created in the Promoter Search will search for promoters in a sequence file. It will:
- identify core promoters which contain a TATA-box and Inr motif with the appropriate spacing
- take one argument: the name of the sequence file
- return one variable: the list of potential TSSs
- display (print) the 100 nucleotide core promoter region with a space before the TSS
- be entirely self-contained, so that the function only uses the argument provided and doesn't rely on any other existing variables


### Synthetic Promoter Generator
<p align="justify"> Most of our understanding of how promoter sequences regulate transcription have come from studying existing promoters across a range of species. Another approach is to generate synthetic promoter sequences with different combinations of the known motifs and study how effective they are. With current technologies, libraries of tens of thousands of DNA sequences can be synthesized and screened using functional assays. </p>

The function created in Synthetic Promoter Generator will generate promoter sequences with the following properties:
- sequences 500 nucleotides in length
- sequences contain a core promoter consisting of a TATA-box and Inr motif with the appropriate spacing
- the TSS will be positioned at nucleotide 450
- the first four nucleotides of all sequences will be AGGT and the last four nucleotides will be CGAA. This is to allow for cloning the sequences using Golden Gate assembly.
- The region between nucleotides 50 and 400 will contain a random selection of between 1 and 6 PDX1, MAFA and/or SP1 binding sites
- all other nucleotides in the sequence will be a random selection of the four nucleotides (A, C, G and T) selected with equal probability
- the positioning of the transcription factor binding sites and the TATA-box will be random within the constraints described above. ie. the TATA-box will be located between 24 and 31 nucleotides upstream of the TSS but this precise position will vary randomly within these constraints rather than being fixed in all sequences.
- The program will generate 100 sequences and write them to a file named promoters.txt
