import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of each grid location
grid_size = 20
grid_width = 40
grid_height = 30

# Set the width and height of the game window
window_width = grid_width * grid_size
window_height = grid_height * grid_size

# Set the speed of the snake
snake_speed = 10

# Set the direction of the snake (initially moving right)
snake_x = grid_width // 2 * grid_size
snake_y = grid_height // 2 * grid_size
snake_dx = grid_size
snake_dy = 0

# Set the initial length of the snake
snake_length = 1
snake_body = []

# Generate the initial position of the food
food_x = random.randint(0, grid_width - 1) * grid_size
food_y = random.randint(0, grid_height - 1) * grid_size

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set the game over flag
game_over = False

# Set the score to zero
score = 0

# Set the font for displaying the score
font = pygame.font.SysFont(None, 24)

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy != grid_size:
                snake_dx = 0
                snake_dy = -grid_size
            elif event.key == pygame.K_DOWN and snake_dy != -grid_size:
                snake_dx = 0
                snake_dy = grid_size
            elif event.key == pygame.K_LEFT and snake_dx != grid_size:
                snake_dx = -grid_size
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx != -grid_size:
                snake_dx = grid_size
                snake_dy = 0

    # Update snake position
    snake_x += snake_dx
    snake_y += snake_dy

    # Check for collision with the food
    if snake_x == food_x and snake_y == food_y:
        # Increase the score
        score += 1

        # Generate new position for the food
        food_x = random.randint(0, grid_width - 1) * grid_size
        food_y = random.randint(0, grid_height - 1) * grid_size

        # Increase the length of the snake
        snake_length += 1

    # Check for collision with the walls
    if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height:
        game_over = True

    # Check for collision with the snake's body
    for segment in snake_body:
        if segment[0] == snake_x and segment[1] == snake_y:
            game_over = True

    # Add the current position of the snake to the body
    snake_body.append([snake_x, snake_y])

    # Remove the oldest segments if the snake is longer than its length
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Clear the game window
    window.fill(BLACK)

    # Draw the snake's body
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], grid_size, grid_size))

    # Draw the food
    pygame.draw.rect(window, RED, (food_x, food_y, grid_size, grid_size))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the game display
    pygame.display.update()

    # Set the game speed
    pygame.time.Clock().tick(snake_speed)

# Game over message
game_over_text = font.render("Game Over", True, WHITE)
window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2))
pygame.display.update()

# Wait for 2 seconds before quitting
time.sleep(2)

# Quit the game
pygame.quit()
