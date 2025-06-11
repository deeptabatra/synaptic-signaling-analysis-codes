# synaptic-signaling-analysis-codes

Synaptic Signaling Analysis Codes
Python Code for Mass Spectrometry-Based Synaptic Signaling Analysis

Protein Absolute Quantification: emPAI Method
The Exponentially Modified Protein Abundance Index (emPAI) method is employed as a primary approach for converting relative protein abundances to absolute values. This method addresses the challenge of accurately quantifying proteins in complex biological mixtures.
1. Protein Abundance Index (PAI)
The PAI is the foundation of emPAI and is calculated as:
PAI=NobsdNobsbl(Eq. 1)\text{PAI} = \frac{N_{\text{obsd}}}{N_{\text{obsbl}}} \quad \text{(Eq. 1)} 
Where:
•	NobsdN_{\text{obsd}} = Number of observed peptides
•	NobsblN_{\text{obsbl}} = Number of theoretically observable peptides
2. emPAI Calculation
emPAI is derived from PAI using an exponential transformation:
emPAI=10PAI−1(Eq. 2)\text{emPAI} = 10^{\text{PAI}} - 1 \quad \text{(Eq. 2)} 
3. Protein Content Estimation
•	Molar percentage (mol%):
\text{Protein content (mol%)} = \frac{\text{emPAI}}{\sum (\text{emPAI})} \times 100 \quad \text{(Eq. 3)} 
•	Weight percentage (weight%):
\text{Protein content (weight%)} = \frac{\text{emPAI} \times M_r}{\sum (\text{emPAI} \times M_r)} \times 100 \quad \text{(Eq. 4)} 
Where MrM_r is the molecular weight of the protein.
4. Rationale Behind emPAI
•	PAI normalizes raw peptide counts to account for protein size and sequence bias.
•	A logarithmic relationship was observed between PAI and actual protein concentrations (e.g., high correlation r=0.89r = 0.89 in mouse neuro2a cell lysate).
•	The “−1” in the emPAI formula ensures zero output when no peptides are observed, setting a correct baseline.

Protein Absolute Quantification: Protein Concentration Conversion Method
To derive biologically meaningful values (e.g., copy number, molar concentration) from label-free quantification (LFQ), a multi-step computational pipeline is used:
1. Weighted Intensity Calculation
•	Compute mwWeightNormSumIntens, a weighted sum of LFQ intensities.
•	Adjusts for both peptide detectability and protein molecular weight.
2. Protein Copy Number Estimation
•	Estimated using:
o	Normalized LFQ intensity
o	Protein molecular weight
o	Assumed cellular protein content (200 pg per cell)
o	Avogadro’s constant
3. Total Protein Volume
•	Calculate total cellular protein volume by:
o	Multiplying protein molecular weights by their estimated copy numbers.
o	Normalizing using an assumed protein concentration (200 g/L).
4. Molar Concentration Calculation
•	Divide each protein's copy number by the total cell volume and Avogadro’s number to obtain molar concentration.

