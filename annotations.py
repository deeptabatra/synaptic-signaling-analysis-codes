import pandas as pd
import requests
import time

df = pd.read_csv(r"C:\Users\Hp\Downloads\hello.csv")

def get_annotation_score(protein_id):
    url = f"https://rest.uniprot.org/uniprotkb/{protein_id}.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('annotationScore', 'NA')  # fetch the score if available
        else:
            return 'NA'
    except:
        return 'NA'

df['Annotation score'] = df['Protein_ID'].apply(get_annotation_score)

df.to_csv(r'C:\Users\Hp\Downloads\editedproteins.csv', index=False)

print("Annotation scores added and file saved successfully.")


