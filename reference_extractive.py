import pandas as pd
from nltk.tokenize import sent_tokenize

# 1. Charger le dataset nettoyé
df = pd.read_csv("dataset_nettoye.csv")

# 2. Extraire les 3 premières phrases de chaque article
df["reference_extractive"] = df["text"].apply(
    lambda article: " ".join(
        sent_tokenize(str(article), language="french")[:3]
    )
)

# 3. Enregistrer le nouveau dataset
df.to_csv("dataset_avec_reference.csv", index=False, encoding="utf-8-sig")

# 4. Afficher un exemple
print("Nombre d'articles :", len(df))
print("\nExemple de référence extractive :")
print(df["reference_extractive"].iloc[0])

print("\nFichier créé : dataset_avec_reference.csv")
