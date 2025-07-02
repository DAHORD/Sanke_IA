# 🐍🤖 Snake IA – Jeu Snake avec Intelligence Artificielle (Deep Q-Learning)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange.svg)](https://pytorch.org/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache2.0-yellow.svg)](LICENSE)

## Présentation

**Snake IA** est une version moderne du jeu Snake développée en Python avec [pygame](https://www.pygame.org/), intégrant une intelligence artificielle avancée basée sur le **Deep Q-Learning (DQN)** avec **PyTorch**. Ce projet illustre l'apprentissage par renforcement profond appliqué à un jeu classique, en visant des performances élevées et une qualité de code professionnelle.

---

## Fonctionnalités principales

-   **Jeu Snake jouable manuellement** avec interface graphique moderne.
-   **Entraînement autonome d'une IA** via Deep Q-Learning (DQN).
-   **Réseau de neurones profonds** pour la prise de décision, permettant la généralisation.
-   **Algorithmes avancés** incluant *Experience Replay* et *Double DQN* pour un apprentissage stable et efficace.
-   **Représentation d'état améliorée** avec détection de pièges par BFS ("vision stratégique").
-   **Sauvegarde automatique** du modèle IA (`.pth`) et de l'historique complet des scores.
-   **Visualisation graphique** de la progression de l’IA (`plot_dqn_progress.py`).
-   **Lecture des parties** jouées par le modèle final de l'IA (`play_dqn_game.py`).
-   **Arrêt manuel sécurisé** pendant l’entraînement avec sauvegarde garantie.
-   **Structure de projet claire** pour une prise en main et une expérimentation rapides.

---

## Structure du projet
