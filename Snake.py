import random
import pygame
from Bullets import Bullet
from pygame.time import Clock


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
clock = Clock


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed=2):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.dx = 0  # Horizontal velocity
        self.dy = 0  # Vertical velocity
        self.special_attack_available = False
        self.bullets = pygame.sprite.Group()
        self.dash_distance = 10
        self.cooldown_time = 0
        self.cooldown_duration = 0

    def update(self):
        keys = pygame.key.get_pressed()  # get the current state of the keyboard
        # update the snake velocity based on the pressed keys
        if keys[pygame.K_w]:
            self.dx = 0
            self.dy = -self.speed
        elif keys[pygame.K_s]:
            self.dx = 0
            self.dy = self.speed
        elif keys[pygame.K_a]:
            self.dx = -self.speed
            self.dy = 0
        elif keys[pygame.K_d]:
            self.dx = self.speed
            self.dy = 0
            # if no keys are pressed, stop the snake
        else:
            self.dx = 0
            self.dy = 0

        # Update the snake's position
        self.rect.x += self.dx
        self.rect.y += self.dy

        # keep the snake within the screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def dash(self):
        if self.cooldown_time <= 0:  # Check if dash is ready
            pressed_keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if pressed_keys[pygame.K_a]:
                dx = -self.dash_distance
            elif pressed_keys[pygame.K_d]:
                dx = self.dash_distance
            if pressed_keys[pygame.K_w]:
                dy = -self.dash_distance
            elif pressed_keys[pygame.K_s]:
                dy = self.dash_distance

            # Perform the dash
            self.rect.x += dx
            self.rect.y += dy

            # Set flag after a successful dash (assuming timer is in the snake object)
            self.cooldown_time = self.cooldown_duration
            self.dash_available = True  # Set flag back to True after dash

            # Keep the snake within the screen boundaries after the dash
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

            self.cooldown_time = self.cooldown_duration  # Start cooldown after a dash




    def shoot_bullet(self, mouse_pos, special_attack=False):
        if not special_attack:   # Placeholder for creating a regular bullet at the snake's position
            bullet = Bullet(self.rect.centerx, self.rect.centery, 0, -5)  # Example: Bullet moving  upwards
            self.bullets.add(bullet)  # Add the bullet to the bullets group
            print("Shooting regular bullet towards position:", mouse_pos)
        else:
            if self.special_attack_available:
                print("Performing special attack at position:", mouse_pos)
                # Add special attack logic here
                self.special_attack_available = False
            else:
                print("Special attack not available")

    def collect_special_item(self):
        self.special_attack_available = True
        print("Special item collected")

    def activate_special_attack(self):
        if self.special_attack_available:
            self.shoot_bullet(self.rect.center, special_attack=True)
            print("Special attack activated")
        else:
            print("Special attack not available")


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

    return False  # No collision


