def dna_to_anticodon(dna_sequence):
    # DNA'yı mRNA'ya dönüştür
    mrna = dna_sequence.upper().replace('T', 'U')

    # Kodonları 3'lü gruplara ayır
    codons = [mrna[i:i + 3] for i in range(0, len(mrna), 3)]

    # Antikodonları hesapla
    anticodon_dict = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    anticodons = []

    for codon in codons:
        reversed_codon = codon[::-1]  # Kodonu ters çevir
        anticodon = ''.join([anticodon_dict[base] for base in reversed_codon])
        anticodons.append(anticodon)

    return anticodons


# Kullanım örneği
dna_input = input("DNA dizisini girin: ").strip().upper()
result = dna_to_anticodon(dna_input)

print("Antikodonlar:", result)