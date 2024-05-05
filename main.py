import pygame
from Snake import Snake
from Bullets import Special_item as SpecialItem
from Enemy import Enemy

pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
# Set up the game objects

background_image = pygame.image.load("G:\\Game\\pythonProject4\\images\\background.jpg.png")
snake = Snake(screen_width // 10, screen_height // 10, "G:\\Game\\pythonProject4\\images\\dude2.png")
enemy_image = pygame.image.load("G:\\Game\\pythonProject4\\images\\fish_png.png").convert_alpha()
enemy = Enemy(screen_width // 10, screen_height // 10, enemy_image)
special_item = SpecialItem()

scaled_snake = pygame.transform.scale(snake.image, (48, 60))
snake.image = scaled_snake

red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)


def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, white, (x - 5, y - 5, 410, 40))
    pygame.draw.rect(screen, red, (x, y, 400, 30))
    pygame.draw.rect(screen, yellow, (x, y, 400 * ratio, 30))


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

    # Check for key presses snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        snake.dash()

    # enemy
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_ENTER]:
        enemy.dash()

        # Handle other events (like shooting bullets) outside the event loop
    if pygame.mouse.get_pressed()[0]:  # left click
        snake.shoot_bullet(pygame.mouse.get_pos(), special_attack=False)
    elif pygame.mouse.get_pressed()[2]:  # right click
        snake.activate_special_attack()

    for obj in (snake, enemy):
        if obj.rect.colliderect(special_item.rect):
            obj.collect_special_item()
            special_item.spawn()
            break

        # Check if it's time to spawn a new special item
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time >= spawn_interval:
            special_item.spawn()
            last_spawn_time = current_time

    for snake_bullet in snake.bullets:  # Loop through snake`s bullets
        if enemy.rect.colliderect(snake_bullet.rect):
            # Snake bullet hit enemy
            snake_bullet.kill()  # Remove the bullet
            enemy.kill()
            enemy.health -= 1
            print('enemy dead!')

    for enemy_bullet in enemy.bullets:
        if snake.rect.colliderect(enemy_bullet.rect):
            enemy_bullet.kill()
            snake.kill()
            snake.health -= 1
            print('snake dead')

    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))

    # Update
    snake.update()
    enemy.update({keys})
    snake.bullets.update()  # Update bullet positions
    enemy.bullets.update()

    screen.blit(snake.image, snake.rect)  # Draw the snake

    current_animation_surface = enemy.draw(screen)
    screen.blit(current_animation_surface, enemy.rect)
    screen.blit(special_item.image, special_item.rect)  # draw the special item
    snake.bullets.draw(screen)  # Draw bullets
    enemy.bullets.draw(screen)
    draw_health_bar(snake.health, 20, 20)
    draw_health_bar(enemy.health, 580, 20)
    screen.blit(scaled_snake, snake.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
