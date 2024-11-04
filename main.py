# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
# Import game constants
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #clock object to help set FPS
    clock = pygame.time.Clock()
    dt = 0   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in asteroids:
            if obj.collides_with(player):
                print("Game over!")
                sys.exit()

        for obj in updatable:
            obj.update(dt)

        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # limit framerate to 60FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()