# snake_project/play_saved_games.py

import pygame
import sys
import numpy as np
import pickle
import os
import argparse # Pour la gestion des arguments de ligne de commande

from settings import *
from main_nb import SnakeGameAI  # Import de la classe de jeu principale
from game_objects import Snake, Food
from agent import Agent

class SnakeGameReplay(SnakeGameAI): # Hérite de votre classe existante pour réutiliser le code de jeu
    def __init__(self, agent_instance):
        super().__init__()
        self.agent = agent_instance # Utilise l'agent chargé
        self.n_current_game = 0 # Pour suivre la partie en cours de relecture

    def run_replay(self, start_game, end_game):
        if not self.agent.q_table:
            print("Erreur : La Q-table n'est pas chargée. Impossible de rejouer des parties.")
            return

        total_games_loaded = self.agent.n_games if hasattr(self.agent, 'n_games') else 0

        # Ajuste l'intervalle si nécessaire
        start_game = max(1, start_game)
        end_game = min(total_games_loaded, end_game)
        
        if start_game > end_game:
            print(f"L'intervalle spécifié ({start_game}-{end_game}) est invalide.")
            return

        print(f"\nRelecture des parties de l'IA de {start_game} à {end_game}...")

        # Désactive l'exploration pour la relecture (comportement déterministe)
        original_epsilon = self.agent.epsilon
        self.agent.epsilon = 0.0

        game_counter = 0
        while game_counter < end_game:
            if self.n_current_game >= start_game -1 : # n_current_game est 0-indexé
                game_counter += 1
                print(f"Relecture de la partie {game_counter}...")
                self.reset()
                done = False
                while not done:
                    state_old = self.agent.get_state(self)
                    final_move = self.agent.get_action(state_old) # L'action est déterminée par la Q-table
                    
                    # Permet de quitter pendant la relecture
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    # Simule un pas de jeu, mais sans entraînement
                    reward, done, score = self.play_step(final_move)
                    
                    # La relecture s'arrête si la partie est terminée
                    if done:
                        print(f"    Fin de la partie {game_counter}. Score: {score}")
                        break
            
            # Passe à la partie suivante dans la logique de l'agent
            self.n_current_game += 1
            if self.n_current_game >= end_game:
                break


        # Restaure l'epsilon si vous prévoyez de réutiliser l'agent ailleurs
        self.agent.epsilon = original_epsilon 
        pygame.quit()
        print("\nRelecture terminée.")

def main():
    parser = argparse.ArgumentParser(description="Rejouer les parties de l'IA Snake en utilisant un modèle Q-learning sauvegardé.")
    parser.add_argument("--start", type=int, default=1, 
                        help="Numéro de la première partie à rejouer (par défaut: 1).")
    parser.add_argument("--end", type=int, default=None,
                        help="Numéro de la dernière partie à rejouer (par défaut: toutes les parties du modèle).")
    
    args = parser.parse_args()

    # Initialise l'agent en chargeant le modèle
    agent = Agent(load_model=True)
    if not agent.q_table:
        print("Avertissement : Le modèle n'a pas pu être chargé ou est vide. Assurez-vous que le chemin MODEL_PATH est correct et que le fichier .pkl existe.")
        print("Veuillez d'abord entraîner l'IA pour créer ou mettre à jour le modèle.")
        return

    game_replay = SnakeGameReplay(agent)

    # Si 'end' n'est pas spécifié, rejoue jusqu'à la dernière partie connue
    if args.end is None:
        args.end = agent.n_games

    game_replay.run_replay(args.start, args.end)

if __name__ == '__main__':
    # Nous importons SnakeGameAI ici pour éviter une dépendance circulaire si elle n'est pas nécessaire
    # pour read_model_pkl.py
    from main_nb import SnakeGameAI 
    main()