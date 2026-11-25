
import pandas as pd

# Charger les résultats
df = pd.read_csv("resultats_200.csv")

print("Avant nettoyage :", len(df), "lignes")

# Supprimer les doublons en conservant une seule ligne par article
df = df.drop_duplicates(subset="article_id", keep="first")

# Trier les articles dans l'ordre
df = df.sort_values("article_id").reset_index(drop=True)

# Sauvegarder le fichier propre
df.to_csv("resultats_200_propres.csv", index=False, encoding="utf-8-sig")

print("Après nettoyage :", len(df), "lignes")
print("Articles uniques :", df["article_id"].nunique())
print("Fichier créé : resultats_200_propres.csv")
