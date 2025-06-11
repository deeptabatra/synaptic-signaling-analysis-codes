import pandas as pd
import requests

def fetch_sequence(protein_id):
    """Fetch the FASTA sequence from UniProt for a given protein ID."""
    url = f"https://rest.uniprot.org/uniprotkb/{protein_id}.fasta"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "Error fetching sequence"

def process_csv(input_file, output_file, protein_column):
   df = pd.read_csv(input_file)
   df[protein_column] = df[protein_column].astype(str)
   df['FASTA_Sequence'] = df[protein_column].apply(fetch_sequence)
   df.to_csv(output_file, index=False)
    print(f"✅ FASTA sequences saved to: {output_file}")


process_csv(
    input_file=r'C:\Users\Hp\Downloads\protein_peptide_summary_with_pg.csv',
    output_file=r'C:\Users\Hp\Downloads\output_with_sequences.csv',
    protein_column='ProteinID'
)
