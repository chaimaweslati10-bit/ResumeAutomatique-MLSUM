
import pandas as pd
from rouge_score import rouge_scorer

# 1. Charger les résultats nettoyés des 200 articles
df = pd.read_csv("resultats_200_propres.csv")

print("Nombre d'articles :", len(df))

# Vérifier les 200 articles
assert len(df) == 200, "Erreur : le fichier doit contenir exactement 200 articles."

# 2. Initialiser ROUGE pour le français
scorer = rouge_scorer.RougeScorer(
    ["rouge1", "rouge2", "rougeL"],
    use_stemmer=False
)

# 3. Définir les trois méthodes
methodes = ["zero_shot", "few_shot", "contrainte_longueur"]

resultats = []

# 4. Calculer les scores pour chaque méthode
for methode in methodes:

    scores_methode = []

    for _, ligne in df.iterrows():

        reference = str(ligne["resume_reference"])
        resume_genere = str(ligne[methode])

        scores = scorer.score(reference, resume_genere)

        scores_methode.append({
            "ROUGE-1": scores["rouge1"].fmeasure,
            "ROUGE-2": scores["rouge2"].fmeasure,
            "ROUGE-L": scores["rougeL"].fmeasure
        })

    # Calculer les moyennes
    resultats.append({
        "Methode": methode,
        "ROUGE-1": sum(s["ROUGE-1"] for s in scores_methode) / len(scores_methode),
        "ROUGE-2": sum(s["ROUGE-2"] for s in scores_methode) / len(scores_methode),
        "ROUGE-L": sum(s["ROUGE-L"] for s in scores_methode) / len(scores_methode)
    })

# 5. Afficher les résultats
tableau = pd.DataFrame(resultats)

print("\n===== SCORES ROUGE MOYENS SUR 200 ARTICLES =====")
print(tableau.to_string(index=False))

# 6. Sauvegarder les scores
tableau.to_csv(
    "scores_rouge_200_propres.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nFichier créé : scores_rouge_200_propres.csv")
print("ÉVALUATION TERMINÉE !")
