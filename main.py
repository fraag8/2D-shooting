import pygame
from Snake import Snake
from Snake import Special_item as SpecialItem
from pygame.time import Clock


pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set up the game objects
background_image = pygame.image.load("G:\\Game\\pythonProject4\\images\\background.jpg.png")
snake = Snake(screen_width // 2, screen_height // 2, "G:\\Game\\pythonProject4\\images\\gus_jpg.png")
special_item = SpecialItem()


# Variables for tracking time
last_spawn_time = pygame.time.get_ticks()
spawn_interval = 5000  # Milliseconds between spawns

# Main game loop
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        snake.dash()


    # Handle other events (like shooting bullets) outside the event loop
    if pygame.mouse.get_pressed()[0]:  # left click
        snake.shoot_bullet(pygame.mouse.get_pos(), special_attack=False)
    elif pygame.mouse.get_pressed()[2]:  # right click
        snake.activate_special_attack()

    # Update and draw
    # (your update and draw logic here)


    # Update
    snake.update()
    snake.bullets.update()  # Update bullet positions

    # Check if it's time to spawn a new special item
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time >= spawn_interval:
        special_item.spawn()
        last_spawn_time = current_time

    # Check for collision between snake and special item
    if snake.rect.colliderect(special_item.rect):
        snake.collect_special_item()
        special_item.spawn()  # Respawn the special item



    # Draw
    screen.blit(background_image, (0, 0))
    screen.blit(snake.image, snake.rect)  # Draw the snake
    screen.blit(special_item.image, special_item.rect)  # draw the special item
    snake.bullets.draw(screen)  # Draw bullets
    pygame.display.flip()

    clock.tick(100)  # Cap the frame rate to 60 FPS

pygame.quit()
