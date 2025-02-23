import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    timeclock = pygame.time.Clock()
    dt = 0
    updatable =  pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        pygame.Surface.fill(screen, 000000)

        for asteroid in asteroids:
            if asteroid.check_for_collisions(player):
                print("Game over!")
                exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_for_collisions(asteroid):
                    shot.kill()
                    asteroid.split()
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        dt = (timeclock.tick(60) / 1000)

if __name__ == "__main__":
    main()