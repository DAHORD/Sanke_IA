# snake_project/agent.py

import random
import numpy as np
import pickle
import os
from collections import deque
# Importations corrigées et complètes
from settings import (BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, MAX_MEMORY, 
                      BATCH_SIZE, LEARNING_RATE, DISCOUNT_FACTOR, MODEL_PATH)

class Agent:
    def __init__(self, load_model=True):
        self.n_games = 0
        self.memory = deque(maxlen=MAX_MEMORY)
        self.gamma = DISCOUNT_FACTOR
        self.epsilon = 0
        self.q_table = {}
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
            (dir_r and self._is_collision(point_r, game.snake.body)) or 
            (dir_l and self._is_collision(point_l, game.snake.body)) or 
            (dir_u and self._is_collision(point_u, game.snake.body)) or 
            (dir_d and self._is_collision(point_d, game.snake.body)),
            (dir_u and self._is_collision(point_r, game.snake.body)) or 
            (dir_d and self._is_collision(point_l, game.snake.body)) or 
            (dir_l and self._is_collision(point_u, game.snake.body)) or 
            (dir_r and self._is_collision(point_d, game.snake.body)),
            (dir_d and self._is_collision(point_r, game.snake.body)) or 
            (dir_u and self._is_collision(point_l, game.snake.body)) or 
            (dir_r and self._is_collision(point_u, game.snake.body)) or 
            (dir_l and self._is_collision(point_d, game.snake.body)),
            dir_l, dir_r, dir_u, dir_d,
            game.food.pos.x < head.x,
            game.food.pos.x > head.x,
            game.food.pos.y < head.y,
            game.food.pos.y > head.y
        ]
        return tuple(state)

    def _is_collision(self, pt, snake_body):
        # Utilise les constantes importées de settings.py
        if pt[0] >= SCREEN_WIDTH or pt[0] < 0 or pt[1] >= SCREEN_HEIGHT or pt[1] < 0:
            return True
        # Crée un Rect temporaire pour le point à tester
        test_rect = pygame.Rect(pt[0], pt[1], BLOCK_SIZE, BLOCK_SIZE)
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
        for state, action, reward, next_state, done in mini_sample:
            self.train_short_memory(state, action, reward, next_state, done)

    def train_short_memory(self, state, action, reward, next_state, done):
        q_values = list(self.q_table.get(state, [0, 0, 0]))
        target = reward
        if not done:
            next_q_values = self.q_table.get(next_state, [0, 0, 0])
            target = reward + self.gamma * np.max(next_q_values)
        
        action_index = np.argmax(action)
        q_values[action_index] = (1 - LEARNING_RATE) * q_values[action_index] + LEARNING_RATE * target
        self.q_table[state] = tuple(q_values)

    def get_action(self, state):
        self.epsilon = 80 - self.n_games
        final_move = [0, 0, 0]
        if random.randint(0, 200) < self.epsilon:
            move_index = random.randint(0, 2)
        else:
            q_values = self.q_table.get(state, [0, 0, 0])
            move_index = np.argmax(q_values)
        final_move[move_index] = 1
        return final_move
        
    def save_model(self):
        with open(MODEL_PATH, 'wb') as f:
            pickle.dump({'n_games': self.n_games, 'q_table': self.q_table}, f)

    def load_model(self):
        if os.path.exists(MODEL_PATH):
            with open(MODEL_PATH, 'rb') as f:
                data = pickle.load(f)
                self.n_games = data['n_games']
                self.q_table = data['q_table']
                print(f"Modèle chargé : {self.n_games} parties déjà jouées.")

# Il faut importer pygame ici pour que la classe Agent puisse l'utiliser sans planter
import pygame