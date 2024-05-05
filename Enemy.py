import pygame
from pythonProject4.Bullets import Bullet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed=2):
        super().__init__()
        self.animation_frames_width = 30
        self.num_frames_per_direction = 3
        self.image = pygame.image.load("G\\Game\\pythonProject4\\images\\fish_png.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image = image
        self.speed = speed
        self.animation_frame_width = 30  # Adjust frame width based on your image
        self.animation_frame_height = 30
        self.dx = 0
        self.dy = 0
        self.direction = "down"
        self.bullets = pygame.sprite.Group
        self.dash_distance = 10
        self.cooldown_time = 0
        self.controls = {}
        self.aim_direction = (0, 0)
        self.dash_available = True
        self.centerx = 0
        self.bullets = pygame.sprite.Group()
        self.special_attack_available = False
        self.health = 100
        self.current_frame = 0
        self.animation_frames = {}
        self.animation_frames_per_direction = self.image.get_width() // self.animation_frames_width
        self.load_animation_frames()

    def draw(self, screen):
        frame_x = self.current_frame % self.num_frames_per_direction * self.animation_frame_width
        frame_y = self.animation_frame_height * (
            0 if self.direction == "down" else 1  # Adjust for up/down directions
        )
        subsurface = self.image.subsurface(
            (frame_x, frame_y, self.animation_frame_width, self.animation_frame_height)
        )
        screen.blit(subsurface, self.rect)

    def load_animation_frames(self):
        self.image = pygame.image.load(self.image).convert_alpha()
        frame_width = self.animation_frame_width
        frame_height = self.animation_frame_height
        num_frames_per_direction = self.image.get_rect().width // frame_width

        for direction in ("up", "down", "left", "right"):
            start_index = (self.animation_frames.get(direction, 0) * frame_width)
            self.animation_frames[direction] = []
            for i in range(self.image.get_width() // frame_width):
                frame_rect = pygame.Rect(start_index, 0, frame_width, frame_height)
                frame_surface = self.image.subsurface(frame_rect)
                self.animation_frames[direction].append(frame_surface)
                start_index += 1

        self.rect = self.animation_frames["down"][0].get_rect()
        self.rect.centerx = 0

    def update(self, keys):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.dx = 0
            self.dy = -self.speed
            self.direction = "up"
        elif keys[pygame.K_DOWN]:
            self.dx = 0
            self.dy = self.speed
            self.direction = "down"
        elif keys[pygame.K_LEFT]:
            self.dx = -self.speed
            self.dy = 0
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            self.dx = self.speed
            self.dy = 0
            self.direction = "right"
        else:
            self.dx = 0
            self.dy = 0

        self.current_frame = (self.current_frame + 1) % len(self.animation_frames[self.direction])

        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            # get the current state of the keyboard

        direction_x = 0
        direction_y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP8]:
            direction_y = -1  # Up arrow pressed, shoot upwards
        elif keys[pygame.K_KP2]:
            direction_y = 1  # Down arrow pressed, shoot downwards
        elif keys[pygame.K_KP4]:
            direction_x = -1  # Left arrow pressed, shoot leftwards
        elif keys[pygame.K_KP6]:
            direction_x = 1  # Right arrow pressed, shoot rightwards

            # Create bullet with the calculated direction (if any key is pressed)
        if direction_x != 0 or direction_y != 0:
            bullet = Bullet(self.rect.centerx, self.rect.centery, direction_x, direction_y)
            self.bullets.add(bullet)

    def dash(self):
        if self.cooldown_time <= 0:
            pressed_keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if pressed_keys[pygame.K_LEFT]:
                dx = -self.dash_distance
            elif pressed_keys[pygame.K_RIGHT]:
                dx = self.dash_distance
            if pressed_keys[pygame.K_UP]:
                dy = -self.dash_distance
            elif pressed_keys[pygame.K_DOWN]:
                dy = self.dash_distance

            self.rect.x += dx
            self.rect.y += dy

            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

            self.cooldown_time = self.cooldown_time
            self.dash_available = True

    def can_shoot(self, direction_x, direction_y, special_attack=False):
        # Create bullet with the calculated direction (if any key is pressed
        bullet: Bullet = Bullet(self.rect.centerx, self.rect.centery, direction_x, direction_y)
        self.bullets.add(bullet)

    def collect_special_item(self):
        self.special_attack_available = True
        print("enemy collected ")


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

