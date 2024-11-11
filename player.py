import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.rotation : float = 0

        super().__init__(x, y, PLAYER_RADIUS)

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]