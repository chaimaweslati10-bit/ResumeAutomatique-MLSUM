
import pandas as pd
import matplotlib.pyplot as plt

# Charger les scores ROUGE
df = pd.read_csv("scores_rouge_200_propres.csv")

# Préparer le graphique
df.plot(
    x="Methode",
    y=["ROUGE-1", "ROUGE-2", "ROUGE-L"],
    kind="bar",
    figsize=(10, 6)
)

# Ajouter les titres
plt.title("Comparaison des méthodes de résumé automatique")
plt.xlabel("Méthodes")
plt.ylabel("Score ROUGE")
plt.xticks(rotation=0)
plt.legend(title="Métriques")
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Afficher et enregistrer
plt.tight_layout()
plt.savefig("graphique_rouge_200.png", dpi=300)
plt.show()
