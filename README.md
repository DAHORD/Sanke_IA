# Snake IA – Jeu Snake avec Intelligence Artificielle (Q-Learning)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache-2.0-yellow.svg)](LICENSE)

## Présentation

**Snake IA** est une version moderne du jeu Snake développée en Python avec [pygame](https://www.pygame.org/), intégrant une intelligence artificielle basée sur le Q-Learning. Ce projet a pour but d’illustrer l’apprentissage par renforcement appliqué à un jeu classique, tout en offrant une expérience utilisateur fluide et professionnelle.

---

## Fonctionnalités principales

- **Jeu Snake jouable manuellement** avec interface graphique moderne.
- **Entraînement autonome d’une IA** via Q-Learning, avec contrôle sur le nombre de parties.
- **Sauvegarde automatique** du modèle IA et de l’historique des scores.
- **Visualisation graphique** de la progression de l’IA (scores, moyennes, etc.).
- **Relecture des parties** jouées par l’IA à partir de modèles sauvegardés.
- **Arrêt manuel sécurisé** pendant l’entraînement.
- **Structure de projet claire** pour une prise en main rapide.

---

## Structure du projet

```
.
├── assets/                # Ressources graphiques (pomme, police, etc.)
│   ├── apple.png
│   └── font.ttf
├── model/                 # Modèles IA sauvegardés (.pkl, dossier obligatoire)
├── snake_ia/              # Code source principal
│   ├── __init__.py
│   ├── agent.py           # Logique Q-Learning (Agent IA)
│   ├── game_objects.py    # Classes Snake et Food
│   ├── games_pkl_ia.py    # Relecture des parties IA sauvegardées
│   ├── graphic_pkl_ia.py  # Visualisation graphique des scores sauvegardés
│   ├── main_game.py       # Jeu Snake classique (manuel)
│   ├── main_nb.py         # Entraînement IA (nombre de parties défini)
│   ├── main_while.py      # Entraînement IA (boucle infinie)
│   ├── plotter.py         # Affichage dynamique des scores pendant l'entraînement
│   └── settings.py        # Paramètres globaux (jeu, IA, chemins)
├── requirements.txt       # Dépendances Python
├── LICENSE                # Licence Apache 2.0
└── .gitignore
```
> **NB :** Le dossier `model` est indispensable pour le bon fonctionnement de l’IA.

Pour voir la totalité des fichiers et dossiers (notamment si le dossier `snake_ia/` comporte plus de 10 fichiers), consultez la page GitHub du dossier : [Voir snake_ia sur GitHub](https://github.com/DAHORD/Sanke_IA/tree/main/snake_ia)

---

## Installation

1. **Cloner le dépôt**
   ```sh
   git clone https://github.com/DAHORD/Sanke_IA.git
   cd Sanke_IA
   ```

2. **Installer les dépendances**
   ```sh
   pip install -r requirements.txt
   ```

3. **Vérifier les ressources**
   - `assets/apple.png` (image de la pomme)
   - `assets/font.ttf` (police d’écriture)
   - Le dossier `model/` (pour les sauvegardes IA)
   - Ajoutez vos propres ressources dans `assets/` si besoin.

---

## Utilisation

### 1. Jouer manuellement

Lancer le jeu Snake en mode classique :
```sh
python snake_ia/main_game.py
```
- Contrôles : Flèches directionnelles du clavier.
- Appuyez sur une touche pour démarrer ou rejouer.

---

### 2. Entraîner l’IA

#### a) Avec un nombre fixe de parties (`TOTAL_GAMES_TO_TRAIN` dans `settings.py`)
```sh
python snake_ia/main_nb.py
```
- L’IA s’entraîne sur le nombre de parties défini.
- Les scores et le modèle sont sauvegardés dans `model/`.

#### b) En boucle infinie (arrêt manuel)
```sh
python snake_ia/main_while.py
```
- Arrêtez l’entraînement via la croix de la fenêtre ou Ctrl+C.

---

### 3. Visualiser la progression de l’IA

Afficher les graphiques des scores à partir des modèles sauvegardés :
```sh
python snake_ia/graphic_pkl_ia.py
```

---

### 4. Rejouer des parties de l’IA

Rejouez les parties de l’IA à partir d’un modèle sauvegardé :
```sh
python snake_ia/games_pkl_ia.py --start 1 --end 10
```
- `--start` : numéro de la première partie (défaut : 1)
- `--end` : numéro de la dernière partie (défaut : toutes)

---

## Personnalisation & Configuration

- **Paramètres du jeu et de l’IA** : modifiez [`snake_ia/settings.py`](snake_ia/settings.py)
- **Chemins des ressources** : adaptez `FONT_PATH`, `FOOD_IMAGE_PATH`, `MODEL_PATH` si besoin.
- **Nombre de parties d’entraînement** : changez `TOTAL_GAMES_TO_TRAIN` dans les paramètres.

---

## Dépendances

- pygame
- numpy
- matplotlib
- pandas

Installez-les rapidement :
```sh
pip install -r requirements.txt
```

---

## Licence

Projet sous licence [Apache 2.0](LICENSE).

---

## Auteur

- DAHORD

---

## Contribution & Support

- Les modèles IA sont sauvegardés dans [`model/`](model/).
- Pour toute question, suggestion ou amélioration, ouvrez un ticket (issue) ou une pull request.
- Toute contribution est la bienvenue afin d’améliorer ce projet open source.

---

Bon jeu et bon apprentissage avec Snake IA ! 🐍🤖
