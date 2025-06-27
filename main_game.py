# snake_project/main.py

import pygame
import sys
from settings import *
from game_objects import Snake, Food

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Python Snake")
        self.clock = pygame.time.Clock()
        # --- MODIFIÉ : Utilise la police personnalisée ---
        try:
            self.font = pygame.font.Font(FONT_PATH, 36)
        except pygame.error:
            print(f"Police non trouvée à '{FONT_PATH}'. Utilisation de la police par défaut.")
            self.font = pygame.font.Font(None, 36) # Police de secours
        
        self.running = True
        self.score = 0
        self.snake = Snake()
        self.food = Food(self.snake.body)

    # La méthode handle_events et update restent INCHANGÉES.
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(pygame.math.Vector2(0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(pygame.math.Vector2(0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(pygame.math.Vector2(-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(pygame.math.Vector2(1, 0))

    def update(self):
        self.snake.move()
        if self.snake.body[0].colliderect(self.food.pos):
            self.snake.grow_snake()
            self.food.randomize_position(self.snake.body)
            self.score += 1
        head = self.snake.body[0]
        if not (0 <= head.left < SCREEN_WIDTH and 0 <= head.top < SCREEN_HEIGHT):
            self.running = False
        if self.snake.check_collision():
            self.running = False

    # --- MÉTHODE DE DESSIN MODIFIÉE ---
    def draw(self):
        """Dessine tous les éléments, y compris la nouvelle grille de fond."""
        self.screen.fill(BACKGROUND_COLOR)
        self._draw_grid() # Nouvelle méthode pour la grille
        
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        score_text = self.font.render(f"Score: {self.score}", True, (248, 248, 242)) # Couleur de texte claire
        self.screen.blit(score_text, (10, 10))
        
        pygame.display.flip()

    # --- NOUVELLE MÉTHODE PRIVÉE ---
    def _draw_grid(self):
        """Dessine une grille subtile en arrière-plan."""
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

    # La méthode run reste INCHANGÉE.
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(SNAKE_SPEED)
        self.show_game_over()

    def show_game_over(self):
        """Affiche l'écran de fin de partie avec le nouveau design."""
        # --- MODIFIÉ : Utilise la nouvelle police et les couleurs ---
        try:
            game_over_font = pygame.font.Font(FONT_PATH, 72)
            score_font = pygame.font.Font(FONT_PATH, 48)
        except pygame.error:
            game_over_font = pygame.font.Font(None, 72)
            score_font = pygame.font.Font(None, 48)

        game_over_text = game_over_font.render("GAME OVER", True, RED)
        final_score_text = score_font.render(f"Score: {self.score}", True, (248, 248, 242))
        
        # Superposition semi-transparente pour faire ressortir le texte
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150)) # Noir avec 150/255 d'opacité
        self.screen.blit(overlay, (0, 0))

        self.screen.blit(game_over_text, (SCREEN_WIDTH/2 - game_over_text.get_width()/2, SCREEN_HEIGHT/3))
        self.screen.blit(final_score_text, (SCREEN_WIDTH/2 - final_score_text.get_width()/2, SCREEN_HEIGHT/2))
        
        pygame.display.flip()
        pygame.time.wait(3000)

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()