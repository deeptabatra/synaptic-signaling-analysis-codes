# synaptic-signaling-analysis-codes
Python code for mass spectrometry-based synaptic signaling analysis

Protein Absolute Quantification: emPAI Method
The Exponentially Modified Protein Abundance Index (emPAI) method was employed as a primary approach for converting relative protein abundances to absolute values. This method addresses the challenge of accurately quantifying proteins in complex biological mixtures.

The Protein Abundance Index (PAI) serves as the foundation for emPAI and is calculated as the ratio of the number of observed peptides (Nobsd​) for a specific protein to the number of theoretically observable peptides (Nobsbl​) for that protein 1:
PAI=Nobsbl​Nobsd​​ (Eq. 1)

The emPAI is then derived from the PAI using an exponential transformation 1:
emPAI=10PAI−1 (Eq. 2)

Once the emPAI value is determined, the protein content in molar percentage (mol%) and weight percentage (weight%) can be calculated using the emPAI values and the molecular weight (Mr​) of the protein 1:
Proteincontent(mol%)=∑(emPAI)emPAI​×100 (Eq. 3)

Proteincontent(weight%)=∑(emPAI×Mr​)emPAI×Mr​​×100 (Eq. 4)

The underlying logic of emPAI is rooted in empirical observations. The PAI normalizes raw peptide counts, thereby accounting for biases related to protein size and composition. While PAI itself is not directly proportional to molar amount, a pivotal discovery demonstrated a consistent linear relationship between the logarithm of protein concentration and PAI values. This relationship was observed for human serum albumin and validated across diverse proteins in mouse neuro2a cell lysate, showing a high correlation (r=0.89). The "minus one" adjustment in the emPAI formula was empirically determined through experimental fitting to optimize this direct proportionality. This adjustment ensures that if a PAI of 0 is obtained (indicating no peptides were observed and the protein is effectively absent), then emPAI also correctly yields a value of 0 (100−1=0), establishing a proper baseline and a direct proportionality between emPAI and protein content.


Protein Absolute Quantification: Protein Concentration Conversion Method
To convert label-free quantification (LFQ) values into biologically meaningful metrics such as protein copy number, molar concentration, and total protein volume, we employed a multi-step computational method distinct from traditional emPAI-based approaches. The process begins with the calculation of a weighted intensity measure, referred to as mwWeightNormSumIntens. This value adjusts LFQ intensities by accounting for both the theoretical detectability of peptides and the molecular weight of each protein, ensuring that differences in protein size and peptide abundance are normalized appropriately.
Building upon this, the protein copy number per cell is estimated using a formula that incorporates the normalized LFQ intensity, the molecular weight of the protein, and an assumed protein content of 200 picograms per cell, alongside Avogadro’s constant. This allows us to estimate how many molecules of a given protein are present in an average cell. To determine the total protein volume within a cell, the method then calculates the cumulative molecular weight of all detected proteins, multiplied by their respective copy numbers and normalized using a constant for total protein concentration, which is assumed to be 200 grams per liter. Finally, individual protein concentrations are derived by dividing their copy number by the calculated total cellular volume and Avogadro’s number, yielding the molar concentration for each protein.
