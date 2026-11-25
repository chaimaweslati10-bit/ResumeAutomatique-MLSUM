import pandas as pd
import matplotlib.pyplot as plt

# Charger les résultats
df = pd.read_csv("scores_temperatures.csv", index_col=0)

# Transposer le tableau
df = df.T

# Créer le graphique
df.plot(
    kind="bar",
    figsize=(9, 6)
)

# Personnalisation
plt.title("Comparaison des températures selon les scores ROUGE")
plt.xlabel("Température")
plt.ylabel("Score ROUGE")
plt.xticks(rotation=0)
plt.legend(title="Métriques")
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Enregistrer le graphique
plt.tight_layout()
plt.savefig("graphique_temperatures.png", dpi=300)
plt.show()