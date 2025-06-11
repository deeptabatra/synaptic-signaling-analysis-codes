import pandas as pd

input_file = r'C:\Users\Hp\Downloads\New Method- 30m_D_PE - Sheet1.csv'
df = pd.read_csv(input_file)

df.columns = df.columns.str.strip()
df.rename(columns={
    'Pg quant': 'LFQ',
    'Ntheo': 'Ntheo',
    'MW': 'MW'
}, inplace=True)

df['LFQ'] = pd.to_numeric(df['LFQ'], errors='coerce')
df['Ntheo'] = pd.to_numeric(df['Ntheo'], errors='coerce')
df['MW'] = pd.to_numeric(df['MW'].astype(str).str.replace(',', ''), errors='coerce')  # remove commas

df['weighted_intensity'] = (df['LFQ'] / df['Ntheo']) / df['MW']
mw_weight_norm_sum_intens = df['weighted_intensity'].sum()

prot_per_cell = 200e-12  # 200 pg in grams
avogadro = 6.022e23
total_cell_prot_conc = 235e-6  # 235 micrograms in grams

df['CopyNumber'] = (df['LFQ'] / df['Ntheo']) * (prot_per_cell * avogadro) / mw_weight_norm_sum_intens

numerator = (df['CopyNumber'] * df['MW']).sum()
total_volume = numerator / (avogadro * total_cell_prot_conc)

print(f"Total cell volume calculated: {total_volume:.6e} liters")

output_file = 'output_with_total_volume.csv'
df['Total_Volume_Liters'] = total_volume
df.to_csv(output_file, index=False)
print(f"Results saved to: {output_file}")
