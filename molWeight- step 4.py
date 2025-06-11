import requests
import pandas as pd
import json

def fetch_molweight(protein_idsss):
    url = f"https://rest.uniprot.org/uniprotkb/{protein_idsss}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        mol_weight = data.get('sequence', {}).get('molWeight', 'MolWeight not found')
        return mol_weight
    else:
        return "Error fetching data"

def process_csv(input_file, output_file, protein_column):
    df = pd.read_csv(input_file)
    if protein_column not in df.columns:
        raise KeyError(f"Column '{protein_column}' not found in the input file.")
    
    df['molWeight'] = df[protein_column].apply(fetch_molweight)
    df.to_csv(output_file, index=False)
    print(f"Molecular weights saved to {output_file}")

process_csv(r'C:\Users\Hp\Downloads\hello.csv', 'weights.csv', 'Protein_ID')
