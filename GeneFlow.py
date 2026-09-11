codon = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "STOP",
    "UAG": "STOP", "UGU": "Cys", "UGC": "Cys", "UGA": "STOP",
    "UGG": "Trp",

    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",

    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",

    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}


# DNA input standardizer
with open("input_dna.txt","r") as file :
	dna = file.read().upper().strip().replace(" ", ""). replace ("\n", "")
#dna = input(" Enter your desired DNA sequence : ").upper().strip().replace(" ", "")
min_length = int(input (" The minimum ORF length should be : "))
bases = ["A", "T", "G", "C"]
valid = True

for base in dna:
    if base not in bases:  # Validation checking
        valid = False

if valid == True:
    print(" Entered sequence is a Valid DNA")

    # Sequence Analyzer
    length = (len(dna))
    adenine_count = (dna.count("A"))
    thymine_count = (dna.count("T"))
    guanine_count = (dna.count("G"))
    cytosine_count = (dna.count("C"))

    gc_per = (((guanine_count + cytosine_count) / (len(dna))) * 100)
    at_per = (((adenine_count + thymine_count) / (len(dna))) * 100)

    print(" The length of the sequence is :", length)
    print(" The number of Adenine bases in the sequence is :", adenine_count)
    print(" The number of Thymine bases in the sequence is :", thymine_count)
    print(" The number of Guanine bases in the sequence is :", guanine_count)
    print(" The number of Cytosine bases in the sequence is :", cytosine_count)
    print(f" AT Percentage is :{round(at_per, 2)}%")
    print(f" GC Percentage is :{round(gc_per,2)}%")

    # Multiple ORF Tracker

    starting_position = 0
    orf_number = 0
    orf_found = False
    no_orf_exists = False

    for start_codon in dna:
        start = dna.find("ATG", starting_position)

        if start == -1:

            if orf_found == False and no_orf_exists == False:
                print("No ORF exists")
            break

        else:
            stop_found = False
            stop_codon = ["TAA", "TAG", "TGA"]
            orf = ""

            for s in range(start, length, 3):
                stop = dna[s:s + 3]

                if len(stop) != 3:
                    break

                if stop not in stop_codon:
                    orf = orf + stop

                else:
                    orf = orf + stop
                    stop_found = True
                    orf_length = len(orf)
                    orf_end = s + 3
                    
                    if orf_length < min_length :
                    	starting_position = s + 3
                    	stop_found = False
                    	break
                    orf_number = orf_number + 1
                    starting_position = s + 3
                    break

            # Transcription and Translation

            if stop_found == True:
                orf_found = True

                print(f" ∆ This is ORF No. : {orf_number}")
                print(f" The ORF sequence is : {orf}")
                print(f" ORF Starts from : {start + 1}")
                print(f" ORF Ends at : {orf_end}")
                print(" Length of the ORF is :", orf_length)

                mRna = orf.replace("T", "U")
                print(f" The transcribed mRNA sequence is : {mRna} ")

                length_mRna = len(mRna)

                amino_list = []

                for m in range(0, length_mRna, 3):
                    codon_now = mRna[m:m + 3]
                    amino_acids = (codon.get(codon_now))

                    if amino_acids == "STOP":
                        break
                    
                    amino_list.append(amino_acids) 
                    protein = "-".join(amino_list)

                print(f" The translated amino acid chain is : {protein}")

            else:
                starting_position = start + 3

else:
    print(" Entered sequence is an Invalid DNA")
