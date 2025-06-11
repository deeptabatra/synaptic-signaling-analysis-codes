import pandas as pd
input_file = r"C:\Users\Hp\Downloads\Absolute Values- D_I_5min - Set 3 .csv"  # replace with your actual file
df = pd.read_csv(input_file)
df['PeptideSequence'] = df['PeptideSequence'].astype(str)
df['ProteinID'] = df['ProteinID'].astype(str)
df['ProteinID'] = df['ProteinID'].str.split(';')
df_exploded = df.explode('ProteinID').reset_index(drop=True)
df_exploded['PG.Quantity'] = pd.to_numeric(df_exploded['PG.Quantity'], errors='coerce').fillna(0)
result = df_exploded.groupby('ProteinID').agg(
    Num_Peptides=('PeptideSequence', lambda x: len(set(x))),
    PeptideSequences=('PeptideSequence', lambda x: ', '.join(sorted(set(x)))),
    Total_PG_Quantity=('PG.Quantity', 'sum')
).reset_index()


output_file = r"C:\Users\Hp\Downloads\protein_peptide_summary_with_pg.csv"
result.to_csv(output_file, index=False)

print(f"Summary saved to: {output_file}")
