# snake_project/game_objects.py

import pygame
import random
from settings import *

class Snake:
    def __init__(self):
        self.body = [
            pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(SCREEN_WIDTH // 2 - BLOCK_SIZE, SCREEN_HEIGHT // 2, BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(SCREEN_WIDTH // 2 - 2 * BLOCK_SIZE, SCREEN_HEIGHT // 2, BLOCK_SIZE, BLOCK_SIZE)
        ]
        self.direction = pygame.math.Vector2(1, 0)
        self.grow = False

    def move(self):
        if self.grow:
            new_head = self.body[0].copy()
            new_head.move_ip(self.direction.x * BLOCK_SIZE, self.direction.y * BLOCK_SIZE)
            self.body.insert(0, new_head)
            self.grow = False
        else:
            tail = self.body.pop()
            tail.topleft = self.body[0].topleft + self.direction * BLOCK_SIZE
            self.body.insert(0, tail)

    def change_direction(self, new_direction):
        if new_direction + self.direction != pygame.math.Vector2(0, 0):
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True

    def check_collision(self):
        return self.body[0] in self.body[1:]

    def draw(self, surface):
        head = self.body[0]
        pygame.draw.rect(surface, SNAKE_HEAD_COLOR, head, border_radius=7)
        for segment in self.body[1:]:
            pygame.draw.rect(surface, SNAKE_BODY_COLOR, segment, border_radius=5)
        self._draw_eyes(surface)

    def _draw_eyes(self, surface):
        head = self.body[0]
        eye_size = 3
        if self.direction == pygame.math.Vector2(1, 0):
            eye1_pos = (head.right - eye_size * 2, head.top + eye_size * 2)
            eye2_pos = (head.right - eye_size * 2, head.bottom - eye_size * 2)
        elif self.direction == pygame.math.Vector2(-1, 0):
            eye1_pos = (head.left + eye_size, head.top + eye_size * 2)
            eye2_pos = (head.left + eye_size, head.bottom - eye_size * 2)
        elif self.direction == pygame.math.Vector2(0, 1):
            eye1_pos = (head.left + eye_size * 2, head.bottom - eye_size * 2)
            eye2_pos = (head.right - eye_size, head.bottom - eye_size * 2)
        else: # Vector2(0, -1)
            eye1_pos = (head.left + eye_size * 2, head.top + eye_size)
            eye2_pos = (head.right - eye_size, head.top + eye_size)
        pygame.draw.circle(surface, EYE_COLOR, eye1_pos, eye_size)
        pygame.draw.circle(surface, EYE_COLOR, eye2_pos, eye_size)

class Food:
    def __init__(self, snake_body):
        self.image = pygame.image.load(FOOD_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        self.pos = self.image.get_rect()
        self.randomize_position(snake_body)

    def randomize_position(self, snake_body):
        while True:
            x = random.randrange(0, SCREEN_WIDTH // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randrange(0, SCREEN_HEIGHT // BLOCK_SIZE) * BLOCK_SIZE
            self.pos.topleft = (x, y)
            if not any(segment.colliderect(self.pos) for segment in snake_body):
                break

    def draw(self, surface):
        surface.blit(self.image, self.pos)