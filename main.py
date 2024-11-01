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
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0),)
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        # limit framerate to 60FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()