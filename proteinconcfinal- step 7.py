import pandas as pd
input_path = r'C:\Users\Hp\Downloads\new.csv'
output_path = r'C:\Users\Hp\Downloads\newfurther.csv'
df = pd.read_csv(input_path)
df.columns = df.columns.str.strip()
df.rename(columns={'weight%': 'weight_percent', 'total protein loaded': 'total_protein_loaded'}, inplace=True)
df['mw'] = df['mw'].astype(str).str.replace(',', '').astype(float)
df['total_protein_loaded'] = pd.to_numeric(df['total_protein_loaded'], errors='coerce')
df['weight_percent'] = pd.to_numeric(df['weight_percent'], errors='coerce')
df['absolute_ug'] = (df['weight_percent'] / 100) * df['total_protein_loaded']
df['pmol'] = (df['absolute_ug'] * 1000) / df['mw']
df['mol'] = df['pmol'] * 1e-12
df.to_csv(output_path, index=False)
print(f"Saved with pmol and mol: {output_path}")

