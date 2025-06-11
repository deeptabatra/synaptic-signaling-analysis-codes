import pandas as pd
df = pd.read_csv(r'C:\Users\Hp\weights.csv')
df["MW"] = df["MW"].str.replace(",", "").astype(float)
df["Pg quant"] = df["Pg quant"].astype(float)
df["fmol"] = (df["Pg quant"] * 1000) / df["MW"]
df["emPAI"] = (10 ** (df["Nobs"] / df["Ntheo"])) - 1
output_path = r'C:\Users\Hp\Downloads\results.csv'
df.to_csv(output_path, index=False)
print("Results saved to:", output_path)
print(df)
