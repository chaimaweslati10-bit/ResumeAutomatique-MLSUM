import pandas as pd

# Charger le dataset nettoyé
df = pd.read_csv("dataset_nettoye.csv")

# Calculer la longueur des articles et des résumés
df["text_length"] = df["text"].apply(len)
df["summary_length"] = df["summary"].apply(len)

# Afficher les statistiques
print("LONGUEUR DES ARTICLES")
print(df["text_length"].describe())

print("\nLONGUEUR DES RESUMES")
print(df["summary_length"].describe())

# Calculer le taux de compression moyen
compression = (
    df["summary_length"].mean() /
    df["text_length"].mean()
) * 100

print("\nTaux de compression moyen :", round(compression, 2), "%")