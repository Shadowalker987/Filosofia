import pygame
import random
import math

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Título y Icono
pygame.display.set_caption("Juego Complicado")
icon = pygame.image.load('icon.png')  # Debes colocar tu propio icono
pygame.display.set_icon(icon)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Jugador
player_img = pygame.image.load('player.png')  # Coloca tu propio sprite
player_x = screen_width / 2 - 32
player_y = screen_height - 70
player_speed = 5

# Función para dibujar al jugador
def player(x, y):
    screen.blit(player_img, (x, y))

# Enemigos
enemy_img = pygame.image.load('enemy.png')  # Coloca tu propio sprite
num_enemies = 5
enemy_list = []

for i in range(num_enemies):
    enemy_x = random.randint(0, screen_width - 64)
    enemy_y = random.randint(50, 150)
    enemy_speed_x = random.choice([-4, 4])
    enemy_speed_y = 40
    enemy_list.append([enemy_x, enemy_y, enemy_speed_x, enemy_speed_y])

# Función para dibujar a los enemigos
def draw_enemies():
    for enemy in enemy_list:
        screen.blit(enemy_img, (enemy[0], enemy[1]))

# Disparo
bullet_img = pygame.image.load('bullet.png')  # Coloca tu propio sprite
bullet_x = 0
bullet_y = screen_height - 70
bullet_speed = 10
bullet_fired = False

# Función para disparar
def fire_bullet(x, y):
    global bullet_fired
    bullet_fired = True
    screen.blit(bullet_img, (x + 16, y))

# Colisiones
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    return distance < 27

# Puntuación
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def show_score(x, y):
    score_value = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_value, (x, y))

# Juego principal
running = True
while running:
    # Rellenar la pantalla
    screen.fill(BLACK)

    # Eventos del jugador
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - 64:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not bullet_fired:
        bullet_x = player_x
        fire_bullet(bullet_x, bullet_y)

    # Movimiento de la bala
    if bullet_fired:
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_speed

    if bullet_y <= 0:
        bullet_y = screen_height - 70
        bullet_fired = False

    # Movimiento del enemigo
    for enemy in enemy_list:
        enemy[0] += enemy[2]

        if enemy[0] <= 0 or enemy[0] >= screen_width - 64:
            enemy[2] = -enemy[2]
            enemy[1] += enemy[3]

        # Colisión
        if is_collision(enemy[0], enemy[1], bullet_x, bullet_y):
            bullet_y = screen_height - 70
            bullet_fired = False
            score += 1
            enemy[0] = random.randint(0, screen_width - 64)
            enemy[1] = random.randint(50, 150)

        # Dibujar enemigo
        screen.blit(enemy_img, (enemy[0], enemy[1]))

    # Mostrar puntuación
    show_score(10, 10)

    # Dibujar al jugador
    player(player_x, player_y)

    # Actualizar pantalla

