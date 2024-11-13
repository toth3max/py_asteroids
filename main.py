import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
player = None
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    global player, asteroids, shots
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    loop()

def loop():
    global running
    global dt
    global player, asteroids, shots

    asteroids_field: AsteroidField
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        asteroids_field = AsteroidField()
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        for u in updatable:
            u.update(dt)
        
        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            a.update(dt)
            if player.is_colliding(a):
                print("Game over!")
            for s in shots:
                if s.is_colliding(a):
                    a.kill()
                    s.kill()

        #player.update(dt)
        #player.draw(screen)
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()