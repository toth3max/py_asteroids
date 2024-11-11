import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.rotation : float = 0

        super().__init__(x, y, PLAYER_RADIUS)

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(dt, False)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt, True)

    def rotate(self, dt, clockwise: bool):
        if clockwise:
            self.rotation += dt * PLAYER_TURN_SPEED
        else:
            self.rotation -= dt * PLAYER_TURN_SPEED


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]