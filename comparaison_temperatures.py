
import pandas as pd
import ollama
import os

# Charger les 200 articles
df = pd.read_csv("dataset_avec_reference.csv")

# Fichier de sauvegarde
fichier = "resultats_temperatures.csv"

# Reprendre si le traitement a déjà commencé
if os.path.exists(fichier):
    anciens = pd.read_csv(fichier)
    articles_traites = set(anciens["article_id"])
    print("Articles déjà traités :", len(articles_traites))
else:
    articles_traites = set()

resultats = []

# Fonction de génération
def generer_resume(article, temperature):
    prompt = f"""
Résume cet article de presse en français.
Rédige un résumé clair et fidèle.
N'invente aucune information.
Donne uniquement le résumé.

Article :
{article}
"""

    reponse = ollama.chat(
        model="qwen2.5:1.5b",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": temperature}
    )

    return reponse["message"]["content"].strip()


# Comparer les deux températures
for i, ligne in df.iterrows():

    if i in articles_traites:
        continue

    article = str(ligne["text"])

    print(f"Article {i + 1}/200")

    resume_02 = generer_resume(article, 0.2)
    resume_07 = generer_resume(article, 0.7)

    resultat = {
        "article_id": i,
        "resume_reference": ligne["summary"],
        "resume_temp_02": resume_02,
        "resume_temp_07": resume_07
    }

    # Sauvegarder après chaque article
    pd.DataFrame([resultat]).to_csv(
        fichier,
        mode="a",
        header=not os.path.exists(fichier),
        index=False,
        encoding="utf-8-sig"
    )

print("\nCOMPARAISON TERMINEE !")
print("Fichier créé :", fichier)

