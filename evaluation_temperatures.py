
import pandas as pd
from rouge_score import rouge_scorer

# Charger les résultats
df = pd.read_csv("resultats_temperatures.csv")

# Éviter les doublons
df = df.drop_duplicates(subset="article_id", keep="first")

print("Nombre d'articles :", len(df))

# Vérifier les 200 articles
if len(df) != 200:
    raise ValueError("Attention : le fichier ne contient pas 200 articles.")

# Préparer ROUGE
scorer = rouge_scorer.RougeScorer(
    ["rouge1", "rouge2", "rougeL"],
    use_stemmer=False
)

scores_02 = []
scores_07 = []

# Calculer les scores
for _, ligne in df.iterrows():

    reference = str(ligne["resume_reference"])

    resultat_02 = scorer.score(
        reference, str(ligne["resume_temp_02"])
    )

    resultat_07 = scorer.score(
        reference, str(ligne["resume_temp_07"])
    )

    scores_02.append([
        resultat_02["rouge1"].fmeasure,
        resultat_02["rouge2"].fmeasure,
        resultat_02["rougeL"].fmeasure
    ])

    scores_07.append([
        resultat_07["rouge1"].fmeasure,
        resultat_07["rouge2"].fmeasure,
        resultat_07["rougeL"].fmeasure
    ])

# Calculer les moyennes
moyennes_02 = pd.DataFrame(
    scores_02,
    columns=["ROUGE-1", "ROUGE-2", "ROUGE-L"]
).mean()

moyennes_07 = pd.DataFrame(
    scores_07,
    columns=["ROUGE-1", "ROUGE-2", "ROUGE-L"]
).mean()

# Afficher les résultats
comparaison = pd.DataFrame({
    "Temperature 0.2": moyennes_02,
    "Temperature 0.7": moyennes_07
})

print("\n===== COMPARAISON DES TEMPERATURES =====")
print(comparaison.round(6))

# Sauvegarder
comparaison.to_csv(
    "scores_temperatures.csv",
    encoding="utf-8-sig"
)

print("\nFichier créé : scores_temperatures.csv")
print("EVALUATION TERMINEE !")

