# 🐍 Snake IA

Jeu Snake en Python avec Intelligence Artificielle basée sur le Q-Learning.

## Présentation

Ce projet propose deux modes :
- **Mode Classique** : Jouer au Snake avec les flèches du clavier.
- **Mode IA** : Une IA apprend à jouer au Snake grâce à l’algorithme de Q-Learning.

L’interface graphique est réalisée avec [Pygame](https://www.pygame.org/).
L’IA fonctionne sur des parties enregistrées dans une table `.pkl` (pickle Python).

---

## Nouveautés

- **Lecture et visualisation des parties enregistrées** :
  - `games_pkl_ia.py` permet de lire une table `.pkl` de parties sauvegardées, avec la possibilité de choisir un intervalle de parties à afficher via des paramètres en ligne de commande.
  - `graphic_pkl_ia.py` permet également de visualiser les parties sauvegardées de façon graphique.

---

## Installation

1. **Cloner le dépôt** :
    ```bash
    git clone https://github.com/DAHORD/Sanke_IA.git
    cd Sanke_IA
    ```

2. **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

---

## Utilisation

### Jouer au Snake (mode classique)
```bash
python main_game.py
```

### Lancer l’IA sur un nombre de parties
```bash
python main_nb.py
```
Le nombre de parties est défini dans `settings.py` (variable `TOTAL_GAMES_TO_TRAIN`).

### Visualiser des parties sauvegardées

#### 1. Avec `games_pkl_ia.py`

- **Syntaxe** :
    ```bash
    python games_pkl_ia.py [start] [end]
    ```
    - `start` et `end` : indices des parties à visualiser (optionnels).
    - Exemple pour afficher les parties 10 à 20 :
        ```bash
        python games_pkl_ia.py 10 20
        ```
    - Si aucun paramètre n'est renseigné, toutes les parties sont affichées.

#### 2. Avec `graphic_pkl_ia.py`
```bash
python graphic_pkl_ia.py
```
Affiche graphiquement les parties sauvegardées dans la table `.pkl`.

---

## Structure du projet

```
Sanke_IA/
├── __init__.py
├── main_game.py
├── main_nb.py
├── main_while.py
├── agent.py
├── games_pkl_ia.py         # NOUVEAU : lecture/filtrage des parties .pkl
├── graphic_pkl_ia.py       # NOUVEAU : visualisation graphique des parties .pkl
├── game_objects.py
├── plotter.py
├── settings.py
├── assets/
├── requirements.txt
├── README.md
├── LICENSE
```

---

## Personnalisation

- Change les couleurs, la vitesse ou la taille du plateau dans `settings.py`.
- Améliore l’IA ou crée tes propres environnements !

---

## Crédits

- Réalisé par [DAHORD](https://github.com/DAHORD)
- Basé sur Python, Pygame, Numpy, Matplotlib

---

## Licence

Ce projet est sous licence Apache 2.0 – voir le fichier [LICENSE](LICENSE) pour plus d’informations.