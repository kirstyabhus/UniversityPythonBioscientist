import random

# while the function generates the sequence nucleotide by nucleotide, the program will use the length of the 
# current generated sequence to determine whether the next position of the seq, at the current length, is 
# a position for one of the required promoter properties.
# e.g. if the seq length = 449, the index of the LAST nucleotide in the seq is 448. Therefore, adding the YR motif
# to this seq will put the Inr at index 450.

# function to create promoter sequences with length of 500bp & promoter properties
def create_promoter():

    # empty promoter sequence starting with required 4 nucleotides
    promoter = "AGGT"
    
    # Transcription factors and their corresponding binding sequences
    tfbs = {
        "PSX1": "TCTAAT",
        "MAFA": "TGCA",
        "SP1": "CCGCCC"
           }

    # all possible nucleotides
    nucleotide = ["A", "T", "C", "G"]
    
    # last 4 nucleotides for all promoters
    end_seq = "CGAA" 
    
    # TATA motif sequence
    TATA_motif = "TATAA"
    
    # all possible combinations for a YR Inr motif
    Inr_motif = ["CA", "CG", "TA", "TG"]
    
    # generates a random position for the TATA motif, 24-31 (both included) upstream of the TSS,
    # by generating the length the sequence will be before the TFBS sequence is added to promoter sequence
    TATA_distance = 450 - random.randint(24,31)
    
    # generates random number of transcription factor binding sites that will be incorporated into seq
    tfbs_count = random.randint(1,6)
    
    # dictionary that will later contain the random position(s) of the TFBS and its sequence 
    # key = position, value = Transcription factor binding site
    tfbs_choices = {}
    
    # stores the first randomly generated postion of the first binding site sequence
    # 394 max generated position will be the max position to put a BS sequence so that
    # the added TFBS does not end out of the 400 range/index
    pos = random.randint(50, 394)
    
    # stores the first randomly generated position for TFBS as a key for a randomly generated TFBS
    tfbs_choices[pos] = random.choice(list(tfbs.values()))


    # for loop will fill dictionary with randomly generated positions and their random TFBS
    # minus 1, because we've already generated one position + TFBS before (lines 46 & 49).
    # for loop iterates a number of times depending on the chosen number of TFBS
    for j in range(tfbs_count - 1):
        
        # generates a provisional position for the next binding site
        pos = random.randint(50, 394)
        
        # loop to ensure the newly generated position is not within 6 bases before or after any of the
        # previously generated positions.  (to ensure no overlapping)
        for k in tfbs_choices.keys():
            # checks every position already in key to see if the new position is within its bounds or at the same position
            
            # if overlapping, a new position will be generated until it is not within the bounds of any positons already stored
            while ((pos > k - 6 ) and (pos < k + 6)) or (pos == k):
                pos = random.randint(50, 394)
        
        # postion stored as key with the TFBS as value
        tfbs_choices[pos] = random.choice(list(tfbs.values()))
              
    
    # this will loop until the last index filled is 495
    # we only want this loop to go on until this index is filled, so that index 496,497,498,499 (the final 4 indexes) 
    # will be our required end sequence of "CGAA"
    while len(promoter) < 497:
                
        # if the length of the promoter is at one of the randomly generated positions for the TFBS sites
        # add the site for this position into the sequence
        if len(promoter) in tfbs_choices:
            promoter += tfbs_choices[len(promoter)]
            
        # if the length is at the randomly generated distance for the TATA motif, add the TATA motif to the sequence
        if len(promoter) == TATA_distance:
            promoter += TATA_motif

        elif len(promoter) == 449:
            # when the len is 449, the last index of the generated promoter seq is 448.
            # positions 449 and 450 will now be the two characters of the YR motif
            promoter += random.choice(Inr_motif)
            
        elif len(promoter) == 496:
            # when there's 4 more bases left till the end of the 500bp sequence, use the required 4 base sequence.
            promoter += end_seq
            
        else:
            # if the length of the sequence is not one of the important lengths required for
            # the promoter properties, a random nucleotide will be added to the promoter sequence
            promoter += random.choice(nucleotide)
    
    # return the randomly generated promoter sequence
    return promoter


# open the file for writing, overwriting any existing content. Will create a new file if it does not exist.
filecontent = open("promoters.txt", "w")        
        
# generates 100 random promoter sequences, and writes them in the file. Each sequence is separated by a new line
for r in range(100):
    filecontent.write(create_promoter())
    filecontent.write("\n")

# closes file
filecontent.close()
