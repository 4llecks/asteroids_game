import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shots import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    osd_font = pygame.font.SysFont("Arial" , 18 , bold = True)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield_object = AsteroidField()

    Player.containers = (drawable, updatable)
    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (updatable, drawable, shots)
    
    # Game Loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for thing in updatable:
            thing.update(dt)
        for obj in asteroids:
            if obj.check_collision(player_object):
                print("Game Over!")
                exit()
        for thing in drawable:
            thing.draw(screen)
        osd_var(screen, int(clock.get_fps()), osd_font, (0,0)) # FPS counter
        pygame.display.flip()
        dt = clock.tick(120)/1000 # Limits FPS to 60

def osd_var(screen, var, font, pos):
    text_to_display = font.render(str(var), 1, pygame.Color("RED"))
    screen.blit(text_to_display, (pos))

if __name__ == "__main__":
    main()
