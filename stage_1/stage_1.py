codon_table = {
    'UUU': 'F', 'UUC': 'F',  # Phenylalanine
    'UUA': 'L', 'UUG': 'L',  # Leucine
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',  # Serine
    'UAU': 'Y', 'UAC': 'Y',  # Tyrosine
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',  # Stop codons
    'UGU': 'C', 'UGC': 'C',  # Cysteine
    'UGG': 'W',  # Tryptophan
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',  # Leucine
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # Proline
    'CAU': 'H', 'CAC': 'H',  # Histidine
    'CAA': 'Q', 'CAG': 'Q',  # Glutamine
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',  # Arginine
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',  # Isoleucine
    'AUG': 'M',  # Methionine (start codon)
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # Threonine
    'AAU': 'N', 'AAC': 'N',  # Asparagine
    'AAA': 'K', 'AAG': 'K',  # Lysine
    'AGU': 'S', 'AGC': 'S',  # Serine
    'AGA': 'R', 'AGG': 'R',  # Arginine
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',  # Valine
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # Alanine
    'GAU': 'D', 'GAC': 'D',  # Aspartic Acid
    'GAA': 'E', 'GAG': 'E',  # Glutamic Acid
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'   # Glycine
}


def translate_DNA_Protein(sequence: str):
    protein = []
    stop = False
    i = 0
    while (stop  == False):
        if sequence[i:i+3] in codon_table:
            protein.append(codon_table[sequence[i:i+3]])
            i += 3
        if codon_table[sequence[i:i+3]] == "Stop":
            stop = True
    return protein

mrna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGAUGG"
print(translate_DNA_Protein(mrna))