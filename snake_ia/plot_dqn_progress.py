# snake_project/plot_dqn_progress.py

import torch
import matplotlib.pyplot as plt
import os
from settings import MODEL_PATH

def plot_training_progress():
    if not os.path.exists(MODEL_PATH):
        print(f"Erreur : Le fichier du modèle '{MODEL_PATH}' est introuvable. Veuillez d'abord entraîner l'IA.")
        return

    try:
        # On utilise torch.load pour lire le fichier .pth
        data = torch.load(MODEL_PATH)
        
        n_games = data.get('n_games', 0)
        scores = data.get('scores_history', [])
        mean_scores = data.get('mean_scores_history', [])

        if not scores:
            print("Aucune donnée de score trouvée dans le modèle.")
            return

        plt.style.use('seaborn-v0_8-darkgrid')
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_title(f'Progression de l\'entraînement DQN ({n_games} parties)')
        ax.set_xlabel('Nombre de Parties')
        ax.set_ylabel('Score')

        ax.plot(scores, label='Score de la partie', alpha=0.5, marker='.', linestyle='None')
        ax.plot(mean_scores, label='Score moyen', color='red', linewidth=2.5)
        
        ax.set_ylim(bottom=0)
        ax.legend(loc='upper left')
        
        print(f"Affichage de la progression pour {n_games} parties.")
        print(f"Meilleur score : {max(scores) if scores else 'N/A'}")
        print(f"Dernier score moyen : {mean_scores[-1]:.2f}" if mean_scores else "N/A")

        plt.show()

    except Exception as e:
        print(f"Une erreur est survenue lors du chargement ou de l'affichage du modèle : {e}")

if __name__ == '__main__':
    plot_training_progress()