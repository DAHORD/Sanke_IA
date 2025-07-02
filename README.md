# 🐍🤖 Snake IA – Jeu Snake avec Intelligence Artificielle (Deep Q-Learning)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange.svg)](https://pytorch.org/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache2.0-yellow.svg)](LICENSE)

---

## Présentation

**Snake IA** est un projet Python qui réinvente le célèbre jeu Snake en y intégrant une intelligence artificielle basée sur le Deep Q-Learning (DQN). Ce projet a pour vocation d’être à la fois un support d’apprentissage pour l’IA de type reinforcement learning et un socle technique robuste pour expérimenter autour de l’automatisation de jeux classiques.

---

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Aperçu visuel](#aperçu-visuel)
- [Architecture du projet](#architecture-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Configuration & Personnalisation](#configuration--personnalisation)
- [Dépendances](#dépendances)
- [Tests & Qualité](#tests--qualité)
- [Roadmap](#roadmap)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Contact](#contact)

---

## Fonctionnalités

- 🎮 Jeu Snake jouable manuellement avec interface graphique moderne (pygame)
- 🤖 Intelligence Artificielle basée sur Deep Q-Learning (DQN)
- 🧠 Réseau de neurones profond pour la prise de décision
- 🌱 Algorithmes avancés : Experience Replay, Double DQN, détection de pièges par BFS
- 💾 Sauvegarde automatique du modèle IA et de l’historique des scores
- 📊 Visualisation graphique de la progression de l’IA
- ▶️ Lecture des parties jouées par le modèle final
- 🛑 Arrêt sécurisé pendant l’entraînement avec sauvegarde garantie
- 🗂️ Structure modulaire et claire du projet

---

## Aperçu visuel

<p align="center">
  <img src="assets/snake_demo.gif" alt="Aperçu du jeu Snake IA" width="500"/>
</p>

---

## Architecture du projet

```text
.
├── assets/                # Ressources graphiques (pomme, police, gifs)
│   ├── apple.png
│   ├── font.ttf
│   └── snake_demo.gif
├── model/                 # Modèles IA sauvegardés (.pth)
├── snake_ia/              # Code source principal
│   ├── __init__.py
│   ├── agent.py           # Logique Deep Q-Learning (Agent DQN)
│   ├── game_objects.py    # Classes Snake et Food
│   ├── model.py           # Architecture du réseau de neurones & Trainer
│   ├── plot_dqn_progress.py # Visualisation graphique des scores
│   ├── play_dqn_game.py   # Lecture des parties de l'IA finale
│   ├── main_nb.py         # Entraînement IA (nombre de parties défini dans settings.py)
│   ├── main_while.py      # Entraînement IA (boucle infinie)
│   ├── plotter.py         # Affichage dynamique des scores
│   └── settings.py        # Paramètres globaux (jeu, IA, chemins)
├── requirements.txt       # Dépendances Python
└── README.md
```
> **Remarque :** Le dossier `model/` est indispensable pour le bon fonctionnement de l’IA.

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

#### a) Pour entraîner l’IA en boucle infinie :
```sh
python snake_ia/main_while.py
```
- Arrêtez l'entraînement à tout moment via la croix de la fenêtre ou Ctrl+C.
- Le modèle et l'historique des scores sont sauvegardés automatiquement à l'arrêt.

#### b) Pour entraîner l’IA sur un nombre défini de parties :
```sh
python snake_ia/main_nb.py
```
- Le nombre de parties à jouer est paramétrable dans `snake_ia/settings.py` (variable `NB_GAMES` par exemple).
- Pratique pour des tests, benchmarks ou pour limiter la durée d’apprentissage.

### 2. Visualiser la progression de l’IA

Pour afficher le graphique des scores :
```sh
python snake_ia/plot_dqn_progress.py
```

### 3. Regarder l'IA jouer

Pour lancer une démonstration :
```sh
python snake_ia/play_dqn_game.py --games 5
```
- `--games` : nombre de parties à jouer (défaut : 3).

---

## Configuration & Personnalisation

- **Paramètres du jeu et de l’IA** : modifiez `snake_ia/settings.py` (`LEARNING_RATE`, `DISCOUNT_FACTOR`, `HIDDEN_LAYER_SIZE`, `NB_GAMES`, etc.).
- **Chemins des ressources** : adaptez `FONT_PATH`, `FOOD_IMAGE_PATH`, `MODEL_PATH` si besoin.
- **Visualisation** : le fichier `plot_dqn_progress.py` permet de suivre l’évolution des performances de l’IA au fil du temps.

---

## Dépendances

- Python 3.8+
- pygame
- numpy
- matplotlib
- torch

Installation rapide :
```sh
pip install -r requirements.txt
```

---

## Tests & Qualité

- Des tests unitaires peuvent être ajoutés dans un dossier `tests/` pour garantir la robustesse du code.
- Suivi des performances et log des scores via les scripts fournis.

---

## Roadmap

- [ ] Ajout d’une interface web (streamlit)
- [ ] Support pour d’autres algorithmes (A3C, PPO…)
- [ ] Tests automatisés et CI/CD
- [ ] Améliorations graphiques (animations, thèmes)
- [ ] Documentation technique détaillée

---

## Contribuer

Les contributions sont les bienvenues !  
Pour proposer une amélioration, ouvrez une [issue](https://github.com/DAHORD/Snake_IA/issues) ou une [pull request](https://github.com/DAHORD/Snake_IA/pulls).

---

## Licence

Projet sous licence [Apache 2.0](LICENSE).

---

## Contact

Créé par [DAHORD](https://github.com/DAHORD)  
Pour toute question ou suggestion : ouvrez une issue ou contactez-moi sur GitHub.

---