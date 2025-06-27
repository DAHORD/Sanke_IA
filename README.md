# 🐍 Snake IA

Jeu Snake en Python avec Intelligence Artificielle basée sur le Q-Learning.

## Présentation

Ce projet propose deux modes :
- **Mode Classique** : Joue au Snake avec les flèches du clavier.
- **Mode IA** : Une IA apprend automatiquement à jouer au Snake grâce à l’algorithme de Q-Learning.

L’interface graphique est réalisée avec [Pygame](https://www.pygame.org/).  
L’IA peut être entraînée sur un nombre défini de parties.

---

## Démonstration

<img src="https://user-images.githubusercontent.com/your_screenshot.gif" alt="Demo GIF" width="400"/>

---

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/DAHORD/Sanke_IA.git
   cd Sanke_IA
   ```

2. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

---

## Utilisation

### Jouer au Snake (mode classique)

```bash
python main_game.py
```
- Contrôles : Flèches du clavier pour diriger le serpent.

### Entraîner l’IA sur un nombre de parties

```bash
python main_nb.py
```
- Le nombre de parties est défini dans `settings.py` (`TOTAL_GAMES_TO_TRAIN`).
- À la fin de l’entraînement, le modèle est sauvegardé (ex : `model.pkl`).

### Entraîner l’IA en boucle infinie

```bash
python main_while.py
```
- L’IA joue indéfiniment jusqu’à arrêt manuel.

---

## Structure du projet

```
.
Sanke_IA/
├── sanke_ia/
│   ├── __init__.py
│   ├── main_game.py
│   ├── main_nb.py
│   ├── main_while.py
│   ├── agent.py
│   ├── game_objects.py
│   ├── plotter.py
│   ├── settings.py
├── assets/
│   └── (images, polices, etc.)
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Personnalisation

- Change les couleurs, la vitesse ou la taille du plateau dans `settings.py`.
- Améliore le design du Snake et du jeu selon tes envies !

---

## Crédits

- Réalisé par [DAHORD](https://github.com/DAHORD)
- Basé sur Pygame, Numpy, Matplotlib

---

## Licence

Ce projet est sous licence Apache 2.0 – voir [LICENSE](LICENSE) pour plus d’informations.