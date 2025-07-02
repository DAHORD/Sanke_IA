# 🐍🤖 Snake IA – Jeu Snake avec Intelligence Artificielle (Deep Q-Learning)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange.svg)](https://pytorch.org/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache2.0-yellow.svg)](LICENSE)

---

## Présentation

**Snake IA** est une version moderne du jeu Snake développée en Python avec [pygame](https://www.pygame.org/), intégrant une intelligence artificielle avancée basée sur le **Deep Q-Learning (DQN)**.

---

## Fonctionnalités principales

- Jeu Snake jouable manuellement avec interface graphique moderne.
- Entraînement autonome d'une IA via Deep Q-Learning (DQN).
- Réseau de neurones profond pour la prise de décision, permettant la généralisation.
- Algorithmes avancés incluant *Experience Replay* et *Double DQN*.
- Représentation d'état améliorée avec détection de pièges par BFS ("vision stratégique").
- Sauvegarde automatique du modèle IA (`.pth`) et de l'historique des scores.
- Visualisation graphique de la progression de l’IA (`plot_dqn_progress.py`).
- Lecture des parties jouées par le modèle final de l'IA (`play_dqn_game.py`).
- Arrêt manuel sécurisé pendant l’entraînement avec sauvegarde garantie.
- Structure de projet claire pour une prise en main rapide.

---

## Structure du projet

```text
.
├── assets/                # Ressources graphiques (pomme, police)
│   ├── apple.png
│   └── font.ttf
├── model/                 # Modèles IA sauvegardés (.pth)
├── snake_ia/              # Code source principal
│   ├── __init__.py
│   ├── agent.py           # Logique Deep Q-Learning (Agent DQN)
│   ├── game_objects.py    # Classes Snake et Food
│   ├── model.py           # Architecture du réseau de neurones et Trainer
│   ├── plot_dqn_progress.py # Visualisation graphique des scores
│   ├── play_dqn_game.py   # Lecture des parties de l'IA finale
│   ├── main_nb.py         # Entraînement IA (nombre de parties défini)
│   ├── main_while.py      # Entraînement IA (boucle infinie)
│   ├── plotter.py         # Affichage dynamique des scores
│   └── settings.py        # Paramètres globaux (jeu, IA, chemins)
├── requirements.txt       # Dépendances Python
└── README.md
```
> **NB :** Le dossier `model` est indispensable pour le bon fonctionnement de l’IA.

---

## Installation

1. **Cloner le dépôt**
    ```sh
    git clone https://github.com/DAHORD/Snake_IA.git
    cd Snake_IA
    ```
2. **Installer les dépendances**
    ```sh
    pip install -r requirements.txt
    ```

---

## Utilisation

### 1. Entraîner l’IA

Lancer l'entraînement en boucle infinie (recommandé pour atteindre de hauts scores) :
```sh
python snake_ia/main_while.py
```
- Arrêtez l'entraînement à tout moment via la croix de la fenêtre ou Ctrl+C.
- Le modèle et l'historique des scores sont sauvegardés automatiquement à l'arrêt.

### 2. Visualiser la progression de l’IA

Affichez le graphique des scores à partir du dernier modèle sauvegardé :
```sh
python snake_ia/plot_dqn_progress.py
```

### 3. Regarder l'IA jouer

Lancez une démonstration pour regarder le meilleur modèle jouer :
```sh
# Lance 5 parties de démonstration
python snake_ia/play_dqn_game.py --games 5
```
- `--games` : nombre de parties à jouer (défaut : 3).

---

## Personnalisation & Configuration

- **Paramètres du jeu et de l’IA** : modifiez `snake_ia/settings.py` pour changer le `LEARNING_RATE`, `DISCOUNT_FACTOR`, la taille du réseau (`HIDDEN_LAYER_SIZE`), etc.
- **Chemins des ressources** : adaptez `FONT_PATH`, `FOOD_IMAGE_PATH`, `MODEL_PATH` si besoin.

---

## Dépendances

- pygame
- numpy
- matplotlib
- torch

Installez-les rapidement avec :
```sh
pip install -r requirements.txt
```

---

## Licence

Projet sous licence [Apache 2.0](LICENSE).

---

## Auteur

- [DAHORD](https://github.com/DAHORD)

---

## Contribution & Support

Pour toute question, suggestion ou amélioration, n'hésitez pas à ouvrir une issue ou une pull request. Toute contribution est la bienvenue !

---

Bon jeu et bon apprentissage avec Snake IA ! 🐍🤖
