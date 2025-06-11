import pandas as pd
import numpy as np


input_path = r'C:\Users\Hp\Downloads\results.csv'
output_path = r'C:\Users\Hp\Downloads\new.csv'
df = pd.read_csv(input_path)
df.columns = df.columns.str.strip()
df['MW'] = df['MW'].astype(str).str.replace(',', '', regex=False)
df['MW'] = pd.to_numeric(df['MW'], errors='coerce')
df['emPAI'] = pd.to_numeric(df['emPAI'], errors='coerce')
print(f"Original rows: {len(df)}")
df = df.dropna(subset=['MW', 'emPAI'])
print(f"After dropping NaN: {len(df)}")
df = df[np.isfinite(df['emPAI']) & np.isfinite(df['MW'])]
print(f"After removing infinite values: {len(df)}")
df = df[(df['MW'] > 0) & (df['emPAI'] > 0)]
print(f"After removing zeros: {len(df)}")

if len(df) == 0:
    print("ERROR: No valid data remaining!")
    exit()

print(f"emPAI range: {df['emPAI'].min()} to {df['emPAI'].max()}")
print(f"emPAI sum: {df['emPAI'].sum()}")
df['mol%'] = (df['emPAI'] / df['emPAI'].sum()) * 100
df['emPAI_x_MW'] = df['emPAI'] * df['MW']
df['weight%'] = (df['emPAI_x_MW'] / df['emPAI_x_MW'].sum()) * 100
df.drop(columns='emPAI_x_MW', inplace=True)
df['mol%'] = df['mol%'].round(6)
df['weight%'] = df['weight%'].round(6)
df.to_csv(output_path, index=False, float_format='%.6f')

print(f"\n SUCCESS! Protein content with mol% and weight% saved to:\n{output_path}")
print(f"\nFirst 10 results:")
print(df[['ProteinID', 'emPAI', 'mol%', 'weight%']].head(10))
print(f"\nValidation:")
print(f"mol% sum: {df['mol%'].sum():.2f}% (should be ~100%)")
print(f"weight% sum: {df['weight%'].sum():.2f}% (should be ~100%)")
