import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta-time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:  # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()  # refresh the screen
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
