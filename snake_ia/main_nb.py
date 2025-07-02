# snake_project/main_while.py (CORRIGÉ)

import pygame
import sys
import numpy as np
from settings import *
from game_objects import Snake, Food
from agent import Agent
from plotter import Plotter

class QuitTraining(Exception):
    pass

class SnakeGameAI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("IA Snake - DQN (Stable)")
        self.clock = pygame.time.Clock()
        try:
            self.font = pygame.font.Font(FONT_PATH, 24)
        except pygame.error:
            self.font = pygame.font.Font(None, 24)
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.score = 0
        self.frame_iteration = 0

    def play_step(self, action):
        self.frame_iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise QuitTraining()
        self._move(action)
        self.snake.move()
        
        game_over = False
        # Récompense simple et claire
        reward = 0 
        
        if self._is_collision():
            game_over = True
            reward = -10
            return reward, game_over, self.score
            
        if self.snake.body[0].colliderect(self.food.pos):
            self.score += 1
            reward = 10 # Récompense fixe et forte
            self.snake.grow_snake()
            self.food.randomize_position(self.snake.body)
            self.frame_iteration = 0
            
        # Pénalité si l'IA tourne en rond trop longtemps
        if self.frame_iteration > 100 * (len(self.snake.body) + 1):
             game_over = True
             reward = -10

        self._update_ui()
        self.clock.tick(SNAKE_SPEED)
        return reward, game_over, self.score

    def _is_collision(self, pt=None):
        if pt is None: pt_rect = self.snake.body[0]
        else: pt_rect = pygame.Rect(pt[0], pt[1], BLOCK_SIZE, BLOCK_SIZE)
        if pt_rect.left < 0 or pt_rect.right > SCREEN_WIDTH or pt_rect.top < 0 or pt_rect.bottom > SCREEN_HEIGHT: return True
        if pt is None and self.snake.check_collision(): return True
        if pt is not None and any(segment.colliderect(pt_rect) for segment in self.snake.body): return True
        return False

    def _move(self, action):
        clock_wise = [self.snake.direction, pygame.math.Vector2(self.snake.direction.y, -self.snake.direction.x), pygame.math.Vector2(-self.snake.direction.y, self.snake.direction.x)]
        idx = np.argmax(action)
        self.snake.change_direction(clock_wise[idx])

    def _update_ui(self):
        self.screen.fill(BACKGROUND_COLOR)
        self._draw_grid()
        self.snake.draw(self.screen); self.food.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, (248, 248, 242))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

    def _draw_grid(self):
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE): pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE): pygame.draw.line(self.screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def train():
    agent = Agent()
    plotter = Plotter()
    if agent.scores_history:
        plotter.scores = agent.scores_history; plotter.mean_scores = agent.mean_scores_history
        plotter.total_score = sum(agent.scores_history)
        record = max(agent.scores_history) if agent.scores_history else 0
        print(f"Reprise de l'entraînement. Record précédent : {record}")
    else: record = 0
    
    game = SnakeGameAI()
    
    try:
        while   agent.n_games < TOTAL_GAMES_TO_TRAIN:
            state_old = agent.get_state(game)
            final_move = agent.get_action(state_old)
            reward, done, score = game.play_step(final_move)
            state_new = agent.get_state(game)
            agent.train_short_memory(state_old, final_move, reward, state_new, done)
            agent.remember(state_old, final_move, reward, state_new, done)
            
            if done:
                game.reset()
                agent.n_games += 1
                agent.train_long_memory()

                # Mise à jour du réseau cible (target network) toutes les C parties
                if agent.n_games % 10 == 0:
                    agent.target_model.load_state_dict(agent.model.state_dict())
                    print("Réseau cible mis à jour.")

                if score > record: record = score
                
                plotter.plot(score)
                print(f'Partie {agent.n_games}/{TOTAL_GAMES_TO_TRAIN}, Score: {score}, Record: {record}, Epsilon: {max(0, 80 - agent.n_games)}')
                agent.save_model(scores=plotter.scores, mean_scores=plotter.mean_scores)
    
    except QuitTraining: print("\nArrêt manuel détecté.")
    finally:
        print("Sauvegarde finale...")
        agent.save_model(scores=plotter.scores, mean_scores=plotter.mean_scores)
        pygame.quit()
        print("Modèle sauvegardé.")
        import matplotlib.pyplot as plt
        plt.ioff()
        plt.show()

if __name__ == '__main__':
    train()