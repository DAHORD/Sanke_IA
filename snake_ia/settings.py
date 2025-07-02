# snake_project/settings.py

# -- Chemins des ressources --
FONT_PATH = '../assets/font.ttf'
FOOD_IMAGE_PATH = '../assets/apple.png'
MODEL_PATH = '../model/model_db_q.pth' 

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
SNAKE_SPEED = 1000

# -- Paramètres du Deep Q-Learning (RÉGLÉS POUR LA STABILITÉ) --
HIDDEN_LAYER_SIZE = 256
MAX_MEMORY = 100_000   # Une mémoire un peu plus petite peut aider au début
BATCH_SIZE = 1000
# MODIFIÉ : Taux d'apprentissage plus faible et plus sûr
LEARNING_RATE = 0.001
DISCOUNT_FACTOR = 0.9

# -- Paramètre pour la version avec un nombre de parties défini --
TOTAL_GAMES_TO_TRAIN = 200