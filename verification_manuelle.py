
import pandas as pd

# Charger les articles et les résumés générés
articles = pd.read_csv("dataset_avec_reference.csv")
resultats = pd.read_csv("resultats_200_propres.csv")
temperatures = pd.read_csv("resultats_temperatures.csv")

# Sélectionner les 20 premiers articles
selection = articles.head(20).copy()

# Ajouter les résumés des trois méthodes
selection["zero_shot"] = resultats["zero_shot"].head(20).values
selection["few_shot"] = resultats["few_shot"].head(20).values
selection["contrainte_longueur"] = resultats["contrainte_longueur"].head(20).values

# Ajouter les résumés des deux températures
selection["temperature_02"] = temperatures["resume_temp_02"].head(20).values
selection["temperature_07"] = temperatures["resume_temp_07"].head(20).values

# Préparer le tableau de vérification
verification = selection[
    [
        "text",
        "summary",
        "zero_shot",
        "few_shot",
        "contrainte_longueur",
        "temperature_02",
        "temperature_07"
    ]
]

# Sauvegarder le fichier
verification.to_csv(
    "verification_20_articles.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Nombre d'articles sélectionnés :", len(verification))
print("Nombre de résumés à vérifier :", len(verification) * 5)
print("Fichier créé : verification_20_articles.csv")
