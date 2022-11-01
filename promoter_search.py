# a function that outputs the core promoter sequences, and returns the positions of the TSSs, from a given sequence file
def promoters(sequence):
    # open DNA sequence text file
    filecontent3 = open(sequence, "r")

    # read content of DNA sequence text file & close the file
    seq = filecontent3.read().strip()
    filecontent3.close()
    
    # find the length of the sequence
    seq_len = len(seq)
    
    
    # determine the TATAA motif 
    TATA_motif = "TATAA"
    # determine possible YR motifs
    YR_motifs = ["CA", "CG", "TA", "TG"]
    # storage for the TSS indexes (2nd character of YR motif)
    TSS_indexes = []
    # storage for TATAA indexes (1st character of the TATAA)
    TATA_index = []

    # FINDING THE TATAA's and their TSSs
    # iterates through sequence to look for TATAA motifs (-4 so search does not go out of range)
    for i in range(seq_len-4):
        # stores characters 5 consecutive characters
        tata_search = seq[i:i+5]
        
        # compares the 5 stored characters to the TATAA motif & records index of first 
        # character if the five characters are the TATAA motif
        if tata_search == TATA_motif: 
            
            # for a found TATAA motif this loop will check characters 24 to 31 (both included) nucleotides away from it
            # to see if they are a YR motif
            for j in range(24,32):
                
                # make sure the calculated index is not out of range (not larger than the sequence)
                if (i+j) < seq_len:
                    # the second character of the YR motif is what should be 24 to 31 nucleotides from the START of the TATAA
                    YR_search = seq[i+j-1] + seq[i+j]
                    
                    # checks if the two characters YR motif
                    if YR_search in YR_motifs:
                        # if so, index of 1st character of TATAA stored
                        TATA_index.append(i)
                        # index of 2nd character of the YR motif is stored
                        TSS_indexes.append(i+j)
                        # so only the position of TATAA motifs with correctly spaced YR will be recorded
    
    # FINDING THE CORE PROMOTER SEQUENCE
    # storing the core promoter sequences
    promoter = ""

    print("The core promoter sequences:")
    # iterate throught each of the previously found TSS indexes
    # k will equal the index of the TSS (2nd character of the YR motif)
    for k in TSS_indexes:
    
        # to give position of first nucleotide in the 100bp sequence -> it should be 50 nucleotides before the TSS
        promo_start = k-50
    
        # to give the position of the nucleotide after the last nucleotide in the 100bp sequence 
        promo_end = k + 50
    
        # checking that the TSS has 50 bases before it and 49 bases after it / within the range of the sequence
        # (checking the calculated bounds are not more than the len of the sequence or under 0)
        if (promo_start > 0) and ((promo_end-1) < seq_len):
        
            # adds the first 50 bases of the core promoter (the 50 bases up to the TSS & not including it)
            promoter += seq[promo_start:k]
        
            # the space before the TSS
            promoter += " "
        
            # adds the next 50 bases of core promoter, from the TSS to the next 49 nucleotides
            promoter += seq[k:promo_end]
            print(promoter)
            promoter = ""
      
    return "The positions of the TSSs", TSS_indexes

# calls the function
# the sequence file is provided as an argument for the promoters function
promoters("seq2.txt")
