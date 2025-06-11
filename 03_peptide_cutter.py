import pandas as pd
import re

def count_trypsin_cleavages(sequence):
    if not isinstance(sequence, str):
        return 0
    cleavage_sites = re.findall(r'(?<=[KR])(?!P)', sequence)
    return len(cleavage_sites)

def process_csv(input_file, output_file, sequence_column):
    df = pd.read_csv(input_file)
    df['Trypsin_Cleavage_Count'] = df[sequence_column].apply(count_trypsin_cleavages)
    df.to_csv(output_file, index=False)
    print(f"Trypsin cleavage counts saved to {output_file}")

input_file = 'C:\\Users\\Hp\\Downloads\\output_with_sequences.csv'
output_file = 'pepcutterr.csv'
sequence_column = 'Sequence'

process_csv(input_file, output_file, sequence_column)
