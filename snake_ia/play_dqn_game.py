# snake_project/play_dqn_game.py (CORRIGÉ)

import pygame
import sys
import argparse
from agent import Agent
# On importe la classe de jeu
from main_while import QuitTraining, SnakeGameAI 

def play_game(agent, num_games):
    game = SnakeGameAI()
    
    for i in range(num_games):
        game.reset()
        done = False
        print(f"\nLancement de la partie de démonstration n°{i + 1}/{num_games}")
        
        while not done:
            try:
                state_old = agent.get_state(game)
                final_move = agent.get_action(state_old, is_playing=True)
                reward, done, score = game.play_step(final_move)

                # MODIFIÉ : On impose une vitesse lente et visible
                game.clock.tick(15)

                if done:
                    print(f"    Fin de la partie. Score final : {score}")
            except (pygame.error, SystemExit, QuitTraining): # Ajout de QuitTraining
                print("Fenêtre de jeu fermée.")
                pygame.quit()
                return

    pygame.quit()
    print("\nDémonstration terminée.")

# Le reste du fichier main() est inchangé
def main():
    parser = argparse.ArgumentParser(description="Regarder l'IA Snake (DQN) jouer avec un modèle sauvegardé.")
    parser.add_argument("--games", type=int, default=3, help="Nombre de parties de démonstration à lancer (par défaut: 3).")
    args = parser.parse_args()
    agent = Agent(load_model=True)
    if not any(p.numel() for p in agent.model.parameters()):
        print("Erreur : Le modèle est vide ou n'a pas pu être chargé.")
        return
    play_game(agent, args.games)

if __name__ == '__main__':
    main()