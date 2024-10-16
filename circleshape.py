import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def check_collision(self, other):
        dist_vec = self.position - other.position
        dist = (dist_vec.x**2 + dist_vec.y**2)**0.5
        return dist <= (self.radius + other.radius)
    
    def wrap_around(self):
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x -= SCREEN_WIDTH + self.radius
        if self.position.x < 0 - self.radius:
            self.position.x += SCREEN_WIDTH + self.radius
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y -= SCREEN_HEIGHT + self.radius
        if self.position.y < 0 - self.radius:
            self.position.y += SCREEN_HEIGHT + self.radius