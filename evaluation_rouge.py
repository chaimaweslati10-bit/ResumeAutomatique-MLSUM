
import pandas as pd
from rouge_score import rouge_scorer

# 1. Charger les résultats des 200 articles
df = pd.read_csv("resultats_200_propres.csv")

print("Nombre d'articles :", len(df))

assert len(df) == 200, "Erreur : le fichier doit contenir exactement 200 articles."

# 2. Initialiser ROUGE
scorer = rouge_scorer.RougeScorer(
    ["rouge1", "rouge2", "rougeL"],
    use_stemmer=False
)

# 3. Définir les méthodes
methodes = ["zero_shot", "few_shot", "contrainte_longueur"]

resultats = []
scores_individuels = []

# 4. Calculer les scores pour chaque article et chaque méthode
for methode in methodes:

    scores_methode = []

    for index, ligne in df.iterrows():

        reference = str(ligne["resume_reference"])
        resume_genere = str(ligne[methode])

        scores = scorer.score(reference, resume_genere)

        rouge1 = scores["rouge1"].fmeasure
        rouge2 = scores["rouge2"].fmeasure
        rougeL = scores["rougeL"].fmeasure

        scores_methode.append({
            "ROUGE-1": rouge1,
            "ROUGE-2": rouge2,
            "ROUGE-L": rougeL
        })

        # Sauvegarder les scores individuels
        scores_individuels.append({
            "article_id": ligne["article_id"] if "article_id" in df.columns else index + 1,
            "Methode": methode,
            "ROUGE-1": rouge1,
            "ROUGE-2": rouge2,
            "ROUGE-L": rougeL
        })

    # Calculer les moyennes
    resultats.append({
        "Methode": methode,
        "ROUGE-1": sum(s["ROUGE-1"] for s in scores_methode) / len(scores_methode),
        "ROUGE-2": sum(s["ROUGE-2"] for s in scores_methode) / len(scores_methode),
        "ROUGE-L": sum(s["ROUGE-L"] for s in scores_methode) / len(scores_methode)
    })

# 5. Afficher les moyennes
tableau = pd.DataFrame(resultats)

print("\n===== SCORES ROUGE MOYENS SUR 200 ARTICLES =====")
print(tableau.to_string(index=False))

# 6. Sauvegarder les moyennes
tableau.to_csv(
    "scores_rouge_200_propres.csv",
    index=False,
    encoding="utf-8-sig"
)

# 7. Sauvegarder les scores individuels
tableau_individuel = pd.DataFrame(scores_individuels)

tableau_individuel.to_csv(
    "scores_rouge_individuels.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nFichier créé : scores_rouge_200_propres.csv")
print("Fichier créé : scores_rouge_individuels.csv")
print("\nÉVALUATION TERMINÉE !")
