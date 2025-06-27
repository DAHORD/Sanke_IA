# Snake IA – Jeu Snake avec Intelligence Artificielle (Q-Learning)

![Aperçu du jeu](assets/apple.png)

## Présentation

Ce projet propose une version moderne du jeu Snake, développée en Python avec [pygame](https://www.pygame.org/), enrichie d’une intelligence artificielle basée sur le Q-Learning. Il permet de jouer manuellement, d’entraîner une IA, de visualiser la progression de l’entraînement et de rejouer les parties sauvegardées.

---

## Fonctionnalités

- **Jeu Snake classique** avec interface graphique moderne.
- **Entraînement d’une IA** via Q-Learning (réglable en nombre de parties).
- **Sauvegarde automatique** du modèle IA et de l’historique des scores.
- **Visualisation graphique** de la progression de l’IA (scores, scores moyens).
- **Relecture des parties** jouées par l’IA à partir du modèle sauvegardé.
- **Gestion propre de l’arrêt manuel** lors de l’entraînement.

---

## Structure du projet

```
.
├── assets/                # Ressources graphiques (pomme, police)
│   ├── apple.png
│   └── font.ttf
├── model/                 # Modèles IA sauvegardés (.pkl)
│   └── test_10.pkl
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

---

## Installation

1. **Cloner le dépôt :**
   ```sh
   git clone <url_du_repo>
   cd <nom_du_dossier>
   ```

2. **Installer les dépendances :**
   ```sh
   pip install -r requirements.txt
   ```

3. **Vérifier la présence des ressources :**
   - `assets/apple.png` (image de la pomme)
   - `assets/font.ttf` (police d’écriture)
   - Si besoin, place tes propres fichiers dans le dossier `assets/`.

---

## Utilisation

### 1. Jouer manuellement

Lance le jeu Snake classique :
```sh
python snake_ia/main_game.py
```
- Contrôles : Flèches directionnelles du clavier.
- Appuie sur une touche pour démarrer ou rejouer.

---

### 2. Entraîner l’IA

#### a) Avec un nombre de parties défini (`TOTAL_GAMES_TO_TRAIN` dans `settings.py`)
```sh
python snake_ia/main_nb.py
```
- L’IA s’entraîne pendant le nombre de parties défini.
- Les scores et le modèle sont sauvegardés dans `model/test_10.pkl`.

#### b) En boucle infinie (arrêt manuel)
```sh
python snake_ia/main_while.py
```
- Arrête l’entraînement avec la croix de la fenêtre ou Ctrl+C.

---

### 3. Visualiser la progression de l’IA

Affiche le graphique des scores et scores moyens à partir du modèle sauvegardé :
```sh
python snake_ia/graphic_pkl_ia.py
```

---

### 4. Rejouer les parties sauvegardées par l’IA

Rejoue les parties de l’IA à partir du modèle :
```sh
python snake_ia/games_pkl_ia.py --start 1 --end 10
```
- `--start` : numéro de la première partie à rejouer (défaut : 1)
- `--end` : numéro de la dernière partie à rejouer (défaut : toutes)

---

## Personnalisation

- **Paramètres du jeu et de l’IA** : modifie [`snake_ia/settings.py`](snake_ia/settings.py)
- **Chemins des ressources** : adapte `FONT_PATH`, `FOOD_IMAGE_PATH`, `MODEL_PATH` si besoin.
- **Nombre de parties pour l’entraînement** : change `TOTAL_GAMES_TO_TRAIN`.

---

## Dépendances

- pygame
- numpy
- matplotlib
- pandas

Installe-les avec :
```sh
pip install -r requirements.txt
```

---

## Licence

Ce projet est sous licence [Apache 2.0](LICENSE).

---

## Auteur

- DAHORD

---

## Remarques

- Le modèle IA est sauvegardé dans [`model/test_10.pkl`](model/test_10.pkl) (modifiable dans les paramètres).
- Pour toute question ou amélioration, n’hésite pas à ouvrir une issue ou une pull request.

---

Bon jeu et bon entraînement de ton IA Snake !