# snake_project/settings.py

# -- Chemins des ressources --
FONT_PATH = '../assets/font.ttf'
FOOD_IMAGE_PATH = '../assets/apple.png'
MODEL_PATH = '../model/q_table_5.pkl'

# -- Dimensions de la fenêtre --
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20

# -- Couleurs (format RGB) --
BACKGROUND_COLOR = (40, 42, 54)
GRID_COLOR = (45, 47, 60)
SNAKE_HEAD_COLOR = (139, 233, 253)
SNAKE_BODY_COLOR = (80, 250, 123)
EYE_COLOR = (255, 255, 255)
RED = (255, 85, 85)

# -- Paramètres du jeu --
SNAKE_SPEED = 20  # Vitesse du jeu (plus élevé = plus rapide)

# -- Paramètres de l'IA (Q-Learning) --
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001
DISCOUNT_FACTOR = 0.9

# NOUVEAU PARAMÈTRE
TOTAL_GAMES_TO_TRAIN = 5