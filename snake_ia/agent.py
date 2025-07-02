# snake_project/agent.py

import torch
import random
import numpy as np
from collections import deque
import os
from settings import *
from model import Linear_QNet, QTrainer

# On passe à un état plus complexe
STATE_SIZE = 14
ACTION_SIZE = 3

class Agent:
    def __init__(self, load_model=True):
        self.n_games = 0
        self.epsilon = 0
        self.scores_history = []
        self.mean_scores_history = []
        self.memory = deque(maxlen=MAX_MEMORY)
        
        self.model = Linear_QNet(STATE_SIZE, HIDDEN_LAYER_SIZE, ACTION_SIZE)
        self.target_model = Linear_QNet(STATE_SIZE, HIDDEN_LAYER_SIZE, ACTION_SIZE)
        
        self.trainer = QTrainer(self.model, self.target_model, lr=LEARNING_RATE, gamma=DISCOUNT_FACTOR)

        if load_model:
            self.load_model()
            self.target_model.load_state_dict(self.model.state_dict())
        
        self.target_model.eval()

    def find_safe_path_bfs(self, game, start_pos):
        q = deque([start_pos])
        visited = {start_pos}
        count = 0
        while q:
            count += 1
            # Si on trouve un espace suffisamment grand, on considère le chemin sûr
            if count > len(game.snake.body) + 2:
                return True
            x, y = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_pos = (x + dx * BLOCK_SIZE, y + dy * BLOCK_SIZE)
                if next_pos not in visited and not game._is_collision(next_pos):
                    visited.add(next_pos)
                    q.append(next_pos)
        return False

    def get_state(self, game):
        head = game.snake.body[0]
        point_l = (head.x - BLOCK_SIZE, head.y); point_r = (head.x + BLOCK_SIZE, head.y)
        point_u = (head.x, head.y - BLOCK_SIZE); point_d = (head.x, head.y + BLOCK_SIZE)
        dir_l = game.snake.direction.x == -1; dir_r = game.snake.direction.x == 1
        dir_u = game.snake.direction.y == -1; dir_d = game.snake.direction.y == 1

        # Mouvements relatifs
        dir_vec = game.snake.direction
        move_straight = (head.x + dir_vec.x * BLOCK_SIZE, head.y + dir_vec.y * BLOCK_SIZE)
        move_right = (head.x + dir_vec.y * BLOCK_SIZE, head.y - dir_vec.x * BLOCK_SIZE)
        move_left = (head.x - dir_vec.y * BLOCK_SIZE, head.y + dir_vec.x * BLOCK_SIZE)

        state = [
            # Dangers immédiats
            (dir_r and game._is_collision(point_r)) or (dir_l and game._is_collision(point_l)) or (dir_u and game._is_collision(point_u)) or (dir_d and game._is_collision(point_d)),
            (dir_u and game._is_collision(point_r)) or (dir_d and game._is_collision(point_l)) or (dir_l and game._is_collision(point_u)) or (dir_r and game._is_collision(point_d)),
            (dir_d and game._is_collision(point_r)) or (dir_u and game._is_collision(point_l)) or (dir_r and game._is_collision(point_u)) or (dir_l and game._is_collision(point_d)),
            # Direction du mouvement
            dir_l, dir_r, dir_u, dir_d,
            # Position de la nourriture
            game.food.pos.x < head.x, game.food.pos.x > head.x,
            game.food.pos.y < head.y, game.food.pos.y > head.y,
            # Vision stratégique (détection de pièges)
            not self.find_safe_path_bfs(game, move_straight),
            not self.find_safe_path_bfs(game, move_right),
            not self.find_safe_path_bfs(game, move_left),
        ]
        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE: mini_sample = random.sample(self.memory, BATCH_SIZE)
        else: mini_sample = self.memory
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(np.array(states), np.array(actions), np.array(rewards), np.array(next_states), np.array(dones))

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state, is_playing=False):
        self.epsilon = 80 - self.n_games
        final_move = [0, 0, 0]
        if is_playing or random.randint(0, 200) < self.epsilon:
            move_index = random.randint(0, 2)
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move_index = torch.argmax(prediction).item()
        final_move[move_index] = 1
        return final_move

    def save_model(self, scores=None, mean_scores=None):
        data_to_save = {'model_state_dict': self.model.state_dict(), 'n_games': self.n_games, 'scores_history': scores, 'mean_scores_history': mean_scores}
        self.model.save(data_to_save)

    def load_model(self):
        if not os.path.exists(MODEL_PATH): print("Aucun modèle trouvé."); return
        try:
            data = torch.load(MODEL_PATH)
            self.model.load_state_dict(data['model_state_dict'])
            self.n_games = data.get('n_games', 0)
            self.scores_history = data.get('scores_history', [])
            self.mean_scores_history = data.get('mean_scores_history', [])
            print(f"Modèle chargé : {self.n_games} parties déjà jouées.")
        except Exception as e: print(f"Erreur lors du chargement du modèle : {e}.")