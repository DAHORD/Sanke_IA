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
        try:
            self.font = pygame.font.Font(FONT_PATH, 36)
        except pygame.error:
            self.font = pygame.font.Font(None, 36)
        self.running = True
        self.score = 0
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.show_menu = True
        self.score_anim_timer = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.show_menu:
                    self.show_menu = False
                else:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(pygame.math.Vector2(0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(pygame.math.Vector2(0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(pygame.math.Vector2(-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(pygame.math.Vector2(1, 0))

    def update(self):
        if self.show_menu:
            return
        self.snake.move()
        if self.snake.body[0].colliderect(self.food.pos):
            self.snake.grow_snake()
            self.food.randomize_position(self.snake.body)
            self.score += 1
            self.score_anim_timer = 10
        head = self.snake.body[0]
        if not (0 <= head.left < SCREEN_WIDTH and 0 <= head.top < SCREEN_HEIGHT):
            self.running = False
        if self.snake.check_collision():
            self.running = False
        if self.score_anim_timer > 0:
            self.score_anim_timer -= 1

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self._draw_grid()
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self._draw_score()
        if self.show_menu:
            self._draw_menu()
        pygame.display.flip()

    def _draw_score(self):
        # Animation du score qui grossit
        size = 36 + (8 if self.score_anim_timer > 0 else 0)
        try:
            font = pygame.font.Font(FONT_PATH, size)
        except pygame.error:
            font = pygame.font.Font(None, size)
        score_text = font.render(f"Score: {self.score}", True, (248, 248, 242))
        self.screen.blit(score_text, (10, 10))

    def _draw_grid(self):
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

    def _draw_menu(self):
        # Menu de démarrage simplifié
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))
        try:
            big_font = pygame.font.Font(FONT_PATH, 64)
            small_font = pygame.font.Font(FONT_PATH, 32)
        except pygame.error:
            big_font = pygame.font.Font(None, 64)
            small_font = pygame.font.Font(None, 32)
        title = big_font.render("SNAKE", True, (0, 230, 150))
        info = small_font.render("Appuie sur une touche pour commencer", True, (230, 230, 230))
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(info, (SCREEN_WIDTH // 2 - info.get_width() // 2, SCREEN_HEIGHT // 2))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(SNAKE_SPEED)
        self.show_game_over()

    def show_game_over(self):
        try:
            game_over_font = pygame.font.Font(FONT_PATH, 72)
            score_font = pygame.font.Font(FONT_PATH, 48)
            restart_font = pygame.font.Font(FONT_PATH, 32)
        except pygame.error:
            game_over_font = pygame.font.Font(None, 72)
            score_font = pygame.font.Font(None, 48)
            restart_font = pygame.font.Font(None, 32)
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))
        game_over_text = game_over_font.render("GAME OVER", True, RED)
        final_score_text = score_font.render(f"Score: {self.score}", True, (248, 248, 242))
        restart_text = restart_font.render("Appuie sur une touche pour rejouer", True, (180, 180, 180))
        self.screen.blit(game_over_text, (SCREEN_WIDTH/2 - game_over_text.get_width()/2, SCREEN_HEIGHT/3))
        self.screen.blit(final_score_text, (SCREEN_WIDTH/2 - final_score_text.get_width()/2, SCREEN_HEIGHT/2))
        self.screen.blit(restart_text, (SCREEN_WIDTH/2 - restart_text.get_width()/2, SCREEN_HEIGHT/2 + 80))
        pygame.display.flip()
        self.wait_for_restart()

    def wait_for_restart(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    waiting = False
        # Reset game state
        self.__init__()
        self.run()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()