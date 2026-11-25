
import pandas as pd
import ollama

# Charger le dataset
df = pd.read_csv("dataset_avec_reference.csv")

# Article à tester : le troisième
article = df.iloc[2]["text"]

# Deux exemples pour la méthode Few-shot
exemple1 = df.iloc[0]
exemple2 = df.iloc[1]

# Méthode 1 : Zero-shot (sans exemple)
prompt_zero = f"""
Résume cet article de presse en français.
Sois fidèle au texte et conserve les informations importantes.

Article :
{article}
"""

# Méthode 2 : Few-shot (avec deux exemples)
prompt_few = f"""
Voici deux exemples de résumés :

Article 1 :
{exemple1['text']}

Résumé 1 :
{exemple1['summary']}

Article 2 :
{exemple2['text']}

Résumé 2 :
{exemple2['summary']}

Maintenant, résume cet article en français de la même manière :

{article}
"""

# Méthode 3 : avec une contrainte de longueur
prompt_longueur = f"""
Résume cet article en français en respectant ces règles :
- Maximum 100 mots.
- Conserve les informations essentielles.
- N'invente aucune information.

Article :
{article}
"""

# Fonction pour appeler Ollama
def generer_resume(prompt):
    resultat = ollama.chat(
        model="qwen2.5:1.5b",
        messages=[{"role": "user", "content": prompt}]
    )
    return resultat["message"]["content"]

# Génération des trois résumés
print("\n===== ZERO-SHOT =====")
print(generer_resume(prompt_zero))

print("\n===== FEW-SHOT =====")
print(generer_resume(prompt_few))

print("\n===== CONTRAINTE DE LONGUEUR =====")
print(generer_resume(prompt_longueur))
