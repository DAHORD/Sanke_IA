# snake_project/agent.py

import random
import numpy as np
import pickle
import os
import pygame
from collections import deque
from settings import (BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, MAX_MEMORY, 
                      BATCH_SIZE, LEARNING_RATE, DISCOUNT_FACTOR, MODEL_PATH)

class Agent:
    def __init__(self, load_model=True):
        self.n_games = 0
        self.memory = deque(maxlen=MAX_MEMORY)
        self.gamma = DISCOUNT_FACTOR
        self.epsilon = 1.0 
        self.q_table = {}
        self.scores_history = []  # Nouveau: pour stocker l'historique des scores par partie
        self.mean_scores_history = [] # Nouveau: pour stocker l'historique des scores moyens
        if load_model:
            self.load_model()

    def get_state(self, game):
        head = game.snake.body[0]
        
        point_l = (head.x - BLOCK_SIZE, head.y)
        point_r = (head.x + BLOCK_SIZE, head.y)
        point_u = (head.x, head.y - BLOCK_SIZE)
        point_d = (head.x, head.y + BLOCK_SIZE)
        
        dir_l = game.snake.direction.x == -1
        dir_r = game.snake.direction.x == 1
        dir_u = game.snake.direction.y == -1
        dir_d = game.snake.direction.y == 1

        state = [
            # Danger droit devant
            (dir_r and self._is_collision(point_r, game.snake.body)) or 
            (dir_l and self._is_collision(point_l, game.snake.body)) or 
            (dir_u and self._is_collision(point_u, game.snake.body)) or 
            (dir_d and self._is_collision(point_d, game.snake.body)),

            # Danger à droite (en tournant)
            (dir_u and self._is_collision(point_r, game.snake.body)) or # Si va vers le haut et qu'à droite il y a danger (droite du serpent)
            (dir_d and self._is_collision(point_l, game.snake.body)) or # Si va vers le bas et qu'à gauche il y a danger (gauche du serpent)
            (dir_l and self._is_collision(point_u, game.snake.body)) or # Si va vers la gauche et qu'en haut il y a danger (haut du serpent)
            (dir_r and self._is_collision(point_d, game.snake.body)), # Si va vers la droite et qu'en bas il y a danger (bas du serpent)
            
            # Danger à gauche (en tournant)
            (dir_d and self._is_collision(point_r, game.snake.body)) or # Si va vers le bas et qu'à droite il y a danger (droite du serpent)
            (dir_u and self._is_collision(point_l, game.snake.body)) or # Si va vers le haut et qu'à gauche il y a danger (gauche du serpent)
            (dir_r and self._is_collision(point_u, game.snake.body)) or # Si va vers la droite et qu'en haut il y a danger (haut du serpent)
            (dir_l and self._is_collision(point_d, game.snake.body)), # Si va vers la gauche et qu'en bas il y a danger (bas du serpent)
            
            # Direction actuelle
            dir_l, dir_r, dir_u, dir_d,
            
            # Position de la nourriture relative à la tête
            game.food.pos.x < head.x, # Nourriture à gauche
            game.food.pos.x > head.x, # Nourriture à droite
            game.food.pos.y < head.y, # Nourriture en haut
            game.food.pos.y > head.y  # Nourriture en bas
        ]
        return tuple(state)

    def _is_collision(self, pt, snake_body):
        # Vérifie la collision avec les bords de l'écran
        if pt[0] >= SCREEN_WIDTH or pt[0] < 0 or pt[1] >= SCREEN_HEIGHT or pt[1] < 0:
            return True
        # Vérifie la collision avec le corps du serpent
        test_rect = pygame.Rect(pt[0], pt[1], BLOCK_SIZE, BLOCK_SIZE)
        # On ne teste pas la collision avec la tête elle-même, seulement le reste du corps
        if any(segment.colliderect(test_rect) for segment in snake_body):
            return True
        return False

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        
        # Le déploiement du mini_sample ici est plus clair
        for state, action, reward, next_state, done in mini_sample:
            self.train_short_memory(state, action, reward, next_state, done)

    def train_short_memory(self, state, action, reward, next_state, done):
        # Utilise .get() pour gérer les états non encore présents dans la q_table
        q_values = list(self.q_table.get(state, [0.0, 0.0, 0.0])) # S'assure que les valeurs sont float
        target = reward
        if not done:
            next_q_values = self.q_table.get(next_state, [0.0, 0.0, 0.0]) # S'assure que les valeurs sont float
            target = reward + self.gamma * np.max(next_q_values)
        
        action_index = np.argmax(action)
        q_values[action_index] = (1 - LEARNING_RATE) * q_values[action_index] + LEARNING_RATE * target
        self.q_table[state] = tuple(q_values)

    def get_action(self, state):
        # --- STRATÉGIE D'EPSILON AMÉLIORÉE ---
        # Epsilon va maintenant décroître plus lentement, avec un minimum.
        # Après 500 parties, le taux d'exploration sera d'environ 5%.
        # Vous pouvez ajuster le "500" pour une exploration plus ou moins longue.
        exploration_rate = 1 - (self.n_games / 500)
        self.epsilon = max(0.05, exploration_rate) # Taux d'exploration minimum de 5%

        final_move = [0, 0, 0] # [tout droit, droite, gauche]
        if random.uniform(0, 1) < self.epsilon:
            move_index = random.randint(0, 2) # Action aléatoire (exploration)
        else:
            q_values = self.q_table.get(state, [0.0, 0.0, 0.0]) # Valeurs par défaut si l'état n'existe pas
            move_index = np.argmax(q_values) # Meilleure action connue (exploitation)
        
        final_move[move_index] = 1
        return final_move
        
    def save_model(self, scores=None, mean_scores=None):
        # Utilise les scores et mean_scores passés en paramètre si disponibles,
        # sinon utilise les attributs de l'agent (mis à jour à chaque appel de plot)
        data_to_save = {
            'n_games': self.n_games,
            'q_table': self.q_table,
            'scores_history': scores if scores is not None else self.scores_history,
            'mean_scores_history': mean_scores if mean_scores is not None else self.mean_scores_history
        }
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True) # S'assure que le répertoire existe
        with open(MODEL_PATH, 'wb') as f:
            pickle.dump(data_to_save, f)
        # print(f"Modèle sauvegardé dans {MODEL_PATH}") # Peut être utile pour le débogage

    def load_model(self):
        if os.path.exists(MODEL_PATH):
            try:
                with open(MODEL_PATH, 'rb') as f:
                    data = pickle.load(f)
                    self.n_games = data.get('n_games', 0)
                    self.q_table = data.get('q_table', {})
                    # Charge l'historique des scores, avec une valeur par défaut vide si non présent
                    self.scores_history = data.get('scores_history', []) 
                    self.mean_scores_history = data.get('mean_scores_history', []) 
                    print(f"Modèle chargé : {self.n_games} parties déjà jouées. Q-table contient {len(self.q_table)} états.")
            except (EOFError, pickle.UnpicklingError) as e:
                print(f"Erreur lors du chargement du modèle {MODEL_PATH}: {e}. Le fichier est peut-être corrompu ou vide. Initialisation d'un nouveau modèle.")
                # Réinitialiser les attributs si le chargement échoue
                self.n_games = 0
                self.q_table = {}
                self.scores_history = []
                self.mean_scores_history = []
        else:
            print(f"Aucun modèle trouvé à {MODEL_PATH}. Démarrage d'un nouvel entraînement.")