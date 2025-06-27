# snake_project/read_model_pkl.py

import pickle
import matplotlib.pyplot as plt
import os
from settings import MODEL_PATH

def plot_training_progress():
    if not os.path.exists(MODEL_PATH):
        print(f"Erreur : Le fichier du modèle '{MODEL_PATH}' est introuvable. Veuillez d'abord entraîner l'IA.")
        return

    try:
        with open(MODEL_PATH, 'rb') as f:
            data = pickle.load(f)
            
            n_games = data.get('n_games', 0)
            scores = data.get('scores_history', [])
            mean_scores = data.get('mean_scores_history', [])

            if not scores:
                print("Aucune donnée de score trouvée dans le modèle. Assurez-vous que l'entraînement a été exécuté après la mise à jour pour sauvegarder les scores.")
                return

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.set_title(f'Progression de l\'entraînement de l\'IA Snake ({n_games} parties)')
            ax.set_xlabel('Nombre de Parties')
            ax.set_ylabel('Score')

            ax.plot(scores, label='Score de la partie', alpha=0.7)
            ax.plot(mean_scores, label='Score moyen', linewidth=2)
            
            ax.set_ylim(bottom=0)
            ax.legend(loc='upper left')
            
            print(f"Affichage de la progression pour {n_games} parties.")
            print(f"Dernier score : {scores[-1] if scores else 'N/A'}")
            print(f"Dernier score moyen : {mean_scores[-1]:.2f} " if mean_scores else "Dernier score moyen : N/A")

            plt.grid(True)
            plt.show()

    except Exception as e:
        print(f"Une erreur est survenue lors du chargement ou de l'affichage du modèle : {e}")

if __name__ == '__main__':
    plot_training_progress()