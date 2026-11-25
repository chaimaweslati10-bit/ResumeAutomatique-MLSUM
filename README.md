# Système de résumé automatique d'articles en français

**Projet de Traitement Automatique du Langage Naturel (TALN)**

---

## 1. Présentation du projet

Ce projet consiste à concevoir et expérimenter un système de **résumé automatique de textes en français** en utilisant des modèles de langage (LLM) et des techniques de traitement automatique du langage naturel.

L'objectif principal est de générer des résumés courts, cohérents et informatifs à partir d'articles de presse, tout en conservant les informations essentielles du texte original.

Pour réaliser ce travail, nous utilisons le dataset **MLSUM (Multilingual Summarization)**, qui contient des articles de presse en français accompagnés de résumés de référence.

Le projet repose sur un modèle de langage local exécuté avec **Ollama**, ce qui permet de générer des résumés sans dépendre d'une API externe.

### Objectifs

- Préparer et exploiter un dataset de 200 articles en français.
- Générer automatiquement des résumés selon plusieurs stratégies.
- Étudier l'influence des paramètres de génération.
- Évaluer la qualité des résumés avec les métriques ROUGE.
- Analyser les erreurs et les hallucinations produites par le modèle.
- Comparer les performances des différentes configurations à l'aide de tableaux et de graphiques.

## 2. Méthodologie

Plusieurs approches de résumé automatique sont étudiées.

### 2.1. Résumé extractif

Cette méthode consiste à sélectionner les trois premières phrases de l'article original pour construire un résumé de référence simple (baseline).

### 2.2. Résumé génératif avec Zero-shot

Le modèle reçoit uniquement une instruction lui demandant de résumer le texte, sans exemple préalable.

### 2.3. Résumé génératif avec Few-shot

Le modèle reçoit deux exemples de résumés avant de traiter un nouvel article afin de mieux comprendre le format attendu.

### 2.4. Résumé avec contrainte de longueur

Le modèle doit produire un résumé en respectant une limite de longueur définie dans la consigne.

### 2.5. Comparaison des températures

Deux températures sont étudiées :

- **0.2** : génération plus contrôlée et généralement moins aléatoire.
- **0.7** : génération plus variable et créative.

Cette comparaison permet d'étudier l'influence de la température sur les résultats.

## 3. Outils et technologies

| Outil         | Rôle                             |
| ------------- | -------------------------------- |
| Python 3.12   | Langage de programmation         |
| MLSUM         | Dataset d'articles en français   |
| Ollama        | Exécution locale du modèle       |
| Qwen 2.5 1.5B | Modèle de génération des résumés |
| Pandas        | Manipulation des données         |
| NLTK          | Traitement du texte              |
| ROUGE         | Évaluation automatique           |
| Matplotlib    | Visualisation des résultats      |

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

Vérifier son installation :

```powershell
ollama list
```

## 6. Exécution du projet

Le projet est organisé en plusieurs étapes :

1. Chargement et préparation du dataset MLSUM.
2. Sélection de 200 articles en français.
3. Génération des résumés avec les différentes méthodes.
4. Comparaison des températures 0.2 et 0.7.
5. Calcul des scores ROUGE.
6. Vérification manuelle de 20 articles pour détecter les hallucinations.
7. Création des tableaux et des graphiques de comparaison.

Pour afficher les graphiques :

```powershell
python graphique_rouge.py
```

```powershell
python graphique_temperatures.py
```

Les résultats sont enregistrés dans des fichiers CSV et les graphiques dans des fichiers PNG.

## 7. Évaluation des résultats

### 7.1. Évaluation avec ROUGE

Trois métriques sont utilisées :

- **ROUGE-1** : mesure le chevauchement des mots entre le résumé généré et le résumé de référence.
- **ROUGE-2** : mesure le chevauchement des groupes de deux mots consécutifs.
- **ROUGE-L** : mesure la plus longue sous-séquence commune entre les deux résumés.

### 7.2. Analyse des hallucinations

Une vérification manuelle de 20 articles est prévue pour identifier les informations inventées ou incorrectes.

Chaque résumé est analysé en le comparant à l'article original :

- 0 : aucune hallucination détectée.
- 1 : au moins une hallucination détectée.

Cette étape permet de compléter l'évaluation automatique par une analyse qualitative.

### 7.3. Principaux résultats obtenus

Sur les 200 articles traités, les scores ROUGE moyens obtenus pour les trois méthodes sont :

| Méthode                |    ROUGE-1 |    ROUGE-2 |    ROUGE-L |
| ---------------------- | ---------: | ---------: | ---------: |
| Zero-shot              |     0.1980 |     0.0715 |     0.1328 |
| Few-shot               |     0.1943 |     0.0759 |     0.1356 |
| Contrainte de longueur | **0.2280** | **0.0813** | **0.1557** |

La méthode avec contrainte de longueur obtient les meilleurs scores sur les trois métriques.

La comparaison des températures montre également de meilleurs scores ROUGE avec une température de 0.2 qu'avec 0.7.

**Remarque :** les scores ROUGE mesurent la similarité avec les résumés de référence. Ils ne suffisent pas à garantir l'exactitude des informations générées.

## 8. Limites du projet

Ce travail présente certaines limites :

- Les résultats dépendent du modèle de langage utilisé.
- Une température plus élevée peut entraîner des variations dans les résumés.
- ROUGE ne reconnaît pas toujours les reformulations correctes.
- Un résumé ayant un bon score ROUGE peut contenir des informations incorrectes.
- La vérification manuelle nécessite du temps et reste en partie subjective.

## 9. Auteurs

**Réalisé par :**

- Chaima Oueslati
- Hiba Larnaout

**Année universitaire : 2026-2027**
# Système de résumé automatique d'articles en français

**Projet de Traitement Automatique du Langage Naturel (TALN)**

---

## 1. Présentation du projet

Ce projet consiste à concevoir et expérimenter un système de **résumé automatique de textes en français** en utilisant des modèles de langage (LLM) et des techniques de traitement automatique du langage naturel.

L'objectif principal est de générer des résumés courts, cohérents et informatifs à partir d'articles de presse, tout en conservant les informations essentielles du texte original.

Pour réaliser ce travail, nous utilisons le dataset **MLSUM (Multilingual Summarization)**, qui contient des articles de presse en français accompagnés de résumés de référence.

Le projet repose sur un modèle de langage local exécuté avec **Ollama**, ce qui permet de générer des résumés sans dépendre d'une API externe.

### Objectifs

- Préparer et exploiter un dataset de 200 articles en français.
- Générer automatiquement des résumés selon plusieurs stratégies.
- Étudier l'influence des paramètres de génération.
- Évaluer la qualité des résumés avec les métriques ROUGE.
- Analyser les erreurs et les hallucinations produites par le modèle.
- Comparer les performances des différentes configurations à l'aide de tableaux et de graphiques.

## 2. Méthodologie

Plusieurs approches de résumé automatique sont étudiées.

### 2.1. Résumé extractif

Cette méthode consiste à sélectionner les trois premières phrases de l'article original pour construire un résumé de référence simple (baseline).

### 2.2. Résumé génératif avec Zero-shot

Le modèle reçoit uniquement une instruction lui demandant de résumer le texte, sans exemple préalable.

### 2.3. Résumé génératif avec Few-shot

Le modèle reçoit deux exemples de résumés avant de traiter un nouvel article afin de mieux comprendre le format attendu.

### 2.4. Résumé avec contrainte de longueur

Le modèle doit produire un résumé en respectant une limite de longueur définie dans la consigne.

### 2.5. Comparaison des températures

Deux températures sont étudiées :

- **0.2** : génération plus contrôlée et généralement moins aléatoire.
- **0.7** : génération plus variable et créative.

Cette comparaison permet d'étudier l'influence de la température sur les résultats.

## 3. Outils et technologies

| Outil         | Rôle                             |
| ------------- | -------------------------------- |
| Python 3.12   | Langage de programmation         |
| MLSUM         | Dataset d'articles en français   |
| Ollama        | Exécution locale du modèle       |
| Qwen 2.5 1.5B | Modèle de génération des résumés |
| Pandas        | Manipulation des données         |
| NLTK          | Traitement du texte              |
| ROUGE         | Évaluation automatique           |
| Matplotlib    | Visualisation des résultats      |

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

Vérifier son installation :

```powershell
ollama list
```

## 6. Exécution du projet

Le projet est organisé en plusieurs étapes :

1. Chargement et préparation du dataset MLSUM.
2. Sélection de 200 articles en français.
3. Génération des résumés avec les différentes méthodes.
4. Comparaison des températures 0.2 et 0.7.
5. Calcul des scores ROUGE.
6. Vérification manuelle de 20 articles pour détecter les hallucinations.
7. Création des tableaux et des graphiques de comparaison.

Pour afficher les graphiques :

```powershell
python graphique_rouge.py
```

```powershell
python graphique_temperatures.py
```

Les résultats sont enregistrés dans des fichiers CSV et les graphiques dans des fichiers PNG.

## 7. Évaluation des résultats

### 7.1. Évaluation avec ROUGE

Trois métriques sont utilisées :

- **ROUGE-1** : mesure le chevauchement des mots entre le résumé généré et le résumé de référence.
- **ROUGE-2** : mesure le chevauchement des groupes de deux mots consécutifs.
- **ROUGE-L** : mesure la plus longue sous-séquence commune entre les deux résumés.

### 7.2. Analyse des hallucinations

Une vérification manuelle de 20 articles est prévue pour identifier les informations inventées ou incorrectes.

Chaque résumé est analysé en le comparant à l'article original :

- 0 : aucune hallucination détectée.
- 1 : au moins une hallucination détectée.

Cette étape permet de compléter l'évaluation automatique par une analyse qualitative.

### 7.3. Principaux résultats obtenus

Sur les 200 articles traités, les scores ROUGE moyens obtenus pour les trois méthodes sont :

| Méthode                |    ROUGE-1 |    ROUGE-2 |    ROUGE-L |
| ---------------------- | ---------: | ---------: | ---------: |
| Zero-shot              |     0.1980 |     0.0715 |     0.1328 |
| Few-shot               |     0.1943 |     0.0759 |     0.1356 |
| Contrainte de longueur | **0.2280** | **0.0813** | **0.1557** |

La méthode avec contrainte de longueur obtient les meilleurs scores sur les trois métriques.

La comparaison des températures montre également de meilleurs scores ROUGE avec une température de 0.2 qu'avec 0.7.

**Remarque :** les scores ROUGE mesurent la similarité avec les résumés de référence. Ils ne suffisent pas à garantir l'exactitude des informations générées.

## 8. Limites du projet

Ce travail présente certaines limites :

- Les résultats dépendent du modèle de langage utilisé.
- Une température plus élevée peut entraîner des variations dans les résumés.
- ROUGE ne reconnaît pas toujours les reformulations correctes.
- Un résumé ayant un bon score ROUGE peut contenir des informations incorrectes.
- La vérification manuelle nécessite du temps et reste en partie subjective.

## 9. Auteurs

**Réalisé par :**

- Chaima Oueslati
- Hiba Larnaout

**Année universitaire : 2026-2027**
