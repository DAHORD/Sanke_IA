# snake_project/main.py

import pygame
import sys
import numpy as np
from settings import *
from game_objects import Snake, Food
from agent import Agent
from plotter import Plotter

# NOUVEAU : Une exception personnalisée pour gérer un arrêt propre
class QuitTraining(Exception):
    pass

class SnakeGameAI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("IA Snake")
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
            # MODIFIÉ : On ne quitte plus brutalement. On lève notre exception.
            if event.type == pygame.QUIT:
                raise QuitTraining()
        
        distance_avant = pygame.math.Vector2(self.snake.body[0].center).distance_to(self.food.pos.center)
        self._move(action)
        self.snake.move()
        distance_apres = pygame.math.Vector2(self.snake.body[0].center).distance_to(self.food.pos.center)
        
        game_over = False
        reward = 0
        
        if distance_apres < distance_avant:
            reward = 0.1
        else:
            reward = -0.2

        if self.frame_iteration > 150 * (len(self.snake.body)):
            game_over = True
            reward = -10
        
        if self.snake.body[0].colliderect(self.food.pos):
            self.score += 1
            reward = 10 
            self.snake.grow_snake()
            self.food.randomize_position(self.snake.body)
            self.frame_iteration = 0
        
        if self._is_collision():
            game_over = True
            reward = -10
            
        self._update_ui()
        self.clock.tick(SNAKE_SPEED)
        return reward, game_over, self.score

    def _is_collision(self):
        head = self.snake.body[0]
        if not (0 <= head.left < SCREEN_WIDTH and 0 <= head.top < SCREEN_HEIGHT):
            return True
        if self.snake.check_collision():
            return True
        return False

    def _move(self, action):
        clock_wise = [self.snake.direction, pygame.math.Vector2(self.snake.direction.y, -self.snake.direction.x), pygame.math.Vector2(-self.snake.direction.y, self.snake.direction.x)]
        idx = np.argmax(action)
        new_dir = clock_wise[idx]
        self.snake.change_direction(new_dir)

    def _update_ui(self):
        self.screen.fill(BACKGROUND_COLOR)
        self._draw_grid()
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, (248, 248, 242))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

    def _draw_grid(self):
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def train():
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    plotter = Plotter()
    
    try:
        while agent.n_games < TOTAL_GAMES_TO_TRAIN:
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
                
                if score > record:
                    record = score
                    # Sauvegarde le modèle, les scores et les scores moyens
                    agent.save_model(scores=plotter.scores, mean_scores=plotter.mean_scores) # MODIFIÉ
                
                print(f'Partie {agent.n_games}/{TOTAL_GAMES_TO_TRAIN}, Score: {score}, Record: {record}, Epsilon: {agent.epsilon:.2f}')
                plotter.plot(score)
    
    except QuitTraining:
        print("\nArrêt manuel détecté. Fin de l'entraînement.")
    
    finally:
        print("Sauvegarde finale du modèle en cours...")
        # Sauvegarde finale du modèle, scores et scores moyens
        agent.save_model(scores=plotter.scores, mean_scores=plotter.mean_scores) # MODIFIÉ
        pygame.quit()
        print("Modèle sauvegardé. Programme terminé.")
        import matplotlib.pyplot as plt
        plt.ioff()
        plt.show()

if __name__ == '__main__':
    from settings import TOTAL_GAMES_TO_TRAIN 
    train()