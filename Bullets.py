import pygame
import random


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.image = pygame.Surface((5, 5))  # Placeholder image for the bullet
        self.image.fill((255, 0, 0))  # Red color for the bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dx = dx
        self.dy = dy
        self.enemy = pygame.sprite.Group()
        self.snake = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def check_collision(self, bullets, enemy, snake):
        # Iterate over each bullet in the bullets group
        for bullet in bullets:
            # Check if the enemy's rect collides with the bullet's rect
            if self.rect.colliderect(bullet.rect):
                enemy.kill()
                snake.kill()
                # Perform actions when collision occurs
                self.kill()  # Destroy the enemy
                bullet.kill()  # Destroy the bullet


class Special_item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # create a placeholder image for the special item
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.x = random.randint(0, 780)  # adjust the range according to the screen size
        self.rect.y = random.randint(0, 580)


def check_collision(self, screen_width, screen_height):
    # ... (existing collision logic for top and bottom walls)

    # Check for collisions with left and right edges
    if self.rect.left < 0 or self.rect.right > screen_width:
        # Handle the collision (e.g., stop movement, bounce back)
        return True  # Indicate collision

    return False   # No collision