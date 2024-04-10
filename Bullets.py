import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.image = pygame.Surface((5, 5))  # Placeholder image for the bullet
        self.image.fill((255, 0, 0))  # Red color for the bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dx = dx
        self.dy = dy


    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
