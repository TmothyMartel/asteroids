# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# Import game constants
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #clock object to help set FPS
    clock = pygame.time.Clock()
    dt = 0   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
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