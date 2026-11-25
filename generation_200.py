
import pandas as pd
import ollama
import os

# Charger les 200 articles
df = pd.read_csv("dataset_avec_reference.csv")

# Fichier de sauvegarde
fichier_sortie = "resultats_200.csv"

# Reprendre le traitement si le fichier existe déjà
if os.path.exists(fichier_sortie):
    resultats_existants = pd.read_csv(fichier_sortie)
    articles_deja_traites = set(resultats_existants["article_id"])
    print(f"{len(articles_deja_traites)} articles déjà traités.")
else:
    resultats_existants = pd.DataFrame()
    articles_deja_traites = set()

# Fonction pour interroger Ollama
def generer_resume(prompt):
    reponse = ollama.chat(
        model="qwen2.5:1.5b",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.2}
    )
    return reponse["message"]["content"].strip()

# Exemples pour la méthode Few-shot
exemple_1 = df.iloc[0]
exemple_2 = df.iloc[1]

resultats = []

for i, ligne in df.iterrows():

    if i in articles_deja_traites:
        continue

    article = str(ligne["text"])
    resume_reference = str(ligne["summary"])

    print(f"\nTraitement de l'article {i + 1}/200...")

    # Méthode 1 : Zero-shot
    prompt_zero = f"""
Résume cet article de presse en français.
Rédige un texte continu, clair et fidèle.
N'invente aucune information.
Donne uniquement le résumé.

Article :
{article}
"""
    resume_zero = generer_resume(prompt_zero)

    # Méthode 2 : Few-shot avec deux exemples
    prompt_few = f"""
Voici deux exemples de résumés.

Article 1 :
{str(exemple_1['text'])[:1500]}

Résumé 1 :
{exemple_1['summary']}

Article 2 :
{str(exemple_2['text'])[:1500]}

Résumé 2 :
{exemple_2['summary']}

Résume maintenant le nouvel article en français.
Écris un texte continu, sans liste.
N'invente aucune information.
Donne uniquement le résumé.

Nouvel article :
{article}
"""
    resume_few = generer_resume(prompt_few)

    # Méthode 3 : Contrainte de longueur
    prompt_longueur = f"""
Résume cet article en français en 100 mots maximum.
Reste fidèle au contenu.
N'invente aucune information.
Donne uniquement le résumé.

Article :
{article}
"""
    resume_longueur = generer_resume(prompt_longueur)

    # Ajouter les résultats
    nouveau_resultat = {
        "article_id": i,
        "article": article,
        "resume_reference": resume_reference,
        "zero_shot": resume_zero,
        "few_shot": resume_few,
        "contrainte_longueur": resume_longueur
    }

    resultats.append(nouveau_resultat)

    # Sauvegarder après chaque article
    pd.DataFrame(resultats).to_csv(
        fichier_sortie,
        mode="a",
        header=not os.path.exists(fichier_sortie),
        index=False,
        encoding="utf-8-sig"
    )

print("\nTRAITEMENT TERMINE !")
print("Fichier créé :", fichier_sortie)
