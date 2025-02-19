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
            if codon_table[sequence[i:i+3]] == "Stop":
                stop = True
        elif i> len(sequence):
            stop = True
        i += 3
    return protein

mrna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGAUGG"
print(translate_DNA_Protein(mrna))

from numpy import random
import numpy as np
import pandas as pd

x = 100

y = random.randint(0,x)
z = random.randint(0,x)

lag = min(y,z)
exp = max(y,z)


def logistic_growth(starting_pop: int, carrying_cap: int, growth_rate: float):

    x = 100
    y = random.randint(0,x)
    z = random.randint(0,x)
    lag = min(y,z)
    exp = max(y,z)
    # Generate time points
    t = np.linspace(0, exp, 100)

    # Compute population values
    P = np.piecewise(t, [t < lag, t >= lag],
                    [starting_pop, lambda t: starting_pop * np.exp(growth_rate * (t - lag))])

    # Convert to a list
    population_list = P.tolist()
    return population_list



def data_frame(starting_pop: int, carrying_cap: int, growth_rate: float):
    df = pd.DataFrame()
    for i in range(100):
        population = logistic_growth(starting_pop,  carrying_cap, growth_rate)
        df[f"Column_{i}"] = population
    return df

print(data_frame(100, 1000, 0.1))