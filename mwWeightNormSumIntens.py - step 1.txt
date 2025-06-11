import pandas as pd

input_file = r'C:\Users\Hp\Downloads\New Method- 30m_D_PE - Sheet1.csv'
df = pd.read_csv(input_file)
df['MW_clean'] = df['MW'].astype(str).str.replace(',', '').astype(float)
df['mwWeightNormSumIntens'] = (df['Pg quant'] / df['Ntheo']) * df['MW_clean']
total_sum = df['mwWeightNormSumIntens'].sum()
output_file = 'output.csv'
df.to_csv(output_file, index=False)

print(f"Computation complete. Total mwWeightNormSumIntens: {total_sum}")
print(f"Results saved to: {output_file}")
