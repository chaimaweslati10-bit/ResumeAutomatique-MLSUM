# Système de résumé automatique d'articles en français

**Projet de Traitement Automatique du Langage Naturel (TALN)**

---

## 1. Présentation du projet

Ce projet consiste à concevoir et expérimenter un système de **résumé automatique de textes en français** à l'aide d'un modèle de langage local (LLM).

L'objectif est de générer des résumés d'articles de presse tout en conservant les informations essentielles du texte original, puis de comparer différentes méthodes de génération et d'évaluer leur qualité.

Pour réaliser ce travail, nous utilisons le dataset **MLSUM (Multilingual Summarization)**, qui contient des articles de presse en français accompagnés de résumés de référence.

Le modèle de langage utilisé est **Qwen 2.5 1.5B**, exécuté localement avec **Ollama**.

### Objectifs

- Préparer et exploiter un dataset de 200 articles en français.
- Générer automatiquement des résumés selon plusieurs stratégies.
- Étudier l'influence des paramètres de génération.
- Évaluer les résumés avec les métriques ROUGE.
- Analyser les erreurs et les hallucinations produites par le modèle.
- Comparer les différentes configurations à l'aide de tableaux et de graphiques.

## 2. Méthodologie

Plusieurs approches de résumé automatique sont étudiées.

### 2.1. Résumé extractif (baseline)

Cette méthode consiste à sélectionner les trois premières phrases de chaque article original afin de construire un résumé de référence simple.

### 2.2. Résumé génératif avec Zero-shot

Le modèle reçoit uniquement une instruction lui demandant de résumer le texte, sans exemple préalable.

### 2.3. Résumé génératif avec Few-shot

Le modèle reçoit deux exemples de résumés avant de traiter un nouvel article afin de mieux comprendre le format attendu.

### 2.4. Résumé avec contrainte de longueur

Le modèle doit produire un résumé en respectant une limite de longueur définie dans la consigne.

### 2.5. Comparaison des températures

Deux températures sont étudiées :

- **0.2 :** génération plus contrôlée et généralement moins aléatoire.
- **0.7 :** génération plus variable et créative.

Cette comparaison permet d'étudier l'influence de la température sur les résultats.

## 3. Outils et technologies

| Outil | Rôle |
|---|---|
| Python 3.12 | Langage de programmation |
| MLSUM | Dataset d'articles en français |
| Ollama | Exécution locale du modèle |
| Qwen 2.5 1.5B | Modèle de génération des résumés |
| Pandas | Manipulation des données |
| NLTK | Traitement du texte |
| ROUGE | Évaluation automatique |
| Matplotlib | Visualisation des résultats |

## 4. Prérequis

Avant de lancer le projet, il faut disposer de :

- Python 3.12 installé.
- Ollama installé et fonctionnel.
- Le modèle Qwen 2.5 1.5B téléchargé.
- Visual Studio Code ou un autre éditeur Python.
- Une connexion Internet pour télécharger les dépendances et les données lors de la préparation initiale.

## 5. Installation

### Étape 1 : Accéder au dossier du projet

```powershell
cd ResumeAutomatique
```

### Étape 2 : Créer un environnement virtuel

```powershell
python -m venv venv312
```

### Étape 3 : Activer l'environnement virtuel

```powershell
.\venv312\Scripts\Activate.ps1
```

### Étape 4 : Installer les bibliothèques

```powershell
pip install -r requirements.txt
```

### Étape 5 : Télécharger le modèle

Après avoir installé Ollama :

```powershell
ollama pull qwen2.5:1.5b
```

Pour vérifier son installation :

```powershell
ollama list
```

## 6. Exécution du projet

Le projet est organisé en plusieurs étapes :

1. Chargement et préparation du dataset MLSUM.
2. Sélection de 200 articles en français.
3. Création des résumés extractifs de référence.
4. Génération des résumés avec les méthodes Zero-shot, Few-shot et contrainte de longueur.
5. Comparaison des températures 0.2 et 0.7.
6. Calcul des scores ROUGE.
7. Vérification manuelle de 20 résumés pour détecter les hallucinations.
8. Création des tableaux et des graphiques de comparaison.

Les résultats sont enregistrés dans des fichiers CSV et les graphiques dans des fichiers PNG.

## 7. Évaluation et résultats

### 7.1. Évaluation avec ROUGE

Trois métriques sont utilisées :

- **ROUGE-1 :** mesure le chevauchement des mots entre le résumé généré et le résumé de référence.
- **ROUGE-2 :** mesure le chevauchement des groupes de deux mots consécutifs.
- **ROUGE-L :** mesure la plus longue sous-séquence commune entre les deux résumés.

### 7.2. Résultats des trois méthodes de génération

Les scores ROUGE moyens obtenus sur les 200 articles sont :

| Méthode | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---|---:|---:|---:|
| Zero-shot | 0.1980 | 0.0715 | 0.1328 |
| Few-shot | 0.1943 | 0.0759 | 0.1356 |
| Contrainte de longueur | **0.2280** | **0.0813** | **0.1557** |

La méthode avec contrainte de longueur obtient les meilleurs résultats sur les trois métriques. Elle présente donc la meilleure similarité moyenne avec les résumés de référence selon ROUGE.

### 7.3. Comparaison des températures

Deux températures ont été comparées afin d'étudier leur influence sur la génération des résumés.

| Température | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---|---:|---:|---:|
| 0.2 | **0.1937** | **0.0717** | **0.1286** |
| 0.7 | 0.1829 | 0.0609 | 0.1186 |

Les résultats montrent que la température 0.2 obtient de meilleurs scores que la température 0.7 sur les trois métriques. Une génération moins aléatoire permet donc d'obtenir une meilleure similarité avec les résumés de référence dans cette expérience.

### 7.4. Vérification humaine des hallucinations

Une vérification manuelle de **20 résumés** a été réalisée en comparant les informations générées par le modèle avec les articles originaux.

Pour chaque résumé, les informations incorrectes ou inventées ont été relevées.

Les résultats obtenus sont les suivants :

| Méthode | Nombre de faits incorrects |
|---|---:|
| Zero-shot | 9 |
| Few-shot | 7 |
| Contrainte de longueur | 6 |
| Température 0.2 | 7 |
| Température 0.7 | 5 |
| **Total** | **34** |

Au total, **34 faits incorrects** ont été identifiés lors de cette vérification.

La température 0.7 présente le plus petit nombre de faits incorrects dans cet échantillon, tandis que la méthode avec contrainte de longueur présente le meilleur résultat selon les scores ROUGE moyens.

Ces résultats montrent que les scores ROUGE et la vérification humaine évaluent des aspects différents de la qualité des résumés.

### 7.5. Limites de ROUGE

Les métriques ROUGE présentent certaines limites, car elles reposent principalement sur le chevauchement des mots entre le résumé généré et le résumé de référence.

Par exemple, dans l'article concernant le chanteur et guitariste Roky Erickson (article 5), le résumé de référence indique qu'il était l'un des fondateurs du genre musical en 1966 avec son groupe *The 13th Floor Elevators*.

Le résumé généré par la méthode Few-shot reformule cette information en précisant qu'Erickson a commencé sa carrière avec ce groupe, connu pour son style garage et psychédélique.

Les scores obtenus pour cet exemple sont :

- **ROUGE-1 :** 0.0796
- **ROUGE-2 :** 0.0250
- **ROUGE-L :** 0.0597

Cet exemple montre que ROUGE peut attribuer un score faible à un résumé qui reprend une information avec une formulation différente de celle du texte de référence.

Ainsi, un faible score ROUGE ne signifie pas nécessairement que le résumé est incorrect. Il est donc important de compléter l'évaluation automatique par une vérification humaine afin de contrôler la fidélité des informations et de détecter les éventuelles hallucinations.

## 8. Limites du projet

Ce travail présente certaines limites :

- Les résultats dépendent du modèle de langage utilisé.
- Les résumés peuvent contenir des informations incorrectes ou inventées.
- Une température différente peut entraîner des variations dans les résultats.
- ROUGE ne reconnaît pas toujours les reformulations correctes.
- La vérification manuelle nécessite du temps et reste en partie subjective.
- L'évaluation humaine porte sur un échantillon limité de 20 résumés.

## 9. Lien du projet GitHub

**GitHub Repository :**

https://github.com/chaimaweslati10-bit/ResumeAutomatique-MLSUM

## 10. Auteurs

**Réalisé par :**

- Chaima Oueslati
- Hiba Larnaout

**Année universitaire : 2026-2027**