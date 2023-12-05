import pygame
import random
import sys

from pygame.locals import *

pygame.init()

# Window parameters
WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змійка")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Block size and speed
BLOCK_SIZE = 20
SPEED = 100  # Increased speed

# Initial snake coordinates and length
snake_x, snake_y = WIDTH // 2, HEIGHT // 2
snake_length = 1
snake_body = [(snake_x, snake_y)]

# Direction
direction = "RIGHT"

# Initial food coordinates
food_x, food_y = (
    random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
    random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
)

#Speed to increase
speed_increase = 1.5

# Font
font = pygame.font.Font(None, 36)

# Function to draw snake and food
def draw_snake(snake_body):
    for i, segment in enumerate(snake_body):
        if i == len(snake_body) - 1:  # Отрисовываем голову змейки
            pygame.draw.rect(WIN, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
            
            # Рисуем глаза на голове змейки
            eye1_x, eye1_y = segment[0] + BLOCK_SIZE // 4, segment[1] + BLOCK_SIZE // 4
            eye2_x, eye2_y = segment[0] + 3 * BLOCK_SIZE // 4, segment[1] + BLOCK_SIZE // 4
            pygame.draw.rect(WIN, WHITE, (eye1_x, eye1_y, BLOCK_SIZE // 4, BLOCK_SIZE // 4))
            pygame.draw.rect(WIN, WHITE, (eye2_x, eye2_y, BLOCK_SIZE // 4, BLOCK_SIZE // 4))
        else:  # Отрисовываем остальные сегменты
            pygame.draw.rect(WIN, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_food(food_x, food_y):
    pygame.draw.rect(WIN, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

def draw_score(score):
    text = font.render("Рахунок: " + str(score), True, WHITE)
    WIN.blit(text, (10, 10))

# Function to update the screen
def update_screen():
    WIN.fill((0, 0, 0))
    
    # Draw snake eyes
    if len(snake_body) > 1:
        eye1_x, eye1_y = snake_body[-1][0] + BLOCK_SIZE // 4, snake_body[-1][1] + BLOCK_SIZE // 4
        eye2_x, eye2_y = snake_body[-1][0] + 3 * BLOCK_SIZE // 4, snake_body[-1][1] + BLOCK_SIZE // 4
        pygame.draw.rect(WIN, WHITE, (eye1_x, eye1_y, BLOCK_SIZE // 4, BLOCK_SIZE // 4))
        pygame.draw.rect(WIN, WHITE, (eye2_x, eye2_y, BLOCK_SIZE // 4, BLOCK_SIZE // 4))
    
    draw_snake(snake_body)
    draw_food(food_x, food_y)
    draw_score(snake_length - 1)
    pygame.display.update()


# Flag to track game over state
game_over = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                if event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                if event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

    if not game_over:
        if direction == "UP":
            snake_y -= BLOCK_SIZE
        if direction == "DOWN":
            snake_y += BLOCK_SIZE
        if direction == "LEFT":
            snake_x -= BLOCK_SIZE
        if direction == "RIGHT":
            snake_x += BLOCK_SIZE

        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            sys.exit()

        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = (
                random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
            )
            snake_length += 1
            SPEED *= speed_increase

        snake_body.append((snake_x, snake_y))
        if len(snake_body) > snake_length:
            del snake_body[0]

        if snake_body.count((snake_x, snake_y)) > 1:
            sys.exit()
    else:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Reset the game
                snake_x, snake_y = WIDTH // 2, HEIGHT // 2
                snake_length = 1
                snake_body = [(snake_x, snake_y)]
                direction = "RIGHT"
                food_x, food_y = (
                    random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE)
                    * BLOCK_SIZE,
                    random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE)
                    * BLOCK_SIZE,
                )
                game_over = False

    update_screen()
    pygame.time.delay(100)

pygame.quit()
sys.exit()
