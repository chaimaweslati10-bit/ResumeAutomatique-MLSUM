
import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("verification_20_articles.csv")

# Créer un vrai fichier Excel
df.to_excel(
    "verification_20_articles.xlsx",
    index=False,
    engine="openpyxl"
)

print("Conversion terminee !")
print("Fichier : verification_20_articles.xlsx")
print("Nombre de lignes :", len(df))
print("Nombre de colonnes :", len(df.columns))
