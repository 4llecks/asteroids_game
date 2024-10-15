import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_object = Player(SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Game Loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player_object.draw(screen) 
        pygame.display.flip()

        dt = clock.tick(60)/1000 # Limits FPS to 60


if __name__ == "__main__":
    main()
