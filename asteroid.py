import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            print("spawn")
            random_angle = random.uniform(20, 50)
            vector1 = pygame.Vector2(self.velocity.rotate(random_angle))
            vector2 = pygame.Vector2(self.velocity.rotate(-random_angle))

            child_asteroid_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            child_asteroid_one.velocity = vector1 * 1.2

            child_asteroid_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            child_asteroid_two.velocity = vector2 * 1.2
            
            child_asteroid_one.add(self.containers)
            child_asteroid_two.add(self.containers)