# This converts a sequence of genetic DNA or RNA bases into their complimentary counterparts.
# It can also output the chain of amino acids to match if wanted. It's mainly just for my Biology class though.

amino_acids = {"GUU":"Valine","GUC":"Valine","GUA":"Valine","GUG":"Valine",
				"GCU":"Alanine","GCC":"Alanine","GCA":"Alanine","GCG":"Alanine",
				"GAU":"Aspartic Acid","GAC":"Aspartic Acid",
				"GAA":"Glutamic Acid","GAG":"Glutamic Acid",
				"GGU":"Glycine","GGC":"Glycine","GGA":"Glycine","GGG":"Glycine",
				"UUU":"Phenylalanine","UUC":"Phenylalanine",
				"UUA":"Leucine","UUG":"Leucine",
				"UCU":"Serine","UCC":"Serine","UCA":"Serine","UCG":"Serine",
				"UAU":"Tyrosine","UAC":"Tyrosine",
				"UAA":"STOP","UAG":"STOP",
				"UGU":"Cysteine","UGC":"Cysteine",
				"UGA":"STOP",
				"UGG":"Tryptophan",
				"CUU":"Leucine","CUC":"Leucine","CUA":"Leucine","CUG":"Leucine",
				"CCU":"Proline","CCC":"Proline","CCA":"Proline","CCG":"Proline",
				"CAU":"Histidine","CAC":"Histidine",
				"CAA":"Glutamine","CAG":"Glutamine",
				"CGU":"Arginine","CGC":"Arginine","CGA":"Arginine","CGG":"Arginine",
				"AUU":"Isoleucine","AUC":"Isoleucine","AUA":"Isoleucine",
				"AUG":"Methionine",
				"ACU":"Threonine","ACC":"Threonine","ACA":"Threonine","ACG":"Threonine",
				"AAU":"Asparagine","AAC":"Asparagine",
				"AAA":"Lysine","AAG":"Lysine",
				"AGU":"Serine","AGC":"Serine",
				"AGA":"Arginine","AGG":"Arginine"
}


conversions = {"A":"U","T":"A","G":"C","C":"G","U":"A"}


dna_sequence = input("Enter the DNA Sequence: ")
dna_sequence = dna_sequence.upper()
print(dna_sequence)
print("\nConverting to complimentary sequence...")
rna_sequence = [conversions[dna_sequence[0]]]
base_number = 1

for i in range(len(dna_sequence) - 1):
    rna_sequence.append(conversions[dna_sequence[base_number]])
    base_number += 1

number = int(len(rna_sequence)/3 - 1)
number_2 = 3

for i in range(number):
    rna_sequence.insert(number_2, " ")
    number_2 += 4

number = 1
rna_sequence2 = rna_sequence[0]
for i in range(len(rna_sequence) - 1):
    rna_sequence2 += rna_sequence[number]
    number += 1

rna_sequence = rna_sequence2
rna_sequence = rna_sequence.split(" ")

protein = [amino_acids[rna_sequence[0]]]
protein_number = 1
for i in range(len(rna_sequence) - 1):
    protein.append(amino_acids[rna_sequence[protein_number]])
    protein_number = protein_number + 1

print('; '.join(protein))